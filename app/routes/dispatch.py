from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.database import SessionLocal
from app.models import Dispatch
from app.schemas.dispatch import DispatchToutbox
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/hooks/vivo")

API_KEY = os.getenv("API_KEY")


async def get_db():
    async with SessionLocal() as session:
        yield session


async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key não fornecida"
        )
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida"
        )


@router.post("/dispatch", dependencies=[Depends(verify_api_key)])
async def receive_dispatch(payload: DispatchToutbox, db: AsyncSession = Depends(get_db)):
    data = payload.model_dump()

    criacao_pedido = data.pop("CriacaoPedido", None)

    # Aqui, monte seu dict para os campos que tem no model Dispatch
    dispatch_data = {
        "order_id": data.get("NumeroPedido"),
        "unique_id": data.get("NumeroPedidoErp"),
        "client_info": data.get("Seller").model_dump() if data.get("Seller") else None,
        "recipient_info": None,  # Ajuste se tiver dados reais
        "invoice_info": data.get("NotaFiscal").model_dump() if data.get("NotaFiscal") else None,
        "origin_info": None,
        "volumes": None,
    }

    # Exemplo: você pode preencher os campos JSON com o que precisa conforme seu payload.

    new_dispatch = Dispatch(**dispatch_data)

    db.add(new_dispatch)
    await db.commit()
    await db.refresh(new_dispatch)

    return {
        "message": "Pedido recebido com sucesso",
        "id": new_dispatch.id,
        "CriacaoPedido": criacao_pedido
    }
