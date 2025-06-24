from fastapi import APIRouter, Depends, Header, HTTPException, status, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
import os

from app.database import SessionLocal
from app.models import Dispatch
from app.schemas.dispatch import DispatchToutbox

@router.post("/dispatch", dependencies=[Depends(verify_api_key)], status_code=201)
async def receive_dispatch(
    payload: DispatchToutbox,
    db: AsyncSession = Depends(get_db),
    request: Request = None
):
    print("🔍 DispatchToutbox carregado de:", DispatchToutbox.__module__)
    print("📋 Campos e tipos do schema:")
    for campo, tipo in DispatchToutbox.__annotations__.items():
        print(f" - {campo}: {tipo}")

    try:
        item = payload.Itens[0] if payload.Itens else None
        frete = item.Frete if item else None

        print("📦 Frete →", type(frete))
        print("   ⤷ Módulo:", type(frete).__module__ if frete else "None")
        print("🧾 NotaFiscal →", type(payload.NotaFiscal))
        print("   ⤷ Módulo:", type(payload.NotaFiscal).__module__ if payload.NotaFiscal else "None")
        print("📋 InfosAdicionais →", type(payload.InfosAdicionais))
        print("   ⤷ Módulo:", type(payload.InfosAdicionais).__module__ if payload.InfosAdicionais else "None")
    except Exception as e:
        print("🚨 Erro durante diagnóstico dos campos:", e)

    unique_id = payload.NumeroPedidoErp
    if unique_id:
        q = select(Dispatch).filter(Dispatch.unique_id == unique_id)
        res = await db.execute(q)
        if res.scalars().first():
            return {"message": "Dispatch já cadastrado", "unique_id": unique_id}

    order_id = payload.NumeroPedido
    canal_de_venda = payload.CanalDeVenda
    itens = payload.Itens or []

    destinatario = None
    remetente = None
    nota_fiscal = payload.NotaFiscal
    infos_adicionais = payload.InfosAdicionais

    dispatch_data = {
        "order_id": order_id,
        "unique_id": unique_id,
        "client_info": jsonable_encoder(canal_de_venda),
        "recipient_info": jsonable_encoder(destinatario),
        "invoice_info": jsonable_encoder(nota_fiscal),
        "origin_info": jsonable_encoder(remetente),
        "volumes": jsonable_encoder(itens),
    }

    novo = Dispatch(**dispatch_data)
    db.add(novo)
    await db.commit()
    await db.refresh(novo)

    return {"message": "Pedido recebido com sucesso", "id": novo.id}
