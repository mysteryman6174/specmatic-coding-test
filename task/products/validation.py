from marshmallow import Schema, fields, validate
from task import api_specs

product_types = api_specs.schemas["ProductType"]

if not product_types.enum:
    raise ValueError("Missing product types in OpenAPI spec")


class ProductSchema(Schema):
    name = fields.String(required=True)
    type = fields.String(validate=validate.OneOf(product_types.enum), required=True)
    inventory = fields.Integer(required=True)
    cost = fields.Float(required=True)
