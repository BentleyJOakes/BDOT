#! /bin/python
import sys
import os
import subprocess
from optimizationExperiment import *


#quick and dirty script to execute the optimizations on all models


def do_command(command):
    print(command)
    subprocess.call(command, shell=True)

constant_folding_models = ['HSimpleConst', 'Const1', 'Const2', 'HConstfolding']
dead_block_models = ['HSimpleConstDead']
flattening_models = ['HConstfolding_hier', 'Flatten1', 'Flatten2', 'Flatten2_export']

for model in constant_folding_models + dead_block_models + flattening_models:

    print ("Model: " + model)
    for i in range(5):
        experiment = OptimizationExperiment(skip_simulink=False)
        
        if model in constant_folding_models:
            opt = ConstantFoldingOptimization
        elif model in dead_block_models:
            opt = DeadBlockRemovalOptimization
            
        elif model in flattening_models:
            opt = FlatteningOptimization
        
        experiment.run("./examples/", model, opt)
    
