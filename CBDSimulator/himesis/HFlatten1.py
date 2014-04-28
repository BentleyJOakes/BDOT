

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
        self["GUID__"] = UUID('9e1ac534-9239-406e-bfc9-fc9707d3df21')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Subsystem"""
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F255
aF109
aF355
aF151
a.""")
        self.vs[0]["mm__"] = """SubSystem"""
        self.vs[0]["GUID__"] = UUID('a9c13458-c539-48ae-b3b8-6ca73cb58998')
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
        self.vs[1]["GUID__"] = UUID('3e08eb6f-a245-44f4-9177-524c2938c579')
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
        self.vs[2]["GUID__"] = UUID('71221460-c79d-48ea-8619-b8b69fca3129')
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
        self.vs[3]["GUID__"] = UUID('d89a872a-c15c-4ee2-946f-7ee637f9122e')
        self.vs[4]["Name"] = """Constant2"""
        self.vs[4]["SampleTime"] = inf
        self.vs[4]["value"] = 1.0
        self.vs[4]["BackgroundColor"] = """yellow"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F110
aF170
aF140
aF200
a.""")
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('c9af92f6-7c01-4de4-84bf-9f9e936f86b6')
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
        self.vs[5]["GUID__"] = UUID('6a4b6ebe-76ec-4c54-a32a-c9ec55b59ec6')
        self.vs[6]["Name"] = """Product2"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """yellow"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F210
aF117
aF240
aF148
a.""")
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["GUID__"] = UUID('4c8c6349-fefe-488a-b18f-60cbf79b0a47')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F360
aF103
aF390
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('bb2fb20c-727b-450f-9e75-04b22ecf425d')
        self.vs[8]["Inputs"] = """++|"""
        self.vs[8]["Name"] = """Sum2"""
        self.vs[8]["SampleTime"] = -1.0
        self.vs[8]["BackgroundColor"] = """yellow"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F275
aF125
aF295
aF145
a.""")
        self.vs[8]["mm__"] = """Sum"""
        self.vs[8]["IconShape"] = """round"""
        self.vs[8]["GUID__"] = UUID('4a046695-1b82-48b7-bb74-43f7e5ee6949')
        self.vs[9]["Name"] = """Flatten1"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[9]["mm__"] = """SubSystem"""
        self.vs[9]["GUID__"] = UUID('a221bf90-be8d-41b3-8147-7a1367a44b99')
        self.vs[10]["Name"] = """In2"""
        self.vs[10]["BackgroundColor"] = """yellow"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F110
aF133
aF140
aF147
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 2
        self.vs[10]["GUID__"] = UUID('36a226ba-7551-4779-9304-02213540203c')
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
        self.vs[11]["GUID__"] = UUID('a44a6adb-55fb-4dd2-aa4f-23dfa918a5da')
        self.vs[12]["Name"] = """In1"""
        self.vs[12]["BackgroundColor"] = """yellow"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F115
aF93
aF145
aF107
a.""")
        self.vs[12]["mm__"] = """Inport"""
        self.vs[12]["Port"] = 1
        self.vs[12]["GUID__"] = UUID('395fe524-b8a0-4180-9a1c-f2976730500f')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('02f46b8c-702e-44d4-a6e9-e8f411884308')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('d7115cfe-b805-44c6-bc5e-9a3ef36cb93f')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('4caa0a95-c888-460c-a09d-57d76659daf5')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('893d2395-cd8d-4c7c-9d72-6a4dffa80f65')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('1b8557a8-b4d4-447b-9c61-55416638b0d6')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('40bbbf33-a650-42a7-afaa-2a23c490568c')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('8cda0dcb-77dd-4c8a-a4c8-75ffbe9793e5')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('7bdb7d7e-6ed7-4aab-b723-1bef56adbda9')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('e9f63425-f219-49bb-8585-6b27c56b8197')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('9b643d1a-2d4c-4db6-9217-56f972371e6b')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('85736a5f-6e9c-4485-a30a-231a86a8d790')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('597a0ec2-be05-4266-b353-867c0f194c7c')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('f7c34254-9f0e-4e1e-8914-1df9b7b464e6')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('5f07aba5-7ecf-4d8f-8a2f-5e7fffc287e9')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('806fcf11-9132-42de-a1ce-035f4156ce45')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('bb35a302-1125-421a-a454-ae3b2da80001')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('a7bfe501-d82b-4624-a43e-b227e7be373e')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('7885ad78-1df1-433e-a339-24f4f6826036')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('8888dec0-aafa-4ff1-85e7-6b51d130abd1')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('ecc2f85b-d924-4216-abaf-f38d9a4f50d8')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('d518c9bd-728c-407f-92d5-0f23947316dd')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('5c9f1b65-075d-46ec-84b8-5cafd445895f')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('cebfb33c-5d17-4c08-981c-0244b6dc786e')
        self.vs[36]["Name"] = """1"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('c3b4aea6-25f3-403a-b471-4d0749924bdf')
        self.vs[37]["Name"] = """2"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('44d0ef1d-345f-46a7-924c-43316e63e9b5')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('ea4a8b9b-da18-45f8-8815-e65a06558959')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('01dc9698-797f-40e3-85d1-8d5e0da6750d')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('68285d20-441c-400c-8856-eda417abb9aa')
        self.vs[41]["Name"] = """2"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('b2db850b-f5df-48e7-b77a-2266baab77b8')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('26e28c27-ea8e-49d5-afff-2d8dc5cdb965')
        self.vs[43]["Name"] = """1"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('265d54fe-b578-4331-93c4-9132a7cc191c')
        self.vs[44]["Name"] = """2"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('9b8a74e9-7ce2-4f1f-97c4-7fa4db08d869')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('f9293c5d-aae7-4b59-8f63-cd13931e7602')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('b12e4a25-b0a7-4681-b83f-b75ac21e7402')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('c6f2a368-00f8-4349-bac1-ca1b65f758ee')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('85b6e406-a503-40bf-bc32-6bbdc8f36128')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('ceae96b9-6433-4604-aced-7739af9ec97f')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('ece2fe4f-fc48-4f1c-9ee9-cfdbf7fc78e2')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('0b6807b0-be16-4f1d-83b4-02c171e9976a')
        self.vs[52]["Name"] = """None"""
        self.vs[52]["mm__"] = """__Contains__"""
        self.vs[52]["GUID__"] = UUID('ddde6eb4-9ea0-4b85-a20b-549d372ea6d3')
        self.vs[53]["Name"] = """None"""
        self.vs[53]["mm__"] = """__Contains__"""
        self.vs[53]["GUID__"] = UUID('c52a0d86-3037-45ce-a7c6-fb778029b4a1')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('2f206ae2-3a7f-474d-831d-9c9bb7f24825')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('744b39f6-6130-4969-8e38-f262a9e75bd7')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('2b75ba93-8a4c-4eab-8aec-0341e8415ad9')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('b5c6e60b-1257-45d3-ada2-2b7c73030b45')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('d9e2e907-3d4f-4592-822c-1be49f28ebed')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('8a8e4d3d-e8b9-46b3-92e2-52eb3f847622')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('3a5d7a38-45e1-43ac-8717-48973a0fdb91')
        self.vs[61]["mm__"] = """__Block_Inport__"""
        self.vs[61]["GUID__"] = UUID('855d4382-e412-4655-a53c-5a73b3de4c8a')
        self.vs[62]["mm__"] = """__Block_Inport__"""
        self.vs[62]["GUID__"] = UUID('5693adf1-df83-42a5-bfef-869d55cb670e')
        self.vs[63]["mm__"] = """__Block_Inport__"""
        self.vs[63]["GUID__"] = UUID('9d2446d4-82df-43bf-b395-2c62863df40b')
        self.vs[64]["mm__"] = """__Block_Inport__"""
        self.vs[64]["GUID__"] = UUID('05cd63be-4a43-430b-b08f-ccce656c96bf')
        self.vs[65]["mm__"] = """__Block_Inport__"""
        self.vs[65]["GUID__"] = UUID('80fb71f1-ac07-4147-ad5b-37472754b4f8')
        self.vs[66]["mm__"] = """__Block_Inport__"""
        self.vs[66]["GUID__"] = UUID('50e3caa2-6cd2-41c0-bac7-142bc9654bfa')
        self.vs[67]["mm__"] = """__Block_Inport__"""
        self.vs[67]["GUID__"] = UUID('3387f3da-e3af-4e2a-bf4b-e158a87de002')
        self.vs[68]["mm__"] = """__Block_Inport__"""
        self.vs[68]["GUID__"] = UUID('2ec588f3-2a80-411b-b24a-8e2159a4846c')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('2c461866-278f-4f12-95b3-158cc035ab9f')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('fc70b2fe-9509-4f65-8462-955647c46e80')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('e42419e2-6c8d-4e86-b7a0-eeef9afed640')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('74e07906-ed88-42ae-b08f-ce275bbbca85')
        self.vs[73]["mm__"] = """__Relation__"""
        self.vs[73]["GUID__"] = UUID('4ba771fa-54c6-49d6-ae90-39d1398ff633')
        self.vs[74]["mm__"] = """__Relation__"""
        self.vs[74]["GUID__"] = UUID('25c4f084-500f-4da7-b7b9-6b609457e642')
        self.vs[75]["mm__"] = """__Relation__"""
        self.vs[75]["GUID__"] = UUID('1ac166bd-eb95-47c2-915e-4eea53bd8424')
        self.vs[76]["mm__"] = """__Relation__"""
        self.vs[76]["GUID__"] = UUID('97307730-9a65-48af-a32d-2ef87c385791')
        self.vs[77]["mm__"] = """__Relation__"""
        self.vs[77]["GUID__"] = UUID('2e4e5603-8c7e-4f38-a306-6b9f23098099')
        self.vs[78]["mm__"] = """__Relation__"""
        self.vs[78]["GUID__"] = UUID('2faaa73e-af35-49af-a78a-80de331aeac0')
        self.vs[79]["mm__"] = """__Relation__"""
        self.vs[79]["GUID__"] = UUID('e762b75c-c362-4400-884d-17463ad413c0')
        self.vs[80]["mm__"] = """__Relation__"""
        self.vs[80]["GUID__"] = UUID('8f6b006c-9658-49d0-92c9-3cbbe76f94f0')

