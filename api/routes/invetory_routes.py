from typing import Optional
from fastapi import APIRouter
from modules.invetory import schemas
from modules.invetory.schemas import InventoryCreate
from modules.invetory.service import InventoryService  

router = APIRouter(prefix="/inventory", tags=["Inventory"])

@router.get("/", response_model=list[schemas.Inventory])
def list_inventories():
    service = InventoryService()
    return service.get_inventories()    

@router.get("/{id}/", response_model=Optional[schemas.Inventory])
def get_inventory_by_id(id: int):
    service = InventoryService()
    return service.get_inventory_id(id) 

@router.post("/", response_model=schemas.Inventory)
def add_inventory(inventory: InventoryCreate):
    service = InventoryService()
    return service.create_inventory(inventory)  

