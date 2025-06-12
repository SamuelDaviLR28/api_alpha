from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import rastro

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/rastro")
def post_rastro_event(payload: dict, db: Session = Depends(get_db)):
    novo = Rastro(dados=payload)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return {"message": "Ocorrência registrada", "id": novo.id}
