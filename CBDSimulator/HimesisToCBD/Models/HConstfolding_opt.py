

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_opt, self).__init__(name='HConstfolding_opt', num_nodes=52, edges=[])
        
        # Add the edges
        self.add_edges([(1, 28), (2, 51), (2, 50), (2, 49), (2, 48), (2, 47), (2, 46), (2, 45), (2, 44), (3, 33), (4, 36), (5, 24), (6, 30), (9, 23), (10, 38), (11, 25), (12, 26), (13, 27), (14, 39), (15, 29), (16, 37), (17, 42), (18, 32), (19, 40), (20, 43), (21, 35), (22, 41), (44, 5), (45, 0), (46, 1), (47, 6), (48, 7), (49, 3), (50, 8), (51, 4), (23, 5), (24, 10), (25, 0), (26, 1), (27, 1), (28, 14), (29, 6), (30, 16), (31, 17), (32, 3), (33, 19), (34, 20), (35, 4), (36, 22), (37, 11), (38, 15), (39, 9), (40, 13), (41, 12), (42, 18), (43, 21), (7, 31), (8, 34)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_opt"""
        self["GUID__"] = UUID('767f030e-b3f0-46d4-b311-2f2841d21574')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F920
aF63
aF950
aF77
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('069f5384-85bb-4d92-837f-8ae3b0da586a')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F685
aF47
aF715
aF78
a.""")
        self.vs[1]["GUID__"] = UUID('41550ccf-c878-4578-9b55-7934347d6041')
        self.vs[2]["Name"] = """constfolding"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('a1e21951-dddf-43b4-a865-febaaf24c428')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay1"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F605
aF78
aF640
aF112
a.""")
        self.vs[3]["GUID__"] = UUID('fa4da419-453e-475d-93eb-4524917ea764')
        self.vs[4]["InitialCondition"] = 0.0
        self.vs[4]["Name"] = """Unit Delay"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """UnitDelay"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F605
aF13
aF640
aF47
a.""")
        self.vs[4]["GUID__"] = UUID('b7a47306-daba-41a8-815f-e5b90c279396')
        self.vs[5]["Name"] = """Gain2"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["gain"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Gain"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F775
aF55
aF805
aF85
a.""")
        self.vs[5]["GUID__"] = UUID('a68e11db-9a99-406b-8852-5777fbf58443')
        self.vs[6]["Name"] = """Gain3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["gain"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Gain"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F865
aF55
aF895
aF85
a.""")
        self.vs[6]["GUID__"] = UUID('a6fa8b96-2bab-46d1-9d90-dc4852bbe1d3')
        self.vs[7]["value"] = 36.6
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["GUID__"] = UUID('7d717b2d-b27a-47d6-94eb-473abe781efc')
        self.vs[8]["value"] = 16.253
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["GUID__"] = UUID('e3a6ea06-1ba0-408c-954b-4554f78edbfb')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('e3b9b64a-a943-4a40-bc59-1567b6080142')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('f0bfe98d-0bfe-438d-b63f-c3a6c85bcd28')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('7540be81-bece-4a45-85ba-ecfab8dbc132')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('3bc5b92c-0405-4d93-a0af-a5332fcef7ff')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('5647de68-b53b-4dc4-81c2-e42e5032863f')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('6a207e73-7aa3-455d-ae1f-2d3a1b2c644d')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('61067a66-54d7-4303-bfaf-42076e783e33')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('1e92ca06-a1a3-4cfa-a8e4-1e1d7bee491f')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('020adb6a-d299-481e-a659-5b5d08c1e7ea')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('77c77410-4a87-49f1-992f-128be02638a1')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('9679fffa-a5b6-4d69-b115-82b71d49008f')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('d451f496-6e14-4a60-9848-bf6fbfe0193b')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('edbfc46d-b0e5-4df7-b95a-25e0085a4832')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('878b3630-7634-4112-a56c-8c640deca6d2')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('2499f745-5985-4dd3-819e-e7a8633e4ef4')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('447e2432-56d4-4e30-a9a0-081ebbd56ab7')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('ab335821-953c-4611-a161-4360c79a245d')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('6436aa2c-f990-44df-b470-b5102e2c731c')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('e52cb5a4-80d2-46e5-9797-269dc01d04fb')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('31399099-df1d-49bc-97fa-a28015a20716')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('546156cc-4007-478a-8af8-86132aaf790e')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('c50dd2ca-01d4-4702-a1d8-d0647f24d030')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('a1bae37f-3e65-4e0d-b0f0-5f5ef3e95572')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('5c7c36f0-038f-4b91-8fdd-774c4e5eef7c')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('9e25b437-968d-4a96-a951-cdfce0ee0010')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('ca9e7929-3f2e-4d7f-a2cc-9c5277fe718d')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('21322c33-7c06-42a0-9e88-1b2fd8f0f38d')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('0b75b788-522b-4e0b-ad1b-f2ac5075459d')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('9e21dd6a-83f6-4c80-b69e-1a1fba33c76f')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('b29908e5-20a5-4f62-a1f0-2e81bbc4c996')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('23625c29-d120-443f-a867-ec68d0ad04ab')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('b4a5fbdc-6cd6-4549-a07b-510d17ae868f')
        self.vs[41]["mm__"] = """__Relation__"""
        self.vs[41]["GUID__"] = UUID('a11e7d8b-ca2e-4959-be1c-96ea9c3b2c8b')
        self.vs[42]["mm__"] = """__Relation__"""
        self.vs[42]["GUID__"] = UUID('0d8e2c2d-136f-4999-b3da-46b23334295c')
        self.vs[43]["mm__"] = """__Relation__"""
        self.vs[43]["GUID__"] = UUID('492ac5fd-cb46-47e4-9a74-d00f9ffc2d6b')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('d116a589-98bf-488b-b416-8bedb0c4a10a')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('e2f42570-6c6e-448c-ba30-ece3eaef8289')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('3ac5a230-fcec-4978-93a9-af1236d7b790')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('10ed88d4-533f-4325-a93a-abef4dd6fbee')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('c3d3db25-0b05-4790-850f-64213bd545b6')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('9f5e394e-2d6e-41ee-bf3c-58cd728fe936')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('5d59fa20-c02e-41cf-bd48-6fd742c38b26')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('fabc4e0f-6b11-4283-a3a6-46efeb837658')

