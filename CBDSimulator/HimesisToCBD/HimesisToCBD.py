from Server.TCore.core.himesis import Himesis
from CBD import *
from himesis_utils import graph_to_dot

import os
import sys

class HimesisToCBD:

    def __init__(self):
        pass

    def convertFile(self, filename):
        c = self.load_class(filename)
        himesis_graph = c[c.keys()[0]]()
        
        return self.convert(himesis_graph)
               
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
        
        
    def getBlockID(self, block, node_num):
        return block["Name"] + " : " + block["mm__"] + " : " + str(node_num)
        
    def convert(self, h_graph):
    
        graph_name = h_graph.name
        print("Name: " + str(graph_name))
        
        graph_to_dot(graph_name, h_graph)
        
        cbd = CBD(graph_name)
        cbd.delta_t = 0.001
        
        print(h_graph)
        
        
        for i in range(len(h_graph.vs)):
            block = h_graph.vs[i]
            block_name = self.getBlockID(block, i)
            print(block)
            
            cbd.addBlock(GenericBlock(block_name))
            #print(block)
            
           
        for edgeId in range(h_graph.ecount()):
            source = h_graph.es[edgeId].source
            target = h_graph.es[edgeId].target
            
            #print("Source: " + str(source))
            #print("Target: " + str(target))
            
            source_block = h_graph.vs[source]
            source_block_name = self.getBlockID(source_block, source)
            
            target_block = h_graph.vs[target]
            target_block_name = self.getBlockID(target_block, target)
            
            cbd.addConnection(source_block_name, target_block_name)
    
        cbd.dump()
        return cbd

if __name__=="__main__":
    hToCBD = HimesisToCBD()
    cbd = hToCBD.convertFile("HimesisToCBD/HAdapt.py")
