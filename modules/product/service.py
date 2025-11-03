from core.db import DataBase
from modules.product.schemas import ProductCreate
from modules.product.repository import ProductRepository

class ProductService:
    def get_all_products(self):
        repository = ProductRepository()
        return repository.get_all()
    
    def get_product_id(self, product_id: int):
        repository = ProductRepository()
        return repository.get_id(product_id)
    
    def create_product(self, product: ProductCreate):
        repository = ProductRepository()
        return repository.save(product)
    
    def get_products_by_company(self, company_id: int):
        repository = ProductRepository()
        return repository.get_by_company(company_id)
