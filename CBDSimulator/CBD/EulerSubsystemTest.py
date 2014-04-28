__author__ = 'Bart'

from CBD import *
from Subsystems.Integrators.EulerIntegrator import *
from Subsystems.Time.TimeModel import *

class EulerSubsystemTest(CBD):

  def __init__(self, block_name):
      # Don't forget to call the superclass' constructor!
      CBD.__init__(self, block_name)

      # Blocks can be instantiated and added immediately to the CBD
      self.addBlock(ConstantBlock("IC"))
      #self.addBlock(ConstantBlock("IN",value = 1))
      self.addBlock(TimeModel("time"))
      self.addBlock(AdderBlock("a"))
      self.addBlock(EulerIntegrator("integratorEuler"))


      self.addConnection("time","a",outport_name="OUT")
      self.addConnection("integratorEuler","a",outport_name="OUT")
      self.addConnection("a","integratorEuler",inport_name="IN")

      self.addConnection("IC","integratorEuler", inport_name = "IC")










  
