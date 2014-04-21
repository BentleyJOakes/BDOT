import copy

class FlowAnalyzer:

    def __init__(self):
        self.FORWARD_DIR = "FORWARDS"
        self.BACKWARD_DIR = "BACKWARDS"
    
        self.initFcn = None
        self.blockFcn = None
        self.mergeFcn = None
        self.initialApprox = []
        
        self.dirtyBlocks = []
        
        self.approxSets = {}
        self.analysis_direction = self.FORWARD_DIR

        
    def analyze(self, model, depGraph):
    
        self.initFcn()
        
        for component in depGraph:
            self.dirtyBlocks.append(component)
            self.approxSets[component[0].getBlockName()] = copy.copy(self.initialApprox)
            
        if self.analysis_direction == self.BACKWARD_DIR:
            self.dirtyBlocks = self.dirtyBlocks[::-1]
            
        #TODO: handle loops
        for component in self.dirtyBlocks:
            #print(component)
            approx = self.blockFcn(component, self.approxSets)
            self.approxSets[component[0].getBlockName()] = approx
        
        #for component in self.approxSets.keys():
        #    print(str(component) + " : " + str(self.approxSets[component]))
            
        return self.approxSets
