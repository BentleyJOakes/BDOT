from Optimization import *
from Server.Core.SimulinkTransformationToTCore import SimulinkTransformationToHimesis
from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS, HimesisPostConditionPattern
from Server.TCore.t_core.messages import Packet

class FlatteningOptimization(Optimization):
    
    
       
    def __init__(self, simulator, mh):
        
        Optimization.__init__(self, simulator)
        self.mh = mh
        
    def optimize(self, model):
    
        print("Start Flattening")
        
        
        model = self.transform(model, None)
        
        #new_model = self.transform(model, analysis)
        
        return model
        
    #ANALYSIS FUNCTIONS
    
    def transform(self, model, analysis):
    
        transformation = "flattening"
        path = "./examples/"
        
        model_name = model.getBlockName()
        model_name = Himesis.standardize_name(model_name)
        
        # Transfornation to T-Core
        transformationToHimesis = SimulinkTransformationToHimesis(transformation, path, self.mh)
        transformationToHimesis.SimulinkTransformationModelToHimesis()
        
        
        
        # Execute the Transformation
        exec("from himesis."+ model_name + " import " + model_name)
        exec("import temp.T_" + transformation)
        packet = Packet()
        exec("packet.graph = "+ model_name + "()")
        exec('packet = temp.T_'+ transformation +'.packet_in(packet)')
        
        return model
    
