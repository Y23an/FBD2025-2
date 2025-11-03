from fastapi import APIRouter
from modules.type_product import schemas
from modules.type_product.service import TypeProductService

router = APIRouter(prefix="/type_products", tags=["Type Products"])

@router.get("/", response_model=list[schemas.TypeProduct])
def list_type_products():
    service = TypeProductService()
    return service.get_type_products()

@router.get("/{id}/", response_model=schemas.TypeProduct)
def get_type_product_by_id(id: int):
    service = TypeProductService()
    return service.get_type_product_id(id)

@router.post("/", response_model=schemas.TypeProduct)
def add_type_product(type_product: schemas.CreateTypeProduct):
    service = TypeProductService()
    return service.create_type_product(type_product)
