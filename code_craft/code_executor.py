from dataclasses import dataclass
from enum import Enum


class Language(Enum):
    C = "c"
    CPP = "cpp"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    RUBY = "ruby"


_LANGUAGE_TO_FILE_EXTENSIONS: dict[Language, str] = {
    Language.C: "c",
    Language.CPP: "cpp",
    Language.JAVA: "java",
    Language.JAVASCRIPT: "js",
    Language.PYTHON: "py",
    Language.RUBY: "rb",
}


@dataclass
class CodeExecutionResult:
    output: str
    exit_code: int


def execute_code(language: Language, code: str) -> CodeExecutionResult:
    pass


def __create_temp_file(language: Language) -> str:
    pass
