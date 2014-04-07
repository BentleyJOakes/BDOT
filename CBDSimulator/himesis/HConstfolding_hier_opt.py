

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_hier_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_hier_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_hier_opt, self).__init__(name='HConstfolding_hier_opt', num_nodes=68, edges=[])
        
        # Add the edges
        self.add_edges([(0, 29), (1, 30), (2, 31), (3, 32), (4, 36), (5, 62), (5, 61), (5, 60), (5, 59), (5, 58), (5, 57), (5, 28), (8, 67), (8, 66), (8, 65), (8, 64), (8, 63), (9, 33), (10, 34), (11, 35), (12, 43), (13, 46), (14, 44), (15, 42), (16, 38), (17, 45), (18, 39), (19, 18), (20, 17), (21, 15), (22, 14), (23, 13), (23, 12), (27, 16), (28, 19), (29, 20), (30, 21), (31, 22), (32, 23), (33, 24), (34, 25), (35, 26), (36, 27), (47, 37), (48, 38), (49, 39), (50, 40), (51, 41), (52, 42), (53, 43), (54, 44), (55, 45), (56, 46), (5, 47), (5, 48), (6, 49), (1, 50), (1, 51), (2, 52), (2, 53), (3, 54), (4, 55), (7, 56), (57, 1), (58, 2), (59, 3), (60, 9), (61, 11), (62, 7), (63, 5), (64, 6), (65, 0), (66, 10), (67, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('032263ea-1ceb-4473-ab65-7d3b31eaa6ca')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F125
aF125
aF155
aF155
a.""")
        self.vs[0]["GUID__"] = UUID('90df6c85-5178-418a-9248-cb331d85833c')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["GUID__"] = UUID('b8823b48-c616-451e-88a0-b991bbf3ac22')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F275
aF100
aF295
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('19ecde77-52b0-45f4-9cf9-170464305e2b')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F325
aF93
aF360
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('a5e72416-64aa-4509-bd0e-44b5dfbecb4d')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F215
aF125
aF245
aF155
a.""")
        self.vs[4]["GUID__"] = UUID('d6a2dc4d-7bc7-448c-ba28-45cd5eaedc50')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F320
aF24
aF420
aF66
a.""")
        self.vs[5]["GUID__"] = UUID('24f03ea7-fc7c-47a3-9cb1-3878d560f96c')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F485
aF38
aF515
aF52
a.""")
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('f8e8350d-83b3-4346-97c2-a98b9e5a8618')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F425
aF103
aF455
aF117
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('afeee1c8-caec-4f0b-9997-15d0236b2da4')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["GUID__"] = UUID('4c8868b2-f2a2-4f3d-b169-e05be6650c66')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F90
aF153
aF120
aF167
a.""")
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('7f692354-a4fc-4832-9514-c214d1b814d9')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('f6109ac8-53b0-4c22-be8b-22e89a135ffd')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('3600fa44-1358-4307-a5de-e4f13b5663fc')
        self.vs[12]["mm__"] = """__Relation__"""
        self.vs[12]["GUID__"] = UUID('d50f2810-b706-48f1-8a1e-c0c2191ee981')
        self.vs[13]["mm__"] = """__Relation__"""
        self.vs[13]["GUID__"] = UUID('50a1840f-ae80-4aba-8024-f95e3948bbb6')
        self.vs[14]["mm__"] = """__Relation__"""
        self.vs[14]["GUID__"] = UUID('a4064a89-7c0e-40f7-8cb1-1191350ffad0')
        self.vs[15]["mm__"] = """__Relation__"""
        self.vs[15]["GUID__"] = UUID('ccf320ff-a8b1-44f7-b743-5d6a33cf8b20')
        self.vs[16]["mm__"] = """__Relation__"""
        self.vs[16]["GUID__"] = UUID('b818d880-a987-4b4f-b2f1-c8f8b9e03d4b')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('44488f7f-8380-459d-b0dc-ff771b6ccd3c')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('a33707f9-fe2f-4573-88f7-0e2791106e3c')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('b6a50496-2dfe-4afa-ace0-7bc89dae2751')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('04a38215-725d-4666-95ef-b9ba556e4e82')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('162ea952-23d6-4dc0-8c94-b4786f2e2537')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('5bde281d-0479-41b6-89a6-6a97b190f1a2')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('a31c87be-ae17-4fdf-afa4-e54eb17bea72')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('ee8ae99d-87ea-4817-a8f4-607305f4ccef')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('dd169c54-9367-4935-a26c-c24b22f00540')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Output"""
        self.vs[26]["GUID__"] = UUID('f9f949b7-c4fe-44ab-9710-df170d7b382c')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Output"""
        self.vs[27]["GUID__"] = UUID('b31e20b5-5e1c-4577-920e-cf6352170b84')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('5ef290c5-df6b-4eae-908d-deaf93fcfc5f')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('059f6fab-106a-4ac2-852a-134484c305f7')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('cd341607-2983-4fbb-be57-b930b49bb8d1')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('ac23439d-a459-4690-8811-c60c563e582f')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('2ade019d-afca-4a00-90e5-0994ca3db439')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('f83f2815-7d95-42c1-a055-85154617f680')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('728bedb2-989e-4c2e-aba1-284d9f7ac399')
        self.vs[35]["mm__"] = """__Block_Outport__"""
        self.vs[35]["GUID__"] = UUID('d33c2fac-8f7c-4439-9450-f2889c3cf1d3')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('0df0e259-bd11-4845-b16e-2a5794477ed0')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('1adee5f7-a196-48b8-a2eb-acea63e0eda1')
        self.vs[38]["Name"] = """2"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('407769f9-fb40-4494-8ae7-638e1470e214')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('cb3284e1-0efa-4c95-b59f-8f9d302d97b0')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('f5c18642-59db-44e9-a7f7-d6fa72c3f752')
        self.vs[41]["Name"] = """2"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('6cc0b4ba-6fc0-4a8f-9886-d9d31dcae730')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('f6e07b94-c271-4539-9181-f2dbbb8729c3')
        self.vs[43]["Name"] = """2"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('f5d15d55-dab5-49a9-8e1c-94b56e03892a')
        self.vs[44]["Name"] = """1"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('6beeb7e4-1de9-4a08-afa8-e37ec90a146f')
        self.vs[45]["Name"] = """1"""
        self.vs[45]["mm__"] = """Port_Input"""
        self.vs[45]["GUID__"] = UUID('dbfff8a7-ed5e-4fd3-8a97-563b221ee45f')
        self.vs[46]["Name"] = """1"""
        self.vs[46]["mm__"] = """Port_Input"""
        self.vs[46]["GUID__"] = UUID('8824bb86-0a5c-4241-b8e1-944326892fff')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('cfe8a5ed-c587-4f52-8e67-973cf59b6b08')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('c03810fb-0857-4c70-b5ed-f4f83673ed4d')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('8cd4e8e9-cdcd-48cb-b202-a8f2edbc1e2e')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('862f86ae-5fa6-4b6d-8cc0-0d5da933a1b0')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('261996a9-75b7-485d-bf06-1cc2714608f5')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('c07d61b7-e728-4ab6-868e-bd9783883060')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('34cc2d54-09b6-40a3-9e45-a44a67c9d9e0')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('d0c40090-1d4b-4ac6-b99b-9b27996319b8')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('feef8128-047c-46b3-bfe7-0f4684ce26f5')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('7987bd43-aa24-4756-9683-a6f17af87dd5')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('55d0f01d-f29d-477f-8c21-0ec20c4a50b1')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('06502023-f20c-4dc3-8ee3-ffcbec19d060')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('6f15fd78-aa5a-4f91-8dce-f05eceffdcd8')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('b2e88a67-44a4-4989-8a55-34aba2f43279')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('8d621ee8-d07b-4805-8d86-4336ddfa1e67')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('abf25919-75a3-4a72-a2a3-597037e18e9f')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('79e00f04-99c2-4b62-a3b7-21d9e1af3d94')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('5e1e24c4-28c6-49f7-bf18-48799ae14a69')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('a5846f25-1f71-4a62-9ac2-fa6fafc9030d')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('c0e020a2-f96a-4ea7-95c7-6ec58b077704')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('1322ff10-92f7-4356-a9a3-e8df461fedff')

