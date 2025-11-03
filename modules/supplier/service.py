from modules.supplier.repository import SupplierRepository
from modules.supplier import schemas
from core.db import DataBase
from fastapi import HTTPException

class SupplierService:
    VALIDAR_ID_COMPANY = "SELECT id FROM company WHERE id = %s"

    def get_suppliers(self):
        repository = SupplierRepository()
        return repository.get_all()

    def create_supplier(self, supplier: schemas.CreateSupplier):
        db = DataBase()
        query = self.VALIDAR_ID_COMPANY % supplier.company_id
        resultado = db.execute(query, many=False)
        if not resultado:
            raise HTTPException(status_code=404, detail="A empresa (company_id) fornecida não existe.")
        
        repository = SupplierRepository()
        return repository.save(supplier)

    def get_supplier_id(self, id: int):
        repository = SupplierRepository()
        supplier = repository.get_id(id)
        return supplier