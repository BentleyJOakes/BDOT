

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattening(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattening.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattening, self).__init__(name='HFlattening', num_nodes=74, edges=[])
        
        # Add the edges
        self.add_edges([(3, 52), (52, 30), (3, 53), (53, 31), (3, 21), (21, 12), (4, 54), (54, 32), (5, 55), (55, 33), (5, 56), (56, 34), (5, 22), (22, 13), (0, 23), (23, 14), (6, 57), (57, 35), (6, 58), (58, 36), (6, 24), (24, 15), (1, 59), (59, 37), (1, 60), (60, 38), (1, 25), (25, 16), (2, 61), (61, 39), (2, 26), (26, 17), (9, 27), (27, 18), (10, 28), (28, 19), (11, 29), (29, 20), (7, 62), (62, 40), (3, 41), (41, 6), (3, 42), (42, 1), (3, 43), (43, 2), (3, 44), (44, 9), (3, 45), (45, 11), (3, 46), (46, 7), (8, 47), (47, 3), (8, 48), (48, 4), (8, 49), (49, 5), (8, 50), (50, 0), (8, 51), (51, 10), (20, 63), (63, 35), (18, 64), (64, 36), (17, 65), (65, 38), (17, 66), (66, 40), (16, 67), (67, 39), (15, 68), (68, 37), (13, 69), (69, 31), (19, 70), (70, 30), (19, 71), (71, 33), (14, 72), (72, 34), (12, 73), (73, 32)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlattening"""
        self["GUID__"] = UUID('999f523a-046f-4e7c-8387-2e2305e655ca')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F40
aF105
aF70
aF135
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('70298ad2-df42-4616-a4b1-196ea2ff03ac')
        self.vs[1]["Inputs"] = """|++"""
        self.vs[1]["Name"] = """Sum"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[1]["mm__"] = """Sum"""
        self.vs[1]["IconShape"] = """round"""
        self.vs[1]["GUID__"] = UUID('5e7c5fee-f02a-414c-862e-602fb5334223')
        self.vs[2]["InitialCondition"] = 0.0
        self.vs[2]["Name"] = """Unit Delay"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[2]["mm__"] = """UnitDelay"""
        self.vs[2]["GUID__"] = UUID('fa1531ea-5959-46a6-831b-5ebe76f1d98a')
        self.vs[3]["Name"] = """Subsystem"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["GUID__"] = UUID('b83b9fcf-7c4e-4c45-8c14-ec0d9d780eb1')
        self.vs[4]["Name"] = """Out1"""
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[4]["mm__"] = """Outport"""
        self.vs[4]["Port"] = 1
        self.vs[4]["GUID__"] = UUID('7e5d4e8b-f503-4036-baa9-ad764c62694d')
        self.vs[5]["Name"] = """Product"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F170
aF67
aF200
aF98
a.""")
        self.vs[5]["mm__"] = """Product"""
        self.vs[5]["GUID__"] = UUID('cfe6b9e8-ec24-4522-a2c3-00c98dbd5694')
        self.vs[6]["Name"] = """Product"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["GUID__"] = UUID('ac140c1a-0b78-417c-a719-ea429de8b8ec')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F365
aF103
aF395
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('53a6ebe4-a5e9-4752-994a-b790b3643030')
        self.vs[8]["Name"] = """HFlattening"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('99fb0669-e117-4e56-a6bb-6abf15a8af9b')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F150
aF118
aF180
aF132
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('76aa9a14-cda4-4540-8fb6-aebb70c6df1e')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F60
aF48
aF90
aF62
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('d09d6dc0-ce9b-4193-8f34-109c421943c3')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F150
aF88
aF180
aF102
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('36c46f61-31c6-40aa-91a6-f71eee0c0744')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('d577f228-861e-4c75-8f3d-325029053679')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('fe2b98d6-bb5c-4426-a9ce-cc6a896835c9')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('4e4754e9-704b-4c3d-b384-20c1c05fb271')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('0beea150-1852-4fd1-9e0c-0210ec508436')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('3d7e9039-6f11-4641-9c58-7ca2ee8e9bb5')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('9c4ed8ff-113d-4f4b-93af-fe60cacec664')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('de0c2ec6-8cc3-430a-8891-2d0ac65b2280')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('27374c90-a54d-467c-a763-58fd5d10a27a')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('697e1052-8833-4f18-8eda-c0b9bb11076e')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('646b14c2-6447-4a15-84ec-27c6e1a7675e')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('9033fa6c-c7b8-46d5-bf53-459df1dc3963')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('278aeff7-d35f-4437-9a22-6ff9a73012ac')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('ec0420eb-9b21-4227-abdd-d50d9f6765c1')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('ac5e8f4d-cf19-41d0-9685-b586b0684c79')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('8d69fb49-58b5-4c9d-930c-4facebc2a98d')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('c376473d-8434-4b1b-9102-f4c4de648ea4')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('b593d591-1ac0-4449-8128-c55eed62c46f')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('12fbb88e-d30f-4f42-a613-7a091fa5d9db')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('33135fbf-ae52-4dbd-8967-206140416f2c')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('1089c161-a5ce-4946-8465-05641a7009e0')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('f3fdb50c-8573-48a4-bff9-3cdce44fdc08')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('83319725-508a-4e0c-92e4-27340d358cb0')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('b6c9af53-4d13-471d-a158-3527669f5546')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('1fa0ed57-8cfe-4ef7-808c-5ece9f7e23d9')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('a2e5ebc0-d389-4e26-8d63-571ef86a3d0d')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('9cff9c8d-cb04-4681-ae1e-67e23fbf52ec')
        self.vs[38]["Name"] = """2"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('e27535c1-6587-4aaa-a71f-3845dd3ea166')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('f55cf437-0ec7-4406-a557-f79fe8b9e4fe')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('fd7f015f-0183-4e41-9f3e-fae469977740')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('26970a55-753f-4803-bb7f-abe232d7fbc1')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('1c96811e-0697-4204-b784-424f6763563a')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('9fe796ee-3838-4d3c-aceb-7536e61f7373')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('4223cb62-c79d-4c18-9ced-0f2dbfef6008')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('60a6546c-f769-4c26-a086-3b3f7434178f')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('eac4197d-a017-4b63-b926-95121c121699')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('b0686182-1f61-4505-bea6-3a29f59d41f2')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('3693dea0-d23d-4741-965f-9d914a801996')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('3394313c-0a50-42b0-a8f9-ec1ae21cade2')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('9b4dda22-cc6b-4d98-83e5-33d52f16505a')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('dc25760a-1d8e-42b2-b40f-932065e851bd')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('a2a152b6-d5d3-493e-9003-d87af5937649')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('4460fd10-5377-4424-b1c5-51c97ed91463')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('0bb82427-7e02-4e7a-b13f-d6ea6b725535')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('c0ad343f-c0a0-4df3-9a64-60f69a49b091')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('bbbceb8e-15e1-456b-a05a-dd03eec45bc5')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('3e8d8fa8-b3d4-427d-80ea-46ad7ef799a9')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('83c188fe-b0db-4d25-9ed8-9b331b5c5072')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('a76f981d-67cc-451a-be9c-f8e1abd6a6c1')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('a53a164a-0830-41eb-84cc-07e6f4555fea')
        self.vs[61]["mm__"] = """__Block_Inport__"""
        self.vs[61]["GUID__"] = UUID('574e775f-2b2d-4684-940d-2ef8123fc888')
        self.vs[62]["mm__"] = """__Block_Inport__"""
        self.vs[62]["GUID__"] = UUID('74435913-28d8-4b89-8c1c-613c9fc06b46')
        self.vs[63]["mm__"] = """__Relation__"""
        self.vs[63]["GUID__"] = UUID('a4c7d383-24c0-48c5-a029-3ab0f430d387')
        self.vs[64]["mm__"] = """__Relation__"""
        self.vs[64]["GUID__"] = UUID('f67f2d28-2e43-483e-9d13-1dadf05e2f00')
        self.vs[65]["mm__"] = """__Relation__"""
        self.vs[65]["GUID__"] = UUID('2bc69785-0367-433d-80ad-7115944fc237')
        self.vs[66]["mm__"] = """__Relation__"""
        self.vs[66]["GUID__"] = UUID('0c90b580-bd9d-4ee9-b674-9974a016b8e9')
        self.vs[67]["mm__"] = """__Relation__"""
        self.vs[67]["GUID__"] = UUID('4fc3b28e-6e41-489b-848c-b693be63c88c')
        self.vs[68]["mm__"] = """__Relation__"""
        self.vs[68]["GUID__"] = UUID('355e078f-ddae-4b94-a8cd-857436e92e04')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('1598c021-684c-4882-8170-e9280b66094b')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('01f0a185-2757-42bb-8d9d-edd772d6dcce')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('4b3274f6-ffd7-4e94-bc71-f7a2ce3f00ba')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('c58ac0c4-b890-4a4b-9f05-0c638bbb6835')
        self.vs[73]["mm__"] = """__Relation__"""
        self.vs[73]["GUID__"] = UUID('8da843bf-bb08-4783-b52f-6e43588cb2ba')

