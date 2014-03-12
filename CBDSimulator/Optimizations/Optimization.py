

class Optimization:

    def __init__(self, simulator):
        self.simulator = simulator
        
        
    def isA(self, obj, classes):
        for c in classes:
            if isinstance(obj, c):
                return True
        return False
        
    def optimize(self, model):
        pass
        
    def analyze(self, model):
        pass
        
    def transform(self, model):
        pass
        
