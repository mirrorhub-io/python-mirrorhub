"""Submodules which provides useful helper methods."""
from subprocess import run, DEVNULL, STDOUT


def exec_cmd(command):
    """Execute a shell command.

    Args:
        command (str): shell command
    """
    run(command, stdout=DEVNULL, stderr=STDOUT, shell=True)


def exec_rsync(source, dest):
    """Sync files from the source url to destination path.

    Args:
        source (str): source url to sync from
        dest (str): destination path
    """
    exec_cmd(' '.join(['/usr/bin/rsync', '-rlvh', '--update', '--delete',
                       'rsync://' + source, dest]))
