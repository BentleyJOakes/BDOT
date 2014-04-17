

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HEasy(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HEasy.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEasy, self).__init__(name='HEasy', num_nodes=36, edges=[])
        
        # Add the edges
        self.add_edges([(0, 20), (20, 15), (0, 21), (21, 16), (0, 11), (11, 7), (3, 22), (22, 17), (4, 12), (12, 8), (1, 23), (23, 18), (1, 13), (13, 9), (5, 24), (24, 19), (6, 14), (14, 10), (2, 30), (30, 0), (2, 31), (31, 3), (2, 32), (32, 4), (2, 33), (33, 1), (2, 34), (34, 5), (2, 35), (35, 6), (10, 25), (25, 16), (10, 26), (26, 18), (9, 27), (27, 17), (8, 28), (28, 15), (7, 29), (29, 19)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HEasy"""
        self["GUID__"] = UUID('f48f06e4-92e4-4da6-96be-e7222537acf0')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Product"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["mm__"] = """Product"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F240
aF82
aF270
aF113
a.""")
        self.vs[0]["GUID__"] = UUID('5e12b1d6-1406-4661-a9cb-84c1e3a80f15')
        self.vs[1]["Name"] = """Gain"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["gain"] = 1.0
        self.vs[1]["BackgroundColor"] = """yellow"""
        self.vs[1]["mm__"] = """Gain"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F250
aF185
aF280
aF215
a.""")
        self.vs[1]["GUID__"] = UUID('6b6934b2-c1d5-4b6a-b58f-6cc28e592416')
        self.vs[2]["Name"] = """HEasy"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('af47307a-d75d-4fae-b581-7e66b436b207')
        self.vs[3]["NumInputPorts"] = """1"""
        self.vs[3]["Name"] = """Scope1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Scope"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F345
aF184
aF375
aF216
a.""")
        self.vs[3]["LimitDataPoints"] = """on"""
        self.vs[3]["GUID__"] = UUID('14bb463a-706d-4bf2-9cfd-d26972af52ff')
        self.vs[4]["Name"] = """Constant"""
        self.vs[4]["SampleTime"] = inf
        self.vs[4]["value"] = 1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F155
aF75
aF185
aF105
a.""")
        self.vs[4]["GUID__"] = UUID('d41f64e6-0a96-4ca9-8854-c6184b39ec76')
        self.vs[5]["NumInputPorts"] = """1"""
        self.vs[5]["Name"] = """Scope"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Scope"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F345
aF79
aF375
aF111
a.""")
        self.vs[5]["LimitDataPoints"] = """on"""
        self.vs[5]["GUID__"] = UUID('03b7a056-5de8-404b-adb7-e11843012767')
        self.vs[6]["Name"] = """Constant1"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F150
aF125
aF180
aF155
a.""")
        self.vs[6]["GUID__"] = UUID('4c02be1c-ed70-4e4c-9ae4-ad1cabc8cf64')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Output"""
        self.vs[7]["GUID__"] = UUID('7bca7b54-21d3-424a-b3a7-ef59458128ef')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('232f3e22-e806-43a1-8af9-c70915fbdb69')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('3e6aa32a-a783-42f2-9663-adaac073ba51')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('4354fc91-967b-498d-8314-635d2250b637')
        self.vs[11]["mm__"] = """__Block_Outport__"""
        self.vs[11]["GUID__"] = UUID('40de2608-4541-4ac0-82b9-36d2a3d86e71')
        self.vs[12]["mm__"] = """__Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('05725242-941d-438d-ad8b-43910c18b852')
        self.vs[13]["mm__"] = """__Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('e4853fde-dc70-42df-8da2-3abf5e57100b')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('8b539a6e-d506-434e-8c46-67e1639f7642')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('e00119fb-8750-4722-803e-24386ecb023b')
        self.vs[16]["Name"] = """2"""
        self.vs[16]["mm__"] = """Port_Input"""
        self.vs[16]["GUID__"] = UUID('56a1d5ed-63f3-49be-936f-33387ffcde22')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('93a7e0f5-5729-4e62-86b0-7ca9d14274b9')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('57d42849-c483-42fc-863b-575e40ba6bf0')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('403eddc6-feac-4098-be2c-2f0dab4b0d04')
        self.vs[20]["mm__"] = """__Block_Inport__"""
        self.vs[20]["GUID__"] = UUID('222211c2-3598-42fc-8f68-4f736a8e4527')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('cd1e1857-8868-4d8c-badc-06994d46c5e9')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('b5a67d96-7fbb-4458-9d15-ffa98a602aaa')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('9b1d8456-598b-4576-8ddf-622dce104f19')
        self.vs[24]["mm__"] = """__Block_Inport__"""
        self.vs[24]["GUID__"] = UUID('5e88e06a-cc1f-4d20-8a10-d8664b418ddf')
        self.vs[25]["mm__"] = """__Relation__"""
        self.vs[25]["GUID__"] = UUID('002cfe86-b168-4fd6-bbb8-092ef5c4a853')
        self.vs[26]["mm__"] = """__Relation__"""
        self.vs[26]["GUID__"] = UUID('3c631b45-71b6-44ab-80bf-5cce289befaf')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('6860bacf-07d5-43ad-9184-7883490d769c')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('064400e8-1b0a-4787-a99a-2c67c3479e24')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('7eafa0df-8625-4645-b691-f84e6097ddcc')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('7ed32821-ae39-4ef6-921f-2fff3c51ee13')
        self.vs[31]["Name"] = """None"""
        self.vs[31]["mm__"] = """__Contains__"""
        self.vs[31]["GUID__"] = UUID('6a1857c6-8c14-403e-a850-f32a2dd704c8')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('82feb148-f7d5-4ef3-8e71-53b1036eead5')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('058d9e20-49c2-4cd0-b4ce-588146ed60b2')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('d630e07b-c2c0-4511-96f6-ddaffd21fd02')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('d01a89b3-9c6d-4139-a07a-1f78665d05ed')

