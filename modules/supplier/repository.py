from core.db import DataBase
from modules.supplier.schemas import CreateSupplier

class SupplierRepository:
    QUERY_SUPPLIERS = "SELECT id, name, cnpj, status, company_id FROM supplier;"
    QUERY_SUPPLIERS_ID = "SELECT id, name, cnpj, status, company_id FROM supplier WHERE id= %s;"
    QUERY_CREATE_SUPPLIER = "INSERT INTO supplier (name, cnpj, company_id, status) VALUES (%s, %s, %s, %s) RETURNING id;"

    def get_all(self):
        db = DataBase()
        suppliers = db.execute(self.QUERY_SUPPLIERS)
        resultados = []
        for supplier in suppliers:
            resultados.append({
                "id": supplier[0],
                "name": supplier[1],
                "cnpj": supplier[2],
                "status": supplier[3],
                "company_id": supplier[4]
            })
        return resultados
    
    def get_id(self, id: int):
        db = DataBase()
        query = self.QUERY_SUPPLIERS_ID % id
        supplier = db.execute(query, many=False)
        if supplier:
            return {
                "id": supplier[0],
                "name": supplier[1],
                "cnpj": supplier[2],
                "status": supplier[3],
                "company_id": supplier[4]}
        return {}
    
    def save(self, supplier: CreateSupplier):
        db = DataBase()
        default_status = 'ATIVO'

        query = self.QUERY_CREATE_SUPPLIER % (
            f"'{supplier.name}'", 
            f"'{supplier.cnpj}'", 
            supplier.company_id, 
            f"'{default_status}'"
        )
        
        resultado = db.commit(query)
        if resultado:
            novo_id_criado = resultado[0]
            return self.get_id(novo_id_criado)
        return {}