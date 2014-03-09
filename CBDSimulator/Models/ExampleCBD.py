from math import *
from CBD import *

class ExampleCBD(CBD):

  def __init__(self, block_name):

    # Don't forget to call the superclass' constructor!
    CBD.__init__(self, block_name)

    # Only for hard-coded Integrator and Derivative    
    self.delta_t = 0.001

    # Blocks can be instantiated and added immediately to the CBD
    self.addBlock(ConstantBlock(block_name="c1", value=1.0))
    self.addBlock(ConstantBlock(block_name="c2"))
    self.addBlock(ConstantBlock("c3", value=3.0))
    self.addBlock(AdderBlock(block_name="a"))
    self.addBlock(DelayBlock(block_name="d"))
    """self.addBlock(NegatorBlock(block_name="n"))
    self.addBlock(NegatorBlock(block_name="nn"))"""
    self.addBlock(ProductBlock(block_name="p"))
    # A generic function block using the Math library's "sin" operator
    """self.addBlock(GenericBlock(block_name="g", block_operator="sin"))
    # A hard-coded Integrator
    self.addBlock(IntegratorBlock(block_name="integ", time_increment=self.delta_t))
    # A hard-coded Derivative
    self.addBlock(DerivativeBlock(block_name="deriv", time_increment=self.delta_t))
    self.addBlock(TestBlock(block_name="tst"))"""

    # Connection between output of block c1 and input of block a
    self.addConnection("c1", "a")

    self.addConnection("c3", "p")

    self.addConnection("p", "d")
    
    self.addConnection("a", "p")

    self.addConnection("d", "a")
    # Connection between output of block c3 and name input port IC of block a
    self.addConnection("c2", "d", port_name="IC")

    """self.addConnection("d", "a")
    
    self.addConnection("d", "n")

    self.addConnection("n", "p")
    self.addConnection("d", "p")

    self.addConnection("p", "g")

    self.addConnection("c1", "integ")
    self.addConnection("c2", "integ", port_name="IC")

    self.addConnection("integ", "nn")

    self.addConnection("integ", "deriv")
    self.addConnection("c2", "deriv", port_name="IC")

    self.addConnection("integ", "tst")
    self.addConnection("c3", "tst", port_name="TRUE")
    self.addConnection("c1", "tst", port_name="FALSE")
     
    # Blocks can be instantiated and referred to by a Python variable
    c11 = ConstantBlock(block_name="c11", value=100.0)
    # Adding blocks can be by name (as above) or by reference to an instance block (as here) 
    self.addBlock(c11)

    i = InverterBlock(block_name="i")
    self.addBlock(i)

    self.addConnection("c11", "i")

    # The main use of explicitly using a Python variable 
    # is to create and link many blocks by means of a loop 
    previous = c11
    blockname_prefix = "negator_"
    for i in range(10):
      newblock = NegatorBlock(blockname_prefix+str(i+1))
      self.addBlock(newblock)
      self.addConnection(previous, newblock)
      previous = newblock"""

if __name__=="__main__":
  myCBD = ExampleCBD("myCBD")
  myCBD.dump()
  myCBD.dumpSignals()

