class FlowAnalyzer:

    def __init__(self):
        self.initFcn = None
        self.blockFcn = None
        self.mergeFcn = None
        
    def analyze(self, model, depGraph):
        for component in depGraph:
            self.blockFcn(component)
    
        
