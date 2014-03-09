from Optimization import *
from CBD import *

class ConstantFoldingOptimization(Optimization):
    
    def __init__(self, simulator):
        Optimization.__init__(self, simulator)
        
        
    def optimize(self, model):
    
        print("Start Constant Folding")
        self.__depGraph = self.simulator.getDepGraph()
        self.sortedGraph = self.__depGraph.getStrongComponents()
        
        self.foldConstants(self.sortedGraph)
        #model.foldConstants(self.sortedGraph)
        
    def analyze(self, model):
        pass
        
    def transform(self, model):
        pass
        
        
    def foldConstants(self, sortedList):
      print sortedList
      constantFoldingList = []
      tempConstValues= []
      for component in sortedList:
        if len(component) == 1:
            block = component[0]
            print block.getBlockName()
            if isinstance(block,ConstantBlock):
                constantFoldingList.append(block)
            else:
                numberOfInfluencers = len(block.linksIN)
                numberOfConstInfluencers = 0
                for influenceBlock in block.linksIN:
                    if influenceBlock in constantFoldingList:
                        numberOfConstInfluencers +=1
                        if not isinstance(influenceBlock, ConstantBlock):
                            block.linksIN.remove(influenceBlock)
                            self.addConnection(influenceBlock.getBlockName()+".fold", block)
                            tempConstValues.append(self.getBlockByName(influenceBlock.getBlockName()+".fold").getValue())
                        else:
                            tempConstValues.append(influenceBlock.getValue())
                            print tempConstValues
                if numberOfConstInfluencers == numberOfInfluencers:
                    for influenceBlock in block.linksIN:
                        self.__blocks.remove(influenceBlock)
                        del self.__blocksDict[influenceBlock.getBlockName()]
                    if isinstance(block, AdderBlock):
                        constBlockValue = sum(tempConstValues)
                    if isinstance(block,ProductBlock):
                        constBlockValue = 1
                        for number in tempConstValues:
                            constBlockValue *= number
                    #add the new constantblock to the model
                    self.addBlock(ConstantBlock(block.getBlockName()+".fold", value=constBlockValue))
                    constantFoldingList.append(self.getBlockByName(block.getBlockName()+".fold"))
                    self.__blocks.remove(block)
                    del self.__blocksDict[block.getBlockName()]
                    del tempConstValues[:]
                    constantFoldingList.append(block)
                else:
                    pass

