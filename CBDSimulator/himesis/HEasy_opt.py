

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HEasy_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HEasy_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HEasy_opt, self).__init__(name='HEasy_opt', num_nodes=36, edges=[])
        
        # Add the edges
        self.add_edges([(0, 11), (3, 13), (1, 35), (1, 34), (1, 33), (1, 32), (1, 31), (1, 30), (4, 12), (6, 14), (7, 26), (8, 29), (9, 25), (10, 28), (10, 27), (11, 7), (12, 8), (13, 9), (14, 10), (20, 15), (21, 16), (22, 17), (23, 18), (24, 19), (0, 20), (0, 21), (2, 22), (3, 23), (5, 24), (25, 17), (26, 19), (27, 16), (28, 18), (29, 15), (30, 0), (31, 2), (32, 4), (33, 3), (34, 5), (35, 6)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HEasy_opt"""
        self["GUID__"] = UUID('4b98e2cd-ad5c-4b47-8284-e4b4f8fadf0e')
        
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
        self.vs[0]["GUID__"] = UUID('d263fa84-e3cf-4163-9892-e7761bc65bf2')
        self.vs[1]["Name"] = """easy"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('b910c56d-8fdb-4113-ae08-ce78b79293ce')
        self.vs[2]["NumInputPorts"] = """1"""
        self.vs[2]["Name"] = """Scope1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Scope"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F345
aF184
aF375
aF216
a.""")
        self.vs[2]["LimitDataPoints"] = """on"""
        self.vs[2]["GUID__"] = UUID('d67674ca-b001-462c-a8f7-dad7002c96a2')
        self.vs[3]["Name"] = """Gain"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["gain"] = 1.0
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["mm__"] = """Gain"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F250
aF185
aF280
aF215
a.""")
        self.vs[3]["GUID__"] = UUID('cfd87825-d0c8-473f-b3ae-7b845fd60caf')
        self.vs[4]["Name"] = """Constant"""
        self.vs[4]["SampleTime"] = """inf"""
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
        self.vs[4]["GUID__"] = UUID('357fa1fc-d422-4372-bf72-00d4b3f45544')
        self.vs[5]["NumInputPorts"] = """1"""
        self.vs[5]["Name"] = """Gain45"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["gain"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Gain"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F345
aF79
aF375
aF111
a.""")
        self.vs[5]["GUID__"] = UUID('50f31a48-e1fd-4897-a832-844e928d9f70')
        self.vs[6]["Name"] = """Constant1"""
        self.vs[6]["SampleTime"] = """inf"""
        self.vs[6]["value"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F150
aF125
aF180
aF155
a.""")
        self.vs[6]["GUID__"] = UUID('80b3a947-08ee-4aaf-8260-d6d090745e07')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Output"""
        self.vs[7]["GUID__"] = UUID('103f1618-17f4-4939-bd21-61f398b3cb17')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('afba47b2-b08e-4666-8879-6bb1175547b6')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('171113df-16e8-4b84-ab31-ba991c802bb0')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('ccb937fd-632b-4bf0-9c40-e31f404c4dc9')
        self.vs[11]["mm__"] = """__Block_Outport__"""
        self.vs[11]["GUID__"] = UUID('e2d6a5c8-a83e-4ea4-84d8-fe2831a6c1fc')
        self.vs[12]["mm__"] = """__Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('bc305799-3898-4498-a413-29575746926c')
        self.vs[13]["mm__"] = """__Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('15c15a0f-57ee-4ef8-b4f9-df5c9706977f')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('c0727382-0882-44b4-8aee-71e5ff08ed2d')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('ae2d717e-6118-43a6-8def-222425a42744')
        self.vs[16]["Name"] = """2"""
        self.vs[16]["mm__"] = """Port_Input"""
        self.vs[16]["GUID__"] = UUID('ed2e9add-89c5-4f8c-ae4c-947ec51c6b21')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('63f38302-5b86-420c-b4be-bb8476899e10')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('a075117f-8349-4016-9d74-59740e408f7d')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('3ec433f9-378e-47f3-a4ec-c33f57c1d879')
        self.vs[20]["mm__"] = """__Block_Inport__"""
        self.vs[20]["GUID__"] = UUID('13f5f639-1c5b-4442-9ba9-a5977b7fbc1a')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('e4233b96-f88d-469c-9500-c278b11e32a1')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('52381b95-e0c9-450b-85a2-6a1f67056508')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('deccfb27-4073-4cf0-8eb6-edb53ea72ff8')
        self.vs[24]["mm__"] = """__Block_Inport__"""
        self.vs[24]["GUID__"] = UUID('b50622de-9c2e-4eb6-a0c7-5c62b3d1be6b')
        self.vs[25]["mm__"] = """__Relation__"""
        self.vs[25]["GUID__"] = UUID('69afa8c1-16f6-45a1-892b-d66a0297d542')
        self.vs[26]["mm__"] = """__Relation__"""
        self.vs[26]["GUID__"] = UUID('0118cbba-a127-4aca-85b9-cde33c98d2de')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('0c7580fb-190c-4cff-978c-0c857d9c0893')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('7a86cd8b-ee1c-4b96-a89f-d9341a215974')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('7b78f2d3-433c-4231-8b39-6a37edb77bc1')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('31a1908f-4011-4dfb-8105-d79696442c6b')
        self.vs[31]["Name"] = """None"""
        self.vs[31]["mm__"] = """__Contains__"""
        self.vs[31]["GUID__"] = UUID('46860888-52d4-4028-8fd2-545806aa5811')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('1a0ffd03-d720-4b63-89a8-00d36a8c1771')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('5a050239-f09b-4ba2-9447-fe4fe9906220')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('77707076-2c44-4024-a7da-c154f9c99bba')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('f5030950-e363-4f28-8ea6-778e976494ea')

