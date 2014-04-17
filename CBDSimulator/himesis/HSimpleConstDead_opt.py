

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConstDead_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConstDead_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConstDead_opt, self).__init__(name='HSimpleConstDead_opt', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(1, 14), (2, 15), (3, 23), (3, 22), (3, 21), (3, 20), (4, 16), (11, 5), (12, 6), (13, 7), (8, 18), (9, 19), (10, 17), (0, 11), (1, 12), (1, 13), (14, 8), (15, 9), (16, 10), (17, 6), (18, 5), (19, 7), (20, 0), (21, 1), (22, 2), (23, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConstDead_opt"""
        self["GUID__"] = UUID('50e56ef4-6e50-4611-8dc3-c98c3b762916')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F390
aF118
aF420
aF132
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('fe18ea1d-7f41-4a5f-a002-de637058fb9e')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F305
aF132
aF335
aF163
a.""")
        self.vs[1]["GUID__"] = UUID('28696dfb-ed30-4ee6-89ce-d14f3956d894')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F170
aF178
aF200
aF192
a.""")
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('6950623b-64f8-46ab-899f-edbffbbb78f2')
        self.vs[3]["Name"] = """HSimpleConstDead"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('bdca4a31-159b-4105-a373-cb786b3818f7')
        self.vs[4]["Name"] = """Constant2"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 433.22
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F50
aF82
aF105
aF118
a.""")
        self.vs[4]["GUID__"] = UUID('d289932a-ec0a-47ea-a1a3-590e07e45942')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('74c0f496-5d78-454e-afd1-84484a1af968')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('c5bff6ac-ced3-439e-a28f-badd05361011')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('285a7891-057d-4871-92f8-6ea6b3de60fd')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('4db961a0-c98d-45ec-aa3f-0b0ca4dd9c3a')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('49869bf5-b96b-4c39-9ff0-9c395d79765d')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('c225dd05-5b00-4397-b09f-587efa70f449')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('82dfa82b-aa13-4005-9489-7883fec3842f')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('41eafb72-3bb9-41b4-9bbc-c85cd1d47394')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('9162f996-d0b6-4d7e-b74b-6a332ec2b4c5')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('dac4d289-89c8-4e9c-8dfb-436f816e0064')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('2555f036-a626-4268-92fc-6a7731696c9b')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('5acabeef-870d-47ca-956b-bf6d840c807b')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('9a2b3ea7-e9ba-4a01-a433-5cc8dbac5bd3')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('b63ee0fc-526a-49bd-b72b-32aa327f1e4e')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('a23475b8-bbea-4a2d-9fd0-43939a79ac1e')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('8056de80-096a-410e-bf0e-7eaede6402c7')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('5097c17b-fef4-49d2-914b-36caa9e04457')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('df8ee59e-383c-497e-a151-4f5f92b565d9')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('8f1071df-34c8-4fcc-9ae1-4b031a410c0c')

