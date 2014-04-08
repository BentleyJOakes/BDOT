

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
        self["GUID__"] = UUID('e75abd26-056c-450c-925f-d6952db03add')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F125
aF125
aF155
aF155
a.""")
        self.vs[0]["GUID__"] = UUID('bb289f89-9a0a-4bba-80bd-606923f0fffd')
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
        self.vs[1]["GUID__"] = UUID('816e5dbc-8131-4f6f-84bf-3b510a830809')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F275
aF100
aF295
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('939a8311-b13a-41c9-8568-97c25cef7978')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F325
aF93
aF360
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('c2f688cc-284d-492e-a381-de1ad630e011')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F215
aF125
aF245
aF155
a.""")
        self.vs[4]["GUID__"] = UUID('f8f43a7e-2ead-47d3-8bdc-68f7e7eff08f')
        self.vs[5]["Name"] = """Out1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Outport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F485
aF38
aF515
aF52
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('6377f1dc-d9c2-4601-bfb8-a609cb17a65a')
        self.vs[6]["Name"] = """HConstfolding_hier"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('05d1afc3-d508-4058-a16f-5ee3d7056e36')
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
        self.vs[7]["GUID__"] = UUID('b3210fc4-7dbf-48d4-9738-8376be0c4b71')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('980929f4-d418-4e3e-be20-4afa0da576fb')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('e177ed0d-aa5c-49a0-adf7-aa284fd4f799')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('e9061e5b-8720-46df-9dbf-c4c6adda2e0b')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('ae11390b-02a2-42d8-88f4-a0a565bda584')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('33d81c2f-3388-4f87-94d7-e824124dcf8e')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('4946f75c-053b-4c2e-b067-fd91f01fa281')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('bf4cddcf-eb58-4bbc-b208-eaa3520b9936')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('44efc213-5713-449a-9625-9996876f0ac3')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('7afdb2de-0303-4f86-bcb0-95719755dca5')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('744e7b27-c8a2-4976-a318-31a2f010815e')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('71e8efda-f540-42a6-aed6-1d040554562e')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('0c2622e8-22ad-4c80-9d6f-933f5a94dc7f')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Input"""
        self.vs[20]["GUID__"] = UUID('2f5b5030-08a9-4529-a542-5c303608e3f9')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('571c5eac-79e0-4a62-b4c4-f1d7a5428d09')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('3d0031a4-7d81-477b-a9d8-0b8040a04526')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('1dcb6601-cd37-42b8-be05-2ab3502e9ac4')
        self.vs[24]["Name"] = """2"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('379a5479-bf40-4b34-9048-cff77d5f1e1a')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('06ddef6d-2280-486d-b31b-0eadcfe051df')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('bc3b1059-0abc-4dab-9853-98037ed2ac24')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('b641cb07-4ecb-49fb-8e3e-098d4e885af1')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('048e1663-351c-432d-95f3-e08a181a9736')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('e6e4b63b-5d80-4511-a48d-300d2db92cc6')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('4c818312-22bf-4a38-8347-99c0eb971a1e')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('cd9edaf2-9c42-4300-a5ea-7d0d8c2c537b')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('51ebea14-8af4-47e0-962d-b4e9aa198c21')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('abe2ce4f-c82a-4af8-862c-3acdec002ead')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('a65ce373-a5b5-4afd-be18-de30b24df5b2')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('dd081dd1-26a9-4c3c-a728-2da92ec49d07')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('8e7f084c-4eb1-4644-a488-ea05f93f78ac')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('b2ef3643-144b-4e2f-86fb-9f3c9ccac08e')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('440dccf0-34c9-4220-bb41-d9b11222de24')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('23f42fb4-071e-4839-9ab8-65ab5f62bc47')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('5a4e5ae2-c9cd-4fbd-9561-1e05c4b485ee')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('0f6cd949-f77a-432b-9fa2-61faa7ab3517')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('80426169-fdea-4cf7-9246-4ff21580046f')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('19415c85-ed9e-47c5-8004-ce08368653fa')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('a59dec69-b910-4437-934e-c2d00fcdb650')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('ed60cdf5-4aef-4e2c-a5ce-ae1b37dcf111')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('91aa8b9e-aee7-42a1-8a38-e039905ffe66')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('86aad4fd-f857-42c2-b90c-7bdef2cd953b')

