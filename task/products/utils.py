from typing import Any, overload
from flask import abort

from task.database import NewProduct, ProductType


@overload
def validate_int(data: dict[str, Any], name: str, allow_float: bool) -> float: ...

@overload
def validate_int(data: dict[str, Any], name: str) -> int: ...


def validate_int(data: dict[str, Any], name: str, allow_float: bool = False):
    if (value := data.get(name)) is None:
        return abort(400, f"Missing {name}")
    # Booleans are subclasses of int
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        abort(400, f"Invalid {name}, must be an integer")
    elif isinstance(value, float) and not allow_float:
        abort(400, f"Invalid {name}, cannot be a decimal")
    elif value <= 0:
        abort(400, f"Invalid {name}, must be greater than 0")

    return value


@overload
def validate_product_type(value: Any, allow_none: bool) -> ProductType | None: ...


@overload
def validate_product_type(value: Any) -> ProductType: ...


def validate_product_type(value: Any, allow_none: bool = False):
    if value is None:
        if not allow_none:
            abort(400, "Missing product type")
        else:
            return None
    elif value not in ProductType:
        abort(
            400,
            "Invalid product type, must be one of 'book', 'gadget', 'food', 'other'",
        )
    else:
        return ProductType(value)


def validate_product(data: dict[str, str] | None):
    if not data:
        abort(400, "Missing product data")

    if not (name := data.get("name")):
        abort(400, "Missing product name")
    elif not isinstance(name, str) or name.isdigit():
        abort(400, "Invalid product name, must be a string")

    inventory = validate_int(data, "inventory")
    product_type = validate_product_type(data.get("type"))

    return NewProduct(name=name, type=product_type, inventory=inventory)
