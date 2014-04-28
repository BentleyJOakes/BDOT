from math import *
from CBD import *

class ConstantFoldingCBD(CBD):

  def __init__(self, block_name):

    # Don't forget to call the superclass' constructor!
    CBD.__init__(self, block_name)

    # Only for hard-coded Integrator and Derivative    
    self.delta_t = 0.001

    # Blocks can be instantiated and added immediately to the CBD
    self.addBlock(ConstantBlock(block_name="c1", value=1.0))
    self.addBlock(ConstantBlock(block_name="c2"))
    self.addBlock(ConstantBlock("c3", value=3.0))
    
    self.addBlock(ConstantBlock("c4", value=4.4))
    self.addBlock(ConstantBlock("c5", value=5.2))
    self.addBlock(ConstantBlock("c6", value=6.1))
    
    
    self.addBlock(AdderBlock(block_name="add1"))
    self.addBlock(AdderBlock(block_name="add2"))
    
    self.addBlock(DelayBlock(block_name="delay1"))

    self.addBlock(ProductBlock(block_name="product1"))
    self.addBlock(ProductBlock(block_name="product2"))


    # Connection between output of block c1 and input of block a
    self.addConnection("c1", "add1")
    self.addConnection("c2", "delay1", inport_name="IC")
    self.addConnection("c3", "add2")
    
    self.addConnection("c4", "product2")
    self.addConnection("c5", "product2")
    self.addConnection("c6", "product2")

    self.addConnection("delay1", "add1")
    
    self.addConnection("product1", "delay1")
    
    self.addConnection("add1", "product1")
    self.addConnection("add2", "product1")

    self.addConnection("product2", "add2")



if __name__=="__main__":
  myCBD = ConstantFoldingCBD("myCBD")
  myCBD.dump()
  myCBD.dumpSignals()

