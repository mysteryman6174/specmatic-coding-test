import enum
from typing import TypedDict


class MetaEum(enum.EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class ProductType(str, enum.Enum, metaclass=MetaEum):
    BOOK = "book"
    GADGET = "gadget"
    FOOD = "food"
    OTHER = "other"


class NewProduct(TypedDict):
    name: str
    type: ProductType
    inventory: int


class Product(NewProduct):
    id: int


class Database:
    def __init__(self):
        self.data: list[Product] = []
        self.length = 0

    # PRODUCT METHODS
    def get_products(self, product_type: "ProductType|None" = None) -> list[Product]:
        if product_type:
            return [product for product in self.data if product["type"] == product_type]
        return self.data

    def add_product(self, data: NewProduct) -> Product:
        product: Product = {**data, "id": self.length + 1}
        self.data.append(product)
        self.length += 1
        return product
