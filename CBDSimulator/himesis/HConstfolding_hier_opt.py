

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_hier_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_hier_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_hier_opt, self).__init__(name='HConstfolding_hier_opt', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([(0, 14), (1, 15), (2, 16), (3, 17), (4, 19), (6, 41), (6, 42), (6, 43), (6, 47), (6, 46), (6, 45), (6, 44), (7, 18), (8, 40), (9, 37), (10, 36), (11, 35), (11, 34), (12, 39), (13, 38), (14, 8), (15, 9), (16, 10), (17, 11), (18, 12), (19, 13), (27, 20), (28, 21), (29, 22), (30, 23), (31, 24), (32, 25), (33, 26), (5, 27), (1, 28), (1, 29), (2, 30), (2, 31), (3, 32), (4, 33), (34, 24), (35, 20), (36, 25), (37, 23), (38, 22), (39, 21), (40, 26), (41, 1), (42, 2), (43, 3), (44, 5), (45, 0), (46, 7), (47, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('1f17b958-54fc-4027-a140-54c7f0a86f89')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F140
aF65
aF170
aF95
a.""")
        self.vs[0]["GUID__"] = UUID('c3d57f5a-3b0a-4e6c-b0ba-273255b16f29')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["GUID__"] = UUID('13c19812-b5ed-45d7-8760-f12b6d3c03b1')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('07af329c-ae6b-4269-865d-e3bc1a081cb3')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('9c5d4b02-1ea3-4528-b2eb-5ee11e2c3d51')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F205
aF65
aF235
aF95
a.""")
        self.vs[4]["GUID__"] = UUID('f1699829-fb2f-40a9-98de-a2111e82cc10')
        self.vs[5]["Name"] = """Out1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Outport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('66891f58-fcd2-4c15-88f6-3fd76bf51281')
        self.vs[6]["Name"] = """HConstfolding_hier"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('59e76fb2-a475-4cd5-a2c5-134358bf4c85')
        self.vs[7]["Name"] = """In1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Inport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('5d444644-f083-430d-8d2e-c2023215a3bc')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('d2d5e37c-1fdd-4c48-a9f6-a58168aaafc9')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('9f04858b-1e1b-4f00-a31e-8cc3574b6f5e')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('7dc73cd3-7aa2-49e8-a631-2a3ea5cf939e')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('68a47c40-6823-436b-b06d-44d71ffa68eb')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('7b5ba7cb-a0fb-45b7-b91f-0a50e8b3279d')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('b8c3f32c-c3fe-4f30-ac48-8864ce7e6599')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('f8fa65e5-f681-4c5e-a4cf-d9477ec5a144')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('7247927c-7987-42a2-a295-ef76d92ab4dc')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('28c4c3d4-7bb4-4a92-8d6b-73c38b4d087f')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('01731f1d-8900-4e6d-ae1a-f6d961033144')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('36f34ad3-7d90-4249-baaf-0bb6b056736c')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('83521fe4-019b-4270-afc9-3c15111e92fe')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Input"""
        self.vs[20]["GUID__"] = UUID('c4cc7098-b9c5-44c5-bcb2-dbb554640cc8')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('e3bc9e1a-79b0-48ed-b837-8d65c2f603ca')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('4cce617e-f550-4516-a292-5d7a524b327b')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('190e2715-f1af-4084-bed8-a662c054bdd3')
        self.vs[24]["Name"] = """2"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('75f71298-03aa-4ede-bf61-23d2e06690b3')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('7b804712-f480-4458-990c-20c0ea906e38')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('11d15c81-aac1-434c-91b5-0519e5cb3720')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('e75129a0-48eb-430e-9038-9e64dc04549e')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('b41d4fca-67b6-4a93-b632-8ce76709d7c2')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('c19e3942-3c74-48c2-843b-4d57ea58ee4e')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('63a2a08d-2cfe-41c3-a3f6-89f3307011df')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('d12e078a-d2cc-4f66-a3f5-bf08660130f6')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('67b190db-8407-4887-a02b-c3060cba7d97')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('6e5a3b77-54cf-435d-8195-f49e6e26c580')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('460ad2f2-e3ef-44e8-b9cf-b004d90a7f09')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('0fc2f411-0db1-4dcf-9099-b12e80c46401')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('0f4ef256-0b0a-47c7-b54b-5a205aad0af8')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('6ce844cc-4f3c-4e26-970b-8d444b28a487')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('a1897b14-2d93-4f3b-a9b2-71ed4cc53f55')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('19e35a43-6f41-4615-885c-7d66f7862f71')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('f34ba6f1-6fbb-43be-a1f0-158d18d582df')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('8dd0b541-735e-47b2-8e93-432903e70cff')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('f380662e-e89a-4f95-a7fb-214d1a0041e0')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('341cee95-6048-415a-897b-a17346aceeb8')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('cd3cc982-3c0e-4e1f-a45c-8c53bb0c8b68')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('6abf58b6-1cb2-49b9-99b5-987473424344')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('ac2ea92a-8e83-4485-8b74-db6cb87a7e22')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('e9d57156-0434-4ad6-9bfd-547612f6627d')

