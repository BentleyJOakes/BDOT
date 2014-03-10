from CBDsimulator import *
import numpy as np
from Models.ConstantFoldingCBD import *
from Optimizations.ConstantFoldingOptimization import *

class OptimizationExperiment:

  def __init__(self):
    self.model  = ConstantFoldingCBD("ConstantFoldingCBD")
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
  #experiment.dumpModel()
  
  CBDOpt = ConstantFoldingOptimization(experiment.simulator)
  CBDOpt.optimize(experiment.model)
  
  #experiment.dumpModel()
  #experiment.run()
  #experiment.dumpSignals()
  
  #t = np.arange(0.0, 10.0, 0.001)
  #experiment.showScopes(t)

