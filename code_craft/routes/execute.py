import json
from flask import Response, jsonify, request

from . import routes
from code_craft.code_executor import execute_code, CodeExecutionResult, Language
from code_craft.routes.helper.responses import FailureResult, ExecutionResult


@routes.route("/execute", methods=["GET"])
def execute() -> Response:
    """
    REST API to execute a given block of code.
    Accepts 2 parameters: `language` and `code`.
    """

   # Check if both language and code are provided in the request
    if "language" not in request.form or "code" not in request.form:
        return FailureResult("Invalid input, missing code or language").to_flask_response()

    # Get the language and code
    language_str = request.form["language"]
    code = request.form["code"]

    if not language_str or not code:
        return FailureResult("Invalid input, empty code or language").to_flask_response()

    # Check if the provided language is valid
    if language_str.lower() not in [lang.value for lang in Language]:
        return FailureResult(f"{language_str} is not a valid language").to_flask_response()

    # Execute the given block of code
    result = execute_code(Language(language_str), code)
    return ExecutionResult(result.output, result.exit_code).to_flask_response()
    