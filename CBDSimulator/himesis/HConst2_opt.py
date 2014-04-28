

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConst2_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConst2_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConst2_opt, self).__init__(name='HConst2_opt', num_nodes=10, edges=[])
        
        # Add the edges
        self.add_edges([(1, 9), (1, 8), (2, 6), (3, 2), (5, 4), (8, 0), (9, 7), (0, 5), (6, 4), (7, 3)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConst2_opt"""
        self["GUID__"] = UUID('fc0f390a-3a0d-4339-8400-b2825794b677')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F450
aF128
aF480
aF142
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('e06323ac-e1cb-428d-8ea2-e75c413e048c')
        self.vs[1]["Name"] = """Const2"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('db819610-20f0-412b-be52-b9e25b206c78')
        self.vs[2]["Name"] = """1"""
        self.vs[2]["mm__"] = """Port_Output"""
        self.vs[2]["GUID__"] = UUID('68c649ea-6fde-432c-8df7-413c37a3097c')
        self.vs[3]["mm__"] = """__Block_Outport__"""
        self.vs[3]["GUID__"] = UUID('476429a2-5f13-43a2-88e4-3687306d965f')
        self.vs[4]["Name"] = """1"""
        self.vs[4]["mm__"] = """Port_Input"""
        self.vs[4]["GUID__"] = UUID('192bcc3e-8300-4b88-8a96-b8d0860edaab')
        self.vs[5]["mm__"] = """__Block_Inport__"""
        self.vs[5]["GUID__"] = UUID('96086a1d-b6e9-4950-a9ad-5afa4821820e')
        self.vs[6]["mm__"] = """__Relation__"""
        self.vs[6]["GUID__"] = UUID('52d422fd-d6a9-4aaf-b0d2-8e1745a3019e')
        self.vs[7]["Name"] = """Constant9"""
        self.vs[7]["SampleTime"] = """inf"""
        self.vs[7]["value"] = 249.0
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["GUID__"] = UUID('3bf18731-4c63-41fe-b532-c987307a4fab')
        self.vs[8]["Name"] = """None"""
        self.vs[8]["mm__"] = """__Contains__"""
        self.vs[8]["GUID__"] = UUID('07aea2e5-4df3-4d53-9262-a8a5b25ded7f')
        self.vs[9]["Name"] = """None"""
        self.vs[9]["mm__"] = """__Contains__"""
        self.vs[9]["GUID__"] = UUID('16bf042d-49ae-4b33-bc9e-7219bea3f0a8')

