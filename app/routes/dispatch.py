from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Dispatch
from app.schemas.dispatch import DispatchCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/dispatch")
def receive_dispatch(payload: DispatchCreate, db: Session = Depends(get_db)):
    new_dispatch = Dispatch(**payload.dict())
    db.add(new_dispatch)
    db.commit()
    db.refresh(new_dispatch)
    return {"message": "Pedido recebido com sucesso", "id": new_dispatch.id}
