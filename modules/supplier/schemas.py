from pydantic import BaseModel

class Supplier(BaseModel):
    id: int
    name: str
    cnpj: str
    status : str
    company_id: int

    class Config:
        from_attributes = True 

class CreateSupplier(BaseModel):
    name: str
    cnpj: str
    company_id: int
