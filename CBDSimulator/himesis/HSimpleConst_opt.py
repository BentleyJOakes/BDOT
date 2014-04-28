

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
        self["GUID__"] = UUID('228d200f-ffdc-4c0e-bc88-61f51a74216f')
        
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
        self.vs[0]["GUID__"] = UUID('85b89a53-92e7-4a49-98b9-ade6251eff77')
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
        self.vs[1]["GUID__"] = UUID('46ea4a04-b727-4b0d-90bd-c82db7ccd7ee')
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
        self.vs[2]["GUID__"] = UUID('9747bb91-1feb-4f90-9a9f-b5fa912ce93d')
        self.vs[3]["Name"] = """HSimpleConst"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('8cb30c14-54b2-4127-b62a-66894052c034')
        self.vs[4]["Name"] = """Constant23"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 545.54
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('ca0d82da-c399-491d-a2ef-47cce29260b8')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('d6c8213f-7671-4399-bb17-4544bd189947')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('d8ec0094-2bd3-4fa1-a451-22f598058f1d')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('1ae7bae5-a888-4d2d-b0da-44c5148f25ac')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('c0eecf70-8bc1-4bb7-b26c-9fab522ab97a')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('7923f3b4-c14a-4b1f-afe1-ea84f047bfc8')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('4e504525-e7e4-4213-96b7-4b72ab33e667')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('c9f626f5-b777-4681-88aa-4e62be54ddef')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('87b35ee0-6d8e-45f5-86aa-483684061f38')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('e0486d40-a1fb-4da6-aad4-60e94caf2289')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('afef3de3-d565-48be-8c61-51111ab2f43d')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('9166314d-4fe0-4ea5-8b86-7f456bbdd150')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('158943c1-b83a-4b4c-8a9f-98801bcf3a90')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('0502ebca-71f3-43ae-9525-d97fd9cd24bf')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('5f8605d5-c7e2-421d-a9d3-e349b0e0351a')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('47311d73-33ef-4e05-84c8-ae54810328be')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('c11e849e-70d3-4b22-933f-54aa755b441a')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('99e19103-6a62-42b6-b7da-016d14f02b20')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('1bde3c3f-6bba-4112-a44a-a30df40b737b')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('a37caaea-f506-4637-a8c9-1dde6c07bc87')

