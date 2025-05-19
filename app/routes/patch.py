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

@router.patch("/frete-prazo")
def update_frete_prazo(payload: dict, db: Session = Depends(get_db)):
    # Aqui o processamento de valor do frete e prazo
    return {"message": "Frete e prazo atualizados com sucesso"}
