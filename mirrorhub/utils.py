"""Submodules which provides useful helper methods."""
from subprocess import run, DEVNULL, STDOUT


def exec_cmd(command):
    """Execute a shell command.

    Args:
        command (str): shell command
    """
    run(command, stdout=DEVNULL, stderr=STDOUT, shell=True)
