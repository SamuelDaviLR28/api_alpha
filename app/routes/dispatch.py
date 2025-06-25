from fastapi import APIRouter, Request, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.encoders import jsonable_encoder

from app.schemas.vivo import DispatchVivoModel
from app.models import Dispatch
from app.database import SessionLocal

router = APIRouter(prefix="/hooks/vivo")

async def get_db():
    async with SessionLocal() as session:
        yield session

@router.post("/dispatch", status_code=201)
async def receive_dispatch(request: Request, db: AsyncSession = Depends(get_db)):
    try:
        body = await request.json()
        payload = DispatchVivoModel(**body)
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Erro ao processar JSON: {str(e)}")

    item = payload.Itens[0] if payload.Itens else None
    unique_id = payload.NumeroPedidoErp

    if unique_id:
        q = select(Dispatch).filter(Dispatch.unique_id == unique_id)
        res = await db.execute(q)
        if res.scalars().first():
            return {"message": "Dispatch já cadastrado", "unique_id": unique_id}

    dispatch_data = {
        "order_id": payload.NumeroPedido,
        "unique_id": unique_id,
        "client_info": jsonable_encoder(payload.CanalDeVenda),
        "recipient_info": None,
        "invoice_info": jsonable_encoder(payload.NotaFiscal),
        "origin_info": None,
        "volumes": jsonable_encoder(payload.Itens),
    }

    novo = Dispatch(**dispatch_data)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)

    return {"message": "Pedido recebido com sucesso", "id": novo.id}
