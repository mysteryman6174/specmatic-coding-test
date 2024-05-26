from datetime import datetime

from flask import Flask, json, request
from werkzeug.exceptions import HTTPException

from task.database import Database

app = Flask(__name__)
app.url_map.strict_slashes = False
db = Database()


@app.errorhandler(HTTPException)
def http_error_handler(e):
    response = e.get_response()
    response.data = json.dumps(
        {
            "timestamp": datetime.now().isoformat(),
            "path": request.path,
            "status": e.code,
            "error": e.name,
        }
    )
    response.content_type = "application/json"
    return response


from task.products.routes import products  # noqa: E402

app.register_blueprint(products)
