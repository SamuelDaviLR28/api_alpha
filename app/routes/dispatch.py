from fastapi import APIRouter, Request, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi.encoders import jsonable_encoder

from app.schemas.dispatch import DispatchToutbox
from app.models import Dispatch
from app.database import SessionLocal

router = APIRouter(prefix="/hooks/vivo")

async def get_db():
    async with SessionLocal() as session:
        yield session

# ✅ ENDPOINT PRINCIPAL
@router.post("/dispatch", status_code=201)
async def receive_dispatch(
    request: Request,
    db: AsyncSession = Depends(get_db)
):
    try:
        body = await request.json()

        # 🧹 Remove campos potencialmente soltos no root
        body.pop("Transportadora", None)
        body.pop("Tomador", None)

        # 👇 Faz parse manual usando seu modelo Pydantic
        payload = DispatchToutbox(**body)

    except Exception as e:
        print("🚨 Erro ao parsear DispatchToutbox:", str(e))
        raise HTTPException(status_code=422, detail=f"Erro ao processar JSON: {str(e)}")

    item = payload.Itens[0] if payload.Itens else None
    frete = item.Frete if item else None

    unique_id = payload.NumeroPedidoErp
    if unique_id:
        q = select(Dispatch).filter(Dispatch.unique_id == unique_id)
        res = await db.execute(q)
        if res.scalars().first():
            return {"message": "Dispatch já cadastrado", "unique_id": unique_id}

    canal_de_venda = payload.CanalDeVenda
    nota_fiscal = payload.NotaFiscal
    infos_adicionais = payload.InfosAdicionais
    itens = payload.Itens or []

    dispatch_data = {
        "order_id": payload.NumeroPedido,
        "unique_id": unique_id,
        "client_info": jsonable_encoder(canal_de_venda),
        "recipient_info": None,
        "invoice_info": jsonable_encoder(nota_fiscal),
        "origin_info": None,
        "volumes": jsonable_encoder(itens),
    }

    novo = Dispatch(**dispatch_data)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)

    return {"message": "Pedido recebido com sucesso", "id": novo.id}


# ✅ ENDPOINT DE DEBUG PARA INSPECIONAR O SCHEMA
@router.post("/debug-schema")
async def debug_schema():
    campos = list(DispatchToutbox.__annotations__.keys())
    return {
        "Campos no DispatchToutbox": campos,
        "Tipo Transportadora": str(DispatchToutbox.__annotations__.get("Transportadora", "❌ Não definido")),
        "Tipo Tomador": str(DispatchToutbox.__annotations__.get("Tomador", "❌ Não definido"))
    }
