

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConst2b_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConst2b_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConst2b_opt, self).__init__(name='HConst2b_opt', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([(1, 16), (2, 20), (3, 30), (3, 29), (3, 28), (3, 27), (3, 26), (14, 6), (7, 24), (8, 22), (17, 9), (18, 10), (19, 11), (12, 25), (13, 23), (0, 14), (15, 7), (16, 8), (2, 17), (2, 18), (2, 19), (20, 12), (21, 13), (22, 10), (23, 9), (24, 11), (25, 6), (26, 0), (27, 4), (28, 1), (29, 2), (30, 5), (4, 15), (5, 21)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConst2b_opt"""
        self["GUID__"] = UUID('9876988b-196e-4d07-bd32-9da938210a14')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F450
aF128
aF480
aF142
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('e284c6a3-ae32-4477-be75-c9d0db032104')
        self.vs[1]["Name"] = """In1"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Inport"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F165
aF108
aF195
aF122
a.""")
        self.vs[1]["Port"] = 1
        self.vs[1]["GUID__"] = UUID('bb5dbd8f-bada-4ba7-a74b-5263740dfdad')
        self.vs[2]["Name"] = """Switch"""
        self.vs[2]["Threshold"] = 0.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Criteria"] = """u2 >= Threshold"""
        self.vs[2]["mm__"] = """Switch"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F355
aF125
aF405
aF165
a.""")
        self.vs[2]["GUID__"] = UUID('1075b3d7-5926-4717-8bd0-68d2df278f5f')
        self.vs[3]["Name"] = """Const2b"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[3]["GUID__"] = UUID('86c44f60-f3f0-440e-adca-fb6289ea13af')
        self.vs[4]["Name"] = """Constant29"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 439.304
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["GUID__"] = UUID('dfcfbfd2-6a80-46d2-b75b-20f7ab79e13b')
        self.vs[5]["Name"] = """Constant30"""
        self.vs[5]["SampleTime"] = """inf"""
        self.vs[5]["value"] = 249.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["GUID__"] = UUID('465a2d4f-9e01-42d4-a65f-baa5864ba16e')
        self.vs[6]["Name"] = """1"""
        self.vs[6]["mm__"] = """Port_Input"""
        self.vs[6]["GUID__"] = UUID('47cdaba4-f053-4a6b-9fe8-ac31159eb53a')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Output"""
        self.vs[7]["GUID__"] = UUID('2af12f52-efb0-4007-acc7-169c7be5e784')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('28b06357-c879-4fd6-94c0-121222c8acd0')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('8de50e8c-01a3-451d-ab86-44feaa14440f')
        self.vs[10]["Name"] = """2"""
        self.vs[10]["mm__"] = """Port_Input"""
        self.vs[10]["GUID__"] = UUID('8c1413d1-017b-47b9-b9e0-48b74a7d01fa')
        self.vs[11]["Name"] = """3"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('f59d4d1a-facc-4ef5-adb6-957c6f2ab0fc')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('6971b480-5ec4-4d58-83c4-9ae07b53a7c9')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('76999d79-9246-4e1f-a241-8b4ed7efcab0')
        self.vs[14]["mm__"] = """__Block_Inport__"""
        self.vs[14]["GUID__"] = UUID('7bf699b2-4636-4923-960a-4389d2fec495')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('d49838b1-e920-408b-866e-4d15889c1ab3')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('7528623f-10c0-45f1-b130-335cf3295fb6')
        self.vs[17]["mm__"] = """__Block_Inport__"""
        self.vs[17]["GUID__"] = UUID('c6d7dc97-66a8-4eab-bc64-3c29e3eeb158')
        self.vs[18]["mm__"] = """__Block_Inport__"""
        self.vs[18]["GUID__"] = UUID('8f2b2646-45d9-402b-9d17-54d51b4e9a9c')
        self.vs[19]["mm__"] = """__Block_Inport__"""
        self.vs[19]["GUID__"] = UUID('81a3b07a-2255-463e-927b-a24dbe729b36')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('417550ba-7dc2-4608-91f7-80a3027a752d')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('74b116ea-140f-4338-ba54-7ece21510765')
        self.vs[22]["mm__"] = """__Relation__"""
        self.vs[22]["GUID__"] = UUID('ea2966c2-d092-4804-a845-e8a92901a253')
        self.vs[23]["mm__"] = """__Relation__"""
        self.vs[23]["GUID__"] = UUID('32baf6bb-9451-4a88-b476-f029a36f52a4')
        self.vs[24]["mm__"] = """__Relation__"""
        self.vs[24]["GUID__"] = UUID('86952b5f-0090-400d-9e3a-6f667ed258a1')
        self.vs[25]["mm__"] = """__Relation__"""
        self.vs[25]["GUID__"] = UUID('092143c2-4105-4f23-b945-ac19bebb6199')
        self.vs[26]["Name"] = """None"""
        self.vs[26]["mm__"] = """__Contains__"""
        self.vs[26]["GUID__"] = UUID('6eb46867-1382-44dd-b6b9-468daa32fc45')
        self.vs[27]["Name"] = """None"""
        self.vs[27]["mm__"] = """__Contains__"""
        self.vs[27]["GUID__"] = UUID('b9698924-07b5-436f-999c-33ba357e9658')
        self.vs[28]["Name"] = """None"""
        self.vs[28]["mm__"] = """__Contains__"""
        self.vs[28]["GUID__"] = UUID('1ea77cef-6fdd-4a3b-b2fe-242644e8ffda')
        self.vs[29]["Name"] = """None"""
        self.vs[29]["mm__"] = """__Contains__"""
        self.vs[29]["GUID__"] = UUID('1c0d7a9f-92cb-4301-9a43-93be119d7e1d')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('372cb72d-7f57-46a2-9411-43cebafc6b79')

