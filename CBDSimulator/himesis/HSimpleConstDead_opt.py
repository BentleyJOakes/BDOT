

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
        self["GUID__"] = UUID('011d9815-4d3c-484a-9ad5-b7ba77d435a2')
        
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
        self.vs[0]["GUID__"] = UUID('6ff20dda-0303-4c15-90ec-6d05c744fd0b')
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
        self.vs[1]["GUID__"] = UUID('a8232220-051b-4667-93d7-d501c3fd51ca')
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
        self.vs[2]["GUID__"] = UUID('20d7f209-e75e-478d-8529-abc12104d9b7')
        self.vs[3]["Name"] = """HSimpleConstDead"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('91c14f77-8690-4711-b27a-b6d58059f261')
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
        self.vs[4]["GUID__"] = UUID('403e25eb-b424-4df9-8936-2fb8599e7d4c')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('ee777a95-59ec-4599-8c7f-2426d18af89e')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('375fe4e7-61af-4500-ac4f-257d71d190dc')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('50e842e7-ca2a-4967-bd95-d73b2f34fc14')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('4a2ad1b1-280c-4b06-bfac-7b48894b5b2f')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('5274b79a-b5c3-4e63-bab5-b5f6f7e03aa6')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('3d732195-d8d0-418e-90cd-7c035b7481f1')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('4841f0d9-94fa-40ba-ac07-d4f5a966cf4c')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('2a7c83c5-939e-4f49-942e-824c0f4e8bce')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('00e8dadd-5727-4005-8fb5-4f1e1c673bcb')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('8805fa08-01f4-4c07-a3a2-fbee2af8f5c4')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('a401a87b-a7ad-479c-a61a-c6cbb4d024b4')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('bd614c89-dc10-463d-9d65-a14a2051f3b5')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('3716d7af-20b9-4bc8-bdc5-66bea58354c7')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('c52477ed-963e-469d-b168-caec7f24c66c')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('08b17ec9-05e8-4633-8dc8-a4a68e9e1ee9')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('b9a48946-1a37-409d-9e7a-776b20316f5b')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('037266bf-df7c-4e7a-8e5c-29091ea53b14')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('dc1731e6-eb2d-464c-96f3-aab2a1278519')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('122b4c6e-419f-48aa-a9d0-095007c36ec9')

