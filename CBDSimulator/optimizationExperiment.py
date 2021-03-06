from CBDsimulator import *
import numpy as np
from Models.ConstantFoldingCBD import *
from Optimizations.ConstantFoldingOptimization import *
from Optimizations.FlatteningOptimization import *
from Optimizations.DeadBlockRemovalOptimization import *

from HimesisToCBD.HimesisToCBD import *
from HimesisToCBD.CBDToHimesis import *


from Server.Core.MatlabHelper import MatlabHelper
from Server.Core.SimulinkExporter import SimulinkExporter
from Server.Core.SimulinkModelToHimesis import SimulinkModelToHimesis
from Server.Core.SimulinkTransformationToTCore import SimulinkTransformationToHimesis
from Server.TCore.core.himesis import Himesis
from Server.TCore.t_core.messages import Packet
import time

import sys

class OptimizationExperiment:

    def __init__(self, skip_simulink = False):

        self.skip_simulink = skip_simulink
        
        if skip_simulink:
            self.mh = None
        else:
        
            start = time.time()
            
            self.mh = MatlabHelper()
            
            end = time.time()
            print("Time taken to connect to Simulink: " + str(end - start) + " seconds")
        
    
    def run(self, path, model, opt_name):
    
        if not self.mh == None:
        
            start = time.time()
            self.mh.chDir(path)

            
            #turn Simulink model into himesis graph
            modelToHimesis = SimulinkModelToHimesis(self.mh,model,path)
            modelToHimesis.SimulinkModelToHimesis()
         
            end = time.time()
            print("Time taken to import from Simulink: " + str(end - start) + " seconds")
            
            #draw model
            #print("Start drawing")
            #self.mh.drawSystem(model, "~/")
            #print("End drawing")
        
        
        start = time.clock()
        hToCBD = HimesisToCBD()
        self.model = hToCBD.convertFile("himesis/" + Himesis.standardize_name(model) + ".py")
        end = time.clock()
        print("Time taken for Himesis to CBD: " + str(end - start) + " seconds")
        
        
        
        #TODO: only needed for dep graph, should remove this
        start = time.clock()
        self.simulator = CBDsimulator(self.model)
        end = time.clock()
        print("Time taken to build simulator: " + str(end - start) + " seconds")
        
        opt = opt_name(self.simulator, self.mh)
        self.model = opt.optimize(self.model)

        start = time.clock()
        CBDToH = CBDToHimesis()
        h = CBDToH.convert(self.model)
        h2 = CBDToH.convert(self.model, False)
        h.compile("himesis/")
        end = time.clock()
        print("Time taken for CBD to Himesis: " + str(end - start) + " seconds")
 
 
        if not self.mh == None:
        
            start = time.clock()
            simulinkExport = SimulinkExporter(model,self.mh,h)
            simulinkExport.exportSimulink()
            end = time.clock()
            print("Time taken to export to Simulink: " + str(end - start) + " seconds")
            
            self.mh.endLib()
 

        
 
    #CBD functions
    def run2(self, num_steps=10): # one step = {NOW}
        for i in range(num_steps):
            self.simulator.step()

    def dumpModel(self):
     self.model.dump()

    def dumpSignals(self):
        self.model.dumpSignals()

    def showScopes(self,t):
        self.model.showScopes(t)
  
if __name__=="__main__":


    

    args = sys.argv
    
    if len(args) == 0:
        path = "./examples/"
        model = "HSimpleConst"
        opt = "ConstantFolding"
    else:
        path = "./examples/"
        model = sys.argv[1]
        opt = sys.argv[2]
 
    experiment = OptimizationExperiment(skip_simulink=False)
    
    if opt == "ConstantFolding":
        opt = ConstantFoldingOptimization
    elif opt == "Flattening":
        opt = FlatteningOptimization
    elif opt == "DeadBlock":
        opt = DeadBlockRemovalOptimization
    
    
    experiment.run(path, model, opt)
    
    
    

    #experiment.dumpModel()
    #experiment.run()
    #experiment.dumpSignals()

    #t = np.arange(0.0, 10.0, 0.001)
    #experiment.showScopes(t)

