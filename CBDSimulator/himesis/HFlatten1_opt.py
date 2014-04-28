

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten1_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten1_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten1_opt, self).__init__(name='HFlatten1_opt', num_nodes=58, edges=[])
        
        # Add the edges
        self.add_edges([(3, 16), (4, 17), (5, 18), (6, 19), (7, 21), (8, 22), (1, 23), (1, 24), (1, 25), (1, 30), (1, 29), (1, 28), (1, 27), (1, 26), (2, 20), (9, 53), (9, 52), (10, 56), (10, 55), (11, 50), (12, 51), (13, 54), (14, 49), (15, 57), (16, 9), (17, 10), (18, 11), (19, 12), (20, 13), (21, 14), (22, 15), (40, 31), (41, 32), (42, 33), (43, 34), (44, 35), (45, 36), (46, 37), (47, 38), (48, 39), (23, 5), (24, 7), (25, 8), (26, 0), (27, 3), (28, 4), (29, 6), (30, 2), (0, 40), (3, 41), (3, 42), (6, 43), (6, 44), (7, 45), (7, 46), (8, 47), (8, 48), (49, 39), (50, 37), (51, 31), (52, 36), (53, 35), (54, 33), (55, 38), (56, 32), (57, 34)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlatten1_opt"""
        self["GUID__"] = UUID('689971ac-c1c8-4237-989c-dc6223e1dbe2')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F470
aF123
aF500
aF137
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('e035fdf1-1829-4eca-b20f-8f35bdc99201')
        self.vs[1]["Name"] = """Flatten1"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('ecc29dc9-3340-42b4-a957-b8932b2729c4')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F15
aF183
aF45
aF197
a.""")
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('729666d0-5bbb-4341-83cb-e7bbf6efd358')
        self.vs[3]["Name"] = """Product"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Product"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F155
aF147
aF185
aF178
a.""")
        self.vs[3]["GUID__"] = UUID('a4082af0-92f8-49d5-b113-786973c4621c')
        self.vs[4]["Name"] = """Constant"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 12.34
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F25
aF102
aF70
aF138
a.""")
        self.vs[4]["GUID__"] = UUID('17245301-68dd-480c-90fb-62ae38f3cf69')
        self.vs[5]["Name"] = """Constant2"""
        self.vs[5]["SampleTime"] = """inf"""
        self.vs[5]["value"] = 1.0
        self.vs[5]["BackgroundColor"] = """yellow"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F110
aF170
aF140
aF200
a.""")
        self.vs[5]["GUID__"] = UUID('1ba4700c-be4c-45ff-91ab-7930962658d9')
        self.vs[6]["Inputs"] = """|++"""
        self.vs[6]["Name"] = """Sum"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Sum"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F410
aF120
aF430
aF140
a.""")
        self.vs[6]["IconShape"] = """round"""
        self.vs[6]["GUID__"] = UUID('4be000c8-a2ab-41b9-b650-248fd9753a40')
        self.vs[7]["Name"] = """Product2"""
        self.vs[7]["SampleTime"] = -1.0
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["mm__"] = """Product"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F210
aF117
aF240
aF148
a.""")
        self.vs[7]["GUID__"] = UUID('e813af19-0098-47af-b1f7-96f032757c14')
        self.vs[8]["Inputs"] = """++|"""
        self.vs[8]["Name"] = """Sum2"""
        self.vs[8]["SampleTime"] = -1.0
        self.vs[8]["BackgroundColor"] = """yellow"""
        self.vs[8]["mm__"] = """Sum"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F275
aF125
aF295
aF145
a.""")
        self.vs[8]["IconShape"] = """round"""
        self.vs[8]["GUID__"] = UUID('798bc78f-e3cb-4433-b248-3cf98b055dbb')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('5356dd06-4848-4b34-97d7-59055df3965e')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('de60b927-56c7-4e7e-a4ef-43f239d7b441')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('cdb8dc92-3eb7-4965-81b1-9de7d93b057f')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('606a77cb-5c02-4d74-85a2-b812fe61acfb')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('3456d812-8d2e-44f4-99d8-a47e99c78800')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('b620f085-3534-4bf7-b5b6-2ca242253851')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('9c2e5e4e-16d7-4633-a10c-4685a7e3412c')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('147ff0d5-a6db-4dfc-8f5e-6d4e930e7cce')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('f501c4e8-5f33-47ac-9278-1965b43f3a24')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('4490e6ee-a8b2-43e9-be1a-92c5b3f90ae8')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('87d90e1b-1aa9-4f1a-825a-618c911527e1')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('c2c64d80-a194-4691-a869-5f45566c0ffb')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('ce381f93-874a-49d7-bcac-ea44917b7497')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('2d85f7f9-25b2-4011-adcd-5e883ab85dd5')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('f450db1b-5c80-4cbb-af41-1954171b6692')
        self.vs[24]["Name"] = """None"""
        self.vs[24]["mm__"] = """__Contains__"""
        self.vs[24]["GUID__"] = UUID('e496c138-993e-4b25-a178-40ab8f11900f')
        self.vs[25]["Name"] = """None"""
        self.vs[25]["mm__"] = """__Contains__"""
        self.vs[25]["GUID__"] = UUID('69c1a3a6-45da-432e-9883-8fb259a9db42')
        self.vs[26]["Name"] = """None"""
        self.vs[26]["mm__"] = """__Contains__"""
        self.vs[26]["GUID__"] = UUID('55e63940-c4e3-458a-a09f-2a055cd24494')
        self.vs[27]["Name"] = """None"""
        self.vs[27]["mm__"] = """__Contains__"""
        self.vs[27]["GUID__"] = UUID('93099a03-58c1-4e28-a983-5fd99069b2e7')
        self.vs[28]["Name"] = """None"""
        self.vs[28]["mm__"] = """__Contains__"""
        self.vs[28]["GUID__"] = UUID('a0984eef-21bc-4e31-a46a-b7aedc4677af')
        self.vs[29]["Name"] = """None"""
        self.vs[29]["mm__"] = """__Contains__"""
        self.vs[29]["GUID__"] = UUID('7157c7bc-d7e4-4711-8179-25a2ec4259ba')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('76eb0db1-13bc-4491-8f8f-da7810be7e4a')
        self.vs[31]["Name"] = """1"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('29647ee2-6c19-4fd0-b145-900363e5684e')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('2a593fa3-dcee-49e9-b45f-34ba3d3282a4')
        self.vs[33]["Name"] = """2"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('6a9c2bca-d4db-4285-a163-85d78c9a1144')
        self.vs[34]["Name"] = """1"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('6f769b10-3a7a-45dc-aac1-04cc58f60f84')
        self.vs[35]["Name"] = """2"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('ab0aed84-11c9-415e-9c8f-d6bd47c61c24')
        self.vs[36]["Name"] = """1"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('a53227c8-012d-4187-99e9-495b55a99d27')
        self.vs[37]["Name"] = """2"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('db7133ca-1ed5-40d7-bff4-68c382ae461b')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('f51c6973-4015-4d2b-9bd1-6467d61d90f6')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('c0ff0ac6-e8c2-4690-816d-53962bdd3bda')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('5c528c23-1c6b-49f1-b634-e181feb15a57')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('92d8abfa-e821-4cab-b900-819899614888')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('505030bf-94c0-4c05-8cd7-b36054765646')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('a927573b-22a6-494a-b3f1-70bef5bc35e5')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('84e616ee-2f25-4938-8cc9-06620ae9fc88')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('e3377a74-40cc-4cf0-94d5-72b61033ea50')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('095f5b58-9454-4cc7-aa64-0519ca7d6223')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('6894ad17-e574-472a-9457-d2b4354e35c7')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('3cebaccc-a4a4-43cb-b881-185bc428297f')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('90d4f6ee-5834-4b5d-99b6-749926128ef3')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('dcc29043-8c74-441c-9b95-5c098890da01')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('1ecbc834-ad89-46c9-8af8-55e5a6ceb735')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('3c8ee934-589e-4fcc-8145-2cf3b514313e')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('1093e1e7-2747-4b73-b135-cf584c00fc8f')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('03edf849-e0f9-4a80-89a2-b9eb2f1d75b4')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('9251901a-88f9-49e6-b5c4-ec19d4098af6')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('fe3730a1-3ca4-4ff4-b86a-4dc387ae3e50')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('325f6b30-8217-4eff-83cd-cb32cb7a8cfc')

