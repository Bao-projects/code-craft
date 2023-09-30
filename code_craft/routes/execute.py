from flask import request
from flask import Response

from . import routes
from code_craft.code_executor import execute_code
from code_craft.code_executor import Language
from code_craft.routes.helper.responses import ExecutionResult
from code_craft.routes.helper.responses import FailureResult


@routes.route("/execute", methods=["GET"])
def execute() -> Response:
    """
    REST API to execute a given block of code.
    Accepts 2 parameters: `language` and `code`.
    """

    # Check if both language and code are provided in the request and not empty
    for input_arg in ["language", "code"]:
        if input_arg not in request.form:
            return FailureResult(
                f"Input missing field '{input_arg}'"
            ).to_flask_response()
        elif not request.form[input_arg].strip():
            return FailureResult(
                f"Input field '{input_arg}' is empty"
            ).to_flask_response()

    # Get the language and code
    language_str = request.form["language"]
    code = request.form["code"]

    # Check if the provided language is valid
    if language_str.lower() not in [lang.value for lang in Language]:
        return FailureResult(
            f"{language_str} is not a valid language"
        ).to_flask_response()

    # Execute the given block of code
    result = execute_code(Language(language_str), code)
    return ExecutionResult(result.output, result.exit_code).to_flask_response()
