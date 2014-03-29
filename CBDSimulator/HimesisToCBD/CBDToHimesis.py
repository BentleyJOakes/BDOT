from Server.TCore.core.himesis import Himesis
from CBD import *
from SimulinkCBD import *
from himesis_utils import graph_to_dot

import os
import sys

class CBDToHimesis:

    def __init__(self):
        pass
        
    def convert(self, model):
        model_name = model.getBlockName() + "_opt"
        
        h = Himesis(name=model_name)
        h[Himesis.Constants.META_MODEL] = ['Simulink']  # the meta-model type name
        
        h["name"] = model_name
        
        model_blocks = model.getBlocks()
        block_id_dict = {}
        
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
                if ("Input" in source_block_name or "Inport" in source_block_name) and not "__Relation__" in target_block_name:
                    h.add_edge(out_vertex, vertex)
                else:
                    h.add_edge(vertex, out_vertex)
            
            #h.vs[vertex][Himesis.Constants.META_MODEL] = block.getBlockName()
                    
            #print(vertex)
        
        graph_to_dot(model_name, h)
        
        return h
        
    def get_attribs(self, h, vertex, block):
        try:
            #copy details if Simulink block
            if block.block:
                for attrib in block.block.attributes():
                    if attrib == "GUID__":
                        continue
                        
                    h.vs[vertex][attrib] = block.block[attrib]
        except Exception: #not a Simulink block
        
            #TODO: make this more robust
            if isinstance(block, ConstantBlock):
                h.vs[vertex]["mm__"] = "Constant"
                h.vs[vertex]["value"] = block.getValue()
                h.vs[vertex]["Name"] = "Constant" + str(vertex)
                h.vs[vertex]["SampleTime"] = "inf"
                h.vs[vertex]["BackgroundColor"] = "white"
                
        
        
        
    
