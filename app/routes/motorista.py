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

@router.post("/motorista")
def post_motorista(payload: dict, db: Session = Depends(get_db)):
    return {"message": "Informações do motorista recebidas"}
