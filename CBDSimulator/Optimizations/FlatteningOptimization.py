from Optimization import *
from Server.Core.SimulinkTransformationToTCore import SimulinkTransformationToHimesis
from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS, HimesisPostConditionPattern
from Server.TCore.t_core.messages import Packet

from HimesisToCBD.himesis_utils import *

class FlatteningOptimization(Optimization):
    
    
       
    def __init__(self, simulator, mh):
        
        Optimization.__init__(self, simulator)
        self.mh = mh
        
        self.useModelTransformation = True
        
    def optimize(self, model):
    
        print("Start Flattening")
        
        analysis = self.analyze(model)
        model = self.transform(model, analysis)
        
        
        return model
        
    #ANALYSIS FUNCTIONS
    def analyze(self, model):
        subsystems = []
        
        for block in model.getBlocks():
            if isinstance(block, Simulink_SubSystemBlock):
                subsystems.append(block)
        return subsystems
    
    
    def transform(self, model, analysis):
    
        #do code transformation
        if self.useModelTransformation:
            
            transformation = "flattening"
            path = "./examples/"
            
            model_name = model.getBlockName()
            model_name = Himesis.standardize_name(model_name)
            
            if not self.mh == None:
                # Transfornation to T-Core
                transformationToHimesis = SimulinkTransformationToHimesis(transformation, path, self.mh)
                transformationToHimesis.SimulinkTransformationModelToHimesis()
            
            
            # Execute the Transformation
            model_graph = self.get_object('./himesis/' + model_name + ".py")
            
            packet = Packet()
            packet.graph = model_graph
            

            exec("import temp.T_" + transformation)
            exec('packet = temp.T_'+ transformation +'.packet_in(packet)')
            
            print(packet)

        else:
            for subsystem in analysis:
                
                if len(subsystem.linksIN) == 0:
                    continue
                    
                #TODO: Make these pretty
                self.fix_incoming_edges(model, subsystem)
                self.fix_outgoing_edges(model, subsystem)
                self.remove_subsystem(model, subsystem)
          
            
        return model
    
    
    def fix_incoming_edges(self, model, subsystem):
    
        in_ports = {}
    
        for in_block in subsystem.linksIN:   
            if not isinstance(in_block, Simulink___Block_Inport__Block):
                continue
                
                
            in_parent = in_block.linksIN[0]
            if not isinstance(in_parent, Simulink_Port_InputBlock):
                continue
                
            #TODO Is this correct?
            port_num = in_parent.block["Name"]

            in_ports[port_num] = in_parent
            
            
        out_ports = {}
        for out in subsystem.linksOUT:   
            if not isinstance(out, Simulink___Contains__Block):
                continue
                
                
            out_child = out.linksOUT[0]
            if not isinstance(out_child, Simulink_InportBlock):
                continue
                
            port_num = str(out_child.block["Port"])
            
            out_ports[port_num] = out_child
            
        print("Hello")
        
        #now connect the ports
        for key in in_ports.keys():
            
            in_block = in_ports[key]
            out_block = out_ports[key]
            
            
            print ("in_block: " + in_block.getBlockName())
            print ("out_block: " + out_block.getBlockName())
            
            
            curr = out_block
            
            while not isinstance(curr, Simulink_Port_OutputBlock):
                curr = curr.linksOUT[0]
  
            #print ("IN block: " + in_block.getBlockName())
            to_delete = in_block
            to_delete2 = in_block.linksOUT[0]
            
            print ("IN block: " + in_block.getBlockName())
            
            in_parent = in_block.linksIN[0]
            out_child = curr.linksOUT[0].linksOUT[0]
            
            #print ("IN PARENT: " + in_parent.getBlockName())
            #print ("OUT CHILD: " + out_child.getBlockName())
            
            
            
            #in_parent.linksOUT = []
            in_parent.linkOutput(out_child)
            
            out_child.linkInput(in_parent)
            
            
            #delete dead edges
            #TODO: Make general dead-code transformation
            
            
            curr = curr.linksOUT[0]
            
            
            self.remove_blocks(model, curr, Simulink_SubSystemBlock)
            
            #print(to_delete, True)
            #print(to_delete2)
            
            
            model.removeBlock(to_delete)
            model.removeBlock(to_delete2)
            
            


    def fix_outgoing_edges(self, model, subsystem):
        out_ports = {}
    
        for out_block in subsystem.linksOUT:   
            if not isinstance(out_block, Simulink___Block_Outport__Block):
                continue
                
                
            out_child = out_block.linksOUT[0]
            if not isinstance(out_child, Simulink_Port_OutputBlock):
                continue
                
            #TODO Is this correct?
            
            port_num = str(out_child.block["Name"])
            out_ports[port_num] = out_child
            
            
        in_ports = {}
        for in_block in subsystem.linksOUT:   
            if not isinstance(in_block, Simulink___Contains__Block):
                continue
                
                
            in_child = in_block.linksOUT[0]
            if not isinstance(in_child, Simulink_OutportBlock):
                continue
                
            port_num = str(in_child.block["Port"])
            #print ("Key: " + port_num)
            in_ports[port_num] = in_child
            
            
        #now connect the ports
        for key in in_ports.keys():
            
            out_block = out_ports[key]
            in_block = in_ports[key]
            
            #print("OUT NAME: " + out_block.getBlockName())
            #print("IN NAME: " + in_block.getBlockName())
            
            to_delete = out_block.linksOUT[0]
            
            out_block = out_block.linksOUT[0].linksOUT[0]
            #in_block = in_block.linksOUT[0].linksOUT[0]
            
            for new_in_block in in_block.linksIN:
                if isinstance(new_in_block, Simulink___Block_Inport__Block):
                    in_block = new_in_block
                
            #print("IN NAME454545: " + in_block.getBlockName())
            to_delete3 = in_block
            
            in_block = in_block.linksIN[0]
            to_delete2 = in_block
            
            #print("IN NAME3: " + in_block.getBlockName())
            
            for new_in_block in in_block.linksIN:
                if isinstance(new_in_block, Simulink___Relation__Block):
                    in_block = new_in_block
                    
            #print("OUT NAME: " + out_block.getBlockName())
            #print("IN NAME4: " + in_block.getBlockName())
            
            #print(to_delete.getBlockName())
            
            
            to_delete4 = to_delete3.linksOUT[0]

            model.removeBlock(to_delete2)
            model.removeBlock(to_delete3)
            
            #in_block.linksOUT = []
            
            in_block.linkOutput(out_block)
            
            self.remove_blocks(model, to_delete, Simulink_SubSystemBlock)
            self.remove_blocks(model, to_delete4, Simulink_SubSystemBlock)
            
        
    def remove_blocks(self, model, start_block, end_class):
        curr = start_block
        #print("Start removing: " + curr.getBlockName())
        
        while not isinstance(curr, end_class):
            
            parent = curr.linksIN[0]
                
            #print("Removing: " + curr.getBlockName())
            #print(curr)
            model.removeBlock(curr)
            curr = parent
    
    def remove_subsystem(self, model, subsystem):
        
        parent_subsystem = subsystem.linksIN[0].linksIN[0]
        
        for child in subsystem.linksOUT:
            if not isinstance(child, Simulink___Contains__Block):
                continue

            parent_subsystem.linkOutput(child)
            
        subsystem_contains = subsystem.linksIN[0]
        
        model.removeBlock(subsystem_contains)
        model.removeBlock(subsystem)
        
        
