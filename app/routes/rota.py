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

@router.post("/rota")
def post_rota(payload: dict, db: Session = Depends(get_db)):
    return {"message": "Rota recebida"}
