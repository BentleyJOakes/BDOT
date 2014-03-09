__author__ = 'Bart'

from CBD import *

class TimeModel(CBD):
    def __init__(self, block_name, deltaT = 1.0):
        CBD.__init__(self, block_name)

        self.addBlock(DelayBlock("d"))
        self.addBlock(ConstantBlock("c0"))
        self.addBlock(ConstantBlock("c_deltaT", value= deltaT))
        self.addBlock(AdderBlock("a"))

        self.addBlock(OutputBlock("OUT"))

        self.addConnection("c0","d",inport_name="IC")
        self.addConnection("d","a")
        self.addConnection("c_deltaT","a")
        self.addConnection("a","d")
        self.addConnection("d","OUT")



