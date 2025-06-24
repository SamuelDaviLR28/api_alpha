from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Rota

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/rota")
def post_rota(payload: dict, db: Session = Depends(get_db)):
    novo = Rota(dados=payload)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"message": "Rota recebida", "id": novo.id}
