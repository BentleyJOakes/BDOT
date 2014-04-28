

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
        self["GUID__"] = UUID('49dca08a-80d0-4267-be6b-fbb6b8ec2e44')
        
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
        self.vs[0]["GUID__"] = UUID('7244fd0b-d9eb-4297-bb73-5cd6ebf1c425')
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
        self.vs[1]["GUID__"] = UUID('37827ea8-c07b-4f48-aad2-70106ea1dd0f')
        self.vs[2]["Name"] = """Gain"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["gain"] = 5.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Gain"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F235
aF195
aF265
aF225
a.""")
        self.vs[2]["GUID__"] = UUID('c3e2c5e3-8cb5-49d7-8ed8-3662b2188599')
        self.vs[3]["Name"] = """Const2"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('faf464fb-6c98-49e7-a276-95eb58ba75de')
        self.vs[4]["Name"] = """Product"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Product"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F285
aF157
aF315
aF188
a.""")
        self.vs[4]["GUID__"] = UUID('146ee919-5e14-4aae-8a04-54c3ea110f2e')
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
        self.vs[5]["GUID__"] = UUID('780695ae-542f-49bb-8411-bca91b61f1fc')
        self.vs[6]["Name"] = """Constant"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 12.34
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F140
aF197
aF185
aF233
a.""")
        self.vs[6]["GUID__"] = UUID('1094ee46-9e29-4695-8280-64db0bebe79d')
        self.vs[7]["Name"] = """Constant1"""
        self.vs[7]["SampleTime"] = inf
        self.vs[7]["value"] = 7.12
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F145
aF150
aF175
aF180
a.""")
        self.vs[7]["GUID__"] = UUID('8c175cf7-f701-4ef6-b2f3-9c321261c029')
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
        self.vs[8]["GUID__"] = UUID('b23b7ae4-eabd-4119-b65f-e58948b10201')
        self.vs[9]["Name"] = """Constant2"""
        self.vs[9]["SampleTime"] = inf
        self.vs[9]["value"] = 2.0
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F120
aF35
aF150
aF65
a.""")
        self.vs[9]["GUID__"] = UUID('9f244539-14e1-47a1-b5bd-feffc31cd7bc')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('d4d34335-bea2-428e-bc0d-0b27627d5714')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('35ccbe3d-937b-4eba-8716-ab71d2c296af')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('5d3aa7d2-81c3-4bbd-b157-dce38d128e05')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('ddf0abd4-e9b5-4766-9122-7dfc567d7eb3')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('fae2ab12-903c-4811-9497-ba6d835cdbf9')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('e485c265-0bdc-4014-94c2-49e758f0fa5e')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('9f50ff41-08ea-46f1-a491-91708f40a0ed')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('79a5111d-adf7-4304-a2a5-185739ef89d6')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('b12697f0-ab57-4169-b164-fdf66cad2330')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('173a1598-6fbe-4730-b73c-881776ea3305')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('c46861c1-da1b-41a2-a091-db31967ac7d2')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('ddc4bf97-68e2-4ed4-b821-d89543765b2f')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('023b2e26-cce4-4cfe-80bc-cbe14b8f3f00')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('3c7a34a7-41b5-4861-be92-ed1cb3310a2a')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('f1bd5ab2-c82d-4666-b238-aff6eed18984')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('86746bee-0306-4839-9718-4ed3820b2849')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('9e44652f-ce21-4322-a3b3-1f4449725013')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Input"""
        self.vs[27]["GUID__"] = UUID('33934666-1a13-449e-91d5-379cf53bcc11')
        self.vs[28]["Name"] = """2"""
        self.vs[28]["mm__"] = """Port_Input"""
        self.vs[28]["GUID__"] = UUID('ea471065-0fc8-45c7-83cd-45394ad54ba0')
        self.vs[29]["Name"] = """1"""
        self.vs[29]["mm__"] = """Port_Input"""
        self.vs[29]["GUID__"] = UUID('79d8a87c-fe02-466f-bae5-b273b3c5e280')
        self.vs[30]["Name"] = """2"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('e4f3c4ee-a33c-4e4d-97d3-4d4398f128af')
        self.vs[31]["Name"] = """3"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('77eb86fa-07a0-4f23-90dc-2b2ec0d349d3')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('9f2a964d-7cf9-4f34-a00b-9c4cc60453ef')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('f31943dc-75f3-43f0-87f0-b52608a5e335')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('ac4c99cc-b202-40b6-983a-c1bc515a6e8a')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('4d9cac3d-d159-43b7-a1cc-5aa72b360594')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('b375dcf0-0189-4326-ad1c-8453ea1e0bd7')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('a65af782-84fc-4f88-bf0c-4e2d3f25aa82')
        self.vs[38]["Name"] = """None"""
        self.vs[38]["mm__"] = """__Contains__"""
        self.vs[38]["GUID__"] = UUID('344b61aa-d431-488a-8ac0-df3ac3d58f6b')
        self.vs[39]["Name"] = """None"""
        self.vs[39]["mm__"] = """__Contains__"""
        self.vs[39]["GUID__"] = UUID('40ff0c5a-f0a6-4b0d-a6c2-59789a9495c7')
        self.vs[40]["Name"] = """None"""
        self.vs[40]["mm__"] = """__Contains__"""
        self.vs[40]["GUID__"] = UUID('99150675-e086-4320-aefb-c0c75a7cd59a')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('d8a08ded-8978-4ec2-9a00-60594236b193')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('7c9e9649-d49a-4f40-9d6d-b6b0033f3b1c')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('1968feb5-8962-47d1-9d6c-4efb9934a667')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('ab6493da-3036-4dbc-956e-c41760c3baa1')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('a40a146b-3534-4e92-8455-80ac27442333')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('c6609f8c-b4ca-49aa-97b4-d7534d6ea762')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('3d5a4897-b3b6-4c4a-9af0-337a416925a5')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('f2fb3e07-8e02-4e88-bfc2-ab958737ace4')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('adf9cc1d-8463-4180-8ad4-e0c2b78f6354')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('6aaa778f-4bd1-4028-a035-19bff2fcd606')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('dca837f8-d27e-41b3-839d-b0305cdcb8a7')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('2d90835e-9845-463e-8dfc-67174dea800c')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('fcf5e69c-6c9a-4e6d-b603-eff247fb74af')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('49a0fe0b-d9e0-42c7-99c3-5759ca26803d')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('ffe2071b-9d3a-46fb-9ef9-297775851a79')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('dca765d1-6b15-4e11-9de5-96753e705e07')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('0983edd8-50ad-4859-a359-e12d67f83042')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('a5a19c9d-9bc5-4f0d-81b3-9cde23623fcb')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('63d6f895-2192-4a2c-80ba-236ed8a95c8d')
        self.vs[60]["mm__"] = """__Relation__"""
        self.vs[60]["GUID__"] = UUID('349b9791-aee9-4648-9f7a-0a55c32963de')
        self.vs[61]["mm__"] = """__Relation__"""
        self.vs[61]["GUID__"] = UUID('bd732f04-a49a-4ca6-814f-60af2d31e520')

