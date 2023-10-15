from flask import Flask
from flask_cors import CORS

from code_craft.routes import *


app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"
app.register_blueprint(routes)


if __name__ == "__main__":
    app.run()
