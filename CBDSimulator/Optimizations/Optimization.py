from CBD import *
from SimulinkCBD import *
from FlowAnalyzer.FlowAnalyzer import *
import time

class Optimization:

    def __init__(self, simulator):
        self.simulator = simulator
        
        self.SimulinkStructuralBlocks = [Simulink___Block_Outport__Block, Simulink___Block_Inport__Block, Simulink_Port_OutputBlock, Simulink_Port_InputBlock, Simulink___Relation__Block, Simulink___Contains__Block]
        self.SimulinkStructuralNames = []
        for block in self.SimulinkStructuralBlocks:
            name = block.__name__
            name = name.replace("Simulink_", "")
            self.SimulinkStructuralNames.append(name)
            
    def isA(self, obj, classes):
        for c in classes:
            if isinstance(obj, c):
                return True
        return False
        
    def optimize(self, model):
        pass
        
    def analyze(self, model):
        pass
        
    def get_influence_blocks(self, block):
        influence_blocks = []
        for parent in block.linksIN:
            if not isinstance(parent, Simulink___Contains__Block):
                influence_blocks.append(parent)
        return influence_blocks
        
    #TODO: there's probably a fancy way of doing this...
    def print_analysis(self, analysis, skip_structural = False):
        print("Analysis:")
        for component in analysis.keys():
            do_print = True
            if skip_structural == True:
                for name in self.SimulinkStructuralNames:
                    
                    #take the block off of the name of the simulink block
                    if name[:-len("Block")] in str(component):
                        do_print = False
                        break
                        
            if do_print == True:
                print(str(component) + " : " + str(analysis[component]))
        
    def transform(self, model):
        pass
        
