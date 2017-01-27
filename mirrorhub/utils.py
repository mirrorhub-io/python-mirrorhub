'''submodules which provides useful helper methods'''
from subprocess import run, DEVNULL, STDOUT

def exec_cmd(command):
    '''execute a shell command
    args:
        command (str): shell command'''
    run(command, stdout=DEVNULL, stderr=STDOUT, shell=True)
