from datetime import datetime
from flask import Flask, jsonify, request
from marshmallow.exceptions import ValidationError
from openapi_parser import parse
from task.database import Database

app = Flask(__name__)
app.url_map.strict_slashes = False
api_specs = parse("products_api.yaml")
db = Database()


@app.errorhandler(ValidationError)
def http_error_handler(e: "ValidationError"):
    return jsonify(
        {
            "timestamp": datetime.now().isoformat(),
            "path": request.path,
            "status": 400,
            "error": "Bad Request",
        }
    ), 400


from task.products.routes import products  # noqa: E402

app.register_blueprint(products)
