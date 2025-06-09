from fastapi import FastAPI, Header, HTTPException
from dotenv import load_dotenv
import os
from app.routes import dispatch, patch, rastro, motorista, rota, cancelamento

load_dotenv()
app = FastAPI()

API_KEY = os.getenv("API_KEY")

@app.get("/")
def root():
    return {"message": "API rodando online com sucesso!"}

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

app.include_router(dispatch.router)
app.include_router(patch.router)
app.include_router(rastro.router)
app.include_router(motorista.router)
app.include_router(rota.router)
app.include_router(cancelamento.router)
