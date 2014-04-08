

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HDead(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HDead.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDead, self).__init__(name='HDead', num_nodes=36, edges=[])
        
        # Add the edges
        self.add_edges([(0, 20), (20, 15), (0, 21), (21, 16), (0, 11), (11, 7), (3, 22), (22, 17), (4, 12), (12, 8), (1, 23), (23, 18), (1, 13), (13, 9), (5, 24), (24, 19), (6, 14), (14, 10), (2, 30), (30, 0), (2, 31), (31, 3), (2, 32), (32, 4), (2, 33), (33, 1), (2, 34), (34, 5), (2, 35), (35, 6), (9, 25), (25, 17), (7, 26), (26, 19), (10, 27), (27, 16), (10, 28), (28, 18), (8, 29), (29, 15)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """dead"""
        self["GUID__"] = UUID('08f741cb-ec60-4f6b-a49b-eba845147078')
        
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
        self.vs[0]["GUID__"] = UUID('32a87956-76c0-4d4e-8fba-27e97fa18a90')
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
        self.vs[1]["GUID__"] = UUID('5a40a9c8-f964-498d-bc8f-5f197e6f66af')
        self.vs[2]["Name"] = """easy"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('d1721af9-eada-4414-90dd-ac4f5b1b1708')
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
        self.vs[3]["GUID__"] = UUID('3529d78c-dbf9-4426-988c-6a0582447112')
        self.vs[4]["Name"] = """Constant"""
        self.vs[4]["SampleTime"] = inf
        self.vs[4]["value"] = 1.0
        self.vs[4]["Tag"] = """1"""
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F155
aF75
aF185
aF105
a.""")
        self.vs[4]["GUID__"] = UUID('0885ed3f-f7e3-43d2-91d7-6d1d81473205')
        self.vs[5]["NumInputPorts"] = """1"""
        self.vs[5]["Name"] = """Gain45"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Gain"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["gain"] = 1.0
        self.vs[5]["Position"] = pickle.loads("""(lp1
F345
aF79
aF375
aF111
a.""")
        self.vs[5]["GUID__"] = UUID('8c05b4a8-25b2-43c2-aeac-4081f65eaf1e')
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
        self.vs[6]["GUID__"] = UUID('6586a1b4-701d-4243-b1f4-80a471eddd39')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Output"""
        self.vs[7]["GUID__"] = UUID('527e6749-c86b-480a-9f3c-bfb06f80a0b0')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('c381124f-8a1a-44cf-84f8-6dc28db395dd')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('8a684fc3-dd7f-47a9-8168-1fa6ebaadc79')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('63625fd3-8b32-45ff-8649-a2cf5229350f')
        self.vs[11]["mm__"] = """__Block_Outport__"""
        self.vs[11]["GUID__"] = UUID('9b7ebba4-25b1-4294-b8d4-b1e0696e00b6')
        self.vs[12]["mm__"] = """__Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('49884538-cc19-47e9-84af-721f1eaccae9')
        self.vs[13]["mm__"] = """__Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('25baf2d9-c56a-404a-ba40-a7cf79a0b556')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('8bdffa7d-d178-4a2c-9992-fb27c3b2c8cf')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('eb230195-4ff8-4861-85f2-69530e249681')
        self.vs[16]["Name"] = """2"""
        self.vs[16]["mm__"] = """Port_Input"""
        self.vs[16]["GUID__"] = UUID('e7e5694d-df6b-4cc2-aa36-b221d6827327')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('bbe2d4ee-1b40-4416-b638-7d82e81b3910')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('e4037771-04ca-4ed1-9f31-7c24eca92e55')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('5ef2862b-c5d7-49dd-86b5-f078e750e861')
        self.vs[20]["mm__"] = """__Block_Inport__"""
        self.vs[20]["GUID__"] = UUID('b384d945-79b6-4433-a578-d3de03bcd745')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('b56458c7-f2bd-488c-bca8-2e21cfee8c42')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('ef30a5e7-8798-4b71-8c3c-25c8cf17f28f')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('b9c227d3-f04d-43fd-a2d7-2cee2c9c8b36')
        self.vs[24]["mm__"] = """__Block_Inport__"""
        self.vs[24]["GUID__"] = UUID('02960e9e-a0a5-4e2b-8701-8b0d17e2115f')
        self.vs[25]["mm__"] = """__Relation__"""
        self.vs[25]["GUID__"] = UUID('679bf4fe-4292-475b-b12e-3b5290f5d147')
        self.vs[26]["mm__"] = """__Relation__"""
        self.vs[26]["GUID__"] = UUID('23591f8d-8d87-4c4d-85c6-dce138ceb1bc')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('f157984d-0019-4459-b2f9-256e28a49e62')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('08e9623d-063e-4980-a760-fa10c64a1bae')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('a89d4fa1-9511-4274-882e-02c3dc2ff5cd')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('811d1e62-aa83-4497-855f-67d97dbb2e9e')
        self.vs[31]["Name"] = """None"""
        self.vs[31]["mm__"] = """__Contains__"""
        self.vs[31]["GUID__"] = UUID('c77daa8e-0dd4-4234-9e25-291b45aec8d8')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('9d2e2be2-0c41-4702-882d-6c355d5fa96e')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('d71bc34b-8424-40d4-876f-24102c1ea6ba')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('1ef1c20a-2ac4-429a-b996-634af77271ea')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('64bc036b-99c9-4ed9-8e04-06373ce4ea80')

