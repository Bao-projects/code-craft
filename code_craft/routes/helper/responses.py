from dataclasses import dataclass

from flask import jsonify
from flask import Response


@dataclass
class ExecutionResult:
    stdout: str
    stderr: str
    exit_code: int

    def to_flask_response(self) -> tuple[Response, int]:
        return (
            jsonify(
                {
                    "success": True,
                    "data": {
                        "stdout": self.stdout,
                        "stderr": self.stderr,
                        "exit_code": self.exit_code,
                    },
                }
            ),
            200,
        )


@dataclass
class FailureResult:
    error_messsage: str

    def to_flask_response(self) -> tuple[Response, int]:
        return jsonify({"success": False, "error_message": self.error_messsage}), 400
