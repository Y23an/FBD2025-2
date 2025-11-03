from typing import Optional
from fastapi import APIRouter
from modules.product import schemas
from modules.product.schemas import ProductCreate
from modules.product.service import ProductService

router = APIRouter(prefix="/product", tags=["Product"])

@router.get("/", response_model=list[schemas.ProductDetail])
def list_products():
    service = ProductService()
    return service.get_all_products()


@router.get("/{product_id}", response_model=Optional[schemas.ProductDetail])
def get_product(product_id: int):
    service = ProductService()
    return service.get_product_id(product_id)

@router.post("/", response_model=schemas.ProductDetail)
def create_product(product: ProductCreate):
    service = ProductService()
    return service.create_product(product) 

@router.get("/company/{company_id}", response_model=list[schemas.ProductDetail])
def get_products_by_company(company_id: int):
    service = ProductService()
    return service.get_products_by_company(company_id)