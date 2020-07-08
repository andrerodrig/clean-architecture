from .repositories import ProductDatabaseRepo
from .unit_repositories import ProductRepo
from .interactors import GetProductInteractor


class ProductDatabaseRepoFactory:

    @staticmethod
    def get():
        return ProductDatabaseRepo()

    
class ProductRepoFactory:

    @staticmethod
    def get():
        db_repo = ProductDatabaseRepoFactory.get()

        return ProductRepo(db_repo)
        
    
class GetProductInteractorFactory:
    
    @staticmethod
    def get():
        product_repo = ProductRepoFactory.get()
        return GetProductInteractor(product_repo)


class ProductViewFactory:

    @staticmethod
    def create():
        get_product_interactor = GetProductInteractorFactory.get()
        return ProductView(get_product_interactor)