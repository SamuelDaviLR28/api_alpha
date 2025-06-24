@router.post("/dispatch", dependencies=[Depends(verify_api_key)], status_code=201)
async def receive_dispatch(
    payload: DispatchToutbox,
    db: AsyncSession = Depends(get_db)
):
    # ✅ Diagnóstico para descobrir o tipo real no runtime
    print("🔎 DispatchToutbox carregado de:", DispatchToutbox.__module__)
    print("📋 Tipos dos campos:", DispatchToutbox.__annotations__)

    try:
        item = payload.Itens[0] if payload.Itens else None
        frete = item.Frete if item else None

        print("📦 Frete recebido →", type(frete))
        print("   ⤷ Módulo:", type(frete).__module__)
        print("🧾 NotaFiscal recebida →", type(payload.NotaFiscal))
        print("   ⤷ Módulo:", type(payload.NotaFiscal).__module__)
        print("📋 InfosAdicionais recebida →", type(payload.InfosAdicionais))
        print("   ⤷ Módulo:", type(payload.InfosAdicionais).__module__)
    except Exception as e:
        print("🚨 Erro ao acessar campos:", e)

    # Lógica de duplicidade
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
