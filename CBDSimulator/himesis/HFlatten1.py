

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten1, self).__init__(name='HFlatten1', num_nodes=81, edges=[])
        
        # Add the edges
        self.add_edges([(0, 57), (57, 33), (0, 58), (58, 34), (0, 23), (23, 13), (1, 59), (59, 35), (2, 60), (60, 36), (2, 61), (61, 37), (2, 24), (24, 14), (3, 25), (25, 15), (4, 26), (26, 16), (5, 62), (62, 38), (5, 63), (63, 39), (5, 27), (27, 17), (10, 28), (28, 18), (11, 29), (29, 19), (12, 30), (30, 20), (6, 64), (64, 40), (6, 65), (65, 41), (6, 31), (31, 21), (7, 66), (66, 42), (8, 67), (67, 43), (8, 68), (68, 44), (8, 32), (32, 22), (0, 45), (45, 4), (0, 46), (46, 10), (0, 47), (47, 12), (0, 48), (48, 6), (0, 49), (49, 7), (0, 50), (50, 8), (9, 51), (51, 0), (9, 52), (52, 1), (9, 53), (53, 2), (9, 54), (54, 3), (9, 55), (55, 5), (9, 56), (56, 11), (21, 69), (69, 44), (20, 70), (70, 43), (16, 71), (71, 41), (18, 72), (72, 40), (17, 73), (73, 35), (13, 74), (74, 38), (14, 75), (75, 34), (14, 76), (76, 39), (19, 77), (77, 37), (15, 78), (78, 33), (15, 79), (79, 36), (22, 80), (80, 42)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """Flatten1"""
        self["GUID__"] = UUID('00acc747-bbf1-41a7-b5b5-1167c1a824d5')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Subsystem"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F255
aF109
aF355
aF151
a.""")
        self.vs[0]["mm__"] = """SubSystem"""
        self.vs[0]["GUID__"] = UUID('ce698757-ce7f-4758-8938-01ca8f418474')
        self.vs[1]["Name"] = """Out1"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F470
aF123
aF500
aF137
a.""")
        self.vs[1]["mm__"] = """Outport"""
        self.vs[1]["Port"] = 1
        self.vs[1]["GUID__"] = UUID('695173d0-52ff-476e-b90b-76eb02ddd532')
        self.vs[2]["Name"] = """Product"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F155
aF147
aF185
aF178
a.""")
        self.vs[2]["mm__"] = """Product"""
        self.vs[2]["GUID__"] = UUID('693adb38-732a-4780-8df1-9657980c4456')
        self.vs[3]["Name"] = """Constant"""
        self.vs[3]["SampleTime"] = inf
        self.vs[3]["value"] = 12.34
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F25
aF102
aF70
aF138
a.""")
        self.vs[3]["mm__"] = """Constant"""
        self.vs[3]["GUID__"] = UUID('203c3ae9-eba7-46f2-b572-09a99b1d535f')
        self.vs[4]["Name"] = """Constant2"""
        self.vs[4]["SampleTime"] = inf
        self.vs[4]["value"] = 1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F110
aF170
aF140
aF200
a.""")
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('e93489a6-7a63-4a69-8c97-db421dd1e08d')
        self.vs[5]["Inputs"] = """|++"""
        self.vs[5]["Name"] = """Sum"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F410
aF120
aF430
aF140
a.""")
        self.vs[5]["mm__"] = """Sum"""
        self.vs[5]["IconShape"] = """round"""
        self.vs[5]["GUID__"] = UUID('9d59d3ce-f9f8-4376-8982-3f75f4af6fff')
        self.vs[6]["Name"] = """Product2"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F210
aF117
aF240
aF148
a.""")
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["GUID__"] = UUID('89a5c339-651f-4dc9-9223-5b69b00fc1ce')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F360
aF103
aF390
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('b58bdfb2-4f76-4ba2-8a76-9e642ae6f8bf')
        self.vs[8]["Inputs"] = """++|"""
        self.vs[8]["Name"] = """Sum2"""
        self.vs[8]["SampleTime"] = -1.0
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F275
aF125
aF295
aF145
a.""")
        self.vs[8]["mm__"] = """Sum"""
        self.vs[8]["IconShape"] = """round"""
        self.vs[8]["GUID__"] = UUID('94d0955f-d247-47a8-b85e-a5ca1b8460ca')
        self.vs[9]["Name"] = """Flatten1"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[9]["mm__"] = """SubSystem"""
        self.vs[9]["GUID__"] = UUID('282c8511-9546-4a43-97f3-3f09462e2eaf')
        self.vs[10]["Name"] = """In2"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F110
aF133
aF140
aF147
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 2
        self.vs[10]["GUID__"] = UUID('98e96627-91bc-4af6-b0b9-a4acc8f76158')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F15
aF183
aF45
aF197
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('96a11836-1683-42b9-b435-a91802cf6b52')
        self.vs[12]["Name"] = """In1"""
        self.vs[12]["BackgroundColor"] = """white"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F115
aF93
aF145
aF107
a.""")
        self.vs[12]["mm__"] = """Inport"""
        self.vs[12]["Port"] = 1
        self.vs[12]["GUID__"] = UUID('a4632cd6-d89a-497c-a57a-ff4ac34e6d08')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('8706fa76-9062-4cf2-9b74-b36b20078139')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('212bc684-8fad-41b5-b0df-8dae5c20997f')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('557fdada-aaeb-43b1-b099-4f424705720d')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('08ee0cde-c92e-4606-ac62-7822e20ab4e5')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('f770b6ef-9768-40ef-bfb3-20223e9cca83')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('5615c3bd-4bb2-49ff-b1e3-41edd05ac27b')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('d96467a2-a230-4756-aa00-6fc5052ce12b')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('8e420ada-176c-4c1e-a2b8-be8b28d6c08b')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('a85c5c69-a960-473b-9a08-9b84d932e6e6')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('7eefb117-db72-48b5-bdf1-58974514f0c3')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('b67ad771-7107-4821-9255-6a2a1b33f106')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('88d8959b-cc2b-4e98-9981-03bf0dd37fb4')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('b71c0eee-a4d3-48b8-b0ef-2bfadccafcf9')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('f629140b-e2e7-4e18-999e-01e1a526d26b')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('6b4d44e1-941c-4862-930a-6199ac1622d6')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('82103ca6-147a-4b3c-b905-599e57fa03e3')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('9ff4ab5f-107b-44a5-a1c9-86a5ba4a1b49')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('3a3999c7-150e-46cf-89c6-fc911fec52c8')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('eabe4fcc-fa74-4726-839a-2135c8d05885')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('ea7219ab-2ec4-474a-b52b-92278edcc0fb')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('f764bfd5-c30c-4854-9759-e125e8187455')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('f0bc4d72-b953-4583-8cfe-9c3d93890e6f')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('a38fd31e-cc21-42d6-82b3-6a9fdd268d88')
        self.vs[36]["Name"] = """1"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('fcadad23-1486-4ad8-8f46-9d2f69469d72')
        self.vs[37]["Name"] = """2"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('6fe6fdf3-4446-4ab2-a650-b9d6367d4a95')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('724654f4-89a5-4463-a9ee-0be6bbdf3764')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('0d809d55-0000-4275-b341-f63c287f531a')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('95a86125-8f58-40be-9d6b-f623b1a7b132')
        self.vs[41]["Name"] = """2"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('519db949-91e9-4f9f-a5f6-49e2d004e55c')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('ddb7c7f7-cf12-48f6-ac63-105e175dfc05')
        self.vs[43]["Name"] = """1"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('2071b635-0d03-4d93-ba15-5a012a108411')
        self.vs[44]["Name"] = """2"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('ca45c84d-0c9d-442f-9e26-8d4b72009821')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('95479889-373f-4226-9507-c0576df64d23')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('2d390adb-84c3-41cf-9dfd-0f4581476aa8')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('f7dae46b-af7b-4345-87ef-138ee91b0de0')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('078b0d1e-4a93-4ffc-a5b6-aa0c283d5714')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('cc6d562c-214d-4791-a2c4-351f118fbe62')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('23a80af2-58f1-406d-b039-b72940f6add9')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('7897498e-76e0-4547-acd8-9bb49cf8f777')
        self.vs[52]["Name"] = """None"""
        self.vs[52]["mm__"] = """__Contains__"""
        self.vs[52]["GUID__"] = UUID('b03929d6-5cf0-410d-9d45-b102a8a5a5ae')
        self.vs[53]["Name"] = """None"""
        self.vs[53]["mm__"] = """__Contains__"""
        self.vs[53]["GUID__"] = UUID('244a5089-d0a9-496f-b848-337359793961')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('be88c7bb-6050-4c17-8de6-fac27a405f02')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('d527e19c-a654-4d23-8370-d93f5262d9d6')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('30a29d15-40cf-4671-91ae-f22d8fbe63d7')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('e7fbf621-4d61-4791-ba03-88baa292c39f')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('25acf532-9314-4ca0-9bc9-e06591bdf18d')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('38fa2ef6-61e5-4e4e-b3b8-9030342a6143')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('3b13ceda-3e62-44d5-8b4d-7e4c416f73b1')
        self.vs[61]["mm__"] = """__Block_Inport__"""
        self.vs[61]["GUID__"] = UUID('86b7edc6-835c-4d2f-8d98-a7b6646922fd')
        self.vs[62]["mm__"] = """__Block_Inport__"""
        self.vs[62]["GUID__"] = UUID('10d0a7a0-107a-4958-b6cd-8958506e4e71')
        self.vs[63]["mm__"] = """__Block_Inport__"""
        self.vs[63]["GUID__"] = UUID('90aa5cf9-5b7d-460b-89b2-bada38ff5d02')
        self.vs[64]["mm__"] = """__Block_Inport__"""
        self.vs[64]["GUID__"] = UUID('56d9e560-826c-4101-8f7e-17ac0b78094b')
        self.vs[65]["mm__"] = """__Block_Inport__"""
        self.vs[65]["GUID__"] = UUID('e883deb2-52ee-4789-ae6b-04bad0b807a7')
        self.vs[66]["mm__"] = """__Block_Inport__"""
        self.vs[66]["GUID__"] = UUID('ea07b926-953a-49f0-8129-7dd68ed65575')
        self.vs[67]["mm__"] = """__Block_Inport__"""
        self.vs[67]["GUID__"] = UUID('a35dda38-c9bb-4a57-b328-685c1c5bdd27')
        self.vs[68]["mm__"] = """__Block_Inport__"""
        self.vs[68]["GUID__"] = UUID('680c9b32-0611-4750-a14e-1e3c6809879f')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('64b53da3-2048-400c-ad42-6f72017d30c8')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('0a599ca3-b422-40e4-bb8f-272d0902108a')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('48871f46-320c-4b6e-9215-0afb948548e2')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('0b1ac780-0bf4-4d54-a4e6-2fb76be6402b')
        self.vs[73]["mm__"] = """__Relation__"""
        self.vs[73]["GUID__"] = UUID('08d70e0c-fd92-450b-89c0-c0b9314ff761')
        self.vs[74]["mm__"] = """__Relation__"""
        self.vs[74]["GUID__"] = UUID('d894df06-b629-43fe-81a3-549702dc26da')
        self.vs[75]["mm__"] = """__Relation__"""
        self.vs[75]["GUID__"] = UUID('317b6e5a-8949-46f5-bc9d-e8713ec09128')
        self.vs[76]["mm__"] = """__Relation__"""
        self.vs[76]["GUID__"] = UUID('3cf59bdf-fa7c-4d0f-b276-e3413276af67')
        self.vs[77]["mm__"] = """__Relation__"""
        self.vs[77]["GUID__"] = UUID('5c4938ab-6a92-41c7-8c35-3a11d3b603ea')
        self.vs[78]["mm__"] = """__Relation__"""
        self.vs[78]["GUID__"] = UUID('54422e86-c80a-4ee0-9584-738aca16c381')
        self.vs[79]["mm__"] = """__Relation__"""
        self.vs[79]["GUID__"] = UUID('2ba2a92e-962a-4f8b-a217-4aace1491382')
        self.vs[80]["mm__"] = """__Relation__"""
        self.vs[80]["GUID__"] = UUID('9e10a46b-dcc0-4226-983d-0dbc3d207e1c')

