from sqlalchemy import Column, Integer, String, JSON
from app.database import Base

class Dispatch(Base):
    __tablename__ = "dispatches"
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String(100), index=True)
    unique_id = Column(String(100), unique=True)
    client_info = Column(JSON)
    recipient_info = Column(JSON)
    invoice_info = Column(JSON)
    origin_info = Column(JSON)
    volumes = Column(JSON)
