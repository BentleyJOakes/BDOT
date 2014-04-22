

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_hier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_hier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_hier, self).__init__(name='HConstfolding_hier', num_nodes=71, edges=[])
        
        # Add the edges
        self.add_edges([(5, 40), (40, 30), (5, 41), (41, 31), (5, 21), (21, 12), (6, 42), (42, 32), (0, 22), (22, 13), (1, 43), (43, 33), (1, 44), (44, 34), (1, 23), (23, 14), (2, 45), (45, 35), (2, 46), (46, 36), (2, 24), (24, 15), (3, 47), (47, 37), (3, 25), (25, 16), (9, 26), (26, 17), (10, 27), (27, 18), (11, 28), (28, 19), (4, 48), (48, 38), (4, 29), (29, 20), (7, 49), (49, 39), (5, 60), (60, 1), (5, 61), (61, 2), (5, 62), (62, 3), (5, 63), (63, 9), (5, 64), (64, 11), (5, 65), (65, 7), (8, 66), (66, 5), (8, 67), (67, 6), (8, 68), (68, 0), (8, 69), (69, 10), (8, 70), (70, 4), (19, 50), (50, 33), (17, 51), (51, 34), (16, 52), (52, 36), (16, 53), (53, 39), (15, 54), (54, 37), (14, 55), (55, 35), (20, 56), (56, 31), (18, 57), (57, 30), (13, 58), (58, 38), (12, 59), (59, 32)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier"""
        self["GUID__"] = UUID('9fd244c8-98d2-434d-a64f-0970943148b8')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F140
aF65
aF170
aF95
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('ae26bab9-4a74-488c-94c3-6b25442d5c81')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["GUID__"] = UUID('99ed5f00-e337-419c-879b-29c3199acea6')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('8258ccd8-5f73-451a-8116-72a4b4865703')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["GUID__"] = UUID('a92fc9ae-2373-40d4-af55-913f05bf08bb')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F205
aF65
aF235
aF95
a.""")
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["GUID__"] = UUID('e4b8c3c0-3d7f-4752-b5ee-78a131133e11')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["GUID__"] = UUID('c3c9b078-b741-4c39-a1da-c8b684b2517c')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('30c70ba8-a365-4605-8efc-8ad0f100f134')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F365
aF103
aF395
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('4326cafd-dc16-4c12-b178-a2340511fd16')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('d632d5c1-bfda-4340-b0a1-40648d2b19cc')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F150
aF118
aF180
aF132
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('eca26949-509e-43f0-bc9c-7016d81d2533')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('2f9deda6-b261-4ea6-b738-3e6551083061')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F150
aF88
aF180
aF102
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('613d74f5-5abc-49b0-93aa-b3014fc10de7')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('e83a2e26-a1cb-4719-97d6-1b18616cef63')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('ab3bf766-5179-474c-98b6-440b902624db')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('72fd4610-9ebe-498a-83c3-1bb5e3ca4253')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('e0fb2222-6aa8-4e3c-a4e9-b4cc14add666')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('426be57e-d722-4fec-a17e-7fce0f73064b')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('03e7536e-ebee-4fb7-9bf5-2300646368b3')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('21e867d0-82c7-45cb-a437-73d9c87e6f1f')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('6d134257-e708-4132-90e2-ada60af3bec7')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('68c3c46c-5bca-4da9-a9b9-3ea5096bbfcb')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('0dc5f115-4f43-4874-b1db-5276cd0552ae')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('a458d816-ad57-45d8-a883-75e7cf69c862')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('fb86d1d9-fbdc-4e75-815b-2b9116c24bc7')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('4bf9b174-ba47-4ab4-a297-f42cdbc78180')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('0c8124f6-10cc-414f-b064-7efc2309425d')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('70e986c3-9759-41e6-bb53-4a2122569471')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('ea3e5029-e7b0-4622-a283-3576cdd0ed87')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('2b717781-a7cf-4ade-919c-572bb3872b2c')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('855c8c89-d8e8-47ca-9c32-f6128b951bdf')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('9b74ee94-e009-4628-8930-32879eb1b5d3')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('4ac81080-9955-4400-af86-46da9fe5561d')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('28e5eebc-ee1e-4d92-ae9b-dfee8525810c')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('6fa3f8ef-507d-44c6-b7b5-5a764422493f')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('be22b046-b970-4540-b2d9-cc4daa0702cc')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('bbeb68ca-5a6d-4f74-aecf-b69d9887a279')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('b03b1cba-eb74-4d9b-8d02-fbe2f3f8998c')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('f423384b-e7a1-4de7-94ef-46becca02deb')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('c2ea3d18-63f4-4f9a-9602-90fbda3092f6')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('047efa64-c14e-48de-8f3e-96eb4a1e3882')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('8e1f9aa0-7e88-4002-b53d-2014546d3dc6')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('16ded58d-4874-402c-888b-cb8d64155c3f')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('31b568b6-068d-44a7-8797-a2366f0768c1')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('a67004b4-cf05-4e42-b4b7-3d8bbd5f74ff')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('b8b6e6eb-e563-4b47-8d75-352863d1b1de')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('fd18a72f-c0e0-4357-9841-94d315460bcb')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('0e3dc47d-bccb-4174-a95d-0edee6db86a8')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('9d0eec03-0c05-404c-badf-cbf2165b5207')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('33451c17-d845-4215-912d-4b0ed38992e5')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('76dd5a80-d3a3-4784-8513-4a081c6024fe')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('d5ff3c44-96b0-4898-bd12-1185730f9e46')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('e1184844-a0e8-4933-ac37-bf751fbfe576')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('18536296-569c-4742-9a53-a9fa53b384c5')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('0eeca4c6-2a1d-4c61-9bf2-94cfd7e542a3')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('171fa971-0f48-4fcf-a44e-f4430bce3a78')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('7a6fd786-b828-4fd5-b8d7-edf2876dab33')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('b6ff41bf-d532-4f2d-9eec-228cca5a97ac')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('95cdf2a1-ecb9-4b89-96a5-e258ab6b048b')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('6be6e11b-e794-47e0-b958-bd3fb35c22bc')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('4d056eed-2450-4ea7-b9ed-9bc81c855c02')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('6a3a8921-e486-49a2-ae4f-ee06e84b3343')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('2065c40f-f2c8-4190-b408-e7510d24ed55')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('cd76d7ab-799c-4cc5-93b5-02ee9ae3a7dd')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('28ab1294-602d-48ff-a8c3-4a43eeece22c')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('c4092d88-0e1c-470f-a7e1-490fee16ca50')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('6afc9ca4-2b41-4367-97ef-4b7c61c0474e')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('fadb37c8-af69-436a-ad17-a05590bdb526')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('d6cc17ea-d7a3-414c-a3f9-09fe5f949d44')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('46832446-d571-42a1-b91e-c6087adf8ace')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('5eda95d8-0514-4363-987e-638f60e206bb')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('506365ec-2760-4681-97c2-11aa3e843dcb')

