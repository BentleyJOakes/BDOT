from CBDsimulator import *
import numpy as np
from Models.ConstantFoldingCBD import *
from Optimizations.ConstantFoldingOptimization import *

from HimesisToCBD.HimesisToCBD import *
from HimesisToCBD.CBDToHimesis import *


from Server.Core.MatlabHelper import MatlabHelper
from Server.Core.SimulinkExporter import SimulinkExporter
from Server.Core.SimulinkModelToHimesis import SimulinkModelToHimesis
from Server.Core.SimulinkTransformationToTCore import SimulinkTransformationToHimesis
from Server.TCore.core.himesis import Himesis
from Server.TCore.t_core.messages import Packet


class OptimizationExperiment:

    def __init__(self):


        self.mh = MatlabHelper()
        
    
    def run(self, path, model):
        self.mh.chDir(path)
    
        #turn Simulink model into himesis graph
        #modelToHimesis = SimulinkModelToHimesis(self.mh,model,path)
        #modelToHimesis.SimulinkModelToHimesis()
        
        hToCBD = HimesisToCBD()
        self.model = hToCBD.convertFile("himesis/" + Himesis.standardize_name(model) + ".py")
        
        #TODO: only needed for dep graph, should remove this
        self.simulator = CBDsimulator(self.model)
        
        
        CBDOpt = ConstantFoldingOptimization(self.simulator)
        #self.model = CBDOpt.optimize(self.model)

        CBDToH = CBDToHimesis()
        h = CBDToH.convert(self.model)
        h.compile("himesis/")
 
 
        
        simulinkExport = SimulinkExporter(model,self.mh,h)
        simulinkExport.exportSimulink()
 
 
 
 
 
 
 
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
    model = "HConstfolding"
    
    experiment = OptimizationExperiment()
    
    experiment.run(path, model)
    
    
    

    #experiment.dumpModel()
    #experiment.run()
    #experiment.dumpSignals()

    #t = np.arange(0.0, 10.0, 0.001)
    #experiment.showScopes(t)

