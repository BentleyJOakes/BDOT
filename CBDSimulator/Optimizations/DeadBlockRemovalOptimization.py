from Optimization import *

class DeadBlockRemovalOptimization(Optimization):
    
    
       
    def __init__(self, simulator):
        self.KEEP = "KEEP"
        self.REMOVE = "REMOVE"
        
        Optimization.__init__(self, simulator)
        
        
    def optimize(self, model):
    
        print("Start Dead Block Removal")
        
        
        start = time.clock()
        
        
        #TODO: depGraph should be created another way
        self.__depGraph = self.simulator.getDepGraph()
        self.sortedGraph = self.__depGraph.getStrongComponents()
        
        
        flowAnalyzer = FlowAnalyzer()
        flowAnalyzer.initFcn = self.initFcn
        flowAnalyzer.blockFcn = self.analyzeComponent
        flowAnalyzer.initialApprox = self.REMOVE
        flowAnalyzer.analysis_direction = flowAnalyzer.BACKWARD_DIR
        
        analysis = flowAnalyzer.analyze(model, self.sortedGraph)
        
        end = time.clock()
        print("Time taken for analysis: " + str(end - start) + " seconds")
        
        self.print_analysis(analysis, skip_structural = False)
        
        start = time.clock()
        model = self.transform(model, analysis)
        end = time.clock()
        print("Time taken for transformation: " + str(end - start) + " seconds")
        
        return model
        
    #ANALYSIS FUNCTIONS
    def initFcn(self):
      self.constantFoldingList = []
      self.tempConstValues= []
        
    def analyzeComponent(self, component, approxSets):
        
        block = component[0]
        
        if self.isA(block, [Simulink_OutportBlock, Simulink_ScopeBlock]):
            return self.KEEP
            
        for child in block.linksOUT:
            child_approx = approxSets[child.getBlockName()]
            if child_approx == self.KEEP:
                return self.KEEP
                
        return self.REMOVE
            
                
    #============================================================= 
    #TRANSFORM FUNCTIONS
    def transform(self, model, analysis):
    
        for block_name in analysis.keys():
            
            #get calculated value for this block
            block_value = analysis[block_name]
            
            #print("Name: " + block_name + " Value: " + block_value)
            
            #block should be kept
            if block_value == self.KEEP:
                continue
            
            block = model.getBlockByName(block_name)
            
            #remove this block
            model.removeBlock(block)

                
        return model
       
