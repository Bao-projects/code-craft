from dataclasses import dataclass
from enum import Enum


class Language(Enum):
    """
    Enum representing programming languages.
    """

    C = "c"
    CPP = "cpp"
    JAVA = "java"
    JAVASCRIPT = "javascript"
    PYTHON = "python"
    RUBY = "ruby"


# Map a programming language enum to its corresponding file extension.
_LANGUAGE_TO_FILE_EXTENSIONS: dict[Language, str] = {
    Language.C: "c",
    Language.CPP: "cpp",
    Language.JAVA: "java",
    Language.JAVASCRIPT: "js",
    Language.PYTHON: "py",
    Language.RUBY: "rb",
}

# Directory where the temp files will be stored.
_TEMPFILES_DIR = "/tmp/code-craft/code"


@dataclass
class CodeExecutionResult:
    """
    Represents a code execution result.
    """

    output: str
    exit_code: int


def execute_code(language: Language, code: str) -> CodeExecutionResult:
    """
    Execute a piece of code.

    Args:
        language (Language): The programming language the code is written in.
        code (str): The piece of code to execute.
    """
    return CodeExecutionResult("hello world", 0)


def __generate_run_command(language: Language, filename: str) -> str:
    """
    Generate a command to run a file based on the given language and filepath.
    """
    EXT = _LANGUAGE_TO_FILE_EXTENSIONS[language]
    return {
        language.C: f"gcc {filename}.{EXT} -o {filename} && {filename}",
        language.CPP: f"g++ {filename}.{EXT} -o {filename} && {filename}",
        language.JAVA: f"javac {filename}.{EXT} && java {filename}",
        language.JAVASCRIPT: f"node {filename}.{EXT}",
        language.PYTHON: f"python3 {filename}.{EXT}",
        language.RUBY: f"ruby {filename}.{EXT}",
    }[language]


def __create_tempfile_and_paste_code(filepath: str, code: str) -> bool:
    """
    Create a file from the given path and paste the given code into the file.

    Returns:
        True if the process was successful, False otherwise.
    """


def __generate_random_filename() -> str:
    """
    Generate a random string to be used as a name for a temporary file.
    """


def __delete_file(filepath: str) -> None:
    """
    Delete a given file.
    """
