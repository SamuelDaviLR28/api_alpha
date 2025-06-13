from fastapi import FastAPI, Header, HTTPException, Depends
from dotenv import load_dotenv
import os

from app.routes import dispatch, patch, rastro, motorista, rota, cancelamento
from app.database import engine, Base

import asyncio


load_dotenv()


app = FastAPI()


API_KEY = os.getenv("API_KEY")


def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")


@app.get("/")
def root():
    return {"message": "API rodando online com sucesso!"}


app.include_router(dispatch.router, dependencies=[Depends(verify_api_key)])
app.include_router(patch.router, dependencies=[Depends(verify_api_key)])
app.include_router(rastro.router, dependencies=[Depends(verify_api_key)])
app.include_router(motorista.router, dependencies=[Depends(verify_api_key)])
app.include_router(rota.router, dependencies=[Depends(verify_api_key)])
app.include_router(cancelamento.router, dependencies=[Depends(verify_api_key)])


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(create_tables())
