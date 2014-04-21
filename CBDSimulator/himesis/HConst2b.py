

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConst2b(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConst2b.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConst2b, self).__init__(name='HConst2b', num_nodes=66, edges=[])
        
        # Add the edges
        self.add_edges([(0, 29), (29, 11), (5, 30), (30, 12), (5, 31), (31, 13), (5, 32), (32, 14), (7, 33), (33, 15), (1, 34), (34, 16), (2, 35), (35, 17), (2, 36), (36, 18), (2, 37), (37, 19), (2, 38), (38, 20), (3, 39), (39, 21), (3, 40), (40, 22), (6, 41), (41, 23), (6, 42), (42, 24), (6, 43), (43, 25), (8, 44), (44, 26), (9, 45), (45, 27), (10, 46), (46, 28), (4, 56), (56, 0), (4, 57), (57, 5), (4, 58), (58, 7), (4, 59), (59, 1), (4, 60), (60, 2), (4, 61), (61, 3), (4, 62), (62, 6), (4, 63), (63, 8), (4, 64), (64, 9), (4, 65), (65, 10), (16, 47), (47, 18), (25, 48), (48, 17), (27, 49), (49, 23), (28, 50), (50, 24), (14, 51), (51, 19), (20, 52), (52, 11), (22, 53), (53, 13), (15, 54), (54, 21), (26, 55), (55, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """Const2b"""
        self["GUID__"] = UUID('ab000818-4e4e-4294-a434-a587f73c8cd8')
        
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
        self.vs[0]["GUID__"] = UUID('13026de5-3b7e-4728-9d16-fd6bd4349638')
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
        self.vs[1]["GUID__"] = UUID('35f7fcae-c066-4692-94ac-703a2c57a602')
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
        self.vs[2]["GUID__"] = UUID('c2817121-fe19-4983-83e5-67aee7d43576')
        self.vs[3]["Name"] = """Gain"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["gain"] = 5.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Gain"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F135
aF165
aF165
aF195
a.""")
        self.vs[3]["GUID__"] = UUID('97387207-2df0-4900-af48-c84cf1980204')
        self.vs[4]["Name"] = """Const2b"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('184e30c2-46ba-42c4-ac14-b0f642a38d2e')
        self.vs[5]["Name"] = """Product"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Product"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F225
aF142
aF255
aF173
a.""")
        self.vs[5]["GUID__"] = UUID('06bec845-0678-4d60-916c-a92d1ec0aece')
        self.vs[6]["Name"] = """Product1"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F285
aF62
aF315
aF93
a.""")
        self.vs[6]["GUID__"] = UUID('be5dc622-3a8c-49d9-9498-9dac19587c13')
        self.vs[7]["Name"] = """Constant"""
        self.vs[7]["SampleTime"] = inf
        self.vs[7]["value"] = 12.34
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F45
aF152
aF90
aF188
a.""")
        self.vs[7]["GUID__"] = UUID('ab8f4ac0-9aee-4b1f-be34-763c6e3ea0b5')
        self.vs[8]["Name"] = """Constant1"""
        self.vs[8]["SampleTime"] = inf
        self.vs[8]["value"] = 7.12
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F40
aF80
aF70
aF110
a.""")
        self.vs[8]["GUID__"] = UUID('5a8131b0-a4ca-45e7-92d6-44012df7748c')
        self.vs[9]["Name"] = """Constant3"""
        self.vs[9]["SampleTime"] = inf
        self.vs[9]["value"] = 124.5
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F210
aF35
aF240
aF65
a.""")
        self.vs[9]["GUID__"] = UUID('8c78a969-ec8c-4d3e-bf01-bf6bb2d3b9af')
        self.vs[10]["Name"] = """Constant2"""
        self.vs[10]["SampleTime"] = inf
        self.vs[10]["value"] = 2.0
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["mm__"] = """Constant"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F95
aF40
aF125
aF70
a.""")
        self.vs[10]["GUID__"] = UUID('0847e4b3-10d1-4ad1-aa03-d7ac3edff825')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('557b3f2a-61e6-4e0f-9841-7a9a79d8da32')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('0d90f13f-cfbe-4a38-8ef3-458b90812237')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('21061de0-103a-4765-9a5c-93f9f6ee501d')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('861427ee-389f-4186-9937-2d916dc64690')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('3032ee93-205d-4992-b96e-7e5eda7c42f3')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('f60f0072-434a-4914-acea-7fcb84f2effa')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('14c45d81-0ff3-48be-a0d9-441e9499456e')
        self.vs[18]["Name"] = """2"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('b2fb6865-e906-4792-a0a4-4c56033b0d23')
        self.vs[19]["Name"] = """3"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('c2c50a83-7ab6-4e2d-8ccc-0347e2a62f04')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('7f6c35e4-f642-4b7f-89b6-28528af32058')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('099d8986-f5d0-46a3-938c-813f2a259b03')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('061c8281-737a-402c-a815-4c13a8340808')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('731a89cc-3412-4317-879b-7035eed50200')
        self.vs[24]["Name"] = """2"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('c3bbb64d-461b-48fc-880c-3b29d4e3d6f4')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('15188fa9-7d70-409d-9756-b833bfa55b18')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Output"""
        self.vs[26]["GUID__"] = UUID('d6fab022-8d04-4b62-96d3-b5d1ffc6f6fe')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Output"""
        self.vs[27]["GUID__"] = UUID('93e5d20b-817d-49e1-81dd-377e10fceda2')
        self.vs[28]["Name"] = """1"""
        self.vs[28]["mm__"] = """Port_Output"""
        self.vs[28]["GUID__"] = UUID('bff62a6a-f582-46f1-bab7-4b49e127c52d')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('409de0f5-ae74-403b-ad69-0194d6b2d263')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('f5d23e03-70fb-468d-a95b-af136ca9ad43')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('1d4583e0-bbce-4657-b79c-fdd46728d94c')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('31147bc9-c996-4220-9e8b-ce471fed9a3b')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('60746011-5a4f-4a49-af84-69f72b0b4c8a')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('9df3383e-b0d1-467c-af3e-3e8eae8b7353')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('925e2526-9ea3-4166-bc50-365234924859')
        self.vs[36]["mm__"] = """__Block_Inport__"""
        self.vs[36]["GUID__"] = UUID('3068c1d3-a4b4-4630-a8ce-71bf5d7ffa2a')
        self.vs[37]["mm__"] = """__Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('01a51b7a-63f3-45e7-b367-ae3c2343e30b')
        self.vs[38]["mm__"] = """__Block_Outport__"""
        self.vs[38]["GUID__"] = UUID('ce500665-097e-405d-8b8c-43145cfc9733')
        self.vs[39]["mm__"] = """__Block_Inport__"""
        self.vs[39]["GUID__"] = UUID('1ef4c3fd-d95e-45cf-be1f-1fc106385e0b')
        self.vs[40]["mm__"] = """__Block_Outport__"""
        self.vs[40]["GUID__"] = UUID('4cac1fe1-00cf-42c4-a883-912f939c7034')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('5e4c148a-4039-4d12-bc3e-b84c9d881c0b')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('99002181-69f5-4a97-a005-69b19ba84000')
        self.vs[43]["mm__"] = """__Block_Outport__"""
        self.vs[43]["GUID__"] = UUID('737c067f-52a6-423d-984e-9ff0edc67f58')
        self.vs[44]["mm__"] = """__Block_Outport__"""
        self.vs[44]["GUID__"] = UUID('901a045a-e19c-4f9b-bf2d-8076632cad9c')
        self.vs[45]["mm__"] = """__Block_Outport__"""
        self.vs[45]["GUID__"] = UUID('4fd4ea23-8045-4074-8f78-a2e8e84d06d4')
        self.vs[46]["mm__"] = """__Block_Outport__"""
        self.vs[46]["GUID__"] = UUID('981e15dd-3856-4970-8850-410fbc13cab7')
        self.vs[47]["mm__"] = """__Relation__"""
        self.vs[47]["GUID__"] = UUID('7a8b3b46-0741-4aa0-bc04-e5b47bba29f1')
        self.vs[48]["mm__"] = """__Relation__"""
        self.vs[48]["GUID__"] = UUID('c5c2f7ef-02f9-44c8-afa5-9a3555150252')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('a1c882f3-386f-4967-be69-1bf000d6d184')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('423a04d5-4c82-4483-8c04-9a59ed104b01')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('7cedf234-a1b0-47b8-95e4-b7faeb6f5bce')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('f78f9d16-4db9-4a8b-8ff8-68302265039f')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('2161760e-afab-4930-a302-59a7a5d520e7')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('f840e540-233c-4fa2-b0c2-0a4c32e48569')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('1333c4db-ba99-44b5-89b9-5c3d05124f8b')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('3eb6e85f-f427-4a27-a86d-a5df30e0bd99')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('5729df23-ba42-4823-a7a4-26b298a37e9a')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('26264420-ce73-482c-af14-37dce7282809')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('c728cf64-3e25-475d-a608-0cbe1988e0ea')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('645ae82c-07e9-42be-8cd3-02c4feffe0fe')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('bfa49fbf-a1b8-4c25-9c5e-b20e2de4423c')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('e44a64c7-7587-4bf6-a0ef-332700be9cf3')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('82786c55-ae86-4045-b4ef-7a053bbe14f8')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('071962d7-c86a-41cb-b06a-bfeafaac754d')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('ee0cfcc1-161f-4160-8c69-41816de8403b')

