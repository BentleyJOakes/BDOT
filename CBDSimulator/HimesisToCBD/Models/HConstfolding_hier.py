

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
        self.add_edges([(5, 40), (40, 30), (5, 41), (41, 31), (5, 21), (21, 12), (6, 42), (42, 32), (0, 22), (22, 13), (1, 43), (43, 33), (1, 44), (44, 34), (1, 23), (23, 14), (2, 45), (45, 35), (2, 46), (46, 36), (2, 24), (24, 15), (3, 47), (47, 37), (3, 25), (25, 16), (9, 26), (26, 17), (10, 27), (27, 18), (11, 28), (28, 19), (4, 48), (48, 38), (4, 29), (29, 20), (7, 49), (49, 39), (5, 60), (60, 1), (5, 61), (61, 2), (5, 62), (62, 3), (5, 63), (63, 9), (5, 64), (64, 11), (5, 65), (65, 7), (8, 66), (66, 5), (8, 67), (67, 6), (8, 68), (68, 0), (8, 69), (69, 10), (8, 70), (70, 4), (15, 50), (50, 37), (14, 51), (51, 35), (17, 52), (52, 34), (16, 53), (53, 36), (16, 54), (54, 39), (19, 55), (55, 33), (18, 56), (56, 30), (12, 57), (57, 32), (20, 58), (58, 31), (13, 59), (59, 38)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """constfolding_hier"""
        self["GUID__"] = UUID('71bb47cc-d0bc-4c47-82c3-937c267a1a69')
        
        # Set the node attributes
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F125
aF125
aF155
aF155
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('5f5618bd-dd17-4843-9425-6170cc07d945')
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["GUID__"] = UUID('48836bbe-a96a-4e24-a40a-efbe77a92dbe')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F275
aF100
aF295
aF120
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('7da4da2a-8049-4908-9b93-3e592e0f6c14')
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F325
aF93
aF360
aF127
a.""")
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["GUID__"] = UUID('e8fb31f4-bd2d-4a76-ae1f-abaf94ce1221')
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F215
aF125
aF245
aF155
a.""")
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["gain"] = 0.01
        self.vs[4]["GUID__"] = UUID('00f8d333-080e-433e-bd80-48e15a815f0c')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F320
aF24
aF420
aF66
a.""")
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["GUID__"] = UUID('ecddd33a-1aa1-4f99-bbde-ecbfa9c9472a')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["Port"] = 1
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F485
aF38
aF515
aF52
a.""")
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["GUID__"] = UUID('5347b381-96cf-4bf1-9ba8-380082bdde10')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["Port"] = 1
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F425
aF103
aF455
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["GUID__"] = UUID('47c07116-dd80-4694-af9f-e0c55983de36')
        self.vs[8]["Name"] = """constfolding_hier"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('0c52314f-b3ba-498d-85f2-676923ecc4f5')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["Port"] = 2
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F90
aF153
aF120
aF167
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["GUID__"] = UUID('3633a521-85a6-4f34-a9e0-94f5aef124dc')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["Port"] = 1
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["GUID__"] = UUID('a6d985cb-75d7-47d4-929c-57367302c625')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["Port"] = 1
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["GUID__"] = UUID('d766e11e-0099-496a-80a8-80446895e345')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('c559f142-6b6e-46a6-a63e-31f9f944a907')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('effbdfb0-0002-41b6-bca3-0f044ccad9a9')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('3efedc74-01e9-4d50-8b12-29a5ebbca427')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('6cd1fdb3-f687-4ad0-b980-9282a306a874')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('20476f53-7f14-44d2-b520-3b1e8fe4273d')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('00d6dedd-63fa-4379-854f-db44749a27c1')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('9a27e48d-9fe8-4955-8618-c628ceb9c6ce')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('b37afebd-09c1-4f70-b2b4-fdec701cd161')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('e50b14b8-0ff8-4061-ba51-3993555535e8')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('072fe6de-f8c9-4466-a308-d6750683f8cd')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('646a3c6f-b1f2-4c86-a011-a603467c523b')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('e7949b13-65b5-40c8-b792-56cd1885e4cd')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('92be1b9d-2961-4426-852e-afb49843d3e4')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('cef4f949-74d6-4b4a-85a3-701b153cf8bb')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('3f329d14-6d41-4b52-9ce5-7e86fa9aba64')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('cf046eb7-9d81-4b39-b8ad-c6d987b0dff7')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('acd695bf-c0b3-4f4d-8b72-8df3c2158287')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('acfb6077-dc1b-4954-b982-8b4872ff6f69')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('0acb4c4c-b980-4a95-a705-79fe6d5c6e6d')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('3b036f61-c384-4451-b5eb-f8c9f3b99c14')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('8318988b-7a42-477f-9215-ad3b24c8103e')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('ac442dda-83db-41e0-99cc-8dce76546197')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('f06a3295-04f5-4691-ada1-9abf550db669')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('3fa24811-7a2a-4733-b8aa-7c86d5770549')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('aabcf693-739f-4227-b0bd-2d426f8bccac')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('977f3715-69f1-4dcb-8d39-6b3419bd464d')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('d8c73d18-9b55-47f2-8a8f-02052a49fdd5')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('8e2e37cc-8796-42b0-8e6a-c7721450fda6')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('819e0e07-b718-45ae-b958-a738ead0464e')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('1e9f2093-6f77-4efe-aff4-16ea58f74705')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('10f037d5-2247-421e-88b0-1e1e8b1b4154')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('53f50a4f-6387-4354-9abc-d4389fbba8ee')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('b2020f1b-fa17-490e-b977-5118ecbc4f16')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('bf47970c-82c9-4bcb-8d70-8fdbf891bf10')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('81ff95d7-d16f-48c7-bce3-cac7c09bc8b7')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('b09e6401-0782-473d-adc9-7dcf8fd66464')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('5a450ab6-faa1-4184-807d-2fcf40a254d3')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('35adec56-d614-4321-8d30-a760393ac10f')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('ddbc6390-289a-4bc7-bacc-ff614480e979')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('a7d084a9-0470-46c8-9acc-2400bd1411a2')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('2a3897b6-74c5-4430-9908-718900563676')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('62cd2f32-3ab9-441e-93c0-a8b933b1bff9')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('d345c562-9399-454a-882c-c468a024d3f8')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('450a4383-fdd6-4666-93d5-95cf1b5887c9')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('7eeb9fab-9927-4b31-8bf0-e484a145f814')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('8791011d-68c3-4b7c-9b5e-45cd31851bac')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('70f5c4bc-6992-48fa-b80e-8839d7860744')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('f419bd01-6c12-4dbc-b06c-3dd1253c2e87')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('38539459-730a-4f68-b946-0722979dec89')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('f0a90218-56b5-48b8-bd41-ea9cb6d8a59f')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('0cf9fe28-ff8f-40ee-9713-2d104fc15f31')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('5eba5bfc-0f2f-4dfb-a272-cf2b1b744f62')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('0f954952-09cc-48ad-a8c2-02380cab4b46')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('e73d7aad-ff79-406a-ad9c-ed9ec5b58782')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('4bc5683d-3d2c-461e-b6ea-ef14a2e454f9')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('161424ce-5ed7-48f5-afb7-fb96579e3171')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('7faf661d-312e-42b5-9247-dc73e1f59191')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('6a3192bd-1e1a-4322-bf68-433a3633cd5a')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('55a48084-cf9f-426b-b812-5dccb30c15d6')

