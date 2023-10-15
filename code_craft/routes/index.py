from flask_cors import cross_origin

from . import routes


@routes.route("/")
@cross_origin()
def index():
    return "hello from code-craft"
