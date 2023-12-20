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
    PERL = "perl"
    PHP = "php"
    GO = "go"
    RUST = "rust"


# Map a programming language enum to its corresponding file extension.
_LANGUAGE_TO_FILE_EXTENSIONS: dict[Language, str] = {
    Language.C: "c",
    Language.CPP: "cpp",
    Language.C_SHARP: "cs",
    Language.JAVA: "java",
    Language.JAVASCRIPT: "js",
    Language.PYTHON: "py",
    Language.RUBY: "rb",
    Language.PERL: "pl",
    Language.PHP: "php",
    Language.GO: "go",
    Language.RUST: "rs",
}

# Directory where all the temporary directories will be stored.
_TEMPDIR_PREFIX = "/tmp/code-craft/code"
_TEMP_NAME_LEN = 10


@dataclass
class CodeExecutionResult:
    """
    Represents a code execution result.
    """

    stdout: str
    stderr: str
    exit_code: int


def execute_code(language: Language, code: str) -> CodeExecutionResult:
    """
    Execute a piece of code.

    Args:
        language (Language): The programming language the code is written in.
        code (str): The piece of code to execute.
    """
    dirpath, main_file = __create_tempdir_and_paste_code(language, code)

    # Get the command to run the code based on given language
    run_cmd = __generate_run_command(language, dirpath, main_file)
    result = subprocess.run(run_cmd, shell=True, capture_output=True, text=True)

    # Remove code temp directory
    shutil.rmtree(dirpath)

    return CodeExecutionResult(result.stdout, result.stderr, result.returncode)


def __generate_run_command(language: Language, dir: str, filename: str) -> list[str]:
    """
    Generate a command to run a file based on the given language and filepath.
    """
    file_name_no_ext = ".".join(filename.split(".")[:-1])

    return {
        language.C: f"cd {dir} && gcc {filename} && ./a.out",
        language.CPP: f"cd {dir} && g++ {filename} && ./a.out",
        language.C_SHARP: f"cd {dir} && mcs {filename} && mono {file_name_no_ext}.exe",
        language.JAVA: f"cd {dir} && javac {filename} && java {file_name_no_ext}",
        language.JAVASCRIPT: f"node {dir}/{filename}",
        language.PYTHON: f"python3 {dir}/{filename}",
        language.RUBY: f"ruby {dir}/{filename}",
        language.PERL: f"perl {dir}/{filename}",
        language.PHP: f"php {dir}/{filename}",
        language.GO: f"cd {dir} && go run {filename}",
        language.RUST: f"cd {dir} && rustc {filename} && ./{file_name_no_ext}",
    }[language]


def __create_tempdir_and_paste_code(language: Language, code: str) -> tuple[str, str]:
    """
    Create a directory and paste the given code into a temporary file.
    Returns:
        Path to the temporary directory created.
    """
    random_dir = "".join(random.choices(string.ascii_letters, k=_TEMP_NAME_LEN))
    dirpath = f"{_TEMPDIR_PREFIX}/{random_dir}"
    os.makedirs(dirpath)

    main_file = f"main.{_LANGUAGE_TO_FILE_EXTENSIONS[language]}"
    if language == Language.JAVA:
        main_file = "Main.java"

    with open(f"{dirpath}/{main_file}", "x") as f:
        f.write(code)

    return dirpath, main_file
