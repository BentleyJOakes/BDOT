

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattModel_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattModel_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattModel_opt, self).__init__(name='HFlattModel_opt', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(1, 14), (2, 15), (3, 16), (4, 23), (4, 22), (4, 21), (4, 20), (11, 5), (12, 6), (13, 7), (8, 19), (9, 18), (10, 17), (0, 11), (1, 12), (1, 13), (14, 8), (15, 9), (16, 10), (17, 6), (18, 7), (19, 5), (20, 0), (21, 1), (22, 2), (23, 3)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlattModel_opt"""
        self["GUID__"] = UUID('7cf42400-d7d8-497f-9b5c-2d6dbc81c755')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('779363f0-a96e-43a3-94de-95d5dc8782c0')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F170
aF67
aF200
aF98
a.""")
        self.vs[1]["GUID__"] = UUID('4dc9919c-cc4f-47cf-8c6e-1fa6c20debae')
        self.vs[2]["Name"] = """Constant"""
        self.vs[2]["SampleTime"] = """inf"""
        self.vs[2]["value"] = 1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Constant"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F40
aF105
aF70
aF135
a.""")
        self.vs[2]["GUID__"] = UUID('7a6464c7-23a6-4fb6-a5d6-a960f5c8148d')
        self.vs[3]["Name"] = """In1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Inport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F60
aF48
aF90
aF62
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('b49b284c-3df7-4839-a5f8-fb6a9cd1411e')
        self.vs[4]["Name"] = """HFlattModel"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('d07644ca-7d35-4e04-a6f4-1a68bd8a6bab')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('6e40cf86-0687-420c-9011-84c35366f5e1')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('d7309ec8-a5af-454b-bfbb-1ef44fcc4260')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('33eae7c2-e318-4f41-a3a0-e48249ab6404')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('b39d395f-fbc1-4f19-91fa-aaaa2476bcf4')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('90d30d61-50a8-47c2-9038-398850dfc2b1')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('905849e2-ad1b-48f6-972b-fdf681034d7a')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('369df4b3-8ed7-410a-ad1c-b24e971b629a')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('ab1b738f-0911-46d6-8276-019112506261')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('7be33921-1319-4b4f-9d4c-8b7ac11e0614')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('19602048-a3c3-4cf4-9bcd-2916877bbd23')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('28968522-ad37-4890-9dc5-331e83db6d96')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('85f30271-e267-429d-ae49-3dbd5d164b44')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('b6e2d9b2-a144-4ce6-af88-dc7fe49a5f66')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('4430f776-1ad5-4387-8980-1066fd23a6f3')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('748b82a9-1b12-4824-83c9-5350ae65391c')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('d8f5dd57-997c-4cb5-846d-2f476c6e83e2')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('7a2db484-a95c-4ec0-9b60-490dfb4e457f')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('7c653609-f890-46fd-816a-b5aaacabb833')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('bb537378-7057-4779-83fd-f5974f0f633e')

