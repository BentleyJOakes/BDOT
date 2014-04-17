

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfoldingDead(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfoldingDead.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfoldingDead, self).__init__(name='HConstfoldingDead', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfoldingDead"""
        self["GUID__"] = UUID('14d06d44-08f6-489b-ba04-7fccf64f80fb')
        
        # Set the node attributes

