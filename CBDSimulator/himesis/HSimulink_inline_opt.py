

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimulink_inline_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimulink_inline_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimulink_inline_opt, self).__init__(name='HSimulink_inline_opt', num_nodes=67, edges=[])
        
        # Add the edges
        self.add_edges([(1, 39), (2, 40), (6, 31), (7, 34), (8, 36), (10, 42), (11, 43), (12, 45), (13, 66), (13, 65), (13, 64), (13, 63), (13, 62), (13, 61), (13, 60), (13, 59), (13, 58), (13, 57), (13, 56), (13, 55), (13, 54), (30, 14), (15, 51), (32, 16), (33, 17), (18, 48), (35, 19), (20, 47), (37, 21), (38, 22), (23, 52), (24, 53), (41, 25), (26, 49), (27, 50), (44, 28), (29, 46), (0, 30), (31, 15), (7, 32), (7, 33), (34, 18), (8, 35), (36, 20), (1, 37), (1, 38), (39, 23), (40, 24), (10, 41), (42, 26), (43, 27), (12, 44), (45, 29), (46, 22), (47, 21), (48, 28), (49, 17), (50, 25), (51, 16), (52, 14), (53, 19), (54, 0), (55, 6), (56, 7), (57, 8), (58, 1), (59, 2), (60, 9), (61, 3), (62, 4), (63, 10), (64, 11), (65, 5), (66, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimulink_inline_opt"""
        self["GUID__"] = UUID('79721f00-8f0d-4fd4-a904-1b1cc6674d0e')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F555
aF68
aF585
aF82
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('4bffccce-0a19-47ad-addd-5cff1d1ba972')
        self.vs[1]["Inputs"] = """++"""
        self.vs[1]["Name"] = """Sum"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Sum"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F485
aF57
aF515
aF88
a.""")
        self.vs[1]["IconShape"] = """rectangular"""
        self.vs[1]["GUID__"] = UUID('7048666f-886f-4856-a7ec-b715918ab27a')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F95
aF23
aF125
aF37
a.""")
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('a163e2c0-0fbe-44af-82eb-c487dd9220b5')
        self.vs[3]["Name"] = """View Optimization"""
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["mm__"] = """rtwdemowidgets/View Optimization"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F323
aF315
aF449
aF375
a.""")
        self.vs[3]["GUID__"] = UUID('aa026781-6657-4df8-b016-699f496af436')
        self.vs[4]["Name"] = """Build GRT"""
        self.vs[4]["BackgroundColor"] = """lightBlue"""
        self.vs[4]["mm__"] = """rtwdemowidgets/Build GRT"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F20
aF315
aF149
aF375
a.""")
        self.vs[4]["GUID__"] = UUID('65f28dc4-68fb-4e2f-95fa-0e6b857452cd')
        self.vs[5]["Name"] = """Build ERT"""
        self.vs[5]["BackgroundColor"] = """lightBlue"""
        self.vs[5]["mm__"] = """rtwdemowidgets/Build ERT"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F170
aF315
aF299
aF375
a.""")
        self.vs[5]["GUID__"] = UUID('aae2ea9c-cc2c-4e94-8ce5-21ea73b913de')
        self.vs[6]["Name"] = """Constant"""
        self.vs[6]["SampleTime"] = """inf"""
        self.vs[6]["value"] = """MAX_LIFT"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F75
aF77
aF155
aF103
a.""")
        self.vs[6]["GUID__"] = UUID('c3a4e4cd-24e7-4805-ab75-76c5f6c45aa0')
        self.vs[7]["Name"] = """2D Lookup"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Lookup_n-D"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F315
aF72
aF365
aF143
a.""")
        self.vs[7]["GUID__"] = UUID('0097bf58-a2c1-4f31-8931-8fe965df2e48')
        self.vs[8]["Name"] = """G1"""
        self.vs[8]["SampleTime"] = -1.0
        self.vs[8]["gain"] = 2.0
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Gain"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F290
aF16
aF335
aF44
a.""")
        self.vs[8]["GUID__"] = UUID('d8cb68e2-a33c-4544-9392-06fef493776a')
        self.vs[9]["Name"] = """Inline Parameter Setting1"""
        self.vs[9]["BackgroundColor"] = """yellow"""
        self.vs[9]["mm__"] = """SubSystem"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F473
aF315
aF601
aF376
a.""")
        self.vs[9]["GUID__"] = UUID('38386be4-4f2f-4e1c-8404-f5cdb6165f63')
        self.vs[10]["Name"] = """1D Lookup"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["mm__"] = """Lookup_n-D"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F215
aF113
aF265
aF137
a.""")
        self.vs[10]["GUID__"] = UUID('03be4ad9-7422-4554-93f6-b2e9ed6632fb')
        self.vs[11]["Name"] = """Constant1"""
        self.vs[11]["SampleTime"] = """inf"""
        self.vs[11]["value"] = """SLIDER_POS"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["mm__"] = """Constant"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F75
aF112
aF155
aF138
a.""")
        self.vs[11]["GUID__"] = UUID('29d55841-9ff7-4451-9ec9-c060ed1c08d1')
        self.vs[12]["Name"] = """G2"""
        self.vs[12]["SampleTime"] = -1.0
        self.vs[12]["gain"] = -2.0
        self.vs[12]["BackgroundColor"] = """white"""
        self.vs[12]["mm__"] = """Gain"""
        self.vs[12]["Position"] = pickle.loads("""(lp1
F400
aF95
aF440
aF125
a.""")
        self.vs[12]["GUID__"] = UUID('232644f4-6e74-46c9-8686-e789b32bd9f9')
        self.vs[13]["Name"] = """simulink_inline"""
        self.vs[13]["mm__"] = """SubSystem"""
        self.vs[13]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[13]["GUID__"] = UUID('2bff86f5-ae7f-4f1f-a157-3bea223d01fb')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Input"""
        self.vs[14]["GUID__"] = UUID('f9bdeb28-f4b4-4267-9124-2ed1e6283d83')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('361031d7-bad5-4318-bc69-38814a73cd1b')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Input"""
        self.vs[16]["GUID__"] = UUID('c4f16e4d-0d39-4b66-9108-019af0249837')
        self.vs[17]["Name"] = """2"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('1c53cc2d-15c5-426c-9e7b-a5f6a76bcdfa')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('2c54eb61-9f99-4e8b-964d-854a6d2bd397')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('8437bdd6-d618-45da-9376-6be71e8c4fc9')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('ddbbc0fd-6989-4473-ba62-1a536592bf41')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('1b5073f8-4fc2-4ed6-94d6-5ed4cb688a43')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('46e659e6-1e38-4b49-b2a5-381e95792657')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('1beb0ca5-d35c-4ae3-b0c9-6655c2851f0c')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('b404c39c-3a66-4695-bec0-5eb718ceb79b')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('70cc2ad4-0b8f-4e3d-87fd-479a17f1ed09')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Output"""
        self.vs[26]["GUID__"] = UUID('42ebec7f-66ac-405c-8249-68f63bdddc9c')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Output"""
        self.vs[27]["GUID__"] = UUID('0db19eba-0fe3-43ee-b871-3fc221d3c8f2')
        self.vs[28]["Name"] = """1"""
        self.vs[28]["mm__"] = """Port_Input"""
        self.vs[28]["GUID__"] = UUID('1752294f-3e25-4054-9b15-e6ba7615ddf8')
        self.vs[29]["Name"] = """1"""
        self.vs[29]["mm__"] = """Port_Output"""
        self.vs[29]["GUID__"] = UUID('ecd2ebdc-101b-47c7-b35d-528c73c420cc')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('e885758e-bda0-4525-bb88-b3d39580e4ca')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('7a0a521a-7b4a-484f-8d1c-0068b1513bd2')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('3d3bf014-de9d-48e3-a274-456f15207c59')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('63a936ab-9583-4f53-b6cd-4c2829d2cfe9')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('8ec2ea60-d1ec-4847-b69e-15100e5f7337')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('a2d547ac-bd2c-4616-a077-094385221765')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('cce1b4c5-fc73-41ca-8a31-d2d00d599e0e')
        self.vs[37]["mm__"] = """__Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('3eb7b1b5-5f7e-4423-bfc3-3d2f03ff6d2c')
        self.vs[38]["mm__"] = """__Block_Inport__"""
        self.vs[38]["GUID__"] = UUID('441487f8-cbae-444c-a3e2-dbe7f47ac696')
        self.vs[39]["mm__"] = """__Block_Outport__"""
        self.vs[39]["GUID__"] = UUID('3a597588-a6fb-49fc-8989-17b366e99e81')
        self.vs[40]["mm__"] = """__Block_Outport__"""
        self.vs[40]["GUID__"] = UUID('7904de68-7728-49ea-90a5-da239b7633fa')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('03a49e84-7b1b-4298-9fc7-48b8dd6e8261')
        self.vs[42]["mm__"] = """__Block_Outport__"""
        self.vs[42]["GUID__"] = UUID('8094b2a9-5c0b-47ef-be40-0f7ae83f6206')
        self.vs[43]["mm__"] = """__Block_Outport__"""
        self.vs[43]["GUID__"] = UUID('e5c691c4-d53d-49cc-bb73-56da375b511f')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('931ccb17-ab34-4246-85e2-ca9b54049eed')
        self.vs[45]["mm__"] = """__Block_Outport__"""
        self.vs[45]["GUID__"] = UUID('acf19c43-3daa-451e-a333-ec785b1e022a')
        self.vs[46]["mm__"] = """__Relation__"""
        self.vs[46]["GUID__"] = UUID('f59e0ad3-e772-437c-9c03-be1829dd4fce')
        self.vs[47]["mm__"] = """__Relation__"""
        self.vs[47]["GUID__"] = UUID('497de6d7-35a6-4ff7-92f3-b64d7d06c156')
        self.vs[48]["mm__"] = """__Relation__"""
        self.vs[48]["GUID__"] = UUID('3ca1d7ec-637f-4520-99c3-1f644dd508d1')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('db34a27d-a40c-4df8-b2cd-886f0896c99f')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('c76b3377-e41e-4811-87a4-6725b7bdf13d')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('843a5370-152a-49e4-9316-c177d1e138ae')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('4a865a9b-3845-4611-9fbf-0da95817185a')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('fba2fe0b-4d19-4648-a413-503967c20954')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('e5dd2206-c099-4007-a4c3-c8287be7d1bf')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('6fd6ca04-e38f-4ec0-b622-0c7176e91e95')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('19a3cbd0-6a55-4e11-8298-66cca3ab2bee')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('777114a6-2677-41f4-9f9e-89dc77581f3e')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('701f7a5e-8f70-42e6-abaf-449af1a3d016')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('98ab8ab5-bbdb-49e4-b2f4-3cca5566e179')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('5ab507fe-1d11-42b2-a2b8-650639f4ad93')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('8ea5c163-5270-466f-8af7-d03cd1ee1b86')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('8ae8b043-bd91-4062-b091-c4e1c57b59be')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('b1d86afc-f87d-4b5d-a308-15971c3341c0')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('b5ab03dd-18a1-4c74-b7b7-0bc0c1b91ac2')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('be0a9505-be8c-4458-8c27-ebd1457d4fd5')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('e9467176-185c-4ada-8265-b680d07732cc')

