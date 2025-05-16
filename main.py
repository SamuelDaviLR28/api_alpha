from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

print("DEBUG: DATABASE_URL =", os.getenv("DATABASE_URL"))

from fastapi import FastAPI
from app.routes import dispatch, patch, rastro, motorista, rota, cancelar, comprovante, awb
from app.database import engine, Base

DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL não definido no .env")

app = FastAPI(title="Toutbox Integration API")

Base.metadata.create_all(bind=engine)  

app.include_router(dispatch.router)
app.include_router(patch.router)
app.include_router(rastro.router)
app.include_router(motorista.router)
app.include_router(rota.router)
app.include_router(cancelar.router)
app.include_router(comprovante.router)
app.include_router(awb.router)

print("Banco de dados URL carregado com sucesso")
