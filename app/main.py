from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv
import os
from app.dispatch import router as dispatch_router
from app.patch import router as patch_router
from app.rastro import router as rastro_router
from app.motorista import router as motorista_router
from app.rota import router as rota_router
from app.cancelamento import router as cancelamento_router
from fastapi import Depends

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.get("/")
def root():
    return {"message": "API rodando online com sucesso!"}

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

app.include_router(dispatch.router, dependencies=[Depends(verify_api_key)])
app.include_router(patch.router, dependencies=[Depends(verify_api_key)])
app.include_router(rastro.router, dependencies=[Depends(verify_api_key)])
app.include_router(motorista.router, dependencies=[Depends(verify_api_key)])
app.include_router(rota.router, dependencies=[Depends(verify_api_key)])
app.include_router(cancelamento.router, dependencies=[Depends(verify_api_key)])
