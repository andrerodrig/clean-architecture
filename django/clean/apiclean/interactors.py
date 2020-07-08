class GetProductInteractor:
    
    def __init__(self, product_repo):
        self.product_repo = product_repo

    def set_params(self,reference):
        self.reference = reference
        return self

    def execute(self):
        return self.product_repo.get_product(reference=self.reference)