

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConst2(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConst2.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConst2, self).__init__(name='HConst2', num_nodes=62, edges=[])
        
        # Add the edges
        self.add_edges([(0, 44), (44, 26), (4, 45), (45, 27), (4, 46), (46, 28), (4, 18), (18, 10), (6, 19), (19, 11), (1, 47), (47, 29), (1, 48), (48, 30), (1, 49), (49, 31), (1, 20), (20, 12), (2, 50), (50, 32), (2, 21), (21, 13), (5, 51), (51, 33), (5, 52), (52, 34), (5, 22), (22, 14), (7, 23), (23, 15), (8, 24), (24, 16), (9, 25), (25, 17), (3, 35), (35, 0), (3, 36), (36, 4), (3, 37), (37, 6), (3, 38), (38, 1), (3, 39), (39, 2), (3, 40), (40, 5), (3, 41), (41, 7), (3, 42), (42, 8), (3, 43), (43, 9), (14, 53), (53, 29), (16, 54), (54, 33), (17, 55), (55, 30), (17, 56), (56, 34), (10, 57), (57, 31), (12, 58), (58, 26), (13, 59), (59, 28), (11, 60), (60, 32), (15, 61), (61, 27)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """Const2"""
        self["GUID__"] = UUID('d4bf4dc2-07ee-4b4a-9dea-be27f049e8ee')
        
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
        self.vs[0]["GUID__"] = UUID('b063c5a3-cee6-4097-a36f-deff426ca73d')
        self.vs[1]["Name"] = """Switch"""
        self.vs[1]["Threshold"] = 0.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Criteria"] = """u2 >= Threshold"""
        self.vs[1]["mm__"] = """Switch"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F355
aF125
aF405
aF165
a.""")
        self.vs[1]["GUID__"] = UUID('dbd3a845-e192-4770-a252-0719cf9e176d')
        self.vs[2]["Name"] = """Gain"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["gain"] = 5.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Gain"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F135
aF165
aF165
aF195
a.""")
        self.vs[2]["GUID__"] = UUID('cfab34ae-837f-46ac-aca6-36b4375aff77')
        self.vs[3]["Name"] = """Const2"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('b7ecce8e-82c7-4366-b6a5-6cd9fd4b4ad3')
        self.vs[4]["Name"] = """Product"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Product"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F225
aF142
aF255
aF173
a.""")
        self.vs[4]["GUID__"] = UUID('543eacdd-9079-436e-98ad-0366bee50c38')
        self.vs[5]["Name"] = """Product1"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Product"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F285
aF62
aF315
aF93
a.""")
        self.vs[5]["GUID__"] = UUID('72b81899-76c4-48fc-baf7-c4ee8c4d24b8')
        self.vs[6]["Name"] = """Constant"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 12.34
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F45
aF152
aF90
aF188
a.""")
        self.vs[6]["GUID__"] = UUID('151675df-b822-43b2-a49b-febaf1c8b430')
        self.vs[7]["Name"] = """Constant1"""
        self.vs[7]["SampleTime"] = inf
        self.vs[7]["value"] = 7.12
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F40
aF80
aF70
aF110
a.""")
        self.vs[7]["GUID__"] = UUID('dfa6e60e-3e73-40b7-af61-8cf96c718e04')
        self.vs[8]["Name"] = """Constant3"""
        self.vs[8]["SampleTime"] = inf
        self.vs[8]["value"] = 124.5
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F210
aF35
aF240
aF65
a.""")
        self.vs[8]["GUID__"] = UUID('1a193b18-aa52-426d-8a60-cd522d2d065e')
        self.vs[9]["Name"] = """Constant2"""
        self.vs[9]["SampleTime"] = inf
        self.vs[9]["value"] = 2.0
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F95
aF40
aF125
aF70
a.""")
        self.vs[9]["GUID__"] = UUID('cdad7da0-a88b-47e8-bf5d-7961a657090e')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('fc203e01-fc9f-44d8-933e-51d53bc76705')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('f2e7b62e-5051-4ad9-a23b-ff35e6519d21')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('d229b380-ed3e-49e2-9136-365442e06877')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('d046d2cb-89d4-41af-aa8e-9befd0bb3e93')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('6dbe8258-da4b-4795-825d-b4779ceb95cc')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('99f24562-e190-456a-918d-8aacdf24414c')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('ca2d083b-f846-4d42-a479-1b0f7f7b4d81')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('2ba8287d-8e41-477a-9f4b-3fc8a80457bb')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('a283a7a4-e628-4973-8008-f513e2abbb97')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('2de854d2-3671-4598-a9bc-bd96fbf362f7')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('944122a8-4660-4b2e-a0f3-1f2584b2a696')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('d21757a5-5d3c-4392-a558-fb12adfc0256')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('b175e3d3-f0e4-459e-968d-6d133c2afb65')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('fa703953-1b3c-48ef-b73a-be8f6f32a3f3')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('61a92659-3bc3-4ac5-b4af-ccaaf2c3d9fd')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('bbd3fcc0-af50-48cd-8eae-8a4109e04032')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('869445a5-202d-4049-8bdf-b9dc8ad9a216')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Input"""
        self.vs[27]["GUID__"] = UUID('76784c88-3928-40de-ac8d-3b05cf3605d3')
        self.vs[28]["Name"] = """2"""
        self.vs[28]["mm__"] = """Port_Input"""
        self.vs[28]["GUID__"] = UUID('e2c0f81b-bc15-435a-ba19-f285e2d5cd1c')
        self.vs[29]["Name"] = """1"""
        self.vs[29]["mm__"] = """Port_Input"""
        self.vs[29]["GUID__"] = UUID('79958ca0-8abb-4597-811e-084c8aa4b479')
        self.vs[30]["Name"] = """2"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('b0d8cd9d-795c-47a9-b35e-80df056eb6f7')
        self.vs[31]["Name"] = """3"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('6737024b-0e75-43e8-98fc-873e05203b20')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('9104d201-715a-496f-b046-345031aabbfd')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('f7adee5e-a63c-484b-a087-05c8625a4ffc')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('2891d23e-4f47-42e9-8261-6e7ffb4071fb')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('450c2492-400f-4537-b133-891dacbababc')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('5abe4979-433e-47b3-8b33-633c88c99ad0')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('8d78d492-52b6-4c32-bd45-a91802a5c1b3')
        self.vs[38]["Name"] = """None"""
        self.vs[38]["mm__"] = """__Contains__"""
        self.vs[38]["GUID__"] = UUID('996ae4f6-af70-4a79-88eb-33cf1e98be4a')
        self.vs[39]["Name"] = """None"""
        self.vs[39]["mm__"] = """__Contains__"""
        self.vs[39]["GUID__"] = UUID('4529ec4c-9f97-492c-b44c-fa214b1da6e5')
        self.vs[40]["Name"] = """None"""
        self.vs[40]["mm__"] = """__Contains__"""
        self.vs[40]["GUID__"] = UUID('bced3be9-6397-4234-92a5-d0de6ddaa022')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('7bda2598-6dcc-46e3-919a-38958e634700')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('92ddcae2-3685-4a66-9d99-a1e041ff9932')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('d36bafbc-93c9-4fb7-b6f9-e7e3cefa1424')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('c2b6f68a-d5a4-4858-ae02-fabb2a0a4868')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('af283b6c-e348-4383-a024-e94fcbb6bbab')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('73327809-27e3-4f3e-8649-3ba6bd26447e')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('3a02a733-fcd5-4374-bd3b-4826a0708ef7')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('40a71777-dcf7-4e43-8895-ed9bfa30b88d')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('6876e991-172c-460d-a889-503f58350b4a')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('99ed2a25-2191-4ab8-a89b-cf5b2b0bcdfd')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('e4845a07-0280-4e6e-b9e0-d0f1444ce6f8')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('4b9a3668-ccba-4be4-a343-9675ac265bca')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('4e3653ee-851e-49a7-af64-5e64069ca4d8')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('47fc26c8-1aef-4ee4-aa44-5c78fbfbfebc')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('5168566f-8a14-4a0a-a99b-ceeac434a66e')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('f68fb95d-6467-404f-bbc4-2e1b901bc66d')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('d5aa5754-ce3c-4858-9da9-f01177fbe7c0')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('f99b6a97-59fb-456b-b170-cceea9bfc1c0')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('7193b31d-3d89-4dca-bb3c-edca08a013eb')
        self.vs[60]["mm__"] = """__Relation__"""
        self.vs[60]["GUID__"] = UUID('30b5474f-13f7-4fc6-b430-4860bdd71c97')
        self.vs[61]["mm__"] = """__Relation__"""
        self.vs[61]["GUID__"] = UUID('3fb539b8-4247-40b2-bddc-4be5b6f4324e')

