from Optimization import *

class ConstantFoldingOptimization(Optimization):
    
    
       
    def __init__(self, simulator):
        self.TOP = "TOP"
        self.BOTTOM = "BOTTOM"
        
        Optimization.__init__(self, simulator)
        
        
    def optimize(self, model):
    
        print("Start Constant Folding")
        
        #TODO: depGraph should be created another way
        self.__depGraph = self.simulator.getDepGraph()
        self.sortedGraph = self.__depGraph.getStrongComponents()
        
        
        flowAnalyzer = FlowAnalyzer()
        flowAnalyzer.initFcn = self.initFcn
        flowAnalyzer.blockFcn = self.analyzeComponent
        flowAnalyzer.initialApprox = self.BOTTOM
        
        analysis = flowAnalyzer.analyze(model, self.sortedGraph)
        
        self.print_analysis(analysis, skip_structural = True)
        
        new_model = self.transform(model, analysis)
        
        return new_model
        
    #ANALYSIS FUNCTIONS
    def initFcn(self):
      self.constantFoldingList = []
      self.tempConstValues= []
        
    def analyzeComponent(self, component, approxSets):
        #print("Component: " + str(component))
        
        #TODO: what is this for?
        if not len(component) == 1:
            print("Component length not one")
            return self.TOP
            
        #get the actual block
        block = component[0]
        in_blocks = self.get_influence_blocks(block)
        
        #return the value if the block is a ConstantBlock
        if self.isA(block, [ConstantBlock, Simulink_ConstantBlock]):
            return block.getValue()
            
        #TODO: More sosphicated analysis of DelayBlocks?
        #TODO: handle Simulink_DelayBlocks
        elif isinstance(block,DelayBlock):
            ICBlockName = block.IC.getBlockName()
            ICapprox = approxSets[ICBlockName]
            
            valueBlock = in_blocks[0]
            valueApprox = approxSets[valueBlock.getBlockName()]
            
            if ICapprox == valueApprox:
                return valueApprox
            else:
                return self.TOP
                
        #pass values through demux block, and separate in structural block input
        if isinstance(block, Simulink_DemuxBlock):
            parentBlock = in_blocks[0]
            parentName = parentBlock.getBlockName()
            
            return approxSets[parentName]
        
        if self.isA(block, self.SimulinkStructuralBlocks):

            if len(in_blocks) > 1:
                print("Error: Structural block has more than one parent!")
                
            parentBlock = in_blocks[0]
            parentName = parentBlock.getBlockName()
            
            if not isinstance(parentBlock, Simulink_DemuxBlock):
                return approxSets[parentName]
            else:
                index = parentBlock.linksOUT.index(block)
                print("Index: " + str(index))
                value = approxSets[parentName][index]
                print("Value: " + str(value))
                return value
            
        
        #TODO: Add more special cases    
            
        #TODO: Gain block
               
        #TODO: create 'get_influence_blocks()' function to remove contains blocks
        
        
        if len(in_blocks) == 0:
        
            if not isinstance(block, Simulink_SubSystemBlock):
                print("Error: Non-constant block has no parents!")
                #print(block)
                #print(block.__class__.name)
            return self.TOP
        
        #general case: see if all inputs are constant
        for influenceBlock in in_blocks:
            if isinstance(influenceBlock, Simulink___Contains__Block):
                    continue
            influenceName = influenceBlock.getBlockName()
            influenceApprox = approxSets[influenceName]
            if influenceApprox in [self.TOP, self.BOTTOM]:
                return self.TOP
          
        #all influence values are constant, so do operations on values
        #TODO: make this shorter/more general
        if isinstance(block,AdderBlock):
            returnValue = 0
            for influenceBlock in in_blocks:
                if isinstance(influenceBlock, Simulink___Contains__Block):
                    continue
                influenceName = influenceBlock.getBlockName()
                influenceApprox = approxSets[influenceName]
                returnValue += influenceApprox
            return returnValue
            
        elif isinstance(block,ProductBlock):
            returnValue = 1
            for influenceBlock in in_blocks:
                if isinstance(influenceBlock, Simulink___Contains__Block):
                    continue
                influenceName = influenceBlock.getBlockName()
                influenceApprox = approxSets[influenceName]
                #print("InfluenceApprox: " + str(influenceApprox))
                returnValue *= influenceApprox
            return returnValue
            
        elif isinstance(block,GainBlock):
            returnValue = block.gain
            for influenceBlock in in_blocks:
                if isinstance(influenceBlock, Simulink___Contains__Block):
                    continue
                influenceName = influenceBlock.getBlockName()
                influenceApprox = approxSets[influenceName]
                returnValue *= influenceApprox
            return returnValue
            
        elif isinstance(block,Simulink_MuxBlock):
            returnValue = []
            for influenceBlock in in_blocks:
                if isinstance(influenceBlock, Simulink___Contains__Block):
                    continue
                influenceName = influenceBlock.getBlockName()
                influenceApprox = approxSets[influenceName]
                returnValue.append(influenceApprox)
            return returnValue
                        
        return self.TOP                    
                        
            
                
    #============================================================= 
    #TRANSFORM FUNCTIONS
    def transform(self, model, analysis):
    
        for block_name in analysis.keys():
            
            #get calculated value for this block
            block_value = analysis[block_name]
            
            #block can't be replaced by constant
            if block_value in [self.TOP, self.BOTTOM]:
                continue
            
            block = model.getBlockByName(block_name)
            
            #block was already removed
            if block == None:
                continue
            
            #block already is constant
            if isinstance(block, ConstantBlock):
                continue
                
            #don't replace structural blocks
            if self.isA(block, self.SimulinkStructuralBlocks):
                continue
                
            print("Block to replace: " + block.getBlockName())
                            
            print(block_value)
            
            new_block = ConstantBlock(block.getBlockName() + "_Constant", value=block_value)
            
            model.addBlock(new_block)
            
            for out_block in block.linksOUT:       
                model.addConnection(new_block, out_block)
            
            for in_block in block.linksIN:
                if isinstance(in_block, Simulink___Contains__Block):
                    model.addConnection(in_block, new_block)
                    continue
                    
            self.remove_block(model, block)

                
        return model   
        
    def remove_block(self, model, block):
        #print("Removing: " + block.getBlockName())
        model.removeBlock(block)
            
        for parent in block.linksIN:
            #print("Parent: " + str(parent))
            if len(parent.linksOUT) == 0:
                self.remove_block(model, parent)
       
