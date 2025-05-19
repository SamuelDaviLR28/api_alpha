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

@router.put("/cancelar-suspender")
def cancelar_suspender(payload: dict, db: Session = Depends(get_db)):
    return {"message": "Cancelamento ou suspensão processado"}
