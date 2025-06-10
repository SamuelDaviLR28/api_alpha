from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Dispatch
from app.schemas.dispatch import DispatchToutbox
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter(prefix="/hooks/vivo")

API_KEY = os.getenv("API_KEY")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def verify_api_key(x_api_key: str = Header(None)): 
    if not x_api_key or x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida"
        )

@router.post("/dispatch", dependencies=[Depends(verify_api_key)])
def receive_dispatch(payload: DispatchToutbox, db: Session = Depends(get_db)):
    data = payload.dict()

    # Mantendo CriacaoPedido separadamente caso precise usá-lo depois
    criacao_pedido = data.pop("CriacaoPedido", None)

    # Criando a instância de Dispatch sem campos extras
    new_dispatch = Dispatch(**{key: value for key, value in data.items() if key in Dispatch.__table__.columns.keys()})
    
    db.add(new_dispatch)
    db.commit()
    db.refresh(new_dispatch)
    
    return {
        "message": "Pedido recebido com sucesso",
        "id": new_dispatch.id,
        "CriacaoPedido": criacao_pedido  # Opcional: Retornar CriacaoPedido se necessário
    }
