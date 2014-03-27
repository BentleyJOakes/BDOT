from CBDsimulator import *
import numpy as np
from Models.ConstantFoldingCBD import *
from Optimizations.ConstantFoldingOptimization import *

from HimesisToCBD.HimesisToCBD import *


from Server.Core.MatlabHelper import MatlabHelper
from Server.Core.SimulinkExporter import SimulinkExporter
from Server.Core.SimulinkModelToHimesis import SimulinkModelToHimesis
from Server.Core.SimulinkTransformationToTCore import SimulinkTransformationToHimesis
from Server.TCore.core.himesis import Himesis
from Server.TCore.t_core.messages import Packet


class OptimizationExperiment:

  def __init__(self):
  
  
    self.matlabHelper = MatlabHelper()
    #self.model  = ConstantFoldingCBD("ConstantFoldingCBD")
    hToCBD = HimesisToCBD()
    self.model = hToCBD.convertFile("HimesisToCBD/Models/HEasy2.py")
    
    self.simulator = CBDsimulator(self.model)
 
  def run(self, num_steps=10): # one step = {NOW}
    for i in range(num_steps):
      self.simulator.step()

  def dumpModel(self):
    self.model.dump()

  def dumpSignals(self):
    self.model.dumpSignals()

  def showScopes(self,t):
      self.model.showScopes(t)
  
if __name__=="__main__":

  experiment = OptimizationExperiment()
  experiment.dumpModel()
  
  CBDOpt = ConstantFoldingOptimization(experiment.simulator)
  experiment.model = CBDOpt.optimize(experiment.model)
  
  CBDToH = CBDToHimesis()
  h = CBDToH.convert(experiment.model)
  h.compile("HimesisToCBD/Models")
  
  #experiment.dumpModel()
  #experiment.run()
  #experiment.dumpSignals()
  
  #t = np.arange(0.0, 10.0, 0.001)
  #experiment.showScopes(t)

