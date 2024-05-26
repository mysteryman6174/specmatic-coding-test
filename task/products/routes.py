from flask import Blueprint, jsonify, request

from task.products.utils import validate_product, validate_product_type
from task import db

products = Blueprint("products", __name__, url_prefix="/products")


@products.route("/", methods=["GET"])
def get_products():
    product_type = validate_product_type(request.args.get("type"), allow_none=True)
    return jsonify(db.get_products(product_type)), 200


@products.route("/", methods=["POST"])
def add_product():
    data = validate_product(request.json)
    product = db.add_product(data)
    return jsonify({"id": product["id"]}), 201
