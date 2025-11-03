from pydantic import BaseModel


class TypeProduct(BaseModel):
    id: int
    name: str
    cod: str
    company_id: int

class CreateTypeProduct(BaseModel):
    name: str
    cod: str
    company_id: int
