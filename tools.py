import subprocess
import os
import json

def run_command(command, args):
    '''
    command is a string, args is a list
    takes the inputs and runs them in the bash shell
    '''
    #basically starts a shell that we can write into with stdin.write and read from with stdout.readline
    process = subprocess.Popen(['/bin/bash'], shell = False, stdin = subprocess.PIPE, stdout = subprocess.PIPE)

    exec = command + ' ' + ' '.join(args)
    ret = process.communicate(str.encode(exec))
    return ret

#testing
print(run_command('echo', ['testing', 'test']))
