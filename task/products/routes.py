from typing import Any
from flask import Blueprint, jsonify, request

from task import db
from task.database import NewProduct
from task.products.validation import ProductSchema

products = Blueprint("products", __name__, url_prefix="/products")
prod_schema = ProductSchema()


@products.route("/", methods=["GET"])
def get_products():
    prod_type: dict[str, Any] = prod_schema.load(request.args, partial=True)  # type: ignore[]
    return jsonify(db.get_products(prod_type.get("type"))), 200


@products.route("/", methods=["POST"])
def add_product():
    data: NewProduct = prod_schema.load(request.json)  # type: ignore[]
    product = db.add_product(data)
    return jsonify({"id": product["id"]}), 201
