__author__ = 'Bart'

from CBD import *

class EulerIntegrator(CBD):
    def __init__(self, block_name,deltaT = 1.0):
        CBD.__init__(self, block_name)

        # Add Blocks
        #self.addBlock(DelayBlock("d_in"))
        self.addBlock(DelayBlock("d_out"))
        self.addBlock(ProductBlock("p1"))
        self.addBlock(AdderBlock("a1"))
        #self.addBlock(ConstantBlock("IC_d_in"))

        #self.addBlock(ConstantBlock("IC_d_out")) #replaced by inputblock
        self.addBlock(InputBlock("IC"))
        self.addBlock(ConstantBlock("delta_T", value = deltaT)) # TODO think about what to do with timestep... give in init or change block by inputblock and define step external???
        #self.addBlock(ConstantBlock("in",value = 0.01)) #replaced by inputblock
        self.addBlock(InputBlock("IN"))

        self.addBlock(OutputBlock("OUT"))


        #add Connections
        self.addConnection("IN","p1")
        #self.addConnection("IC_d_in","d_in",inport_name="IC")

        #self.addConnection("d_in","p1")
        self.addConnection("delta_T","p1")

        self.addConnection("p1","a1")

        self.addConnection("a1","d_out")
        self.addConnection("IC","d_out",inport_name="IC" )

        self.addConnection("d_out","a1")

        self.addConnection("d_out","OUT")

        







  