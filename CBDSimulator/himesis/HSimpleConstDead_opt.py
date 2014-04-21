

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConstDead_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConstDead_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConstDead_opt, self).__init__(name='HSimpleConstDead_opt', num_nodes=24, edges=[])
        
        # Add the edges
        self.add_edges([(1, 14), (2, 15), (3, 23), (3, 22), (3, 21), (3, 20), (4, 16), (11, 5), (12, 6), (13, 7), (8, 18), (9, 19), (10, 17), (0, 11), (1, 12), (1, 13), (14, 8), (15, 9), (16, 10), (17, 6), (18, 5), (19, 7), (20, 0), (21, 1), (22, 2), (23, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConstDead_opt"""
        self["GUID__"] = UUID('2da9cd9c-894f-4069-a7da-9baa6f39cc2a')
        
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
        self.vs[0]["GUID__"] = UUID('84eb3d8c-5fe6-435a-a435-a3a69085cc63')
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
        self.vs[1]["GUID__"] = UUID('bef0e843-8452-4760-9f49-0e95153e7950')
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
        self.vs[2]["GUID__"] = UUID('daaf846a-c6ad-420e-9888-ea62795fa34a')
        self.vs[3]["Name"] = """HSimpleConstDead"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('c73e9937-6936-400d-abe5-2b3ed6274a27')
        self.vs[4]["Name"] = """Constant2"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 433.22
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F50
aF82
aF105
aF118
a.""")
        self.vs[4]["GUID__"] = UUID('b0ec15fa-44bc-416b-94f0-c57cd7528078')
        self.vs[5]["Name"] = """1"""
        self.vs[5]["mm__"] = """Port_Input"""
        self.vs[5]["GUID__"] = UUID('e8ad444a-8467-40b9-924d-932796d941d8')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('23068f35-f675-455f-9b8f-054e7f0aebe2')
        self.vs[7]["Name"] = """2"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('46074f46-e09e-429d-af0d-23eff1f36488')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('2e619d94-56f4-4dde-b227-e32cabc578f4')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('ed54a7bf-e9ef-4845-a79f-4dba07c51f7b')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('e3b30f1a-1c48-4db3-ba06-e2f2c9d4876c')
        self.vs[11]["mm__"] = """__Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('54ee4c73-082e-4412-bb40-710ea208263b')
        self.vs[12]["mm__"] = """__Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('5c2107a7-92e1-419a-97f4-edb00e8789c5')
        self.vs[13]["mm__"] = """__Block_Inport__"""
        self.vs[13]["GUID__"] = UUID('c28a138e-6afc-4b37-9b8a-b72ef27b1368')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('8f6227c4-77ce-4684-a344-3be6593dd89b')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('7447e9ac-9c09-4cc9-99e3-c80221ea1c7b')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('3ab1f685-fcce-4fde-b884-0ade795bf17e')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('dbe4c188-3501-4e2e-ba6e-e4cfe8cbaff4')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('c2ad887e-5c7f-4d85-985b-13624fa01c7c')
        self.vs[19]["mm__"] = """__Relation__"""
        self.vs[19]["GUID__"] = UUID('05ae22b6-6c46-4107-bc03-34f4fa6088ea')
        self.vs[20]["Name"] = """None"""
        self.vs[20]["mm__"] = """__Contains__"""
        self.vs[20]["GUID__"] = UUID('39289991-048e-40ba-b626-837092f16514')
        self.vs[21]["Name"] = """None"""
        self.vs[21]["mm__"] = """__Contains__"""
        self.vs[21]["GUID__"] = UUID('c9667e1f-0ca3-4963-ad49-d0f78d85fdab')
        self.vs[22]["Name"] = """None"""
        self.vs[22]["mm__"] = """__Contains__"""
        self.vs[22]["GUID__"] = UUID('60cd287a-8930-4ffa-9fb0-a48ce4766983')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('248639fd-59cd-4dd5-8d43-b7aa07199ee6')

