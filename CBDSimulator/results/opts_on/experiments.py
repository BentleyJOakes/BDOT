#! /bin/python
import sys
import os
import subprocess


def do_command(command):
    print(command)
    subprocess.call(command, shell=True)




time_command = "/usr/bin/time -f'%E'"
fileList = os.listdir(".")
for f in fileList:

    if f.endswith(".mat") or f.endswith(".py") or f.endswith(".txt"):
        continue
        
    if os.path.isdir(f):
        continue
        
    if not "HConstfolding_hier" in f:
        continue
        
    command = time_command + " ./" + f + " 2> " + f + "_timing.txt"
    do_command(command)
    
    for i in range(5):
        command = time_command + " ./" + f + " 2>> " + f + "_timing.txt"
        do_command(command)
