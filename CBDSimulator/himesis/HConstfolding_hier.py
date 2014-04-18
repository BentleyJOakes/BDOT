

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_hier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_hier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_hier, self).__init__(name='HConstfolding_hier', num_nodes=71, edges=[])
        
        # Add the edges
        self.add_edges([(5, 40), (40, 30), (5, 41), (41, 31), (5, 21), (21, 12), (6, 42), (42, 32), (0, 22), (22, 13), (1, 43), (43, 33), (1, 44), (44, 34), (1, 23), (23, 14), (2, 45), (45, 35), (2, 46), (46, 36), (2, 24), (24, 15), (3, 47), (47, 37), (3, 25), (25, 16), (9, 26), (26, 17), (10, 27), (27, 18), (11, 28), (28, 19), (4, 48), (48, 38), (4, 29), (29, 20), (7, 49), (49, 39), (5, 60), (60, 1), (5, 61), (61, 2), (5, 62), (62, 3), (5, 63), (63, 9), (5, 64), (64, 11), (5, 65), (65, 7), (8, 66), (66, 5), (8, 67), (67, 6), (8, 68), (68, 0), (8, 69), (69, 10), (8, 70), (70, 4), (19, 50), (50, 33), (17, 51), (51, 34), (16, 52), (52, 36), (16, 53), (53, 39), (15, 54), (54, 37), (14, 55), (55, 35), (20, 56), (56, 31), (18, 57), (57, 30), (13, 58), (58, 38), (12, 59), (59, 32)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier"""
        self["GUID__"] = UUID('0c3ab8e0-f90e-4371-ade1-6b7d3a2723e2')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F140
aF65
aF170
aF95
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('eaa0607a-c018-4cd1-9f11-b5d778ac7460')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["GUID__"] = UUID('ca4e6aff-3118-4a7c-81b5-32701ca52904')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('87ececd0-a34d-4c54-9cba-83a7bb564c29')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["GUID__"] = UUID('33fb62ba-c153-4909-848b-de29c2281e8e')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F205
aF65
aF235
aF95
a.""")
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["GUID__"] = UUID('9e272dd4-ba28-4dd9-b15e-2457ab58daa5')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["GUID__"] = UUID('df8de636-898b-4d49-abda-3e951f913901')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('666f27e9-7986-4d1f-8714-a9dcc81f1bf5')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F365
aF103
aF395
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('da475a74-4ef7-4559-9bcb-6edf5c081486')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('3d8f2153-e1de-4e23-98ae-42552dd427e5')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F150
aF118
aF180
aF132
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('d217c873-59db-4c22-9126-b11b5f4e0218')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('93f367a0-5ddb-496c-be45-991d979dbb46')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F150
aF88
aF180
aF102
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('e4068139-beaa-4e81-9abb-088bfe0e7b15')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('a0d03735-797f-48dd-8acf-3ced9fc3f048')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('ab27071e-560b-4518-b36c-02ebd6f67adb')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('60b58b65-9bf4-4e3e-83fc-8cdaf62f2460')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('0ff29710-9f1b-4d1d-bd2e-1f28f28230aa')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('2b2fe9ea-c3b3-42b8-b741-33cfa2a93ca5')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('b3c5614c-0255-4de9-b57f-87a9f997b8b6')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('1910dadb-df62-4b24-ac51-3b5197630938')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('3bfd0212-813c-4cf2-85f0-bfc90eb0af74')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('69f98181-71ae-401c-94b5-8bd055428ee3')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('306624a7-7d02-4283-88c7-992387023f5f')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('65c57598-1aaa-4792-b82b-3a2a2e788e8a')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('8e6848a6-f46d-427a-a7b2-3057947492fc')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('58d33dcb-a8d9-4fe2-9d22-4b536aa6117c')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('4c2f8a9c-7717-4843-98ed-40f6a9c91e6c')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('7f035912-9ec5-44ac-91e8-fc4189c0bbab')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('eff10b19-36dd-4d76-acab-395412db3f13')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('7acfd7bc-52c1-4bda-be45-faccfe8e5047')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('43d9c285-ce93-4072-8b99-9ef4f6691cd0')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('0ad47c1d-fd99-4bcd-a9e7-11ed7dcafed0')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('f13ac46e-1b8d-405e-a764-b5e41d2ee349')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('f9904a5e-b9c9-4188-b116-5529cc6dd4d5')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('4cf61dfa-82e2-403c-a3c5-1d0a3e6d8912')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('d55b01ab-45b5-42c0-8b52-57bad4478699')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('360868a8-6e70-4041-91a0-b49d62005279')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('72df49fa-b124-4772-883d-98213d48c2a8')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('14b9966f-1702-44a2-9061-3e500abdb595')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('3b16ee26-43ee-4b80-8202-80fe52f3706a')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('f9c987b4-b8c8-45e1-9250-b07d953ed443')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('00411de8-0039-4dbe-a2cd-fe1d6c88eb9b')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('9c6b8599-4019-47e2-acb8-6626a85e4148')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('eb88eed6-46b9-415f-beb9-f357789e216a')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('a22de4fc-eafb-4ba6-b086-3077089463b8')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('4c6e3595-7c6d-461a-897a-2ac44e52fe71')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('319852f6-9e4a-4508-b8d7-3ae65f7ea78d')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('a12dfd0a-1474-4ef9-bcd8-d2d35b50dfe5')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('fd00ee5b-1954-4a07-b553-34084959b128')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('99a93b94-95d3-458b-89c1-929053214992')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('8070fe51-1f0f-4c20-bc94-d6582b8024fe')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('cee67588-642d-4738-8db8-3137d78e2102')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('6196b68d-8c58-4be9-aa95-600315b08fd4')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('ea93da73-3a71-4298-9cd6-e33e4520b282')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('5666e8c9-ff76-4292-95f7-82c880b4cc58')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('f231d6df-e69e-43b8-aa74-105a8e8801bb')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('e1f982bb-8329-4e1c-9818-8d5e3e3529e3')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('abbd44fb-68c0-4d31-9d5b-3e6093b01632')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('2e4ccd16-eb86-4b38-8bb9-4b461afa4dee')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('3d565436-0aa8-4927-ba3f-f1658abf4e6a')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('6d9b1295-da54-4b70-8a3e-2a7137881186')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('6cb6b59e-6f54-46d4-aeca-690fc731ffcf')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('382322a6-00d8-4c1e-b349-97bd08ff5447')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('122e73f5-ee96-46a5-b191-393a7bfb0490')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('797717ad-8605-4960-a6ec-48518a7a29f3')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('1ece1159-493c-4340-9146-41474795df5b')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('dd5002b2-dfcd-4540-92f8-526d3b32ee55')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('07c1d30b-7b21-4560-9fa3-d64da2691421')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('e15da903-2a9a-44fb-aa06-68288aeb2817')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('044ffd6e-3a23-432a-a06a-ec3494cc0fdd')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('46bfd06c-f927-41ab-b1e5-9427b675ecbf')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('105d0ef4-43bb-4bad-a032-f974ac4451a2')

