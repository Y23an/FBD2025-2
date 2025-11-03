from pydantic import BaseModel, Field
from datetime import datetime

class Inventory(BaseModel):
    id: int
    product_id: int
    product_name: str = Field(alias='name') 
    price: float
    quantity: int
    updated_at: datetime
    class Config:
        from_attributes = True
    
class InventoryCreate(BaseModel):
    product_id: int
    quantity: int

