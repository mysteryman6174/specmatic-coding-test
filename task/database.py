from typing import TypedDict


class NewProduct(TypedDict):
    name: str
    type: str
    inventory: int
    cost: float


class Product(NewProduct):
    id: int


class Database:
    def __init__(self):
        self.data: list[Product] = []
        self.length = 0

    # PRODUCT METHODS
    def get_products(self, product_type: "str|None" = None) -> list[Product]:
        if product_type:
            return [product for product in self.data if product["type"] == product_type]
        return self.data

    def add_product(self, data: NewProduct) -> Product:
        product: Product = {**data, "id": self.length + 1}
        self.data.append(product)
        self.length += 1
        return product
