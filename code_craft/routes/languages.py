from flask import jsonify
from flask_cors import cross_origin

from . import routes
from code_craft.code_executor import Language


@routes.route("/languages")
@cross_origin()
def languages():
    """
    GET API to get a list of supported programming languages.
    """
    langs = [lang.value for lang in Language]
    return jsonify({"success": True, "data": langs})
