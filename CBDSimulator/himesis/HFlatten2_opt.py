

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten2_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten2_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten2_opt, self).__init__(name='HFlatten2_opt', num_nodes=87, edges=[])
        
        # Add the edges
        self.add_edges([(0, 30), (2, 34), (3, 31), (4, 32), (9, 26), (10, 27), (11, 28), (5, 82), (5, 81), (5, 80), (5, 79), (5, 78), (5, 77), (5, 33), (6, 73), (6, 74), (6, 75), (6, 76), (6, 86), (6, 85), (6, 84), (6, 83), (12, 29), (13, 35), (14, 36), (15, 65), (16, 72), (17, 67), (18, 66), (19, 64), (19, 63), (20, 61), (21, 69), (22, 62), (23, 68), (24, 70), (25, 71), (26, 15), (27, 16), (28, 17), (29, 18), (30, 19), (31, 20), (32, 21), (33, 22), (34, 23), (35, 24), (36, 25), (49, 37), (50, 38), (51, 39), (52, 40), (53, 41), (54, 42), (55, 43), (56, 44), (57, 45), (58, 46), (59, 47), (60, 48), (7, 49), (0, 50), (3, 51), (3, 52), (4, 53), (4, 54), (5, 55), (5, 56), (8, 57), (1, 58), (2, 59), (2, 60), (61, 44), (62, 38), (63, 46), (64, 37), (65, 40), (66, 39), (67, 47), (68, 45), (69, 48), (70, 42), (71, 41), (72, 43), (73, 10), (74, 0), (75, 3), (76, 5), (77, 11), (78, 4), (79, 8), (80, 2), (81, 13), (82, 14), (83, 7), (84, 9), (85, 12), (86, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlatten2_opt"""
        self["GUID__"] = UUID('0dd2a6cf-4f18-483b-b590-9dd15c159628')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Gain2"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["gain"] = 5.4
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["mm__"] = """Gain"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F405
aF99
aF445
aF131
a.""")
        self.vs[0]["GUID__"] = UUID('eab758dd-687e-4d6b-abeb-469b30a25a85')
        self.vs[1]["NumInputPorts"] = """1"""
        self.vs[1]["Name"] = """Scope"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Scope"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F345
aF129
aF375
aF161
a.""")
        self.vs[1]["LimitDataPoints"] = """on"""
        self.vs[1]["GUID__"] = UUID('80745496-1f38-4506-8cac-2fb1b325a69b')
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
        self.vs[2]["GUID__"] = UUID('ae39d668-0b73-421f-a761-ca470fc65aa9')
        self.vs[3]["Name"] = """Product2"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["mm__"] = """Product"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F185
aF177
aF215
aF208
a.""")
        self.vs[3]["GUID__"] = UUID('aa6d3a08-620f-401f-9720-1ffefe0f0070')
        self.vs[4]["Name"] = """Product3"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """lightBlue"""
        self.vs[4]["mm__"] = """Product"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F225
aF127
aF255
aF158
a.""")
        self.vs[4]["GUID__"] = UUID('d0612845-c6a9-4375-be6b-f414b7d1aa20')
        self.vs[5]["Name"] = """Subsystem2"""
        self.vs[5]["BackgroundColor"] = """lightBlue"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F270
aF134
aF370
aF176
a.""")
        self.vs[5]["GUID__"] = UUID('b36ee989-9a4a-43ae-ad5c-5c6ad35479b0')
        self.vs[6]["Name"] = """Flatten2"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('aebafc85-2511-46fa-aaa1-aa9cc80e5e2b')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F355
aF98
aF385
aF112
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('1ed517c2-c338-4405-8ebb-0177eeeebd0d')
        self.vs[8]["Name"] = """Out1"""
        self.vs[8]["BackgroundColor"] = """lightBlue"""
        self.vs[8]["mm__"] = """Outport"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F355
aF108
aF385
aF122
a.""")
        self.vs[8]["Port"] = 1
        self.vs[8]["GUID__"] = UUID('546d9f39-d8b6-4448-8a1f-0abefbab54d7')
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
        self.vs[9]["GUID__"] = UUID('01586a34-b5f4-46be-8e19-7271b3f4ec6e')
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
        self.vs[10]["GUID__"] = UUID('20e8626d-e475-4ecd-99b0-0d0e455eadfe')
        self.vs[11]["Name"] = """Constant"""
        self.vs[11]["SampleTime"] = """inf"""
        self.vs[11]["value"] = 66598.0
        self.vs[11]["BackgroundColor"] = """lightBlue"""
        self.vs[11]["mm__"] = """Constant"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F205
aF69
aF250
aF101
a.""")
        self.vs[11]["GUID__"] = UUID('3cb47013-e581-4a4b-970a-379c13f4adf4')
        self.vs[12]["Name"] = """In1"""
        self.vs[12]["BackgroundColor"] = """white"""
        self.vs[12]["mm__"] = """Inport"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F40
aF48
aF70
aF62
a.""")
        self.vs[12]["Port"] = 1
        self.vs[12]["GUID__"] = UUID('fb40bc1e-7073-4e83-bced-36100b77c7f9')
        self.vs[13]["Name"] = """In2"""
        self.vs[13]["BackgroundColor"] = """lightBlue"""
        self.vs[13]["mm__"] = """Inport"""
        self.vs[13]["Position"] = pickle.loads("""(lp1
F115
aF158
aF145
aF172
a.""")
        self.vs[13]["Port"] = 2
        self.vs[13]["GUID__"] = UUID('a173cc4d-70eb-4b8f-b75a-6474a3ca685c')
        self.vs[14]["Name"] = """In1"""
        self.vs[14]["BackgroundColor"] = """lightBlue"""
        self.vs[14]["mm__"] = """Inport"""
        self.vs[14]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[14]["Port"] = 1
        self.vs[14]["GUID__"] = UUID('24e2610f-67a1-484d-9350-40140852b8ed')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('9356cc89-3fcc-4e39-a68a-01ccbc625ec4')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('d7cf3c69-9965-43e4-a5f2-f5c8c6ba98f7')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('a9c2beca-da3d-4920-a678-c8d6095e0fab')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('55972dd7-971d-40dc-b693-9c529e305e89')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('83d84248-9715-4289-ab82-2eb41ac866bb')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('659d8340-bee8-481e-81d7-9d291c121583')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('d98fcbe3-3ca7-4d24-ada0-edc497f9630d')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('8d22322c-f350-43d0-aa66-718b85e1758b')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('5ad1b8b5-aa37-4f46-80cb-349bee569e62')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('1587645b-3cae-4244-84dc-c1b24b15bfc5')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('fd6bd3dd-09fc-4799-a563-d7170bf55f36')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('d983ee6e-f7b2-4eb7-bd7a-7cb5e06f620c')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('645bb7cf-7e8f-486e-b6d2-1b48991ea193')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('dbb75ce1-4884-46c2-a0b8-bc34ea41709f')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('9ce6f443-fb2c-463e-b10d-ce61cb426afd')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('d2ea2d35-f943-4f33-9e5d-63e39dba4172')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('6dd05980-e38b-4ab7-9312-1ba9e788bc93')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('df62a9f1-d752-45ef-942a-bd6fcf67bb17')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('2d326522-abb2-4abd-aba7-1fc92ca52226')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('0b42ad11-631f-4f95-beba-c896df9be7db')
        self.vs[35]["mm__"] = """__Block_Outport__"""
        self.vs[35]["GUID__"] = UUID('cb9e76d9-221b-4615-9e7c-07c21c05cca5')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('71533969-25dc-47d0-8eaf-022c4b80440e')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('861e5d15-fe82-401f-8ed6-eafbcaebd8d6')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('83215178-9c47-4c81-b7fe-e0b458e345b8')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('e8884a04-7b17-4cf3-aeb5-1d46a46ded73')
        self.vs[40]["Name"] = """2"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('5e7b287f-4463-45b2-abf1-789434d326fc')
        self.vs[41]["Name"] = """1"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('8f94cb6e-b57e-48c4-94be-332cc8953c98')
        self.vs[42]["Name"] = """2"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('fc6f85af-56ba-4f7d-a726-1f9d43400b06')
        self.vs[43]["Name"] = """1"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('5681d3fa-6518-48b2-971c-2bd7acdffe1c')
        self.vs[44]["Name"] = """2"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('5058ecb9-22cf-4ffe-ba05-44b134b3ef43')
        self.vs[45]["Name"] = """1"""
        self.vs[45]["mm__"] = """Port_Input"""
        self.vs[45]["GUID__"] = UUID('5240368e-0cf9-4125-a32e-b67746b01ee2')
        self.vs[46]["Name"] = """1"""
        self.vs[46]["mm__"] = """Port_Input"""
        self.vs[46]["GUID__"] = UUID('8f4afa96-112c-434c-b71f-2759b6329d75')
        self.vs[47]["Name"] = """1"""
        self.vs[47]["mm__"] = """Port_Input"""
        self.vs[47]["GUID__"] = UUID('47e1b5b2-e934-41bc-a284-43c0fc280d2c')
        self.vs[48]["Name"] = """2"""
        self.vs[48]["mm__"] = """Port_Input"""
        self.vs[48]["GUID__"] = UUID('f887f36f-0c68-4da5-9a41-176a5f74540c')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('352da430-22d3-4126-850d-ef01f248da5f')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('7ff2959d-1304-4284-85e3-5d126280db62')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('e738704d-c83c-4680-b19f-c41122ef3dbc')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('1f301e1e-fb04-4489-8313-95adf775ef46')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('a4ee0caa-5c9f-46ee-bfd9-dec54b100bfc')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('a6bb50a3-f4c5-4c1d-85ab-ade59d6b1d78')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('505236e0-38f5-4ad2-9c01-f51cdecfc856')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('293b2f7e-5e44-413d-892f-fd0e315a694f')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('70e756a4-277c-4f1b-8819-5364706fac3b')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('59dd238d-534d-40dd-9419-b0fd83370e6a')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('ee9220af-a842-4d4c-a419-61eea025fd62')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('4fb495df-565f-4a8b-b8f8-e0cbbf7d1959')
        self.vs[61]["mm__"] = """__Relation__"""
        self.vs[61]["GUID__"] = UUID('a221b794-918d-4072-9fca-42d6da1fdc83')
        self.vs[62]["mm__"] = """__Relation__"""
        self.vs[62]["GUID__"] = UUID('b873d316-86af-4337-a502-558a1c9905c8')
        self.vs[63]["mm__"] = """__Relation__"""
        self.vs[63]["GUID__"] = UUID('98432b08-8470-4292-96a4-0ba69190ebe9')
        self.vs[64]["mm__"] = """__Relation__"""
        self.vs[64]["GUID__"] = UUID('1d903552-6e90-40c2-8313-e1ac7a047770')
        self.vs[65]["mm__"] = """__Relation__"""
        self.vs[65]["GUID__"] = UUID('9b10857d-bae4-480f-b225-99e643f5ab58')
        self.vs[66]["mm__"] = """__Relation__"""
        self.vs[66]["GUID__"] = UUID('1690f462-03bd-49f7-9c1e-2db5fd8282d6')
        self.vs[67]["mm__"] = """__Relation__"""
        self.vs[67]["GUID__"] = UUID('00b7df32-7163-410e-a8be-20c850968053')
        self.vs[68]["mm__"] = """__Relation__"""
        self.vs[68]["GUID__"] = UUID('4cea1e93-31eb-4c10-b85a-8d0612d624df')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('d0a15801-6cb5-4fbe-94e6-c7e4ff61b490')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('61e76f49-e3a6-443f-a982-21a1449ff123')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('7ddc60c2-4ee6-47ef-834b-e69f0eb17a20')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('01e56c16-c7a0-49b3-b90b-ac8c7e7abcf8')
        self.vs[73]["Name"] = """None"""
        self.vs[73]["mm__"] = """__Contains__"""
        self.vs[73]["GUID__"] = UUID('a18dc378-1bc6-4b19-9843-f783181e81ed')
        self.vs[74]["Name"] = """None"""
        self.vs[74]["mm__"] = """__Contains__"""
        self.vs[74]["GUID__"] = UUID('b6043630-a103-4975-90cb-d7fad174212b')
        self.vs[75]["Name"] = """None"""
        self.vs[75]["mm__"] = """__Contains__"""
        self.vs[75]["GUID__"] = UUID('8775a461-a540-49ae-85b4-bdea96c53701')
        self.vs[76]["Name"] = """None"""
        self.vs[76]["mm__"] = """__Contains__"""
        self.vs[76]["GUID__"] = UUID('6eb6e646-9935-45bf-a430-2f7716675a90')
        self.vs[77]["Name"] = """None"""
        self.vs[77]["mm__"] = """__Contains__"""
        self.vs[77]["GUID__"] = UUID('7fddd2ea-bfb3-4a4f-94d5-511f11335334')
        self.vs[78]["Name"] = """None"""
        self.vs[78]["mm__"] = """__Contains__"""
        self.vs[78]["GUID__"] = UUID('0e0400b3-d6d4-493d-80d3-0f8012ae04e9')
        self.vs[79]["Name"] = """None"""
        self.vs[79]["mm__"] = """__Contains__"""
        self.vs[79]["GUID__"] = UUID('01a55f19-4164-4f5a-80c1-4d2bcebe4cee')
        self.vs[80]["Name"] = """None"""
        self.vs[80]["mm__"] = """__Contains__"""
        self.vs[80]["GUID__"] = UUID('059f871b-4e75-4cec-a00b-aa8931ab179a')
        self.vs[81]["Name"] = """None"""
        self.vs[81]["mm__"] = """__Contains__"""
        self.vs[81]["GUID__"] = UUID('f5db08e5-8c79-4b34-8adb-627312049ff0')
        self.vs[82]["Name"] = """None"""
        self.vs[82]["mm__"] = """__Contains__"""
        self.vs[82]["GUID__"] = UUID('73e6a0fb-b38c-4f5d-b411-836e486c1893')
        self.vs[83]["Name"] = """None"""
        self.vs[83]["mm__"] = """__Contains__"""
        self.vs[83]["GUID__"] = UUID('cf7638e5-6299-4ad7-86bf-640efb8161c4')
        self.vs[84]["Name"] = """None"""
        self.vs[84]["mm__"] = """__Contains__"""
        self.vs[84]["GUID__"] = UUID('40baafc0-c8bf-4084-b547-4d7445ef9eb5')
        self.vs[85]["Name"] = """None"""
        self.vs[85]["mm__"] = """__Contains__"""
        self.vs[85]["GUID__"] = UUID('eaa2ea76-8593-41d6-8a03-8c488ed3b525')
        self.vs[86]["Name"] = """None"""
        self.vs[86]["mm__"] = """__Contains__"""
        self.vs[86]["GUID__"] = UUID('6788949c-66f8-448f-b1af-606d0580ed3f')

