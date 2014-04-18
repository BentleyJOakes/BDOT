

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattModel(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattModel.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattModel, self).__init__(name='HFlattModel', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(0, 11), (11, 5), (1, 12), (12, 6), (1, 13), (13, 7), (1, 14), (14, 8), (2, 15), (15, 9), (3, 16), (16, 10), (4, 20), (20, 0), (4, 21), (21, 1), (4, 22), (22, 2), (4, 23), (23, 3), (10, 17), (17, 6), (9, 18), (18, 7), (8, 19), (19, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlattModel"""
        self["GUID__"] = UUID('5746e1e0-212c-46af-a924-fe40aa09b5b7')
        
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
        self.vs[0]["GUID__"] = UUID('18ca8459-4b91-48b5-838f-ec1a6bc44859')
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
        self.vs[1]["GUID__"] = UUID('23418e17-7a44-4f11-92bf-a3d1b7483fe5')
        self.vs[2]["Name"] = """Constant"""
        self.vs[2]["SampleTime"] = inf
        self.vs[2]["value"] = 1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Constant"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F40
aF105
aF70
aF135
a.""")
        self.vs[2]["GUID__"] = UUID('d689d725-9a5d-4795-9f9b-3e58011ce9b3')
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
        self.vs[3]["GUID__"] = UUID('509f4b7b-22a1-4750-9276-5c079c83a568')
        self.vs[4]["Name"] = """HFlattModel"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('481db310-3fd1-41ba-9b37-216a097a5953')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('32d93222-2a79-48ed-b2b0-092aa87014d2')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('3fb02a9c-5609-4d61-b79f-13a7ff8c097d')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('e0565c65-4632-4493-91b1-f42d56b58c96')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('bf354998-655d-4b1a-966b-0ef0c90ff4c5')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('0c547fab-f6bb-4ab8-b778-df3c40dac6c2')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('bdae5009-74e1-43f6-9ed2-e363620a234f')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('f686511b-985c-4d9b-b203-7f756caa7c3f')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('300384b7-a861-4f61-b0a4-1b42f66d936d')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('556561b4-a5c3-46e3-9ea5-1bc79e2ff103')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('20c161e8-d77d-4fe1-a530-65c2024cb124')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('72234949-d75c-44d6-9496-16c1a6010c14')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('d16ec381-d029-4f1f-aaf3-c82bd913d595')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('932ad43f-154d-485b-9ec4-fe3ce0c7b23c')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('7b630c62-6736-467b-b1a5-54f97e77f980')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('ac148abd-b900-4f53-90b2-72fa05399711')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('22667824-7ffb-4947-9680-87b156359486')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('2bc013ff-6331-46c1-b3ca-ff1682e03fb4')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('c4e2ab72-1f26-41f9-8351-f18f695ff3ec')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('6380ba21-d313-45f1-b3f5-fc14565cdfc7')

