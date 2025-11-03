from modules.type_product import schemas
from modules.type_product.repository import TypeProductRepository
from core.db import DataBase
from fastapi import HTTPException



class TypeProductService:
    VALIDAR_ID_COMPANY = "SELECT id FROM company WHERE id = %s"

    def get_type_products(self):
        repository = TypeProductRepository()
        return repository.get_all()

    def create_type_product(self, type_product: schemas.CreateTypeProduct):
        db = DataBase()
        query = self.VALIDAR_ID_COMPANY % type_product.company_id
        resultado = db.execute(query, many=False)

        if not resultado:
            raise HTTPException(status_code=404, detail="A empresa (company_id) fornecida não existe.")

        repository = TypeProductRepository()
        return repository.save(type_product)

    def get_type_product_id(self, id: int):
        repository = TypeProductRepository()
        type_product = repository.get_id(id)
        return type_product