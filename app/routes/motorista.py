from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Motorista

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/motorista")
def post_motorista(payload: dict, db: Session = Depends(get_db)):
    novo = Motorista(dados=payload)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"message": "Informações do motorista recebidas", "id": novo.id}
