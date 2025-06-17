from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Any
import os
from dotenv import load_dotenv

from app.database import SessionLocal
from app.models import Dispatch
from app.schemas.dispatch import DispatchToutbox

load_dotenv()

router = APIRouter(prefix="/hooks/vivo")

API_KEY = os.getenv("API_KEY")

async def get_db():
    async with SessionLocal() as session:
        yield session

async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key não fornecida")
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="API Key inválida")

@router.post("/dispatch", dependencies=[Depends(verify_api_key)], status_code=201)
async def receive_dispatch(
    payload: DispatchToutbox,
    db: AsyncSession = Depends(get_db)
):
    data: dict[str, Any] = payload.model_dump()
    criacao_pedido = data.pop("CriacaoPedido", None)

    unique_id = data.get("NumeroPedidoErp")

    # Verificar se já existe registro com o mesmo unique_id
    query = select(Dispatch).filter(Dispatch.unique_id == unique_id)
    result = await db.execute(query)
    existing_dispatch = result.scalars().first()

    if existing_dispatch:
        return {
            "message": "Dispatch já existe",
            "id": existing_dispatch.id,
            "CriacaoPedido": criacao_pedido
        }

    dispatch_data = {
        "order_id": data.get("NumeroPedido"),
        "unique_id": unique_id,
        "client_info": data.get("Seller"),
        "recipient_info": data.get("Destinatario") if data.get("Destinatario") else None,
        "invoice_info": data.get("NotaFiscal"),
        "origin_info": data.get("Marketplace"),
        "volumes": data.get("Itens"),
    }

    try:
        new_dispatch = Dispatch(**dispatch_data)
        db.add(new_dispatch)
        await db.commit()
        await db.refresh(new_dispatch)
        return {
            "message": "Pedido recebido com sucesso",
            "id": new_dispatch.id,
            "CriacaoPedido": criacao_pedido,
        }
    except Exception as exc:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro interno ao processar dispatch: {exc}"
        )
