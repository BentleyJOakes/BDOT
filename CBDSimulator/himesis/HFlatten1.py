

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
        self["GUID__"] = UUID('8850d187-68f2-404b-9775-515bff1ed390')
        
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
        self.vs[0]["GUID__"] = UUID('0e5c6383-640e-414c-8238-867daae24d2b')
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
        self.vs[1]["GUID__"] = UUID('62673113-01ae-4546-9656-67f4ac0dcde4')
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
        self.vs[2]["GUID__"] = UUID('0645741f-3753-4732-8763-8e5c51d62461')
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
        self.vs[3]["GUID__"] = UUID('303f736c-2250-4700-b92d-f639a8275b5e')
        self.vs[4]["Name"] = """Constant2"""
        self.vs[4]["SampleTime"] = inf
        self.vs[4]["value"] = 1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F125
aF235
aF155
aF265
a.""")
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('b9cc485a-5243-44e8-b9f4-b09722687d70')
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
        self.vs[5]["GUID__"] = UUID('7c975243-14b8-48b0-9b4e-98090c9af01b')
        self.vs[6]["Name"] = """Product2"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F215
aF167
aF245
aF198
a.""")
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["GUID__"] = UUID('6666b5e1-2c45-4945-904f-eb86b724a5b7')
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
        self.vs[7]["GUID__"] = UUID('2143f1ce-d178-4eca-b5cd-75eb457b959d')
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
        self.vs[8]["GUID__"] = UUID('c6e8c080-ef1d-4f79-9ee9-4039e71664ac')
        self.vs[9]["Name"] = """Flatten1"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[9]["mm__"] = """SubSystem"""
        self.vs[9]["GUID__"] = UUID('20ce1f83-bb53-4766-9cde-5a45bc3f8159')
        self.vs[10]["Name"] = """In2"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F115
aF178
aF145
aF192
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 2
        self.vs[10]["GUID__"] = UUID('829b2b4a-db8e-45d4-ada4-c861e0f35e4c')
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
        self.vs[11]["GUID__"] = UUID('8118bebf-40ee-47b6-b3d6-7ecdfae55d3c')
        self.vs[12]["Name"] = """In1"""
        self.vs[12]["BackgroundColor"] = """white"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[12]["mm__"] = """Inport"""
        self.vs[12]["Port"] = 1
        self.vs[12]["GUID__"] = UUID('cac0902b-207d-4823-85bd-9fc2af3dbb61')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('bbaed65e-5d4f-4ce3-a059-096e610c174d')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('38fd25ad-3f06-47c5-b531-cc3bac159908')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('17cb11e9-d7e7-4ff3-a089-b79429e3e09b')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('f806e731-c5a0-4e3e-982c-22e08f52f780')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('bff3b08d-db51-4157-8a22-90bef311a4ef')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('3cdd1ddf-735e-4eaa-a24f-803a177ef6d2')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('e646bd02-3c50-47bd-afbc-e7b9d617e9f8')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('a6e12739-f0bb-44e1-baa6-15c62ece7312')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('e928460d-2bc8-4b24-a46f-cd8c2f1d98e8')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('5a6f333a-1449-45a4-b5e6-0e0573e2d93f')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('07547c9f-bc10-4070-8cda-3e12a2c83369')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('e8adc2a1-ba54-45a0-b7de-80b72f28b781')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('3b937d04-37ba-4a3f-98c1-1be60f4466f8')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('04a32a52-4921-4bcd-a14f-a2e881dc2cf9')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('dc155917-8233-423c-b48c-32e873943f37')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('cc77e3b3-ff59-477d-b825-99c9f2589f88')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('db0a28e7-790a-4b53-8061-f671500723c4')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('30d21ef0-8cab-41be-8d5e-4a1088c9e9cd')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('5f5f9efd-ef55-4421-a1ab-48d5aaf08f27')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('e7dd88c1-667c-4be8-9457-4b627e4431f8')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('5b2211d0-777e-4166-8048-5c969b0bbdc3')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('a9ceee67-bd67-4a04-a2e3-6c3aa2c58852')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('7477e35f-bc82-4be1-be13-ba94677d8ada')
        self.vs[36]["Name"] = """1"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('cac392f3-8ee8-4ad0-9a35-0384a8ca8b34')
        self.vs[37]["Name"] = """2"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('d11a0d00-10a3-482b-aab9-6ee617def8e3')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('ed93a25a-6513-4bde-83ea-8ea152c88981')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('d4bc3812-10cf-4b54-aa61-94fbe2a1c505')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('b738d3c0-016e-4bcd-a2ac-a34dba483fed')
        self.vs[41]["Name"] = """2"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('259f51d6-8ed7-4383-a21a-c9403d5423f6')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('9e3caa3c-90ee-4400-b3d0-95fac58fe28d')
        self.vs[43]["Name"] = """1"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('c3ec19f2-61fd-46c8-ba4b-df84f6164ebf')
        self.vs[44]["Name"] = """2"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('6190dfa0-5e49-4853-bee2-06af9b6879b0')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('74844e16-ed30-44ee-906f-65d79c14afd7')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('db743ccb-8dd6-4786-b992-8cdd93f11392')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('8522e072-4001-454d-9a52-a1b708e4c621')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('6ce0c879-2767-461e-b8c3-a458edf3ad7c')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('9a916a07-ea85-4292-ab90-d93ca0930634')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('ad80d3c1-113d-423b-b510-8a189f1e95c4')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('fef9ffff-e8e0-4f3d-8475-744400061eca')
        self.vs[52]["Name"] = """None"""
        self.vs[52]["mm__"] = """__Contains__"""
        self.vs[52]["GUID__"] = UUID('df3b37b5-70e3-4043-993a-6d7c335cc1ec')
        self.vs[53]["Name"] = """None"""
        self.vs[53]["mm__"] = """__Contains__"""
        self.vs[53]["GUID__"] = UUID('539c966c-e670-4d9e-8171-207d4429cf82')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('2334c07f-d5ff-40c8-b6c6-78c8a741a28a')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('3166d365-aa0b-4462-876d-6845f34322fb')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('9849fb78-e7e0-45a1-b743-bd00e8219fd2')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('bd4153a1-c1b6-4864-abf9-cab4b9913060')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('e124ea47-70de-4e9e-a567-468164e735c2')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('74b8bc38-17a5-4fe5-a42f-ddd3e7491153')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('d64d3be7-2401-4d7b-9885-384dff0158b8')
        self.vs[61]["mm__"] = """__Block_Inport__"""
        self.vs[61]["GUID__"] = UUID('0de6a043-d9d5-461a-8517-639ac89b515b')
        self.vs[62]["mm__"] = """__Block_Inport__"""
        self.vs[62]["GUID__"] = UUID('c2119a9c-6fb4-47f5-ba8b-ed5d67189f81')
        self.vs[63]["mm__"] = """__Block_Inport__"""
        self.vs[63]["GUID__"] = UUID('2b99bc0d-629d-4b03-9f8b-f120fee714e8')
        self.vs[64]["mm__"] = """__Block_Inport__"""
        self.vs[64]["GUID__"] = UUID('5c63f8ac-fffb-4cb2-98d9-4e0ef8dec047')
        self.vs[65]["mm__"] = """__Block_Inport__"""
        self.vs[65]["GUID__"] = UUID('4d16e3de-7750-4526-a1c8-5a83be421342')
        self.vs[66]["mm__"] = """__Block_Inport__"""
        self.vs[66]["GUID__"] = UUID('a67f726f-515f-491f-8926-38036d74614f')
        self.vs[67]["mm__"] = """__Block_Inport__"""
        self.vs[67]["GUID__"] = UUID('5546c266-4e98-48e3-b92b-66daec05dcda')
        self.vs[68]["mm__"] = """__Block_Inport__"""
        self.vs[68]["GUID__"] = UUID('034b1652-9310-4b02-a945-6c8c2a2fdcf1')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('014610d3-8148-4dbd-94e4-67c834f72ba5')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('8507ce47-0ef4-44f9-b78a-d7fe57e4eb1b')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('4ce6e7ff-014a-4832-aa97-ff37a6c2d4fe')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('f20d0f2d-e2c6-4a9f-8992-946c86b4aebb')
        self.vs[73]["mm__"] = """__Relation__"""
        self.vs[73]["GUID__"] = UUID('74498479-962a-4810-9089-773b692ad1e0')
        self.vs[74]["mm__"] = """__Relation__"""
        self.vs[74]["GUID__"] = UUID('64231a97-f537-4311-8a65-43721a9012b7')
        self.vs[75]["mm__"] = """__Relation__"""
        self.vs[75]["GUID__"] = UUID('17a6deed-565b-4314-b704-010be79336a3')
        self.vs[76]["mm__"] = """__Relation__"""
        self.vs[76]["GUID__"] = UUID('2073bf87-65ec-4aa3-aea8-324cc66b0611')
        self.vs[77]["mm__"] = """__Relation__"""
        self.vs[77]["GUID__"] = UUID('b7847742-324e-493d-807b-29fb817524d4')
        self.vs[78]["mm__"] = """__Relation__"""
        self.vs[78]["GUID__"] = UUID('1fd5fdca-f2b1-4178-a3df-17b0046787fa')
        self.vs[79]["mm__"] = """__Relation__"""
        self.vs[79]["GUID__"] = UUID('488f78cc-b72e-48d2-91a8-e0cc2a9eca85')
        self.vs[80]["mm__"] = """__Relation__"""
        self.vs[80]["GUID__"] = UUID('10cdb8c5-491d-41ec-afb5-634a858899b8')

