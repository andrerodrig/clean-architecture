from .models import ORMProduct
from .entities import Product

class ProductDatabaseRepo:
    
    def get_product(self, reference):
        orm_product = ORMProduct.objects.get(reference=reference)

        return self._decode_orm_product(orm_product)

    def _decode_orm_product(self,orm_product):
        return Product(
            reference=orm_product.reference,
            brand_id=orm_product.brand_id
        )
