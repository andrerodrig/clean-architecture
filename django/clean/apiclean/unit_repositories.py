class ProductRepo:

    def __init__(self, db_repo):
        self.db_repo = db_repo

    def get_product(self, reference):
        product = self.db_repo.get_products(reference)

        return product
