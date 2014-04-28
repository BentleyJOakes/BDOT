

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConstDead(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConstDead.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConstDead, self).__init__(name='HSimpleConstDead', num_nodes=38, edges=[])
        
        # Add the edges
        self.add_edges([(0, 17), (17, 7), (1, 18), (18, 8), (1, 19), (19, 9), (1, 20), (20, 10), (2, 21), (21, 11), (2, 22), (22, 12), (2, 23), (23, 13), (3, 24), (24, 14), (5, 25), (25, 15), (6, 26), (26, 16), (4, 32), (32, 0), (4, 33), (33, 1), (4, 34), (34, 2), (4, 35), (35, 3), (4, 36), (36, 5), (4, 37), (37, 6), (16, 27), (27, 8), (16, 28), (28, 11), (10, 29), (29, 7), (14, 30), (30, 9), (15, 31), (31, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConstDead"""
        self["GUID__"] = UUID('26db28b4-9609-4f7a-b31f-45a5762ff43b')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F390
aF118
aF420
aF132
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('ff5dc90a-85c4-42c0-885e-89bead892ce8')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F305
aF132
aF335
aF163
a.""")
        self.vs[1]["GUID__"] = UUID('35ef53b4-67b5-4075-ab37-553bf7a46986')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F140
aF120
aF160
aF140
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('f6bd25c0-2ebd-4e65-a2b4-1415bde37e82')
        self.vs[3]["Name"] = """In1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Inport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F170
aF178
aF200
aF192
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('d88e363c-661f-400f-8330-9f789d3a3249')
        self.vs[4]["Name"] = """HSimpleConstDead"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('77a5272c-ba78-4429-b382-8e9b29b6aba8')
        self.vs[5]["Name"] = """Constant1"""
        self.vs[5]["SampleTime"] = inf
        self.vs[5]["value"] = 112.32
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F85
aF168
aF135
aF202
a.""")
        self.vs[5]["GUID__"] = UUID('b3eabcc0-9703-4d0d-873a-6287135263ab')
        self.vs[6]["Name"] = """Constant2"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 433.22
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F50
aF82
aF105
aF118
a.""")
        self.vs[6]["GUID__"] = UUID('ca4e153b-1cb3-4826-a623-530d91f7f741')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('2a53c523-a205-49b6-92a4-1c48f1bd9a12')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('525f5e0b-0919-4c2a-a64d-5724eb1d6c34')
        self.vs[9]["Name"] = """2"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('9060a2be-4cbf-4a12-857d-a25f8096cfaf')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('5e02c605-e8e2-4418-8614-e986fdcd850a')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('122a7d6d-4839-4d0e-86bb-da6c82e24690')
        self.vs[12]["Name"] = """2"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('4b3cf0c1-708c-4bb2-82d9-7a13ceb06ebd')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('ab4c724f-d2d8-4b30-8ae5-9669777bd40c')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('f010c3b2-36fa-47a0-a6a2-6d84938dabbc')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('8ed99bbb-75d7-4d94-9e33-e9fd3f6e4fbc')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('f183df0d-348b-484d-95f6-25c0e4fd4284')
        self.vs[17]["mm__"] = """__Block_Inport__"""
        self.vs[17]["GUID__"] = UUID('c47660a4-66b4-4539-8a9d-2a0f3a37b5a5')
        self.vs[18]["mm__"] = """__Block_Inport__"""
        self.vs[18]["GUID__"] = UUID('bd640486-ba66-4546-a9cf-7c51fa06a760')
        self.vs[19]["mm__"] = """__Block_Inport__"""
        self.vs[19]["GUID__"] = UUID('915515dd-12c0-4220-8406-be6ec15deb36')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('4e9ddb9e-8e56-424c-8968-9f3c1f783d8a')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('89e83d87-de41-46e1-9743-107b7faa0232')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('f45bd440-e2af-4269-8e23-52218add23ad')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('305ab234-9491-4f38-8b5a-cb82b537ac73')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('b1dc9692-80e0-4ddc-a8e6-32a13dd92e1d')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('586828dd-4dc2-40ed-83b8-f4094feb3a0f')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('d5c058fe-5552-44b9-b9cb-b27211f07a3c')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('af3f6be8-d954-4a9a-95fc-77bde4a90e3d')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('e0ab5b2f-7788-4d6b-81d8-9764dec7a0a8')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('ec1245ac-8968-4804-b552-e0849f121ab0')
        self.vs[30]["mm__"] = """__Relation__"""
        self.vs[30]["GUID__"] = UUID('e6d03147-e3dd-429e-916e-8c564c0b1161')
        self.vs[31]["mm__"] = """__Relation__"""
        self.vs[31]["GUID__"] = UUID('d745098a-9ff5-4599-a3d5-948897a32e50')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('a9848841-1949-45d4-9155-d441a6786605')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('807ac6fb-3c83-47d1-a51d-3414e558966c')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('45411494-f378-488b-b6cc-34f2690a3790')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('ef3ee2b2-d0c8-465b-99ac-95fd15e2cd3f')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('6856aa90-9128-4a5c-b04a-7acdaf19ec14')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('d6b61651-9b38-4c6e-afec-fcef485ff73c')

