from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/rastro")
def post_rastro_event(payload: dict, db: Session = Depends(get_db)):
    # Armazenar evento de rastreamento
    return {"message": "Ocorrência registrada"}
