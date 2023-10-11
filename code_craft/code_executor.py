import os
import random
import shutil
import string
import subprocess
from dataclasses import dataclass
from enum import Enum


class Language(Enum):
    """
    Enum representing programming languages.
    """

    C = "c"
    CPP = "cpp"
    C_SHARP = "csharp"
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

# Directory where all the temporary directories will be stored.
_TEMPDIR_PREFIX = "/tmp/code-craft/code"
_TEMP_NAME_LEN = 10


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
    dirpath = __create_tempdir_and_paste_code(language, code)

    # Get the command to run the code based on given lagnuage
    run_cmd = __generate_run_command(language, "main")

    result = subprocess.run(
        run_cmd, shell=True, cwd=dirpath, text=True, capture_output=True
    )
    output = result.stdout
    exit_code = result.returncode

    # Remove code temp directory
    shutil.rmtree(dirpath)

    return CodeExecutionResult(output, exit_code)


def __generate_run_command(language: Language, filename: str) -> str:
    """
    Generate a command to run a file based on the given language and filepath.
    """
    EXT = _LANGUAGE_TO_FILE_EXTENSIONS[language]
    return {
        language.C: f"gcc {filename}.{EXT} -o {filename} && ./{filename}",
        language.CPP: f"g++ {filename}.{EXT} -o {filename} && ./{filename}",
        language.C_SHARP: f"mcs {filename}.{EXT} && mono {filename}.exe",
        language.JAVA: f"javac {filename}.{EXT} && java {filename}",
        language.JAVASCRIPT: f"node {filename}.{EXT}",
        language.PYTHON: f"python3 {filename}.{EXT}",
        language.RUBY: f"ruby {filename}.{EXT}",
    }[language]


def __create_tempdir_and_paste_code(language: Language, code: str) -> str:
    """
    Create a directory and paste the given code into a temporary file.
    Returns:
        Path to the temporary directory created.
    """

    random_dir = "".join(random.choices(string.ascii_letters, k=_TEMP_NAME_LEN))
    dirpath = f"{_TEMPDIR_PREFIX}/{random_dir}"
    os.makedirs(dirpath)

    with open(f"{dirpath}/main.{_LANGUAGE_TO_FILE_EXTENSIONS[language]}", "x") as f:
        f.write(code)

    return dirpath
