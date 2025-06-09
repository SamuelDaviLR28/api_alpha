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

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API Key inválida"
        )

@router.post("/dispatch", dependencies=[Depends(verify_api_key)])
def receive_dispatch(payload: DispatchToutbox, db: Session = Depends(get_db)):
    new_dispatch = Dispatch(**payload.dict())
    db.add(new_dispatch)
    db.commit()
    db.refresh(new_dispatch)
    return {"message": "Pedido recebido com sucesso", "id": new_dispatch.id}

@router.get("/dispatch", dependencies=[Depends(verify_api_key)])
def list_dispatches(db: Session = Depends(get_db)):
    dispatches = db.query(Dispatch).all()
    return dispatches
