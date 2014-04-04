

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HStartLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HStartLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HStartLHS, self).__init__(name='HStartLHS', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('e5b90e65-9f97-43ba-a75b-3b6c8f5e73f1')
        
        # Set the node attributes

    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

