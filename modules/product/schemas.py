from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    type_id: int
    supplier_id: int
    company_id: int
    class Config:
        from_attributes = True

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    type_id: int
    supplier_id: int
    company_id: int

class ProductDetail(BaseModel):
    id: int
    name: str
    description: str
    price: float
    company_id: int
    type_name: str     
    supplier_name: str

    class Config:
        from_attributes = True