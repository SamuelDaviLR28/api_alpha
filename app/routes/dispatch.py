from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Any
import os

from app.database import SessionLocal
from app.models import Dispatch
from app.schemas.dispatch import DispatchToutbox

router = APIRouter(prefix="/hooks/vivo")
API_KEY = os.getenv("API_KEY")

async def get_db():
    async with SessionLocal() as session:
        yield session

async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida")

@router.post("/dispatch", dependencies=[Depends(verify_api_key)], status_code=201)
async def receive_dispatch(
    payload: DispatchToutbox,
    db: AsyncSession = Depends(get_db)
):
    # Transformar Pydantic para dict incluindo campos None
    data = payload.model_dump(exclude_none=False)

    # Normalizar para remover chaves com valor None
    data = normalize_none_fields(data)

    unique_id = data.get("NumeroPedidoErp")
    if unique_id:
        q = select(Dispatch).filter(Dispatch.unique_id == unique_id)
        res = await db.execute(q)
        if res.scalars().first():
            return {"message": "Dispatch já cadastrado", "unique_id": unique_id}

    # Serializar objetos aninhados para dicionários simples
    invoice_info = data.get("NotaFiscal")
    if invoice_info and not isinstance(invoice_info, dict):
        invoice_info = invoice_info.model_dump() if hasattr(invoice_info, "model_dump") else invoice_info

    origin_info = data.get("CanalDeVenda")
    if origin_info and not isinstance(origin_info, dict):
        origin_info = origin_info.model_dump() if hasattr(origin_info, "model_dump") else origin_info

    volumes = data.get("Itens")
    if volumes and isinstance(volumes, list):
        volumes = [
            v.model_dump() if hasattr(v, "model_dump") else v
            for v in volumes
        ]

    dispatch_data = {
        "order_id": data.get("NumeroPedido"),
        "unique_id": unique_id,
        "client_info": None,  # Pode preencher conforme necessário
        "recipient_info": None,
        "invoice_info": invoice_info,
        "origin_info": origin_info,
        "volumes": volumes,
    }

    novo = Dispatch(**dispatch_data)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return {"message": "Pedido recebido com sucesso", "id": novo.id}
