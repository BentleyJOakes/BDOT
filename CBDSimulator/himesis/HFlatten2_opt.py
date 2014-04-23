

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
        self["GUID__"] = UUID('f7b6e01c-5b1b-4599-b41b-6ca16a9f7c4d')
        
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
        self.vs[0]["GUID__"] = UUID('e66f4130-a616-4c9a-a08c-32137ea4a52b')
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
        self.vs[1]["GUID__"] = UUID('e0ec3534-e467-496f-a5c7-1023c04ec463')
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
        self.vs[2]["GUID__"] = UUID('aec0dc7e-0207-4a7c-a0a0-adb3b2de6400')
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
        self.vs[3]["GUID__"] = UUID('bc7c2d97-b5f3-48ce-a21b-3982e876337f')
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
        self.vs[4]["GUID__"] = UUID('2ee07d48-dc09-4abf-a7cf-bcea305e00dd')
        self.vs[5]["Name"] = """Subsystem2"""
        self.vs[5]["BackgroundColor"] = """lightBlue"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F270
aF134
aF370
aF176
a.""")
        self.vs[5]["GUID__"] = UUID('ed857d05-2ca6-477a-9ec1-d1935cc3f228')
        self.vs[6]["Name"] = """Flatten2"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('4299ec44-479a-4514-9692-0bb8bd079cb4')
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
        self.vs[7]["GUID__"] = UUID('5f6adfa9-ea76-43bb-8d59-cd5313f25034')
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
        self.vs[8]["GUID__"] = UUID('5b428125-cec1-47e1-a091-a725faa19f13')
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
        self.vs[9]["GUID__"] = UUID('9e07c75e-243b-4b61-916b-a0e43c0310a4')
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
        self.vs[10]["GUID__"] = UUID('b3c8584e-420b-47c4-abed-526904e354ec')
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
        self.vs[11]["GUID__"] = UUID('5fbc59b8-4d91-45d4-ba57-20a72962b148')
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
        self.vs[12]["GUID__"] = UUID('6b3718d1-f1f6-4bd5-be91-b3d16cad2b77')
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
        self.vs[13]["GUID__"] = UUID('bce4465c-535c-45b7-80dd-031e89898937')
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
        self.vs[14]["GUID__"] = UUID('8c7b0145-c382-4a70-a2ac-beee517cca33')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('dfe1c79b-f65b-4875-af09-f752971691e2')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('c08562f2-7286-495e-aaae-f59bc6c4bbc6')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('a5a09cd4-b287-4679-ad7d-462aa1768f00')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('20f4fd38-bb21-41a3-bcc6-7579da8ed2f8')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('d75be72b-cc68-49f8-a83c-c4a9f2fcae0f')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('c959d139-6822-490a-beb9-f4ebedc837e8')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('9a5464dc-942b-499c-b22f-8042b67127ed')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('0b560826-94a3-49cb-9049-a0139328e57a')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('302581b2-9a84-43a6-8b53-10ec5b1769fd')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('8cbdad93-683d-4256-971e-dc10fbc55b53')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('fc8a57ba-3043-43d0-90cf-ed41cf787b66')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('ee04bcf3-0d11-44be-9140-4933264d6795')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('a5028835-6125-4c1e-8f5f-c1608591fc11')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('a755d613-a600-4ec6-9071-ad6b05e018a8')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('f65f07e5-305e-468f-81d2-9a8d7ce8d31d')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('772e0649-4c6e-4011-ad3e-7f11081c769a')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('7e4fa54d-10fd-40fd-80e4-8efed7df29ce')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('9918a81b-14cd-4d5b-9e2e-d881fcf41c60')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('3694ab46-1f4d-41d4-a7fe-24a852538604')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('dec00dc0-15ad-43d1-a145-c31c10437aa3')
        self.vs[35]["mm__"] = """__Block_Outport__"""
        self.vs[35]["GUID__"] = UUID('0961557b-fdf0-4fbc-90a3-0f4ee74c42a4')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('c50e1e95-b91d-4a4a-8757-772a24096265')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('2a2a68f4-b190-48c3-ba1c-eac9df279bfe')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('393ac815-dc86-400d-8ee9-f0e6df0a58c4')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('efcdf885-616d-4354-9fcf-170f553edbb2')
        self.vs[40]["Name"] = """2"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('be911256-38ba-4c80-b849-edb7c2c8f9ec')
        self.vs[41]["Name"] = """1"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('d7e8ed35-e511-47a3-a784-33ab5164916d')
        self.vs[42]["Name"] = """2"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('98751f1d-e444-4c2c-8aa9-492ef03fb51c')
        self.vs[43]["Name"] = """1"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('0cab1f81-f5a7-45bb-888e-960d5254f7ab')
        self.vs[44]["Name"] = """2"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('7dfed1a6-173b-4033-a75f-83d85cfd0e32')
        self.vs[45]["Name"] = """1"""
        self.vs[45]["mm__"] = """Port_Input"""
        self.vs[45]["GUID__"] = UUID('f12f292b-531b-46c7-b1be-932705321110')
        self.vs[46]["Name"] = """1"""
        self.vs[46]["mm__"] = """Port_Input"""
        self.vs[46]["GUID__"] = UUID('74754d6f-449c-41ff-8991-503d594c953f')
        self.vs[47]["Name"] = """1"""
        self.vs[47]["mm__"] = """Port_Input"""
        self.vs[47]["GUID__"] = UUID('0127a3b8-8c46-48c8-9d6a-86bfc8533da1')
        self.vs[48]["Name"] = """2"""
        self.vs[48]["mm__"] = """Port_Input"""
        self.vs[48]["GUID__"] = UUID('439ae60d-c2f1-4534-9424-d85970a6b967')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('9954a2df-2ef8-414f-99d3-8cb18e4bf273')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('ef4d7ced-bbd4-4c5a-a950-11c4d701d214')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('47311cb2-d378-44d6-b8e4-5c951119671a')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('742188df-2eca-436d-909f-dcf3b7fe8af5')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('ec50eaec-96ef-4798-88c9-1440d8531a00')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('0407ca2f-2a8c-4b76-abab-98f3beae24d2')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('8b94f802-259e-4543-bb33-3a1d10ae9d03')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('d8f9804d-d94d-4d19-8b8b-7e9dc11677ee')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('2fd31a24-640e-48d6-bc5a-658251762555')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('063267cd-b537-4f15-a409-875ca85aa7d8')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('9c0c9b1d-82f5-4b76-9664-6df3f2137be9')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('4037ae8a-2f53-4c61-bd4d-528067c67636')
        self.vs[61]["mm__"] = """__Relation__"""
        self.vs[61]["GUID__"] = UUID('bca76677-6dc6-4639-b5cc-d4fbf04ef0f8')
        self.vs[62]["mm__"] = """__Relation__"""
        self.vs[62]["GUID__"] = UUID('23f18d59-d87b-40bd-936e-24e236663454')
        self.vs[63]["mm__"] = """__Relation__"""
        self.vs[63]["GUID__"] = UUID('dd0c12d4-cae2-4260-ae70-7d936f217b54')
        self.vs[64]["mm__"] = """__Relation__"""
        self.vs[64]["GUID__"] = UUID('aa503433-e89a-4dd3-928e-7086837fa570')
        self.vs[65]["mm__"] = """__Relation__"""
        self.vs[65]["GUID__"] = UUID('45c1f8fc-e4e2-4120-885b-7bcdd7c47bf2')
        self.vs[66]["mm__"] = """__Relation__"""
        self.vs[66]["GUID__"] = UUID('ac57d672-dfa3-48b7-ac41-55c9c4b3887d')
        self.vs[67]["mm__"] = """__Relation__"""
        self.vs[67]["GUID__"] = UUID('d433e145-85d9-4d0e-a2a7-701a05458ef9')
        self.vs[68]["mm__"] = """__Relation__"""
        self.vs[68]["GUID__"] = UUID('9353c3ee-ce47-4dad-ab3d-b612895e5c93')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('050500dd-3476-432e-9ab2-743f18320ef4')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('d13d9d2d-f182-4a73-aa7d-e9087d159e94')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('9e680488-b6b7-4085-990b-a57d94953615')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('51b88a99-c05e-479a-bf9b-f32be8149eec')
        self.vs[73]["Name"] = """None"""
        self.vs[73]["mm__"] = """__Contains__"""
        self.vs[73]["GUID__"] = UUID('90ec6c73-4949-45f4-bb47-ae2fe49e264b')
        self.vs[74]["Name"] = """None"""
        self.vs[74]["mm__"] = """__Contains__"""
        self.vs[74]["GUID__"] = UUID('6c9d4b61-20c6-4a95-b057-16fd3e94b459')
        self.vs[75]["Name"] = """None"""
        self.vs[75]["mm__"] = """__Contains__"""
        self.vs[75]["GUID__"] = UUID('d4f87bc8-3d57-4c45-bc74-5a25604e9037')
        self.vs[76]["Name"] = """None"""
        self.vs[76]["mm__"] = """__Contains__"""
        self.vs[76]["GUID__"] = UUID('95c54ba6-ca09-4a37-a748-476f8de08a39')
        self.vs[77]["Name"] = """None"""
        self.vs[77]["mm__"] = """__Contains__"""
        self.vs[77]["GUID__"] = UUID('0ae3a9ee-5847-42c8-bcf9-8e3cd02c9143')
        self.vs[78]["Name"] = """None"""
        self.vs[78]["mm__"] = """__Contains__"""
        self.vs[78]["GUID__"] = UUID('c41a916f-bfcc-4223-995b-2c4e5821d816')
        self.vs[79]["Name"] = """None"""
        self.vs[79]["mm__"] = """__Contains__"""
        self.vs[79]["GUID__"] = UUID('cebcfc6e-cf11-4729-a129-6fb672a5cd7c')
        self.vs[80]["Name"] = """None"""
        self.vs[80]["mm__"] = """__Contains__"""
        self.vs[80]["GUID__"] = UUID('651eeed4-03b8-4277-a76d-e873335abbb0')
        self.vs[81]["Name"] = """None"""
        self.vs[81]["mm__"] = """__Contains__"""
        self.vs[81]["GUID__"] = UUID('34d8a862-8253-4302-9a0e-419376943372')
        self.vs[82]["Name"] = """None"""
        self.vs[82]["mm__"] = """__Contains__"""
        self.vs[82]["GUID__"] = UUID('fe4b4b35-9f3b-40f4-a4b9-9b2b063b3545')
        self.vs[83]["Name"] = """None"""
        self.vs[83]["mm__"] = """__Contains__"""
        self.vs[83]["GUID__"] = UUID('08c0868f-2208-4125-8214-96b650334aed')
        self.vs[84]["Name"] = """None"""
        self.vs[84]["mm__"] = """__Contains__"""
        self.vs[84]["GUID__"] = UUID('e91103bd-69bd-4534-a8a0-1ff236c02e97')
        self.vs[85]["Name"] = """None"""
        self.vs[85]["mm__"] = """__Contains__"""
        self.vs[85]["GUID__"] = UUID('4b4ca875-6182-4cda-8517-1a7cdc66225c')
        self.vs[86]["Name"] = """None"""
        self.vs[86]["mm__"] = """__Contains__"""
        self.vs[86]["GUID__"] = UUID('253899b0-4fdf-4728-9f8a-035b62ecf4c7')

