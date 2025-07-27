import subprocess
import os

#process = subprocess.Popen(['/bin/bash'], shell = False, stdin = subprocess.PIPE, stdout = subprocess.PIPE) #basically starts a shell that we can write into with stdin.write and read from with stdout.readline

def get_subdomains(website):
    """Gets subdomains using various OSINT tools, does not work for CTFs or websites with small footprints"""
    return subprocess.check_output(['assetfinder', '--subs-only', website])

def scan_ports(ip):
    """Uses nmap to scan ports"""
    return subprocess.check_output(['nmap', '-sC', '-sV', ip])
