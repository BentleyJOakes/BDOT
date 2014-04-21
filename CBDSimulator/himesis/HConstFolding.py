

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstFolding(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstFolding.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstFolding, self).__init__(name='HConstFolding', num_nodes=0, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstFolding"""
        self["GUID__"] = UUID('3cb1d262-a892-420f-9a76-8dd0830ac240')
        
        # Set the node attributes

