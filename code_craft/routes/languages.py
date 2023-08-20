from . import routes

from flask import jsonify
from code_craft.code_executor import Language


@routes.route("/languages")
def languages():
    """
    GET API to get a list of supported programming languages.
    """
    langs = [lang.value for lang in Language]
    return jsonify(
        {
            "success": True,
            "data": langs
        }
    )
