from fastapi import Header, HTTPException, status
from app.database import async_session

API_KEY = "suachaveaqui"  # coloque sua chave real aqui

async def get_db():
    async with async_session() as session:
        yield session

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Chave de API inválida.")
