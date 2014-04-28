#! /bin/python
import sys
import os
import subprocess
import numpy

def print_mean_std_dev(arr):

    a = numpy.array(arr)
    print(numpy.mean(a))
    print(numpy.std(a))

i = open("timing2.txt", 'r')

junk_arr = []
connect_arr =[]
import_arr = []
himesis_arr =[]
build_sim_arr = []
analysis_arr = []
transformation_arr = []
export_himesis_arr = []
export_simulink_arr = []

j =0
for l in i:

    #print(l)

    if "Model: " in l:
    
        if not j ==0:
        
            
            print("Connect:")
            print_mean_std_dev(connect_arr)
            connect_arr = []
            
            print("import:")
            print_mean_std_dev(import_arr)
            import_arr = []
            
            print("himesis:")
            print_mean_std_dev(himesis_arr)
            himesis_arr = []
            
            print("build:")
            print_mean_std_dev(build_sim_arr)
            build_sim_arr = []
            
            print("analysis:")
            print_mean_std_dev(analysis_arr)
            analysis_arr = []
            
            print("transformation:")
            print_mean_std_dev(transformation_arr)
            transformation_arr = []
            
            print("export:")
            print_mean_std_dev(export_himesis_arr)
            export_himesis_arr = []
            
            print("export_simulink:")
            print_mean_std_dev(export_simulink_arr)
            export_simulink_arr = []

        
        print("\n" + l)
        continue

    j = j + 1
    arr = junk_arr
    
    if "connect to Simulink" in l:
        arr = connect_arr
    elif "import from Simulink" in l:
        arr = import_arr
    elif "Himesis to CBD" in l:
        arr = himesis_arr
    elif "build simulator" in l:
        arr = build_sim_arr
    elif "for analysis" in l:
        #print(l)
        arr = analysis_arr
    elif "for transformation" in l:
        #print(l)
        arr = transformation_arr
    elif "CBD to Himesis" in l:
        arr = export_himesis_arr
    elif "export to Simulink" in l:
        arr = export_simulink_arr
        
    second = l.split(": ")[1]
    arr.append(float(second.split(" ")[0]))
    
print("Connect:")
print_mean_std_dev(connect_arr)
connect_arr = []

print("import:")
print_mean_std_dev(import_arr)
import_arr = []

print("himesis:")
print_mean_std_dev(himesis_arr)
himesis_arr = []

print("build:")
print_mean_std_dev(build_sim_arr)
build_sim_arr = []

print("analysis:")
print_mean_std_dev(analysis_arr)
analysis_arr = []

print("transformation:")
print_mean_std_dev(transformation_arr)
transformation_arr = []

print("export:")
print_mean_std_dev(export_himesis_arr)
export_himesis_arr = []

print("export_simulink:")
print_mean_std_dev(export_simulink_arr)
export_simulink_arr = []

