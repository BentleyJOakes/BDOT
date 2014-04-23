

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
        self["GUID__"] = UUID('fff18c40-0775-47b1-bb65-f338f710dda6')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Gain2"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["gain"] = 5.4
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F410
aF139
aF450
aF171
a.""")
        self.vs[0]["mm__"] = """Gain"""
        self.vs[0]["GUID__"] = UUID('463935c9-2fa3-48dc-b607-0abb2e13d6a9')
        self.vs[1]["NumInputPorts"] = """1"""
        self.vs[1]["Name"] = """Scope"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F535
aF204
aF565
aF236
a.""")
        self.vs[1]["mm__"] = """Scope"""
        self.vs[1]["LimitDataPoints"] = """on"""
        self.vs[1]["GUID__"] = UUID('786384e5-5796-4355-817e-00605cab65e2')
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
        self.vs[2]["GUID__"] = UUID('e226740b-7f2a-43b3-82f7-e505d7dda4f2')
        self.vs[3]["Name"] = """Out1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F535
aF148
aF565
aF162
a.""")
        self.vs[3]["mm__"] = """Outport"""
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('bd1230c0-8bad-4b1f-9801-64b8423e260d')
        self.vs[4]["Name"] = """Subsystem2"""
        self.vs[4]["BackgroundColor"] = """lightBlue"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F270
aF134
aF370
aF176
a.""")
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["GUID__"] = UUID('ec2d88f1-6ad4-45c5-94af-0084d8d4ab2b')
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
        self.vs[5]["GUID__"] = UUID('37319f9f-be13-4249-bf64-511c07a54a59')
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
        self.vs[6]["GUID__"] = UUID('79d350d7-19f7-4cf4-a828-0bae9fb25b53')
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
        self.vs[7]["GUID__"] = UUID('ab05edba-c7d3-4909-bb14-da6bff7ac7a6')
        self.vs[8]["Name"] = """Flatten2_export"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('bea33e68-c1ac-4a4d-9edb-585c9e7c0e8f')
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
        self.vs[9]["GUID__"] = UUID('8dda3eab-87f8-42dd-be1f-c99a1e2821a5')
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
        self.vs[10]["GUID__"] = UUID('61c2c9e6-0401-4ac9-90d8-ab5c78ac6a04')
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
        self.vs[11]["GUID__"] = UUID('8814d5cb-5ebc-40a9-ab98-8dd6d93384d7')
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
        self.vs[12]["GUID__"] = UUID('65335a01-f7af-4321-894c-7fa9b8aa6f48')
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
        self.vs[13]["GUID__"] = UUID('6a3653cf-ab35-46c6-9845-0e0001618f15')
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
        self.vs[14]["GUID__"] = UUID('2718cece-7e53-4d1b-8c07-44f173c88fe7')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('619128aa-74ae-4d6a-ae90-1a686086b08e')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('06425856-1d7b-4e8d-a4ce-416a13694428')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('98c810e0-2226-4d09-ac2b-0e30b0c10b60')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('913c9338-2704-4849-85f1-7205fabc5e20')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('466a2fe4-9fcf-46e3-9c7a-c74a1c3c136e')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('842b5325-47d7-4097-94e1-7ee483390b70')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('762bf254-63c1-4317-aacc-e15fc3121be2')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('81081074-e41c-4c8a-8b4a-2d488570f9c2')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('bd721409-afa7-4203-bd0a-8971adc53d91')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('84a27e80-23a1-4991-8a4c-32521614a0d6')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('3802a0d6-21b0-4d8a-93d1-0582a076b331')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('c0d6b0d6-db7c-490c-9e27-c41ecf298fc5')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('ca3515d5-8c6e-4aea-a635-e93af5f875ce')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('188d8be7-5b20-4703-8ab8-e2219d884191')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('8721241a-d2e8-4cf8-9dc1-f84eb83d71b1')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('1b3ba836-40d5-4fd9-b5d7-38dac1670771')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('112e6675-b41c-4039-b803-b9bcc2864936')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('94daa0d0-22f9-4df7-af69-0ce2b1839e53')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('0a9cc0b2-b03c-4491-8c3c-341003498406')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('5bf6dd31-d5b1-4cd4-bee3-28ef51ffca7c')
        self.vs[35]["mm__"] = """__Block_Outport__"""
        self.vs[35]["GUID__"] = UUID('b7d56f18-b969-4407-a3bc-f8451094bcde')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('45b307aa-230f-4a8e-87b4-82a4ad7bc7bb')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('231c1397-1ad1-4896-a299-025a1c13c3fe')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('22ec3ac2-9882-4395-b9bc-0b925db52a42')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('103321de-d423-42bb-b8e2-8ca4d2e9e742')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('c7358e64-445c-4ee7-9875-b0229fc919cf')
        self.vs[41]["Name"] = """1"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('41616e92-e4d0-4ce5-8402-5d87bb91ed70')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('4cd79746-566a-4cf5-bc5c-447bd28cbd80')
        self.vs[43]["Name"] = """2"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('8ccf3f1c-7265-4855-9194-1b315cf8d396')
        self.vs[44]["Name"] = """1"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('8497a77b-6f03-433e-bc38-3400b5f6bda7')
        self.vs[45]["Name"] = """2"""
        self.vs[45]["mm__"] = """Port_Input"""
        self.vs[45]["GUID__"] = UUID('5da731d0-1d17-4f8b-8093-5e43439b012d')
        self.vs[46]["Name"] = """1"""
        self.vs[46]["mm__"] = """Port_Input"""
        self.vs[46]["GUID__"] = UUID('686c94ad-094d-4ea0-a453-3158bb5ef961')
        self.vs[47]["Name"] = """1"""
        self.vs[47]["mm__"] = """Port_Input"""
        self.vs[47]["GUID__"] = UUID('74dbe281-52a6-41dd-88f4-a88fd2eea10a')
        self.vs[48]["Name"] = """2"""
        self.vs[48]["mm__"] = """Port_Input"""
        self.vs[48]["GUID__"] = UUID('0521c06a-d23d-4a63-9b44-449127410899')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('cd974186-5b30-4fd5-a7cf-a77f3666935c')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('64c71b23-912c-41d0-a926-fff2a9173a4d')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('0f981119-495b-4583-9545-c3b567f897b1')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('65783f45-2ce8-4ca4-8d6d-e1debf8641f1')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('f4f15da2-d307-423b-87cd-598517a81aa2')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('e88c0f76-7725-4a03-971d-585a6d903b42')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('40e76b6f-1a21-4878-9cff-db12784a8e25')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('37168f06-da46-4df9-9fcd-a6cc74cdd2fc')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('62776dd1-47d1-4862-9b17-3c3991e8bb5b')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('953732c2-4dcd-4020-a227-825589ea75d4')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('cbd34259-5158-488c-a7df-ef29b6211674')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('a77d2298-7f34-4ac3-a981-efcae4b94780')
        self.vs[61]["mm__"] = """__Relation__"""
        self.vs[61]["GUID__"] = UUID('6fdc2487-c3f9-49a1-9921-3138331b59f4')
        self.vs[62]["mm__"] = """__Relation__"""
        self.vs[62]["GUID__"] = UUID('bdb78bdd-7bf5-4c09-a1c2-ca808a35996a')
        self.vs[63]["mm__"] = """__Relation__"""
        self.vs[63]["GUID__"] = UUID('3fe20754-e88e-4794-bd7c-b5349fada909')
        self.vs[64]["mm__"] = """__Relation__"""
        self.vs[64]["GUID__"] = UUID('145dba29-cd63-4d7a-b583-a5d2dcade6ae')
        self.vs[65]["mm__"] = """__Relation__"""
        self.vs[65]["GUID__"] = UUID('dfb9f69d-787a-48c0-a756-911060c7b9d1')
        self.vs[66]["mm__"] = """__Relation__"""
        self.vs[66]["GUID__"] = UUID('fde3649e-d284-4063-a325-92d8f4edf9d2')
        self.vs[67]["mm__"] = """__Relation__"""
        self.vs[67]["GUID__"] = UUID('e9fb59f3-848b-437c-a11e-f1397371a031')
        self.vs[68]["mm__"] = """__Relation__"""
        self.vs[68]["GUID__"] = UUID('4f60f92a-401a-4205-b6f0-c1a8b78bf868')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('67d34ae4-cec1-4e5e-857c-fabf595cad29')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('afd3dd4f-a556-4a97-8d29-18776fdeaeac')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('1596398f-62bf-4814-b75e-e4a0107a716e')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('6cc2dfcc-d045-4820-95b7-2e02cad38ea7')
        self.vs[73]["Name"] = """None"""
        self.vs[73]["mm__"] = """__Contains__"""
        self.vs[73]["GUID__"] = UUID('4a4f8234-88d9-48f9-b3a7-8e39c178b246')
        self.vs[74]["Name"] = """None"""
        self.vs[74]["mm__"] = """__Contains__"""
        self.vs[74]["GUID__"] = UUID('44875815-0e2a-4860-8211-17a1b501c76c')
        self.vs[75]["Name"] = """None"""
        self.vs[75]["mm__"] = """__Contains__"""
        self.vs[75]["GUID__"] = UUID('a348819e-586a-4407-bfba-6a7727353170')
        self.vs[76]["Name"] = """None"""
        self.vs[76]["mm__"] = """__Contains__"""
        self.vs[76]["GUID__"] = UUID('3ea8c259-634b-4ab8-9006-017f7181f644')
        self.vs[77]["Name"] = """None"""
        self.vs[77]["mm__"] = """__Contains__"""
        self.vs[77]["GUID__"] = UUID('8f35e4d5-3a09-4d91-8b72-1bb6ac639892')
        self.vs[78]["Name"] = """None"""
        self.vs[78]["mm__"] = """__Contains__"""
        self.vs[78]["GUID__"] = UUID('ea929258-9687-4a36-ae40-da8df6462ccd')
        self.vs[79]["Name"] = """None"""
        self.vs[79]["mm__"] = """__Contains__"""
        self.vs[79]["GUID__"] = UUID('1b5658ef-b63e-4f18-826e-62837b6e286e')
        self.vs[80]["Name"] = """None"""
        self.vs[80]["mm__"] = """__Contains__"""
        self.vs[80]["GUID__"] = UUID('b26c80a6-425a-4438-bf89-4c9c2a960e81')
        self.vs[81]["Name"] = """None"""
        self.vs[81]["mm__"] = """__Contains__"""
        self.vs[81]["GUID__"] = UUID('aedd90f6-322c-46fb-ba62-26325b2bd644')
        self.vs[82]["Name"] = """None"""
        self.vs[82]["mm__"] = """__Contains__"""
        self.vs[82]["GUID__"] = UUID('ec8fdcba-77e5-4f91-b74d-29c55059e219')
        self.vs[83]["Name"] = """None"""
        self.vs[83]["mm__"] = """__Contains__"""
        self.vs[83]["GUID__"] = UUID('a1bde283-3969-4115-99b4-6a09a357028e')
        self.vs[84]["Name"] = """None"""
        self.vs[84]["mm__"] = """__Contains__"""
        self.vs[84]["GUID__"] = UUID('c23b4cac-1ba6-4c97-89b3-ce7dc4145fe6')
        self.vs[85]["Name"] = """None"""
        self.vs[85]["mm__"] = """__Contains__"""
        self.vs[85]["GUID__"] = UUID('c7fef0d6-a972-46f4-bd6f-e2a6d7447a1c')
        self.vs[86]["Name"] = """None"""
        self.vs[86]["mm__"] = """__Contains__"""
        self.vs[86]["GUID__"] = UUID('9ce38bb4-e615-4823-aebb-4c5e3a4e6f3b')

