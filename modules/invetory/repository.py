from core.db import DataBase
from modules.invetory.schemas import InventoryCreate

class InventoryRepository:
    QUERY_INVENTORIES = "SELECT i.id, i.product_id, p.name AS name, p.price AS price, i.quantity, i.updated_at FROM inventory i JOIN product p ON p.id = i.product_id;"
    QUERY_INVENTORY_ID = "SELECT i.id, i.product_id, p.name, p.price, i.quantity, i.updated_at FROM inventory i JOIN product p ON i.product_id = p.id WHERE i.id = %s"
    QUERY_CREATE_INVENTORY = "INSERT INTO inventory (product_id, quantity) VALUES (%s, %s) RETURNING id"
    QUERY_TOTAL_BY_PRODUCT = "SELECT p.id AS product_id, p.name AS product_name, SUM(i.quantity) AS total_quantity FROM inventory i JOIN product p ON i.product_id = p.id GROUP BY p.id, p.name;"

    def get_all(self):
        db = DataBase()
        inventario = db.execute(self.QUERY_INVENTORIES)
        resultados = []
        for inventory in inventario:
            resultados.append({
                "id": inventory[0],
                "product_id": inventory[1],
                "name": inventory[2],
                "price": float(inventory[3]),
                "quantity": inventory[4],
                "updated_at": inventory[5]
            })
        return resultados


    def save(self, inventory: InventoryCreate):
        db = DataBase()
        query = self.QUERY_CREATE_INVENTORY % (inventory.product_id, inventory.quantity)
        result = db.commit(query)

        if result:
            new_id = result[0]
            return self.get_id(new_id) 
        
        return {} 


    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_INVENTORY_ID % id
        inventory = db.execute(query, many=False)
        if inventory:
            return {
                "id": inventory[0],
                "product_id": inventory[1],
                "name": inventory[2],
                "price": float(inventory[3]),
                "quantity": inventory[4],
                "updated_at": inventory[5]
            }
        return {}