from core.db import DataBase
from modules.product.schemas import ProductCreate

class ProductRepository:

    QUERY_PRODUCTS = "SELECT p.id, p.name, p.description, p.price, p.company_id, tp.name AS type_name, s.name AS supplier_name FROM product p JOIN type_product tp ON p.type_id = tp.id JOIN supplier s ON p.supplier_id = s.id;"
    QUERY_PRODUCT_ID = "SELECT p.id, p.name, p.description, p.price, p.company_id, tp.name AS type_name, s.name AS supplier_name FROM product p JOIN type_product tp ON p.type_id = tp.id JOIN supplier s ON p.supplier_id = s.id WHERE p.id = %s;"
    QUERY_COMPANY_PRODUCTS = "SELECT p.id, p.name, p.description, p.price, p.company_id, tp.name AS type_name, s.name AS supplier_name FROM product p JOIN type_product tp ON p.type_id = tp.id JOIN supplier s ON p.supplier_id = s.id WHERE p.company_id = %s;"
    QUERY_CREATE_PRODUCT = "INSERT INTO product (name, description, price, type_id, supplier_id, company_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"

    def get_all(self):
        db = DataBase()
        products = db.execute(self.QUERY_PRODUCTS)
        resultados = []
        for product in products:
            resultados.append({
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "price": product[3],
                "company_id": product[4],
                "type_name": product[5],     
                "supplier_name": product[6] 
            })
        return resultados
    
    def get_id(self, product_id: int):
        db = DataBase()
        query = self.QUERY_PRODUCT_ID % product_id
        product = db.execute(query, many=False)
        if product:
            return {
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "price": product[3],
                "company_id": product[4],
                "type_name": product[5],    
                "supplier_name": product[6]  
            }
        return {}
    
    def save(self, product: ProductCreate):
        db = DataBase()
        query = self.QUERY_CREATE_PRODUCT % (
            f"'{product.name}'",
            f"'{product.description}'",
            product.price,
            product.type_id,
            product.supplier_id,
            product.company_id
        )
        result = db.commit(query)

        if result:
            new_id = result[0]
            return self.get_id(new_id) 
        
        return {}
    
    def get_by_company(self, company_id: int):
        db = DataBase()
        query = self.QUERY_COMPANY_PRODUCTS % company_id
        products = db.execute(query)
        resultados = []
        for product in products:
            resultados.append({
                "id": product[0],
                "name": product[1],
                "description": product[2],
                "price": product[3],
                "company_id": product[4],
                "type_name": product[5],     
                "supplier_name": product[6] 
            })
        return resultados