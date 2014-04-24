#! /bin/python
import sys
import os
import subprocess
import numpy


fileList = os.listdir(".")
for f in sorted(fileList):

    if not f.endswith(".txt"):
        continue
        
    if os.path.isdir(f):
        continue
        
        
    i = open(f, 'r')
    print(f)
    
    r = []
    for l in i:    
        #print(l)
        l_arr = l.split(":")
        r.append(float(l_arr[1]))
        
    arr = numpy.array(r)

    
    
    print(r)
    print(numpy.mean(arr))
    print(numpy.std(arr))
    
