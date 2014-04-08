

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HDead_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HDead_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDead_opt, self).__init__(name='HDead_opt', num_nodes=17, edges=[])
        
        # Add the edges
        self.add_edges([(0, 6), (1, 16), (1, 15), (1, 14), (3, 7), (4, 12), (5, 13), (6, 4), (7, 5), (10, 8), (11, 9), (2, 10), (0, 11), (12, 8), (13, 9), (14, 2), (15, 0), (16, 3)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HDead_opt"""
        self["GUID__"] = UUID('fb2090ac-3e46-4260-9e2d-e059d83f39f8')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Gain"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["gain"] = 1.0
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["mm__"] = """Gain"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F250
aF185
aF280
aF215
a.""")
        self.vs[0]["GUID__"] = UUID('7a954933-5292-4d2c-9b5c-a5ea3c984108')
        self.vs[1]["Name"] = """easy"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('729c8e58-bf17-491e-b96c-b29563c4237f')
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
        self.vs[2]["GUID__"] = UUID('e043d4c5-dae4-4deb-843b-08d5ac4840c7')
        self.vs[3]["Name"] = """Constant1"""
        self.vs[3]["SampleTime"] = """inf"""
        self.vs[3]["value"] = 1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Constant"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F150
aF125
aF180
aF155
a.""")
        self.vs[3]["GUID__"] = UUID('abf48b03-21aa-4c55-9f3a-8194a26ba8fe')
        self.vs[4]["Name"] = """1"""
        self.vs[4]["mm__"] = """Port_Output"""
        self.vs[4]["GUID__"] = UUID('119b9d58-4dec-4371-a2c4-c505b9ed33f6')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Output"""
        self.vs[5]["GUID__"] = UUID('02339489-0223-4fc3-8a41-21ce5331519f')
        self.vs[6]["mm__"] = """__Block_Outport__"""
        self.vs[6]["GUID__"] = UUID('47d9a729-ba22-4913-a522-d7729590447d')
        self.vs[7]["mm__"] = """__Block_Outport__"""
        self.vs[7]["GUID__"] = UUID('846b13a6-80b1-4c8c-a702-c8580eed872e')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('822cdc22-75a5-44b8-b8b0-4d0962d38fb4')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('22568878-4223-4f7e-becc-15c55db99112')
        self.vs[10]["mm__"] = """__Block_Inport__"""
        self.vs[10]["GUID__"] = UUID('59224f4e-2d54-493f-9bf2-01dc8d016fb6')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('9171f48e-8b4b-4c9c-89f6-855e156aac5b')
        self.vs[12]["mm__"] = """__Relation__"""
        self.vs[12]["GUID__"] = UUID('36ff4de1-9e1e-4c93-a7c6-38c6d54fff79')
        self.vs[13]["mm__"] = """__Relation__"""
        self.vs[13]["GUID__"] = UUID('09b8bb06-d5df-4b74-b794-cb88eed65caf')
        self.vs[14]["Name"] = """None"""
        self.vs[14]["mm__"] = """__Contains__"""
        self.vs[14]["GUID__"] = UUID('ca3c240b-6b38-4dd7-ab22-b1c00b983bdc')
        self.vs[15]["Name"] = """None"""
        self.vs[15]["mm__"] = """__Contains__"""
        self.vs[15]["GUID__"] = UUID('f1860470-9601-48d3-a94f-66ea6ac9457d')
        self.vs[16]["Name"] = """None"""
        self.vs[16]["mm__"] = """__Contains__"""
        self.vs[16]["GUID__"] = UUID('71c9af64-9e67-4b67-9bae-629449748ff9')

