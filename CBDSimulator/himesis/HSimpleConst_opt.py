

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConst_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConst_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConst_opt, self).__init__(name='HSimpleConst_opt', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(1, 14), (2, 16), (3, 23), (3, 22), (3, 21), (3, 20), (11, 5), (12, 6), (13, 7), (8, 18), (9, 17), (10, 19), (0, 11), (1, 12), (1, 13), (14, 8), (15, 9), (16, 10), (17, 6), (18, 5), (19, 7), (20, 0), (21, 1), (22, 4), (23, 2), (4, 15)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConst_opt"""
        self["GUID__"] = UUID('0e76dacd-1143-43f8-9db5-6a894b8d6e9f')
        
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
        self.vs[0]["GUID__"] = UUID('d00a5813-d2ba-45e3-a217-46bb92527feb')
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
        self.vs[1]["GUID__"] = UUID('49ab72bc-9af3-4e9d-8a4c-c7ed180bff3c')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F170
aF178
aF200
aF192
a.""")
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('e4be5dbc-71d9-4078-89f8-d4011ae8f46c')
        self.vs[3]["Name"] = """HSimpleConst"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('6b34985f-bb8d-4309-b388-196b32e99c63')
        self.vs[4]["Name"] = """Constant23"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 545.54
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('d0932d75-2ab8-41eb-adac-a9336bebece8')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('e4f707fd-e981-49e9-85e2-824be24da9ac')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('0e102190-2401-44a7-b5df-2f8a38082f53')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('bb3d29ce-2ed9-41da-a841-9eb14c44a03f')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('40557227-fc78-4d0d-a5f9-a7e2651ba225')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('6ed91100-a590-4d9f-a7b6-aaf36c2efc8c')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('a82db924-82f3-42dc-8b18-9c47031e95da')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('e8b5a593-1df4-4954-852a-2bde2edc9bfc')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('e91e4ac8-48b3-4a94-a1e2-c97e45df608d')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('4ae283c1-a744-48af-9de6-31622aa08eb1')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('109c29ca-854a-4578-b200-71703bd96351')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('cee192b2-7db4-4c1c-a637-575c9e92c9d9')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('f8b7cbff-1d99-4a7b-86d4-2909d0d17382')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('545ab907-2290-4475-9035-92b30ff8511f')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('6ff77ea0-987b-446e-9bda-22c98e5d6121')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('822313eb-a1b9-4903-a8f9-a060cfd51b16')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('89283fdd-dd9d-4b3b-b54b-18990ec334fb')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('dfb9e024-f433-4312-888b-d57edad5a9de')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('531b86bf-a7bc-4402-92ea-155430e18356')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('f9427a97-3bf0-4dbf-aadb-b3691102f375')

