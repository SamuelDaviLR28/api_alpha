from fastapi import FastAPI, Header, HTTPException, Depends
from dotenv import load_dotenv
import os

from app.routes import dispatch, patch, rastro, motorista, rota, cancelamento
from app.database import engine, Base
from app.schemas.vivo import DispatchVivoSchemaFinal

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_KEY")

async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida")

@app.get("/")
async def root():
    return {"message": "API rodando com sucesso!"}

app.include_router(dispatch.router, dependencies=[Depends(verify_api_key)])
app.include_router(patch.router, dependencies=[Depends(verify_api_key)])
app.include_router(rastro.router, dependencies=[Depends(verify_api_key)])
app.include_router(motorista.router, dependencies=[Depends(verify_api_key)])
app.include_router(rota.router, dependencies=[Depends(verify_api_key)])
app.include_router(cancelamento.router, dependencies=[Depends(verify_api_key)])

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    print("✔️ Schema real usado:", DispatchVivoSchemaFinal.__name__)
