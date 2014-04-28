

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
        self["GUID__"] = UUID('1ef5e87b-593e-4c02-87e3-4f9ee678a8e8')
        
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
        self.vs[0]["GUID__"] = UUID('567562c7-06c9-43fc-9dcd-60a183d369f3')
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
        self.vs[1]["GUID__"] = UUID('4e64b084-2296-4e37-9051-294c6a5c77cc')
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
        self.vs[2]["GUID__"] = UUID('297df820-a9d0-47e3-9e17-14e3956b701a')
        self.vs[3]["Name"] = """Const1"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('1ed8f894-bd71-4f43-8cd3-30f1452a2067')
        self.vs[4]["Name"] = """Constant23"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 439.304
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('9aa79948-d8b3-4055-9107-feb3d2432534')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('a71314b5-457e-4263-9326-33bb0d374f36')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Output"""
        self.vs[6]["GUID__"] = UUID('80f897e2-f92c-4a83-8070-bb265ceeac14')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('07f8be8a-b26f-4d8d-8e7d-6070c8bc8f25')
        self.vs[8]["Name"] = """2"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('b50dcdcd-fe23-477f-91b7-35856d667f10')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('1055317e-d35a-427e-b51d-feae41b77da6')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('29e52ee7-cde5-42cb-b933-d359cfb97982')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('71caa6c5-4031-4100-9c59-e9ba23512856')
        self.vs[12]["mm__"] = """__Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('aa56b085-8449-4b74-8c44-f15703473feb')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('7f38298d-e20b-4fb4-998b-d851b2e323d9')
        self.vs[14]["mm__"] = """__Block_Inport__"""
        self.vs[14]["GUID__"] = UUID('d75c4934-0d4e-4faa-b57e-20a42952c798')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('01feb3f2-bf8d-4dfe-bd06-f95219933be3')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('01bf47fe-4c22-48f1-be42-ad4d1c694c55')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('682799cf-8e61-4a30-bc00-b79de11d63c1')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('e1c96864-9d97-4a51-9b55-7264321f981d')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('6315b295-d8e3-4507-928f-0e5ec938310f')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('33d04e04-6987-4009-9a2c-6d0cd1f6393b')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('7ebf8fba-63f6-45a2-8494-45055721a889')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('627dadd6-b5b5-4dd9-b229-86559054c0c3')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('30f79633-5546-42e4-a54e-62f3913916bf')

