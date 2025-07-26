import subprocess
import os

process = subprocess.Popen(['/bin/bash'], shell = False, stdin = subprocess.PIPE, stdout = subprocess.PIPE) #basically starts a shell that we can write into with stdin.write and read from with stdout.readline

