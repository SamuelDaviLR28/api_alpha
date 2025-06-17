from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any
import logging
import os
from dotenv import load_dotenv

from app.database import SessionLocal
from app.models import Dispatch
from app.schemas.dispatch import DispatchToutbox

load_dotenv()

router = APIRouter(prefix="/hooks/vivo")

API_KEY = os.getenv("API_KEY")
logger = logging.getLogger("uvicorn.dispatch")


async def get_db():
    async with SessionLocal() as session:
        yield session

async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="API Key não fornecida")
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida")

@router.post("/dispatch", dependencies=[Depends(verify_api_key)], status_code=201)
async def receive_dispatch(
    payload: DispatchToutbox,
    db: AsyncSession = Depends(get_db)
):
    """
    Recebe o webhook de Dispatch da Vivo.
    Salva os dados brutos em JSON nas colunas JSON do modelo `Dispatch`.
    """

    data: dict[str, Any] = payload.model_dump()
    criacao_pedido = data.pop("CriacaoPedido", None)

    dispatch_data = {
        "order_id": data.get("NumeroPedido"),
        "unique_id": data.get("NumeroPedidoErp"),
        "client_info": data.get("Seller"),
        # ajuste esses campos conforme evoluir seu payload
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
        logger.info(f"Dispatch salvo (id={new_dispatch.id})")
        return {
            "message": "Pedido recebido com sucesso",
            "id": new_dispatch.id,
            "CriacaoPedido": criacao_pedido,
        }
    except Exception as exc:
        await db.rollback()
        logger.error("Erro ao salvar dispatch: %s", exc, exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erro interno ao processar dispatch"
        )
