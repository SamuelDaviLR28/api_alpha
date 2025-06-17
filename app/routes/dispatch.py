from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
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
    # Removendo exclude_none=True para manter os campos nulos
    data = payload.model_dump()

    # Verificar se o pedido já existe
    unique_id = data.get("NumeroPedidoErp")
    if unique_id:
        q = select(Dispatch).filter(Dispatch.unique_id == unique_id)
        res = await db.execute(q)
        if res.scalars().first():
            return {"message": "Dispatch já cadastrado", "unique_id": unique_id}

    # Extrair dados principais
    order_id = data.get("NumeroPedido")
    canal_de_venda = data.get("CanalDeVenda")
    nota_fiscal = data.get("NotaFiscal")
    itens = data.get("Itens", [])

    # Primeiro item (se existir) para pegar info do frete
    primeiro_frete = itens[0].get("Frete") if itens else None
    destinatario = primeiro_frete.get("Destinatario") if primeiro_frete else None
    remetente = primeiro_frete.get("Remetente") if primeiro_frete else None

    dispatch_data = {
        "order_id": order_id,
        "unique_id": unique_id,
        "client_info": canal_de_venda,
        "recipient_info": destinatario,
        "invoice_info": nota_fiscal,
        "origin_info": remetente,
        "volumes": itens
    }

    # Criar novo dispatch
    novo = Dispatch(**dispatch_data)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)

    return {"message": "Pedido recebido com sucesso", "id": novo.id}
