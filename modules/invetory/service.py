from modules.invetory.repository import InventoryRepository
from modules.invetory import schemas
from core.db import DataBase

VALIDAR_ID_PRODUCT = "SELECT id FROM product WHERE id = %s"

class InventoryService:
    def get_inventories(self):
        repository = InventoryRepository()
        return repository.get_all()

    def create_inventory(self, inventory: schemas.InventoryCreate):
        db = DataBase()
        query = VALIDAR_ID_PRODUCT % inventory.product_id
        resultado = db.execute(query, many=False)
        if not resultado:
            raise ValueError("Produto não existe")
        
        repository = InventoryRepository()
        return repository.save(inventory)

    def get_inventory_id(self, id: int):
        repository = InventoryRepository()
        inventory = repository.get_id(id)
        return inventory

    
    