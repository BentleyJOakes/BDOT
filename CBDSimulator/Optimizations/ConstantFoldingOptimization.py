from Optimization import *
from CBD import *
from FlowAnalyzer.FlowAnalyzer import *


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
        
        print("Analysis:")
        print(analysis)
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
            return
            
        #get the actual block
        block = component[0]
        
        #return the value if the block is a ConstantBlock
        if isinstance(block,ConstantBlock):
            #self.constantFoldingList.append(block)
            return block.getValue()
            
        #TODO: More sosphicated analysis of DelayBlocks?
        elif isinstance(block,DelayBlock):
            ICBlockName = block.IC.getBlockName()
            ICapprox = approxSets[ICBlockName]
            
            valueBlock = block.linksIN[0]
            valueApprox = approxSets[valueBlock.getBlockName()]
            
            if ICapprox == valueApprox:
                return valueApprox
            else:
                return self.TOP
            
        #TODO: Add more special cases    
            
        #TODO: Gain block
               
        #general case: see if all inputs are constant
        for influenceBlock in block.linksIN:
            influenceName = influenceBlock.getBlockName()
            influenceApprox = approxSets[influenceName]
            if influenceApprox in [self.TOP, self.BOTTOM]:
                return self.TOP
            
            
          
        #all influence values are constant, so do operations on values
        #TODO: make this shorter/more general
        if isinstance(block,AdderBlock):
            returnValue = 0
            for influenceBlock in block.linksIN:
                influenceName = influenceBlock.getBlockName()
                influenceApprox = approxSets[influenceName]
                returnValue += influenceApprox
            return returnValue
        elif isinstance(block,ProductBlock):
            returnValue = 1
            for influenceBlock in block.linksIN:
                influenceName = influenceBlock.getBlockName()
                influenceApprox = approxSets[influenceName]
                returnValue *= influenceApprox
            return returnValue
                        
        return self.TOP                    
                        
            
                
                
    #TRANSFORM FUNCTIONS
    def transform(self, model, analysis):
    
        for block_name in analysis.keys():
        
            #get calculated value for this block
            block_value = analysis[block_name]
            
            #block can't be replaced by constant
            if block_value in [self.TOP, self.BOTTOM]:
                continue
            
            block = model.getBlockByName(block_name)
            
            
            #block already is constant
            if isinstance(block, ConstantBlock):
                continue
                
            print(block)
                            
            print(block_value)
            
            dependents = model.getDependents(block)
                
        return model
#        if numberOfConstInfluencers == numberOfInfluencers:
#                for influenceBlock in block.linksIN:
#                    self.__blocks.remove(influenceBlock)
#                    del self.__blocksDict[influenceBlock.getBlockName()]
#                if isinstance(block, AdderBlock):
#                    constBlockValue = sum(tempConstValues)
#                if isinstance(block,ProductBlock):
#                    constBlockValue = 1
#                    for number in tempConstValues:
#                        constBlockValue *= number
#                #add the new constantblock to the model
#                self.addBlock(ConstantBlock(block.getBlockName()+".fold", value=constBlockValue))
#                self.constantFoldingList.append(self.getBlockByName(block.getBlockName()+".fold"))
#                self.__blocks.remove(block)
#                del self.__blocksDict[block.getBlockName()]
#                del self.tempConstValues[:]
#                self.constantFoldingList.append(block)
#            else:
#                pass
    
