import copy

class FlowAnalyzer:

    def __init__(self):
        self.initFcn = None
        self.blockFcn = None
        self.mergeFcn = None
        self.initialApprox = []
        
        self.dirtyBlocks = []
        
        self.approxSets = {}
        
    def analyze(self, model, depGraph):
    
        self.initFcn()
        
        for component in depGraph:
            self.dirtyBlocks.append(component)
            self.approxSets[component[0].getBlockName()] = copy.copy(self.initialApprox)
            
        #TODO: handle loops
        for component in self.dirtyBlocks:
            approx = self.blockFcn(component, self.approxSets)
            self.approxSets[component[0].getBlockName()] = approx
        
        for component in self.approxSets.keys():
            print(str(component) + " : " + str(self.approxSets[component]))
            
        return self.approxSets
