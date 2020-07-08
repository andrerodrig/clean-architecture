class Product:

    def __init__(self, reference, brand_id):
        self._reference = reference
        self._brand_id = brand_id

    @property
    def reference(self):
        return self._reference

    @property
    def brand_id(self):
        return self._brand_id
        