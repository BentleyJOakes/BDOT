from CBD import *
        
        
#definition for the Simulink blocks
#implemented as subclasses of CBD blocks        
        
        
#generic type for when a corresponding type has not yet been created
class Simulink_GenericBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

#------------------------------------------

class Simulink___Contains__Block(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink_Port_InputBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink_Port_OutputBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink_InportBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink_OutportBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
        
class Simulink___Block_Inport__Block(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink___Block_Outport__Block(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink___Relation__Block(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
        
class Simulink_SubSystemBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
#------------------------------------------
# Algebraic blocks
class Simulink_ProductBlock(ProductBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
class Simulink_GainBlock(GainBlock):
    def __init__(self, block_name, block):
        GainBlock.__init__(self, block_name, gain=block["gain"])
        self.block = block
        
class Simulink_ConstantBlock(ConstantBlock):
    def __init__(self, block_name, block):
        ConstantBlock.__init__(self, block_name, value=block["value"])
        self.block = block
        
    #in Simulink, constants have parents
    def linkInput(self, in_block):
        BaseBlock.linkInput(self, in_block)
        

class Simulink_SumBlock(AdderBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
        
class Simulink_SwitchBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        
        self.GREATER_THAN_EQUAL = "GTE"
        self.GREATER_THAN = "GT"
        self.NOT_EQUAL = "NE"
        
        
        for k in block.attributes():
            print(k)
            print(block[k])
            
        if ">=" in block['Criteria']:
            self.criteria = self.GREATER_THAN_EQUAL 
        elif ">" in block['Criteria']:
            self.criteria = self.GREATER_THAN
        else:
            self.criteria = self.NOT_EQUAL
            
        self.threshold = block['Threshold']
        
        
        
        
        
class Simulink_IntegratorBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        

class Simulink_DiscretePulseGeneratorBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

class Simulink_MuxBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

class Simulink_DemuxBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

class Simulink_ScopeBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

class Simulink_UnitDelayBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
        


class Simulink_GotoBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

class Simulink_FromBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block

class Simulink_TransferFcnBlock(BaseBlock):
    def __init__(self, block_name, block):
        BaseBlock.__init__(self, block_name)
        self.block = block
