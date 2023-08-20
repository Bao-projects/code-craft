def test_execute_code() -> None:
    """
    This test make sure the following happens when `execute_code` is called:
        1/ A temporary file is created and the given code is pasted into the file.
        2/ A correct command is used to run the file.
        3/ The file is deleted after the run is complete.
        4/ The output of the command is captured and returned along with the exit code.
    """
