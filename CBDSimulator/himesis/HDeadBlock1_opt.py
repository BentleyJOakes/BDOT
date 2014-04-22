

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HDeadBlock1_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HDeadBlock1_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeadBlock1_opt, self).__init__(name='HDeadBlock1_opt', num_nodes=50, edges=[])
        
        # Add the edges
        self.add_edges([(1, 15), (2, 19), (4, 49), (4, 48), (4, 47), (4, 46), (4, 45), (4, 44), (4, 43), (4, 42), (5, 16), (6, 17), (7, 18), (8, 20), (9, 40), (9, 39), (10, 37), (11, 41), (12, 36), (13, 38), (14, 35), (15, 9), (16, 10), (17, 11), (18, 12), (19, 13), (20, 14), (28, 21), (29, 22), (30, 23), (31, 24), (32, 25), (33, 26), (34, 27), (0, 28), (1, 29), (1, 30), (2, 31), (2, 32), (2, 33), (3, 34), (35, 26), (36, 24), (37, 25), (38, 22), (39, 21), (40, 27), (41, 23), (42, 0), (43, 1), (44, 5), (45, 6), (46, 7), (47, 2), (48, 3), (49, 8)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HDeadBlock1_opt"""
        self["GUID__"] = UUID('a1b8f281-ac21-4148-a2eb-febfac18e125')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F430
aF88
aF460
aF102
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('83f7a4b1-55a5-4b14-ba31-daf94687b90c')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F315
aF157
aF345
aF188
a.""")
        self.vs[1]["GUID__"] = UUID('1aea537c-5693-4a25-8d4f-ceb099375934')
        self.vs[2]["Name"] = """Switch"""
        self.vs[2]["Threshold"] = 0.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Criteria"] = """u2 >= Threshold"""
        self.vs[2]["mm__"] = """Switch"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F185
aF90
aF235
aF130
a.""")
        self.vs[2]["GUID__"] = UUID('97e79ff7-267a-4698-9449-7fa0a4389932')
        self.vs[3]["NumInputPorts"] = """1"""
        self.vs[3]["Name"] = """Scope"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Scope"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F430
aF154
aF460
aF186
a.""")
        self.vs[3]["LimitDataPoints"] = """on"""
        self.vs[3]["GUID__"] = UUID('7e101a5e-efe9-442d-a98b-544fa706bb1a')
        self.vs[4]["Name"] = """DeadBlock1"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('3f349a07-ed83-41aa-990b-4a7325a144d0')
        self.vs[5]["Name"] = """Constant"""
        self.vs[5]["SampleTime"] = """inf"""
        self.vs[5]["value"] = 10.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F45
aF70
aF75
aF100
a.""")
        self.vs[5]["GUID__"] = UUID('06da663e-cd2e-45e4-8b63-8d5bc0ceb4e5')
        self.vs[6]["Name"] = """In1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Inport"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F175
aF198
aF205
aF212
a.""")
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('2056a698-5889-4f15-87a0-0e9bf720f0a2')
        self.vs[7]["Name"] = """In2"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Inport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F45
aF23
aF75
aF37
a.""")
        self.vs[7]["Port"] = 2
        self.vs[7]["GUID__"] = UUID('2e518253-2bfb-45d2-8826-989efa9496f0')
        self.vs[8]["Name"] = """Constant1"""
        self.vs[8]["SampleTime"] = """inf"""
        self.vs[8]["value"] = 123.7
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F25
aF140
aF55
aF170
a.""")
        self.vs[8]["GUID__"] = UUID('1a816778-6418-4248-97e1-66acace78c18')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('0599d8a3-fc2b-411f-9d31-695e7c873e44')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('aed3d4e2-3df1-43c9-bab7-ba12edc7c110')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('fd7df0b0-0473-448a-a7fa-bf37074130ec')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('b194cea6-b5f9-41e2-abbf-b1d3d5656464')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('e4a0da4e-3228-44be-9a95-5a3ddd7c9e5a')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('1763b306-8dbd-4e01-a739-c80d2abfbb25')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('30742be1-6609-4af9-82ee-0a78cce380c4')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('f7360b4b-4944-4aa4-a1dd-779880b21f72')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('a42743e6-31cc-4f66-a3e4-3d58b08d6ec1')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('43d06b8a-f967-41b8-a4f9-43227d3ffd6b')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('0f1dcec2-0047-46fa-b4b5-56056978a6c9')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('6dc34e25-a5d5-4473-91ec-471c7cd05769')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('e90cbab1-57a8-4e4c-a2e7-7705f12b853c')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('0454391e-ee0b-47c8-a8bb-8a29a06d61f9')
        self.vs[23]["Name"] = """2"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('c3fe0024-23f2-43e3-a0f5-d4dea347fb0a')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('91ba70ac-1984-44b2-9fd8-b8e43491ca8c')
        self.vs[25]["Name"] = """2"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('0ebeb234-8599-4e67-98db-46afd3cacbaf')
        self.vs[26]["Name"] = """3"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('6c422fb8-c600-4fdf-8c7b-256a075e9cb3')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Input"""
        self.vs[27]["GUID__"] = UUID('65338ba8-d56a-479b-b76d-fed63a892b6d')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('efce2e4d-bea4-4d1e-be71-cb38b6f6b6df')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('292a5264-29f6-4ad6-9c4f-5ae1d6493da9')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('12cf0e0d-a5d0-4d34-8370-0bfd0e87357f')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('28ccfad1-c07b-4ee1-98cf-70e94b3d8de7')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('7ac14669-c9f9-4727-bac0-ad16a9117372')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('640141cc-317e-4150-9b01-27f2cefff2e1')
        self.vs[34]["mm__"] = """__Block_Inport__"""
        self.vs[34]["GUID__"] = UUID('557d1a6a-56a7-4bb4-a875-c7d992c63e5e')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('05f23c0c-1805-4801-9880-5816f39d5d42')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('581d3300-2104-45fb-a3d3-93979d3fec93')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('7d9943c5-9b54-4420-a56d-a0c39a732ade')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('72c2313f-d592-4a6c-9137-69dce30acc40')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('85857f90-83cb-4418-82c5-c6562791f1f5')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('846581cd-c1d2-43ba-b162-20dea09df1d1')
        self.vs[41]["mm__"] = """__Relation__"""
        self.vs[41]["GUID__"] = UUID('c64daa2b-5962-4d55-922d-cf34a0589086')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('2c2e9fcf-b59d-4aba-bee3-6df6742a0b7b')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('7c572c3d-5abd-42fb-aab1-893522f42309')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('61c2b568-527e-43ef-89a8-a02061cc245f')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('8870c68e-9aa5-4cec-851a-27b18d587985')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('2f4cad75-919c-4293-a9b2-2a0d47a33551')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('85c58afb-3773-4958-814a-9c32906a4df9')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('31d7bb94-3012-40dd-b7ce-7072c77849a5')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('b6506168-aeb1-45fa-b10d-5d842fb21d87')

