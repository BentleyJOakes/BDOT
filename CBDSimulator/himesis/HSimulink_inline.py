

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimulink_inline(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimulink_inline.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimulink_inline, self).__init__(name='HSimulink_inline', num_nodes=67, edges=[])
        
        # Add the edges
        self.add_edges([(0, 30), (30, 14), (6, 31), (31, 15), (7, 32), (32, 16), (7, 33), (33, 17), (7, 34), (34, 18), (8, 35), (35, 19), (8, 36), (36, 20), (1, 37), (37, 21), (1, 38), (38, 22), (1, 39), (39, 23), (2, 40), (40, 24), (10, 41), (41, 25), (10, 42), (42, 26), (11, 43), (43, 27), (12, 44), (44, 28), (12, 45), (45, 29), (13, 54), (54, 0), (13, 55), (55, 6), (13, 56), (56, 7), (13, 57), (57, 8), (13, 58), (58, 1), (13, 59), (59, 2), (13, 60), (60, 9), (13, 61), (61, 3), (13, 62), (62, 4), (13, 63), (63, 10), (13, 64), (64, 11), (13, 65), (65, 5), (13, 66), (66, 12), (29, 46), (46, 22), (20, 47), (47, 21), (18, 48), (48, 28), (26, 49), (49, 17), (27, 50), (50, 25), (15, 51), (51, 16), (23, 52), (52, 14), (24, 53), (53, 19)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """simulink_inline"""
        self["GUID__"] = UUID('25b6d432-406a-4b0b-9855-6ba22d7486b7')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F555
aF68
aF585
aF82
a.""")
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('ed2923a3-38c5-41fa-877c-54b310c05221')
        self.vs[1]["Inputs"] = """++"""
        self.vs[1]["Name"] = """Sum"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F485
aF57
aF515
aF88
a.""")
        self.vs[1]["mm__"] = """Sum"""
        self.vs[1]["IconShape"] = """rectangular"""
        self.vs[1]["GUID__"] = UUID('d95f68fd-56de-464a-ab83-da9ba43dfabd')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F95
aF23
aF125
aF37
a.""")
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('77d24d6e-a029-489b-ba3b-24faf024b0b7')
        self.vs[3]["Name"] = """View Optimization"""
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F323
aF315
aF449
aF375
a.""")
        self.vs[3]["mm__"] = """rtwdemowidgets/View Optimization"""
        self.vs[3]["GUID__"] = UUID('f69287d3-4852-4943-86b0-a20a89383594')
        self.vs[4]["Name"] = """Build GRT"""
        self.vs[4]["BackgroundColor"] = """lightBlue"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F20
aF315
aF149
aF375
a.""")
        self.vs[4]["mm__"] = """rtwdemowidgets/Build GRT"""
        self.vs[4]["GUID__"] = UUID('f72e75b7-48fc-43a5-942b-6b7be5b422ad')
        self.vs[5]["Name"] = """Build ERT"""
        self.vs[5]["BackgroundColor"] = """lightBlue"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F170
aF315
aF299
aF375
a.""")
        self.vs[5]["mm__"] = """rtwdemowidgets/Build ERT"""
        self.vs[5]["GUID__"] = UUID('95b8c093-d7e2-4338-a8a7-ce270f19eb8e')
        self.vs[6]["Name"] = """Constant"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = """MAX_LIFT"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F75
aF77
aF155
aF103
a.""")
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["GUID__"] = UUID('e5b124ad-dea6-477b-9370-e1207920b7cd')
        self.vs[7]["Name"] = """2D Lookup"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F315
aF72
aF365
aF143
a.""")
        self.vs[7]["mm__"] = """Lookup_n-D"""
        self.vs[7]["GUID__"] = UUID('e041b089-40e1-407b-bb64-9d5b83b5d040')
        self.vs[8]["Name"] = """G1"""
        self.vs[8]["SampleTime"] = -1.0
        self.vs[8]["gain"] = 2.0
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F290
aF16
aF335
aF44
a.""")
        self.vs[8]["mm__"] = """Gain"""
        self.vs[8]["GUID__"] = UUID('e9944ddb-e620-4490-93e5-fad002d33ffe')
        self.vs[9]["Name"] = """Inline Parameter Setting1"""
        self.vs[9]["BackgroundColor"] = """yellow"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F473
aF315
aF601
aF376
a.""")
        self.vs[9]["mm__"] = """SubSystem"""
        self.vs[9]["GUID__"] = UUID('d8293fd1-f977-4250-a53a-e966463a8308')
        self.vs[10]["Name"] = """1D Lookup"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F215
aF113
aF265
aF137
a.""")
        self.vs[10]["mm__"] = """Lookup_n-D"""
        self.vs[10]["GUID__"] = UUID('ac535258-2c6b-432e-b2f0-82bf1b28ccb8')
        self.vs[11]["Name"] = """Constant1"""
        self.vs[11]["SampleTime"] = inf
        self.vs[11]["value"] = """SLIDER_POS"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F75
aF112
aF155
aF138
a.""")
        self.vs[11]["mm__"] = """Constant"""
        self.vs[11]["GUID__"] = UUID('f7289c82-6677-47cb-82bb-13eb2afd1ec0')
        self.vs[12]["Name"] = """G2"""
        self.vs[12]["SampleTime"] = -1.0
        self.vs[12]["gain"] = -2.0
        self.vs[12]["BackgroundColor"] = """white"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F400
aF95
aF440
aF125
a.""")
        self.vs[12]["mm__"] = """Gain"""
        self.vs[12]["GUID__"] = UUID('a2b88e7b-7b62-43da-851f-9d66eff81e4c')
        self.vs[13]["Name"] = """simulink_inline"""
        self.vs[13]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[13]["mm__"] = """SubSystem"""
        self.vs[13]["GUID__"] = UUID('cc1eb54d-60fa-4f41-814e-e655e0c20a2b')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Input"""
        self.vs[14]["GUID__"] = UUID('1e567301-1dc3-4c24-97e9-6d2d22e676ed')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('f40c7971-5528-4c6c-9372-0fbc2c1e98d8')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Input"""
        self.vs[16]["GUID__"] = UUID('83c18074-8b6a-4131-a13f-8f9f39cba04d')
        self.vs[17]["Name"] = """2"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('43459386-f490-4ee5-977f-6904bc1b3ad9')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('f4a88769-a3c6-4e9c-9977-b4fdc4ad3ccf')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('51f20454-b38d-4ceb-ac60-e86642ace173')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('eb781fa7-ebc4-45f2-95fb-6b35c3f3be3a')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('1b2bfc78-8237-4c33-bdbc-315a4110a810')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('8af55dd9-9e43-4a7d-a63e-34766f4bd8c0')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('82e7df07-637b-4c91-8fb1-ce9636533bc0')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('f91fc040-cd86-4c5b-bcf1-f600803f8721')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('461cb4cf-0ac4-400d-82f0-dc5e1ab1564d')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Output"""
        self.vs[26]["GUID__"] = UUID('31b5f537-99c6-47e0-b0b8-ff5d1fcbf6a8')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Output"""
        self.vs[27]["GUID__"] = UUID('cae429e3-4467-4ab3-bb14-3d5583c35e72')
        self.vs[28]["Name"] = """1"""
        self.vs[28]["mm__"] = """Port_Input"""
        self.vs[28]["GUID__"] = UUID('5f726a9b-155f-4503-954c-c60ed5d96184')
        self.vs[29]["Name"] = """1"""
        self.vs[29]["mm__"] = """Port_Output"""
        self.vs[29]["GUID__"] = UUID('3ce1beae-c685-46be-b3e2-61673dc5f089')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('8d1f87a2-f157-4e2f-b280-8f49d3e4cd9f')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('1b0dd015-5ced-46a8-bfad-e23d24793d5f')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('ee107ff6-1e8e-4a57-936c-e5eb388fad23')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('4dbb0982-e9c3-45d9-b57c-4c905675e283')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('229cf96f-5732-4ccc-9840-708ae5757f6e')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('ffaae964-72e7-41b0-8916-b28391f56f9f')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('a4e0b250-ba7a-437e-9424-10508b86b5e3')
        self.vs[37]["mm__"] = """__Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('0769461a-5a9f-49f0-b98b-0afed05fbcab')
        self.vs[38]["mm__"] = """__Block_Inport__"""
        self.vs[38]["GUID__"] = UUID('f455ab10-afb0-4dc6-ab25-dfb193e48982')
        self.vs[39]["mm__"] = """__Block_Outport__"""
        self.vs[39]["GUID__"] = UUID('7cff4cb6-b6a5-4e5c-81b1-bd61f00e5de2')
        self.vs[40]["mm__"] = """__Block_Outport__"""
        self.vs[40]["GUID__"] = UUID('5faa11ec-bdc6-4fee-ae3b-98bd4fc4925e')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('2e6fc2d1-c60d-4c80-b865-b13d8b51d406')
        self.vs[42]["mm__"] = """__Block_Outport__"""
        self.vs[42]["GUID__"] = UUID('2f62d11a-12bf-41ea-9997-19491be4d199')
        self.vs[43]["mm__"] = """__Block_Outport__"""
        self.vs[43]["GUID__"] = UUID('bc927cf9-5e31-4acd-92df-cd5bc389eb4f')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('dec46522-5919-4a64-aaf3-98c6aec5fdc8')
        self.vs[45]["mm__"] = """__Block_Outport__"""
        self.vs[45]["GUID__"] = UUID('cf8437d0-47af-4793-9596-9cc91402b55d')
        self.vs[46]["mm__"] = """__Relation__"""
        self.vs[46]["GUID__"] = UUID('db2fcc76-d734-4e58-b168-41bbbb98a196')
        self.vs[47]["mm__"] = """__Relation__"""
        self.vs[47]["GUID__"] = UUID('4ac26e54-c5fd-40d0-9275-9d264b407f89')
        self.vs[48]["mm__"] = """__Relation__"""
        self.vs[48]["GUID__"] = UUID('8047b80b-8410-49d9-bbdc-07022ba476b9')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('1ec71742-b238-4b96-a14a-aabb8a8ae694')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('5c435c65-5a69-415d-9bed-77a891a442b9')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('c396674e-0915-4502-b92d-6e08e274e55a')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('f15e7df5-9bae-4243-8e50-b5db50634ab1')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('aef936c4-9abc-4d9a-9e87-86f1d84606f1')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('56d0f0c5-c181-4949-a009-e09017c5bd86')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('7f049c6c-3a90-4734-93d2-b4e3140540ad')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('aa3de777-6e29-42c8-9434-77eff9260175')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('fe83778b-9521-4cc4-a961-6185b7ca6a9c')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('5c25ecd7-89e7-4e5b-99b4-0a9b54f8d2aa')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('405d3e11-1290-4cf7-9d5c-3542f07cb742')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('0d0ff7d3-6ca3-4cd4-9fe8-d113227e77b0')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('a542fc10-d709-4622-9bb3-a01c2af3d0ad')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('fe185676-ae20-4fba-91ac-e91af6e677b6')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('8f5b2dbe-e66e-4b20-8819-ed1846683c4f')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('bfcf006a-4882-4d47-86fe-bbe105fde72e')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('a197d552-db84-49e2-bd44-2ec6056456a7')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('f30971fd-6eb3-4ddc-8191-e352b0e6ce77')

