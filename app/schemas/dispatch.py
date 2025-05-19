from pydantic import BaseModel
from typing import List, Dict

class DispatchBase(BaseModel):
    order_id: str
    unique_id: str
    client_info: Dict
    recipient_info: Dict
    invoice_info: Dict
    origin_info: Dict
    volumes: List[Dict]

class DispatchCreate(DispatchBase):
    pass
