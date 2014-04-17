

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfoldingDead_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfoldingDead_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfoldingDead_opt, self).__init__(name='HConstfoldingDead_opt', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfoldingDead_opt"""
        self["GUID__"] = UUID('af97af93-c5a5-42b3-a702-4dc680814fb1')
        
        # Set the node attributes

