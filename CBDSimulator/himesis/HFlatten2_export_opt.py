

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten2_export_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten2_export_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten2_export_opt, self).__init__(name='HFlatten2_export_opt', num_nodes=64, edges=[])
        
        # Add the edges
        self.add_edges([(0, 19), (2, 25), (6, 22), (7, 23), (4, 61), (4, 62), (4, 63), (4, 60), (4, 59), (4, 58), (4, 57), (4, 56), (4, 55), (4, 54), (8, 20), (5, 21), (9, 24), (10, 26), (11, 50), (11, 49), (12, 47), (13, 51), (14, 46), (15, 48), (16, 53), (17, 45), (18, 52), (19, 11), (20, 12), (21, 13), (22, 14), (23, 15), (24, 16), (25, 17), (26, 18), (36, 27), (37, 28), (38, 29), (39, 30), (40, 31), (41, 32), (42, 33), (43, 34), (44, 35), (3, 36), (0, 37), (6, 38), (6, 39), (7, 40), (7, 41), (1, 42), (2, 43), (2, 44), (45, 28), (46, 35), (47, 34), (48, 30), (49, 27), (50, 33), (51, 31), (52, 29), (53, 32), (54, 3), (55, 0), (56, 5), (57, 7), (58, 1), (59, 9), (60, 10), (61, 8), (62, 6), (63, 2)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlatten2_export_opt"""
        self["GUID__"] = UUID('ac5a3a93-b4ed-44c4-89fd-2b85b79b1823')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Gain2"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["gain"] = 5.4
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["mm__"] = """Gain"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F410
aF139
aF450
aF171
a.""")
        self.vs[0]["GUID__"] = UUID('4c0715cc-e773-4be7-84d9-be5f2c4461e4')
        self.vs[1]["NumInputPorts"] = """1"""
        self.vs[1]["Name"] = """Scope"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Scope"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F535
aF204
aF565
aF236
a.""")
        self.vs[1]["LimitDataPoints"] = """on"""
        self.vs[1]["GUID__"] = UUID('3538c22f-9305-49d7-b3bc-42d8294cf0cc')
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """lightBlue"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F280
aF90
aF300
aF110
a.""")
        self.vs[2]["GUID__"] = UUID('7634d98c-276e-4f11-a72d-5c8751aec08b')
        self.vs[3]["Name"] = """Out1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Outport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F535
aF148
aF565
aF162
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('aba94929-e0f4-455b-946c-a26cedc99fc6')
        self.vs[4]["Name"] = """Flatten2_export"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('776d584e-6905-46d3-a1ab-b19d7ba621d4')
        self.vs[5]["Name"] = """In1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Inport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F40
aF48
aF70
aF62
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('01660031-da3f-42b0-b668-2217277ab599')
        self.vs[6]["Name"] = """Product3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """lightBlue"""
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F225
aF127
aF255
aF158
a.""")
        self.vs[6]["GUID__"] = UUID('dba2271d-a1fb-458b-94a6-e54e3707c53f')
        self.vs[7]["Name"] = """Product2"""
        self.vs[7]["SampleTime"] = -1.0
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["mm__"] = """Product"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F185
aF177
aF215
aF208
a.""")
        self.vs[7]["GUID__"] = UUID('47b8270d-3cd6-4a82-821b-3af2cec40a72')
        self.vs[8]["Name"] = """Constant"""
        self.vs[8]["SampleTime"] = """inf"""
        self.vs[8]["value"] = 66598.0
        self.vs[8]["BackgroundColor"] = """lightBlue"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F205
aF69
aF250
aF101
a.""")
        self.vs[8]["GUID__"] = UUID('495a1895-ebd4-43c8-a619-528a1c40a83f')
        self.vs[9]["Name"] = """Constant"""
        self.vs[9]["SampleTime"] = """inf"""
        self.vs[9]["value"] = 134.67
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F30
aF127
aF80
aF163
a.""")
        self.vs[9]["GUID__"] = UUID('2536dc54-2346-4bea-966b-f48b9e854913')
        self.vs[10]["Name"] = """Constant2"""
        self.vs[10]["SampleTime"] = """inf"""
        self.vs[10]["value"] = 12.34
        self.vs[10]["BackgroundColor"] = """yellow"""
        self.vs[10]["mm__"] = """Constant"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F175
aF120
aF220
aF150
a.""")
        self.vs[10]["GUID__"] = UUID('d132b3b5-6aab-4a8b-b8dd-3492f78630e4')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('c9bf2af8-b63a-4706-9f8a-0c0694d175b7')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('b983a937-838d-4a23-b22b-1124bbdbf413')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('3bb50e31-ea9e-4e45-bc33-db2e0f3f7bc2')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('04f2860b-aee2-4a53-8b77-651e017b5c77')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('1765f7a5-46ef-43e7-9225-4d4f88694da8')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('3dee408e-bb15-4114-8ac3-20859c537ec5')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('073dbfe1-eefc-43ad-8d72-d3a1be02e24a')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('f4096004-d70c-45f4-a596-90c6fd9c8c77')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('9665b01c-7757-4ea8-9810-903f95c68054')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('55433f12-9b78-4bcb-a0c9-e630f0e41d3b')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('4f6621be-932b-43d7-8f0f-7c91b6c9ed92')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('bd150cc5-57d9-42f3-952d-579d6101c7f8')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('16b8b77a-3d54-4a35-8c8a-d5ba9dc92033')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('99a2a92c-363c-441e-8f6b-6179f213f38c')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('cec03414-4940-4a30-b917-340d2bd794e6')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('7af2e228-91bd-4387-a2ec-cb1fdf8d0151')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Input"""
        self.vs[27]["GUID__"] = UUID('bc536b6b-3deb-4d2a-b495-9ef786b00eff')
        self.vs[28]["Name"] = """1"""
        self.vs[28]["mm__"] = """Port_Input"""
        self.vs[28]["GUID__"] = UUID('c353d845-c743-4430-a618-05ab217deb2e')
        self.vs[29]["Name"] = """1"""
        self.vs[29]["mm__"] = """Port_Input"""
        self.vs[29]["GUID__"] = UUID('601ffc05-32de-4d9e-b2a9-d023248e962b')
        self.vs[30]["Name"] = """2"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('b81f2308-dff7-4d2c-a853-52a4d6fe6338')
        self.vs[31]["Name"] = """1"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('efd46104-4532-49fc-828f-2af0d8061563')
        self.vs[32]["Name"] = """2"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('5e628eaf-5c4d-4998-a204-74492a7c4aec')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('a6edfe95-c07b-4f89-9a8e-cb029340a330')
        self.vs[34]["Name"] = """1"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('142ff41b-26cc-4ebb-86ce-552e77589562')
        self.vs[35]["Name"] = """2"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('b041c593-36b8-42b3-8bea-865af6a4bf93')
        self.vs[36]["mm__"] = """__Block_Inport__"""
        self.vs[36]["GUID__"] = UUID('6270b298-36fe-4880-9e74-679d6d9b80e4')
        self.vs[37]["mm__"] = """__Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('2a831dc2-80cc-4db4-86ac-2e47688ca806')
        self.vs[38]["mm__"] = """__Block_Inport__"""
        self.vs[38]["GUID__"] = UUID('bd3d3dfd-cd1b-47c3-b0b6-a80a7cd08125')
        self.vs[39]["mm__"] = """__Block_Inport__"""
        self.vs[39]["GUID__"] = UUID('f770f751-a540-4f2f-8db9-5dc6408f52b7')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('7c13e3b2-1dde-4f50-86da-fb2fa4ba9542')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('5951d449-a1ad-4c6b-9b8f-e31113cc22bc')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('4258bcbe-560d-4233-8a13-1a98275a687d')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('723a46ef-e6e5-4922-82d5-50433434f625')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('9421f164-8222-48ea-aed6-0d014f199119')
        self.vs[45]["mm__"] = """__Relation__"""
        self.vs[45]["GUID__"] = UUID('fb6436df-2e70-47f5-9a4c-a47b954ad90b')
        self.vs[46]["mm__"] = """__Relation__"""
        self.vs[46]["GUID__"] = UUID('def81d36-5716-4940-b267-fe64cdb6aa87')
        self.vs[47]["mm__"] = """__Relation__"""
        self.vs[47]["GUID__"] = UUID('9ea2bc16-c2fc-403b-87c3-c5ed74d239dc')
        self.vs[48]["mm__"] = """__Relation__"""
        self.vs[48]["GUID__"] = UUID('ef96e74b-3460-405a-8cd0-1e7ec5a5be3c')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('c66e66a6-17db-4f0d-939b-c1e385da0e71')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('f43e473a-bcc2-402f-b74c-a9b04b62980d')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('97e482ca-76d1-410e-99af-375e821eb69c')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('03d67171-76bb-414c-9d0d-d4a032710218')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('7ab3dfe5-10cb-4881-bb60-7b915f7f521c')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('942aca0f-3eb4-46ab-9519-74181ef69278')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('9ae6f731-3596-4f52-a198-7e068dcd90bc')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('4b653cf1-ff54-4edb-b6e5-15d307b9fc44')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('bc231cf4-8a8e-4071-a586-8839ee63c23d')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('0f23ec85-9d7b-4f0a-b6ab-6589dbb63787')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('35d49620-b449-45aa-96cc-09e6d8bd59f5')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('2a701526-13a2-4547-a27f-cf524765c651')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('0f92a02f-4dd8-467c-b0d9-61db94b4ef1c')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('f431fa34-5efd-47b0-a1f2-523ad7b8b323')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('46c04b4b-8a5a-4613-a29a-a01312dee21a')

