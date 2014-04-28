

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten2_export(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten2_export.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten2_export, self).__init__(name='HFlatten2_export', num_nodes=87, edges=[])
        
        # Add the edges
        self.add_edges([(3, 49), (49, 37), (4, 50), (50, 38), (4, 51), (51, 39), (4, 26), (26, 15), (0, 52), (52, 40), (0, 27), (27, 16), (9, 28), (28, 17), (10, 29), (29, 18), (11, 30), (30, 19), (5, 53), (53, 41), (12, 31), (31, 20), (6, 54), (54, 42), (6, 55), (55, 43), (6, 32), (32, 21), (7, 56), (56, 44), (7, 57), (57, 45), (7, 33), (33, 22), (1, 58), (58, 46), (13, 34), (34, 23), (2, 59), (59, 47), (2, 60), (60, 48), (2, 35), (35, 24), (14, 36), (36, 25), (8, 73), (73, 3), (8, 74), (74, 4), (8, 75), (75, 0), (8, 76), (76, 11), (8, 77), (77, 7), (8, 78), (78, 1), (8, 79), (79, 13), (8, 80), (80, 14), (4, 81), (81, 9), (4, 82), (82, 10), (4, 83), (83, 5), (4, 84), (84, 12), (4, 85), (85, 6), (4, 86), (86, 2), (24, 61), (61, 41), (21, 62), (62, 48), (17, 63), (63, 47), (15, 64), (64, 40), (22, 65), (65, 39), (16, 66), (66, 37), (16, 67), (67, 46), (19, 68), (68, 44), (25, 69), (69, 38), (23, 70), (70, 45), (18, 71), (71, 42), (20, 72), (72, 43)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """Flatten2_export"""
        self["GUID__"] = UUID('1f14ea2b-92b1-4ee6-9d8b-2586c059911e')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Gain2"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["gain"] = 5.4
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F405
aF99
aF445
aF131
a.""")
        self.vs[0]["mm__"] = """Gain"""
        self.vs[0]["GUID__"] = UUID('16b57c5e-59ec-423a-aa46-91d99fd3a130')
        self.vs[1]["NumInputPorts"] = """1"""
        self.vs[1]["Name"] = """Scope"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F345
aF129
aF375
aF161
a.""")
        self.vs[1]["mm__"] = """Scope"""
        self.vs[1]["LimitDataPoints"] = """on"""
        self.vs[1]["GUID__"] = UUID('d7f4eb2b-03f9-4613-8d3c-b4c18eeda733')
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["BackgroundColor"] = """lightBlue"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F280
aF90
aF300
aF110
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["GUID__"] = UUID('de157315-198b-4fe8-8fbf-b513065d3c63')
        self.vs[3]["Name"] = """Out1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F355
aF98
aF385
aF112
a.""")
        self.vs[3]["mm__"] = """Outport"""
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('6c8011d8-0d40-4b61-9dbe-86e495673b83')
        self.vs[4]["Name"] = """Subsystem2"""
        self.vs[4]["BackgroundColor"] = """lightBlue"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F270
aF134
aF370
aF176
a.""")
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["GUID__"] = UUID('91416b52-7f25-4b64-ae60-81896a28c79b')
        self.vs[5]["Name"] = """Out1"""
        self.vs[5]["BackgroundColor"] = """lightBlue"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F355
aF108
aF385
aF122
a.""")
        self.vs[5]["mm__"] = """Outport"""
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('08b0ee06-a763-49d9-90ad-98b94f4b1a9c')
        self.vs[6]["Name"] = """Product3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """lightBlue"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F225
aF127
aF255
aF158
a.""")
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["GUID__"] = UUID('feec4af7-6968-41fe-800d-319194625d94')
        self.vs[7]["Name"] = """Product2"""
        self.vs[7]["SampleTime"] = -1.0
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F185
aF177
aF215
aF208
a.""")
        self.vs[7]["mm__"] = """Product"""
        self.vs[7]["GUID__"] = UUID('3ee35b92-f06d-4917-b22a-cb61dfde8770')
        self.vs[8]["Name"] = """Flatten2_export"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('4780bf56-3fc5-464a-a175-8d7f8d825336')
        self.vs[9]["Name"] = """Constant"""
        self.vs[9]["SampleTime"] = inf
        self.vs[9]["value"] = 66598.0
        self.vs[9]["BackgroundColor"] = """lightBlue"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F205
aF69
aF250
aF101
a.""")
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["GUID__"] = UUID('8e128d2b-55a9-4c0e-ba0d-2c5dac408523')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """lightBlue"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('e54f072a-812f-4ecf-b1a2-cffa1095fb7f')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F40
aF48
aF70
aF62
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('9054a8bc-bc6f-44aa-9245-16bf0a30e48e')
        self.vs[12]["Name"] = """In2"""
        self.vs[12]["BackgroundColor"] = """lightBlue"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F115
aF158
aF145
aF172
a.""")
        self.vs[12]["mm__"] = """Inport"""
        self.vs[12]["Port"] = 2
        self.vs[12]["GUID__"] = UUID('695860e2-1925-4d4d-a762-c615048d63a5')
        self.vs[13]["Name"] = """Constant"""
        self.vs[13]["SampleTime"] = inf
        self.vs[13]["value"] = 134.67
        self.vs[13]["BackgroundColor"] = """white"""
        self.vs[13]["Position"] = pickle.loads("""(lp1
F30
aF127
aF80
aF163
a.""")
        self.vs[13]["mm__"] = """Constant"""
        self.vs[13]["GUID__"] = UUID('9c15299c-1146-4534-ad2f-dbc755d7942d')
        self.vs[14]["Name"] = """Constant2"""
        self.vs[14]["SampleTime"] = inf
        self.vs[14]["value"] = 12.34
        self.vs[14]["BackgroundColor"] = """yellow"""
        self.vs[14]["Position"] = pickle.loads("""(lp1
F175
aF120
aF220
aF150
a.""")
        self.vs[14]["mm__"] = """Constant"""
        self.vs[14]["GUID__"] = UUID('d5bfa501-a141-4d93-9cd0-c187ce9e2577')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('73879253-001c-4f10-9829-08b672463ba8')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('8b50ee3f-e7cc-4f63-b575-72cfd0a7f77d')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('bc75f78d-0f37-479d-9c34-79a9be17111a')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('802ffda1-ec34-4e4a-b9a0-4cd11093619f')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('8bd61137-e815-463f-8515-44ed8a50a89a')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('300ba022-5e22-45e1-b685-ec3866941aa3')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('ac2f78ec-8532-4fe8-b032-af078cb17dad')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('a8be4f2e-40eb-42a6-b596-1b516fb9efac')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('7a19e4a5-8401-4cba-851d-fe7948af3758')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('9a84c4eb-9671-4e28-a307-cb432eaa17b8')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('88972c25-9253-49e6-8361-c22c55068a69')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('ec5b57d5-2363-45c1-ace2-c12d9cf65a79')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('9f0d11fd-2b0b-4b49-ab30-9e4d1bbddbbf')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('c1daa113-e28d-47b5-905e-0800e10ef76b')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('ecc243ee-a43c-486d-ba66-92987cb0f9dc')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('e43adb02-027b-463a-95ad-13c02a902a1f')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('33d1ff26-3e67-410b-b1fa-ee94904b362c')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('9b08d053-74df-4850-92e6-19970546309c')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('a2d70bbf-f74b-40de-ae87-c39a1ca8c6e5')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('20efbc4f-014a-4b52-bf4e-086c882c3731')
        self.vs[35]["mm__"] = """__Block_Outport__"""
        self.vs[35]["GUID__"] = UUID('65415464-8f47-43a2-9a4b-ee4a914289b4')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('e280f38b-04ad-4f35-918d-418eacb4cf71')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('3ec545f9-aa99-4c1f-bc75-6625c8c2a829')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('44f65c66-3b9c-42a0-b7c4-99807b524b8c')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('cdf0fd4d-5121-4177-b16a-84f765b7c5e1')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('12a4ff15-2254-4ccc-9450-9dff74254371')
        self.vs[41]["Name"] = """1"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('1bfce98f-e1c8-45f4-a20a-773637b53a40')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('42dba55d-cffc-4abc-a8c2-51465a37b726')
        self.vs[43]["Name"] = """2"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('a7772186-d727-420b-b96e-c1dc515d88ac')
        self.vs[44]["Name"] = """1"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('4684c0f9-9a84-453d-9431-17d6d5db6f9b')
        self.vs[45]["Name"] = """2"""
        self.vs[45]["mm__"] = """Port_Input"""
        self.vs[45]["GUID__"] = UUID('b446c10c-82dc-474d-9569-af5e0f57fe74')
        self.vs[46]["Name"] = """1"""
        self.vs[46]["mm__"] = """Port_Input"""
        self.vs[46]["GUID__"] = UUID('33d91542-8c27-4c1a-be6f-71095c14a69b')
        self.vs[47]["Name"] = """1"""
        self.vs[47]["mm__"] = """Port_Input"""
        self.vs[47]["GUID__"] = UUID('d6f899de-5c74-404f-bdc3-b207cfe9cf74')
        self.vs[48]["Name"] = """2"""
        self.vs[48]["mm__"] = """Port_Input"""
        self.vs[48]["GUID__"] = UUID('a36d92f4-1940-4fc6-8dc2-2ca3341ae676')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('8ec5b881-1113-4cb1-92bf-354ab4f4d2e6')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('4c030916-74fe-4323-a987-0ca1743949be')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('0ce17df3-5c37-4e40-bfe2-f882e7593a47')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('20bab73f-4deb-4a4d-9e6c-e129dbbae624')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('da2ed824-4ff0-45be-a443-2972fcaff6d9')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('ea2c904e-ff4f-45e0-9a57-76666df3c2f3')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('d20ae826-b70d-4cec-bc9e-29dcbc5f7bfb')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('b8fa8990-9941-4fbe-b9fe-656947e3e523')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('1d19138e-3b5e-4bc8-b174-b217be68dc24')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('c559c5e4-6c08-4077-8f6e-add9360cb175')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('ed012a4f-e134-44fe-aa00-0b83f1afc951')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('701ef4b7-f65d-4002-93f6-9d8a40712db2')
        self.vs[61]["mm__"] = """__Relation__"""
        self.vs[61]["GUID__"] = UUID('7d9a2280-8a29-4bff-b972-b77a579ed0b3')
        self.vs[62]["mm__"] = """__Relation__"""
        self.vs[62]["GUID__"] = UUID('8e2a040c-cb7a-4d3e-917c-7ae25268b859')
        self.vs[63]["mm__"] = """__Relation__"""
        self.vs[63]["GUID__"] = UUID('8ffa5fbd-ae32-451b-952d-9a5fee0ee7ef')
        self.vs[64]["mm__"] = """__Relation__"""
        self.vs[64]["GUID__"] = UUID('21c03ea0-542a-46dd-9a0f-c840c31644ac')
        self.vs[65]["mm__"] = """__Relation__"""
        self.vs[65]["GUID__"] = UUID('28e6c2e6-11a5-48d0-91ff-e5781426510b')
        self.vs[66]["mm__"] = """__Relation__"""
        self.vs[66]["GUID__"] = UUID('42554263-da39-4182-94ae-1632bb1e7fd7')
        self.vs[67]["mm__"] = """__Relation__"""
        self.vs[67]["GUID__"] = UUID('2340b485-47ae-4592-b7c3-cdf25153b421')
        self.vs[68]["mm__"] = """__Relation__"""
        self.vs[68]["GUID__"] = UUID('c24ffa95-78cc-4878-a472-f8af0e63d3c3')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('6433f18f-e7df-41fc-88c3-ab9c77a371ab')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('e757b87b-5bc0-4ab0-8517-e39956ab1501')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('a3303efe-8fae-4f3b-aae9-02108db3c0ad')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('ff8bacc7-2411-4597-9d46-c78128be341d')
        self.vs[73]["Name"] = """None"""
        self.vs[73]["mm__"] = """__Contains__"""
        self.vs[73]["GUID__"] = UUID('3ace5a3d-d8a2-480b-af0a-5164497804a8')
        self.vs[74]["Name"] = """None"""
        self.vs[74]["mm__"] = """__Contains__"""
        self.vs[74]["GUID__"] = UUID('f5b096a2-f7cd-4544-8683-1eae0280f1d1')
        self.vs[75]["Name"] = """None"""
        self.vs[75]["mm__"] = """__Contains__"""
        self.vs[75]["GUID__"] = UUID('77c5c546-a802-4e8d-9bdf-f81de092f9ce')
        self.vs[76]["Name"] = """None"""
        self.vs[76]["mm__"] = """__Contains__"""
        self.vs[76]["GUID__"] = UUID('4990ba08-a2ce-466a-81be-e13747e6ba8b')
        self.vs[77]["Name"] = """None"""
        self.vs[77]["mm__"] = """__Contains__"""
        self.vs[77]["GUID__"] = UUID('962d61fe-2240-4342-bf02-03d0f594fb3f')
        self.vs[78]["Name"] = """None"""
        self.vs[78]["mm__"] = """__Contains__"""
        self.vs[78]["GUID__"] = UUID('c1f0b70b-326c-44b8-ba20-ea0fb6b79517')
        self.vs[79]["Name"] = """None"""
        self.vs[79]["mm__"] = """__Contains__"""
        self.vs[79]["GUID__"] = UUID('1ff92087-98c6-49c5-bd3b-e99014812afe')
        self.vs[80]["Name"] = """None"""
        self.vs[80]["mm__"] = """__Contains__"""
        self.vs[80]["GUID__"] = UUID('a8a9eb7b-dad2-4866-8d6e-ee25dc012a46')
        self.vs[81]["Name"] = """None"""
        self.vs[81]["mm__"] = """__Contains__"""
        self.vs[81]["GUID__"] = UUID('25a5cfd2-04c8-4892-a517-ef33db43b9ed')
        self.vs[82]["Name"] = """None"""
        self.vs[82]["mm__"] = """__Contains__"""
        self.vs[82]["GUID__"] = UUID('f483cc3e-7607-4c60-87e7-712ebf688b22')
        self.vs[83]["Name"] = """None"""
        self.vs[83]["mm__"] = """__Contains__"""
        self.vs[83]["GUID__"] = UUID('8b61f8e5-8bde-49be-8103-060e9d0b5209')
        self.vs[84]["Name"] = """None"""
        self.vs[84]["mm__"] = """__Contains__"""
        self.vs[84]["GUID__"] = UUID('23fa11ea-a498-4f79-9225-ddc32d4eed21')
        self.vs[85]["Name"] = """None"""
        self.vs[85]["mm__"] = """__Contains__"""
        self.vs[85]["GUID__"] = UUID('88c71279-2f0a-45ea-b56e-931e1895f2c6')
        self.vs[86]["Name"] = """None"""
        self.vs[86]["mm__"] = """__Contains__"""
        self.vs[86]["GUID__"] = UUID('73550cbd-6112-4f10-a825-ba63ca9a88b7')

