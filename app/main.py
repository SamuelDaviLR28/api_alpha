from fastapi import FastAPI, Depends
from app.dependencies import get_db, verify_api_key
from sqlalchemy.ext.asyncio import AsyncSession
from app import crud, schemas
import asyncio
from app.database import engine, Base

app = FastAPI(title="API Transportadora Parceira")

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.post("/dispatch", dependencies=[Depends(verify_api_key)])
async def post_dispatch(pedido: schemas.PedidoCreate, db: AsyncSession = Depends(get_db)):
    await crud.criar_pedido(db, pedido)
    await asyncio.sleep(300)  
    return {"message": "Pedido recebido e aguardando processamento."}
