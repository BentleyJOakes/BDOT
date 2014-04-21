

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstFolding_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstFolding_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstFolding_opt, self).__init__(name='HConstFolding_opt', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstFolding_opt"""
        self["GUID__"] = UUID('43029ece-9014-41b6-a21c-5f1d905f8632')
        
        # Set the node attributes

