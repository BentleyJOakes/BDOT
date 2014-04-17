

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
        
        super(HEasy_opt, self).__init__(name='HEasy_opt', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([(0, 18), (0, 17), (0, 16), (0, 15), (3, 12), (4, 11), (5, 3), (6, 4), (9, 7), (10, 8), (1, 9), (2, 10), (11, 7), (12, 8), (15, 14), (16, 1), (17, 13), (18, 2), (13, 6), (14, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HEasy_opt"""
        self["GUID__"] = UUID('2ec72ce8-2c48-415c-9a9d-f10e22f62af2')
        
        # Set the node attributes
        self.vs[0]["Name"] = """HEasy"""
        self.vs[0]["mm__"] = """SubSystem"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[0]["GUID__"] = UUID('741ea763-6271-4be4-b25f-773431e2c829')
        self.vs[1]["NumInputPorts"] = """1"""
        self.vs[1]["Name"] = """Scope1"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Scope"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F345
aF184
aF375
aF216
a.""")
        self.vs[1]["LimitDataPoints"] = """on"""
        self.vs[1]["GUID__"] = UUID('a2dd3ed3-12a1-46e0-a7a2-4f88a15cb487')
        self.vs[2]["NumInputPorts"] = """1"""
        self.vs[2]["Name"] = """Scope"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Scope"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F345
aF79
aF375
aF111
a.""")
        self.vs[2]["LimitDataPoints"] = """on"""
        self.vs[2]["GUID__"] = UUID('8548e94c-643c-4dba-b26e-466a0d6e13ce')
        self.vs[3]["Name"] = """1"""
        self.vs[3]["mm__"] = """Port_Output"""
        self.vs[3]["GUID__"] = UUID('4d30f3e7-0bd1-41ff-939e-36ebbe99f3e5')
        self.vs[4]["Name"] = """1"""
        self.vs[4]["mm__"] = """Port_Output"""
        self.vs[4]["GUID__"] = UUID('8bd6416f-1935-4f75-9eea-c888a3fa699b')
        self.vs[5]["mm__"] = """__Block_Outport__"""
        self.vs[5]["GUID__"] = UUID('28d29a5f-33b0-4282-8717-e4e70b9d6dbd')
        self.vs[6]["mm__"] = """__Block_Outport__"""
        self.vs[6]["GUID__"] = UUID('10af123a-384c-4982-8e28-d5ab64f63fc5')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('d78399e7-f90a-4da4-a67c-2a5873fbd5ee')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('f4011ef2-e307-4072-8240-d09fce5503da')
        self.vs[9]["mm__"] = """__Block_Inport__"""
        self.vs[9]["GUID__"] = UUID('12b6948c-2346-495c-8820-2263aa20f3b4')
        self.vs[10]["mm__"] = """__Block_Inport__"""
        self.vs[10]["GUID__"] = UUID('7c9b9572-75c8-472c-a210-6573c82bc2c4')
        self.vs[11]["mm__"] = """__Relation__"""
        self.vs[11]["GUID__"] = UUID('76c4fef9-6245-478a-a6c3-9e30624848ca')
        self.vs[12]["mm__"] = """__Relation__"""
        self.vs[12]["GUID__"] = UUID('c36f35a2-217d-4421-b79c-31e35ff76aa4')
        self.vs[13]["Name"] = """Constant17"""
        self.vs[13]["SampleTime"] = """inf"""
        self.vs[13]["value"] = 1.0
        self.vs[13]["BackgroundColor"] = """white"""
        self.vs[13]["mm__"] = """Constant"""
        self.vs[13]["GUID__"] = UUID('58cde79b-e9b1-4790-9a34-8da95eb2431f')
        self.vs[14]["Name"] = """Constant18"""
        self.vs[14]["SampleTime"] = """inf"""
        self.vs[14]["value"] = 1.0
        self.vs[14]["BackgroundColor"] = """white"""
        self.vs[14]["mm__"] = """Constant"""
        self.vs[14]["GUID__"] = UUID('e61ef9b4-7fb2-4c9b-a0e2-c86e02023ff3')
        self.vs[15]["Name"] = """None"""
        self.vs[15]["mm__"] = """__Contains__"""
        self.vs[15]["GUID__"] = UUID('643b01ee-9c4d-40dc-ace3-39d6f4846bfe')
        self.vs[16]["Name"] = """None"""
        self.vs[16]["mm__"] = """__Contains__"""
        self.vs[16]["GUID__"] = UUID('ba93f783-4072-4c98-b295-3096cd8858fc')
        self.vs[17]["Name"] = """None"""
        self.vs[17]["mm__"] = """__Contains__"""
        self.vs[17]["GUID__"] = UUID('97e6fa8d-0b2f-4a88-ad50-2c1a8bbf60fa')
        self.vs[18]["Name"] = """None"""
        self.vs[18]["mm__"] = """__Contains__"""
        self.vs[18]["GUID__"] = UUID('a60a2cb4-5894-4897-bb63-768111c3e0a6')

