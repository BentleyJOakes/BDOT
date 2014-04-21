from CBD import *
from SimulinkCBD import *
from FlowAnalyzer.FlowAnalyzer import *
import time
import os    
import sys
class Optimization:

    def __init__(self, simulator, mh):
        self.simulator = simulator
        self.mh = mh
        
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
        
        
    def get_ports(self, block):
    
        ports = {}
        for parent in block.linksIN:
            if isinstance(parent, Simulink___Contains__Block):
                continue
            print(parent.getBlockName())
            
            port_input = parent.linksIN[0]
            port_num = port_input.block["Name"]
            
            ports[port_num] = parent
            
        return ports
        
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
        
    #function to dynamically load a new class
    import importlib

    def load_class(self, full_class_string):
        directory, module_name = os.path.split(full_class_string)
        module_name = os.path.splitext(module_name)[0]

        path = list(sys.path)
        sys.path.insert(0, directory)

        try:
            module = __import__(module_name)
        finally:
            sys.path[:] = path # restore
        return {module_name : getattr(module, module_name)}
        
    def get_object(self, full_class_string):
        d = self.load_class(full_class_string)
        return d.values()[0]()
    
    
        
