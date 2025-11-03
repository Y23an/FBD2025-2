from core.db import DataBase
from modules.type_product.schemas import CreateTypeProduct

class TypeProductRepository:
    QUERY_TYPE_PRODUCTS = "SELECT tp.id, tp.name, tp.cod, tp.company_id FROM type_product tp;"
    QUERY_TYPE_PRODUCT_ID = "SELECT type.id, type.name, type.cod, type.company_id FROM type_product type WHERE type.id = %s"
    QUERY_CREATE_TYPE_PRODUCT = "INSERT INTO type_product (name, cod, company_id) VALUES (%s, %s, %s) RETURNING id"

    def get_all(self):
        db = DataBase()
        type_products = db.execute(self.QUERY_TYPE_PRODUCTS)
        resultados = []
        
        for type_row in type_products:
            resultados.append({
                "id": type_row[0],
                "name": type_row[1],
                "cod": type_row[2],
                "company_id": type_row[3]
            })
        return resultados
    
    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_TYPE_PRODUCT_ID % id
        type_product = db.execute(query, many=False)
        if type_product:
            return {"id": type_product[0],
                    "name": type_product[1],
                    "cod": type_product[2], 
                    "company_id": type_product[3]}
        return {}

    def save(self, type_product: CreateTypeProduct):
        db = DataBase()
        query = self.QUERY_CREATE_TYPE_PRODUCT % (f"'{type_product.name}'", f"'{type_product.cod}'", type_product.company_id)
        resultado = db.commit(query)
        
        if resultado:
            new_id = resultado[0]
            return self.get_id(new_id)
            
        return {} 