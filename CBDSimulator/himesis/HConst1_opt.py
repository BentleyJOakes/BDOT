

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConst1_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConst1_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConst1_opt, self).__init__(name='HConst1_opt', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(1, 15), (2, 16), (3, 23), (3, 22), (3, 21), (3, 20), (11, 5), (6, 18), (13, 7), (14, 8), (9, 17), (10, 19), (0, 11), (12, 6), (1, 13), (1, 14), (15, 9), (16, 10), (17, 5), (18, 8), (19, 7), (20, 0), (21, 4), (22, 1), (23, 2), (4, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConst1_opt"""
        self["GUID__"] = UUID('90ee5485-6cee-4ee9-b94f-6dc504b90959')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F415
aF138
aF445
aF152
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('fb50dc1b-4012-489d-8685-9bb01c304fd2')
        self.vs[1]["Inputs"] = """|++"""
        self.vs[1]["Name"] = """Sum"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Sum"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F300
aF95
aF320
aF115
a.""")
        self.vs[1]["IconShape"] = """round"""
        self.vs[1]["GUID__"] = UUID('c5ccc52b-013c-4a7c-b5ce-03e0a3ff4bbd')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F90
aF48
aF120
aF62
a.""")
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('fc4ff8d5-72ff-4dfa-9e25-7696731f6ad2')
        self.vs[3]["Name"] = """Const1"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('fa6483da-0799-49a4-bf03-68460a5cec1d')
        self.vs[4]["Name"] = """Constant23"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 439.304
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('e1184654-7dd3-4816-b36f-086674526fce')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('223e03c0-1ef2-4ebb-ae25-ada92788c1f0')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Output"""
        self.vs[6]["GUID__"] = UUID('7b0a7bc9-fe13-4dba-86b7-7f1bd76a8599')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('6fd32d20-3343-4fd7-a555-7c2db7e3d207')
        self.vs[8]["Name"] = """2"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('82e9f3ad-c127-48f8-9b65-d0f364f76274')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('130063dd-c50b-405f-ad00-de7d37bd8bba')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('d0c0c0f9-e8df-4cf0-9670-ec0adb2635d9')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('65113697-9c8d-41ef-a63c-6890daccafb0')
        self.vs[12]["mm__"] = """__Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('5e95796c-1654-4104-a5bc-1a43103e4898')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('b01a4ad6-1e24-4f55-a5db-60ccd93d7502')
        self.vs[14]["mm__"] = """__Block_Inport__"""
        self.vs[14]["GUID__"] = UUID('a5ae7805-c77d-4054-9420-16da05a3c59b')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('75d8bcd7-12a0-4ba9-8e4b-ac56a5ab4622')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('e7bfa0f2-7e0b-45a1-a8ad-ebbd79af513b')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('0aa21aa1-8152-41ee-97a3-3c2f410de1d9')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('cedd1ee8-a2b4-40d5-8bc7-f4d50f127d7d')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('dc62255a-1055-4e04-a1de-1d904bec4586')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('ba508c5a-ada0-47ca-adbb-d41fd368adf1')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('573fa072-657b-4061-aad9-2bff30c55a11')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('e082d9ce-eced-4f47-9427-8e502aecf542')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('f2ecbb3d-6ece-4e95-bf7d-7408d84f0494')

