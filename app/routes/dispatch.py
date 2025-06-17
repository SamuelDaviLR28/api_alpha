from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Any
import os

from app.database import SessionLocal
from app.models import Dispatch
from app.schemas.dispatch import DispatchToutbox  # agora existe!

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
    data: dict[str, Any] = payload.model_dump(exclude_none=True)
    unique_id = data.get("NumeroPedidoErp")

    # se já existe, devolve sem erro
    if unique_id:
        q = select(Dispatch).filter(Dispatch.unique_id == unique_id)
        res = await db.execute(q)
        if res.scalars().first():
            return {"message": "Dispatch já cadastrado", "unique_id": unique_id}

    dispatch_data = {
        "order_id": data.get("NumeroPedido"),
        "unique_id": unique_id,
        "client_info": None,
        "recipient_info": None,
        "invoice_info": data.get("NotaFiscal"),
        "origin_info": data.get("CanalDeVenda"),
        "volumes": data.get("Itens"),
    }

    novo = Dispatch(**dispatch_data)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)
    return {"message": "Pedido recebido com sucesso", "id": novo.id}
