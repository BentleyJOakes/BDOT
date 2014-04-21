

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
        self["GUID__"] = UUID('927774e4-c590-4b1b-8eeb-e7b8807bfa9e')
        
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
        self.vs[0]["GUID__"] = UUID('b1491a19-357d-4b3a-9850-372c52b4b7f3')
        self.vs[1]["Name"] = """Const2"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('cb49a6d0-b273-4f61-bfd0-82215b6d9ccf')
        self.vs[2]["Name"] = """1"""
        self.vs[2]["mm__"] = """Port_Output"""
        self.vs[2]["GUID__"] = UUID('dea7d944-da00-410f-b256-5cfa7519fc3c')
        self.vs[3]["mm__"] = """__Block_Outport__"""
        self.vs[3]["GUID__"] = UUID('43b529b6-471e-42dc-a468-326e0973e5df')
        self.vs[4]["Name"] = """1"""
        self.vs[4]["mm__"] = """Port_Input"""
        self.vs[4]["GUID__"] = UUID('60de8d07-9fbd-479c-8dfc-9cfbda25e908')
        self.vs[5]["mm__"] = """__Block_Inport__"""
        self.vs[5]["GUID__"] = UUID('3dcc4423-576c-4b08-8760-77d0e60a6c60')
        self.vs[6]["mm__"] = """__Relation__"""
        self.vs[6]["GUID__"] = UUID('f3760a60-17b4-430e-95c7-93e87db95880')
        self.vs[7]["Name"] = """Constant9"""
        self.vs[7]["SampleTime"] = """inf"""
        self.vs[7]["value"] = 249.0
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["GUID__"] = UUID('07e67375-bdc0-4419-bba1-1fd49affc54d')
        self.vs[8]["Name"] = """None"""
        self.vs[8]["mm__"] = """__Contains__"""
        self.vs[8]["GUID__"] = UUID('85ffdc63-bec3-4932-8fef-ff610b66dd2b')
        self.vs[9]["Name"] = """None"""
        self.vs[9]["mm__"] = """__Contains__"""
        self.vs[9]["GUID__"] = UUID('3b54164a-d1fd-449e-b454-4733e6399c27')

