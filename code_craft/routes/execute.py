from flask import Response

from . import routes


@routes.route("/execute", methods=["GET"])
def execute() -> Response:
    """
    REST API to execute a given block of code.
    Accepts 2 parameters: `language` and `code`.
    """
    language in [lan.value for lan in Language]
