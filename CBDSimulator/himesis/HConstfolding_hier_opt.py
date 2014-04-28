

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
        self["GUID__"] = UUID('2a2b8bde-e9d3-404c-9509-01b1c8e1815d')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F135
aF65
aF165
aF95
a.""")
        self.vs[0]["GUID__"] = UUID('d2f035b8-c4b4-45fe-a2b6-6bd101f29eaa')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """yellow"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F205
aF92
aF235
aF123
a.""")
        self.vs[1]["GUID__"] = UUID('d627c649-2da0-4d68-8a9c-b89339ecdecd')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """yellow"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F250
aF100
aF270
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('73349b13-49fd-45ac-a0dd-4ba3a94e413a')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('5674568b-b8e9-4272-8ce7-50ce46b1aac7')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F200
aF64
aF240
aF96
a.""")
        self.vs[4]["GUID__"] = UUID('1cb1ecb9-c16a-42fa-9d7a-8eceb62ec026')
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
        self.vs[5]["GUID__"] = UUID('a71519b8-9bbe-4e7f-9b0d-33fb3695e709')
        self.vs[6]["Name"] = """HConstfolding_hier"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('2f098911-ff91-4dc7-a860-48dabd2c343f')
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
        self.vs[7]["GUID__"] = UUID('f807c5d1-9580-4a4b-b7d8-4bc9e40157f6')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('a3a5b2c8-8cc8-4c40-80e7-752918977ce0')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('7dffcd1d-1427-4224-980a-8a076c1226f2')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('05dea981-dd19-4935-bbbf-6e7a98ba89af')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('9bcdb949-409d-4018-b17c-8326bbfded4f')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('1c24fa59-3f4a-495b-8fb1-be621c98f3ec')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('6c6d8579-b20d-47d9-b9e3-bae4e7b06155')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('b97d3be4-d259-4b2b-ae90-580cacbf1725')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('445b6654-12f6-411a-8980-0fda2726bed8')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('07fc2fbf-9774-49d9-95e0-3f039b409d89')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('87736388-2ab8-4af2-917e-343b8d0b3b16')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('173b7bae-75c0-4b14-abd0-bec247816bc9')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('1cfb35d5-4f1e-4981-8ac0-30c7c931165e')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Input"""
        self.vs[20]["GUID__"] = UUID('f410d4c9-9da2-44b3-836a-f547a3f5ec61')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('3d3e9960-cac2-44b9-a391-e82749f34b6e')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('3fc86134-1fe5-4e70-abf7-5c34818e7dca')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('a40df953-09e5-4def-a90b-727c06ac19c8')
        self.vs[24]["Name"] = """2"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('22e2c231-6b5a-41c1-8952-ad0f01abede6')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('93951e97-3bbb-4f13-9199-0acc1592da07')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('c60131d8-8cc1-4bd5-bd72-0a6ba6f24a08')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('5c290635-0010-4702-8970-0e1b409e35d7')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('4519bfa4-0df9-4a33-a26d-a626fc66d16c')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('5511387b-e887-4589-8149-6be0a672c01e')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('b3f6901d-16c7-4261-8d02-86e4a524cd4f')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('548af553-d28d-4b29-8a73-15373a679415')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('a8f1cc9a-11d1-4b53-8156-8f9a4e6f4de3')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('22fb7886-2cc2-46d9-82e1-c0d50f86594e')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('b76f09df-4ba4-4a97-9f57-88649d461d5b')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('ceb88f06-97a5-4cd4-965a-e13bdc54a658')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('a13e175c-b046-47b3-b89e-85307285481f')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('e68bfe39-839c-409f-8177-e7e2901c3944')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('02c6e2fc-34c5-4912-8645-fa857250e6ce')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('cff82ea6-ba81-4083-9ec5-e61ddeb1e373')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('fbc1820e-d924-441a-a8ff-dc6e9796855f')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('3e04e783-05e9-4cbf-93a1-a694da2249c8')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('c7a22b62-225f-4785-9973-a778e66a555a')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('f735f095-c8a1-4aad-adb0-d1a870bd38d5')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('74c9432b-d2a1-4a89-a81a-937872daf088')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('c8674edd-7560-4482-a0d5-1f3e40d30549')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('ea04530f-9ead-45ee-9b4c-f3352a9586bf')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('c77a43db-f04c-496d-ad27-eaf690a048e6')

