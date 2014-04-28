from Server.TCore.core.himesis import Himesis
from CBD import *
from SimulinkCBD import *
from himesis_utils import graph_to_dot

import os
import sys

#dumps a CBD model back into a himesis graph



class CBDToHimesis:

    def __init__(self):
        self.SimulinkStructuralBlocks = [Simulink___Block_Outport__Block, Simulink___Block_Inport__Block, Simulink_Port_OutputBlock, Simulink_Port_InputBlock, Simulink___Relation__Block, Simulink___Contains__Block]
        
    def isA(self, obj, classes):
        for c in classes:
            #print(str(c))
            if isinstance(obj, c):
                #print("Class: " + str(c))
                return True
        return False
        
    def convert(self, model, do_switch_hack = True):
        model_name = model.getBlockName() + "_opt"
        
        h = Himesis(name=model_name)
        h[Himesis.Constants.META_MODEL] = ['Simulink']  # the meta-model type name
        
        h["name"] = model_name
        
        model_blocks = model.getBlocks()
        block_id_dict = {}
        
        #need to avoid block name conflicts
        self.block_names = []
       
        
        
        for block in model_blocks:
            vertex = h.add_node()
            block_id_dict[block] = vertex
            
            self.get_attribs(h, vertex, block)

        for block in model_blocks:
            vertex = block_id_dict[block]
            
            
            for out_port in block.linksOUT:
            
                
                out_vertex = block_id_dict[out_port]
                
                target_block_name = out_port.getBlockName()
                source_block_name = block.getBlockName()
                
                
                #TODO: Remove switch hack
                if do_switch_hack and ("Port_Input" in source_block_name or "Block_Inport" in source_block_name) and not "__Relation__" in target_block_name:
                    h.add_edge(out_vertex, vertex)
                else:
                    h.add_edge(vertex, out_vertex)
            
            #h.vs[vertex][Himesis.Constants.META_MODEL] = block.getBlockName()
                    
            #print(vertex)
        
        if not do_switch_hack:
            model_name = model_name + "_real"
        
        graph_to_dot(model_name, h)
        
        return h
        
    def get_attribs(self, h, vertex, block):

        try:
            #copy details of Simulink block if the block still has one
            if block.block:
                for attrib in block.block.attributes():
                    if attrib == "GUID__":
                        continue
                        
                        
                    #TODO: rename blocks with conflicting names
#                    if attrib == "Name":
#                    
#                        #print("Block blockName: " + block.getBlockName())
#                        if self.isA(block, self.SimulinkStructuralBlocks):
#                            continue
#                            
#                        #print("Block blockName2: " + block.getBlockName())
#                            
#                        block_name = block.block[attrib]
#                        
#                        #print("Block name1: " + block_name)
#                        if block_name in self.block_names:
#                            #print("Conflict with: " + block_name)
#                            
#                            old_block_name = block_name
#                            #block_name = block_name + str(vertex)
#                            block.block[attrib] = block_name
#                            
#                            
##                            for es in h.es:
##                                print("Source: " + es.source)
##                                print("Target: " + es.target)
##                            
##                            
##                                if es.source == old_block_name:
##                                    print("Changing edge name source")
##                                    es.source = block_name
##                                if es.target == old_block_name:
##                                    print("Changing edge name target")
##                                    es.target = block_name
#                            
#                            
#                        #print("Block name2: " + block_name)
#                        self.block_names.append(block_name)
                    
                        
                    h.vs[vertex][attrib] = block.block[attrib]
        except Exception: #not a Simulink block
        
            #TODO: make this more robust
            if isinstance(block, ConstantBlock):
                h.vs[vertex]["mm__"] = "Constant"
                h.vs[vertex]["value"] = block.getValue()
                h.vs[vertex]["Name"] = "Constant" + str(vertex)
                h.vs[vertex]["SampleTime"] = "inf"
                h.vs[vertex]["BackgroundColor"] = "white"
                
        
        
        
    
