

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
        self["GUID__"] = UUID('3066fab0-6731-45c6-81da-65c4c14657cf')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F135
aF65
aF165
aF95
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('7244af71-c71a-4e24-a3e0-4532ea1c7b2f')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """yellow"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["GUID__"] = UUID('c21776d6-cbbc-482b-9efa-0e04a05ec1cd')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """yellow"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('b51ea25d-1962-4707-ab10-5236aa68f61f')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["GUID__"] = UUID('94c3fd7d-195a-4fe5-b993-5a95605c388f')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F200
aF64
aF240
aF96
a.""")
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["GUID__"] = UUID('e85a4647-bb82-4114-bb06-4dbb4f57f16e')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """yellow"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["GUID__"] = UUID('b14fd98e-8261-4d94-be2e-4ccf1e238185')
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
        self.vs[6]["GUID__"] = UUID('affd5bbb-8286-4ebb-88de-25ba623e0395')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F365
aF103
aF395
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('3a23d656-b659-43d2-8d75-fe771e878d46')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('eafcf900-1eb0-4794-870d-f70559c3fc2b')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """yellow"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F150
aF118
aF180
aF132
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('36d0cf03-343e-476c-b6cf-0703d15d69c3')
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
        self.vs[10]["GUID__"] = UUID('e25695e6-3300-4024-9f60-4ed9d0956cb8')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """yellow"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F150
aF88
aF180
aF102
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('befd486b-bf78-466e-86fd-5acaeeff5ec5')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('939caeff-d98a-4a4a-be38-e668fccf246c')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('b292bdf0-4e49-49d5-8100-f495fc70d7e5')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('f9ff3977-9244-4768-901c-4b2ddca46aa3')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('b2338faf-0ce2-4857-8096-44c52c9db182')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('7f7c25a4-0151-4673-ac8c-1c969888f27b')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('5fa367be-fe64-436a-94e9-55e3b199b034')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('fed120c7-07af-40f9-b349-b6ca23e71247')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('36d1439e-fc67-4516-99fe-87839c79b58c')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('9447b164-e1aa-483d-9e57-d7f9ba0f4010')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('784f9c15-6c7c-48be-96ba-0c3c708e0f2c')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('aeb336c4-7830-4e72-b324-46d3eb4ef0b4')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('9f282c1d-dfc5-4a11-87e4-12609f2b0695')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('7415e737-a63e-4827-af97-4c5badbb610e')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('8f46f229-259d-43b2-a096-853cf469f199')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('1553ed9c-023a-4129-aefa-0b42c578d30b')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('7e068f32-e1ad-4da6-bc2d-157fa8eeb0eb')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('b6594c31-cb33-46fa-b03e-8db6a957f815')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('6cd5c0d1-2bcd-4de2-beef-d5385dfa6725')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('cdac358b-b80d-4c24-a835-5b171714e116')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('2c501cb2-0d7c-4c7c-95d4-4751af782e08')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('4875326c-5e06-42fa-8caa-4abe6fecc802')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('bcd750a0-2bfe-4d98-84c5-1dcb0e2b9bf8')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('8e767711-fb14-4224-9adc-d12d47dc515c')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('32b495cf-c406-4bbb-9757-6c19ada14d1b')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('d38b91e8-8511-449e-9a35-346dcedc9b5d')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('3d1d30f6-3326-4dc9-ad30-412cd078181c')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('ad90f5c5-e3b8-470a-aac9-821ef5039a98')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('a6aa486d-8e55-47c0-b29a-4aaa7b9fb8b2')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('419d9e52-da2d-4e6d-a4ea-f48e7f0596d2')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('7c73ed73-a97b-4e33-8c98-16626ac426cc')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('e70c863c-53a7-4ccb-b8b6-31e7c287cdbf')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('7e453cf9-0530-4485-98d1-36ff2119fe72')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('f99bf829-4bb1-4871-b624-d6e0ec3e41e3')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('2eed0514-a830-41c0-bff4-3d071e0dbb67')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('f3a6c46d-3b75-477a-bf01-f3e27de852b6')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('e800d0a0-25d3-44c6-8e9c-934f34afc66d')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('6198a84f-3a2a-46dc-a027-206fd88bdaaa')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('a6f4c1a6-8c14-41a2-8ec5-68bb032c4e7f')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('55d3af58-a7d3-4637-860b-f1f2c35f9f54')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('d6ad3d35-ffbf-4b74-a22a-b3f3f842f4c4')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('30ecf3d0-b1ec-4532-8b0b-54c6b561f709')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('5ba78055-3f0f-4a57-88e0-de77ba02fcda')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('e0a75289-35fc-4cc4-b941-deece2d61152')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('7a05f3cc-0bca-4ee9-87cb-2d619561085a')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('7bd763ea-8c00-4a2e-8d7a-73de30b652ea')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('6f78e894-6e6f-48a3-8405-837c094a0ed9')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('ad38159d-b864-4d5c-b85f-464ed96e6822')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('e8c3fc9d-5604-442b-9728-08f764f481ec')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('8e9b93a3-4dee-4760-b315-20229e404465')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('8cf8260d-83d3-4128-b3f5-65c64a2cf58e')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('9653c80e-5a50-494b-b801-2000325aaee8')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('b39590e2-7d24-4aeb-b61b-6633f769614a')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('f7aa102a-91cb-4d99-9d0a-a50610bf6928')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('c83ca4cb-e2ce-4d85-b423-3ccb6fdbf451')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('86fda245-5240-48a1-ad7b-f92afb5c0df4')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('8200c299-675f-4ebc-92c1-4e7efaa11b5b')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('c6ebd6b6-0b9c-4e6d-9817-d2a9b2a13673')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('a511ec51-64c4-4d86-b52c-c4d9cf78c5ba')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('7ba9fc99-7465-472c-b321-8689fedb348d')

