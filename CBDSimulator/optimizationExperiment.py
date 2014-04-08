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
        
    
    def run(self, path, model):
    
        if not self.mh == None:
        
            start = time.time()
            self.mh.chDir(path)

            
            
            #turn Simulink model into himesis graph
            modelToHimesis = SimulinkModelToHimesis(self.mh,model,path)
            modelToHimesis.SimulinkModelToHimesis()
            
            end = time.time()
            print("Time taken to import from Simulink: " + str(end - start) + " seconds")
        
        
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
        
        #Opt = ConstantFoldingOptimization(self.simulator)

        #Opt = FlatteningOptimization(self.simulator, self.mh)
        Opt = DeadBlockRemovalOptimization(self.simulator)
        
        self.model = Opt.optimize(self.model)

        start = time.clock()
        CBDToH = CBDToHimesis()
        h = CBDToH.convert(self.model)
        h.compile("himesis/")
        end = time.clock()
        print("Time taken for CBD to Himesis: " + str(end - start) + " seconds")
 
 
        if not self.mh == None:
        
            start = time.clock()
            simulinkExport = SimulinkExporter(model,self.mh,h)
            simulinkExport.exportSimulink()
            end = time.clock()
            print("Time taken to export to Simulink: " + str(end - start) + " seconds")
 
 
 
 
 
 
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

    path = "./examples/"
    model = "HDead"
    
    experiment = OptimizationExperiment(skip_simulink=True)
    
    experiment.run(path, model)
    
    
    

    #experiment.dumpModel()
    #experiment.run()
    #experiment.dumpSignals()

    #t = np.arange(0.0, 10.0, 0.001)
    #experiment.showScopes(t)

