

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HDeadBlock1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HDeadBlock1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HDeadBlock1, self).__init__(name='HDeadBlock1', num_nodes=50, edges=[])
        
        # Add the edges
        self.add_edges([(0, 28), (28, 21), (1, 29), (29, 22), (1, 30), (30, 23), (1, 15), (15, 9), (5, 16), (16, 10), (6, 17), (17, 11), (7, 18), (18, 12), (2, 31), (31, 24), (2, 32), (32, 25), (2, 33), (33, 26), (2, 19), (19, 13), (3, 34), (34, 27), (8, 20), (20, 14), (4, 42), (42, 0), (4, 43), (43, 1), (4, 44), (44, 5), (4, 45), (45, 6), (4, 46), (46, 7), (4, 47), (47, 2), (4, 48), (48, 3), (4, 49), (49, 8), (14, 35), (35, 26), (12, 36), (36, 24), (10, 37), (37, 25), (13, 38), (38, 22), (9, 39), (39, 21), (9, 40), (40, 27), (11, 41), (41, 23)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """DeadBlock1"""
        self["GUID__"] = UUID('70698c54-3ef5-42fc-9e8d-222beb38d583')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F430
aF88
aF460
aF102
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('5412e238-fa18-4366-b162-778be10a1b88')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F315
aF157
aF345
aF188
a.""")
        self.vs[1]["GUID__"] = UUID('1955a52d-0b64-408f-864f-03d97c623398')
        self.vs[2]["Name"] = """Switch"""
        self.vs[2]["Threshold"] = 0.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Criteria"] = """u2 >= Threshold"""
        self.vs[2]["mm__"] = """Switch"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F185
aF90
aF235
aF130
a.""")
        self.vs[2]["GUID__"] = UUID('ea640a93-234c-4082-82eb-751718f67f93')
        self.vs[3]["NumInputPorts"] = """1"""
        self.vs[3]["Name"] = """Scope"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Scope"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F430
aF154
aF460
aF186
a.""")
        self.vs[3]["LimitDataPoints"] = """on"""
        self.vs[3]["GUID__"] = UUID('70ef7bbf-ef5f-4ccf-96c1-4e4baefa0cc7')
        self.vs[4]["Name"] = """DeadBlock1"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('f92bc91e-7154-4f87-888c-ff73389e20c0')
        self.vs[5]["Name"] = """Constant"""
        self.vs[5]["SampleTime"] = inf
        self.vs[5]["value"] = 10.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F45
aF70
aF75
aF100
a.""")
        self.vs[5]["GUID__"] = UUID('9a73de95-6e19-47a6-bf6a-d7127980141a')
        self.vs[6]["Name"] = """In1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Inport"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F175
aF198
aF205
aF212
a.""")
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('6321d312-8024-4d83-8148-662a998ba5ed')
        self.vs[7]["Name"] = """In2"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Inport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F45
aF23
aF75
aF37
a.""")
        self.vs[7]["Port"] = 2
        self.vs[7]["GUID__"] = UUID('2fe56f8c-ebde-4b12-b785-ee894450e244')
        self.vs[8]["Name"] = """Constant1"""
        self.vs[8]["SampleTime"] = inf
        self.vs[8]["value"] = 123.7
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F25
aF140
aF55
aF170
a.""")
        self.vs[8]["GUID__"] = UUID('e44ada7a-ddbf-49e2-b0dc-bac7fb76c35d')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('efcdb4c7-89c1-43ae-b950-fe2d41cb9c18')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('ae814a48-db26-4be4-b7c3-eb72f34ac669')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('1ffac920-70ad-41a9-8a38-b3f61b286ba5')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('8e9167db-046a-4bae-9931-acf534294bbf')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('6d701b1d-211a-4972-b320-91072fde6aa9')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('0d5eb310-56d5-4895-b021-068078e70d87')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('ff92e5ad-35a5-46f9-82a5-dc6f2ac42168')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('c781edc5-db12-4060-a4e3-a53b5386eadc')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('50a2ef29-8f7d-4d84-81e2-85e82565d73c')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('22ed13f1-49b5-449a-8bf8-38ca43a0dc47')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('ab6588fb-ba47-4287-9b9e-3359229f417a')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('885b2392-393f-4b51-ab05-10a8fb469dd1')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('02452d8a-9069-42d6-bade-dc302425e165')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('d9794469-fb23-4b3e-932a-3c9e1faae3f0')
        self.vs[23]["Name"] = """2"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('7c7cbbe6-5167-4214-9a10-8a25fc27b1ef')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('081c0803-a9ca-4e4d-9418-bb3e699b5e20')
        self.vs[25]["Name"] = """2"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('96d9054b-5aec-43d6-8c8e-21b522ef59ba')
        self.vs[26]["Name"] = """3"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('217c24e9-0ca9-45df-a89d-39ce52ec5dc7')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Input"""
        self.vs[27]["GUID__"] = UUID('86bc6327-0b3c-45a6-8d73-9ff6656d3e0d')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('ef151c63-25a6-4e46-90ae-8ea34a5b62a7')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('c920d850-c316-4099-8874-98a2a2187797')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('65a57efd-a019-42c7-9b23-ff24a35791bf')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('8995fccd-1ce7-48b7-a2a2-49d105d3f7e6')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('4a79f9ca-c31d-4cf7-9b9b-741d4f27aa32')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('39177873-8e6e-452d-8057-05b9850150c1')
        self.vs[34]["mm__"] = """__Block_Inport__"""
        self.vs[34]["GUID__"] = UUID('740f4ac3-a0d4-4a8d-8801-27af84eb6e99')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('5960e0ad-d709-4895-8c1c-6118c39f918e')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('f6e50836-4c17-438c-8407-ad202e76ca25')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('01220769-e549-4b82-a816-a036e25d8c35')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('de9ba9d8-cf06-422f-9340-6c775bf132a5')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('9413a535-1671-4dfe-b006-159c3879badc')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('03a03514-2305-47b9-936a-77e7dcf4edf9')
        self.vs[41]["mm__"] = """__Relation__"""
        self.vs[41]["GUID__"] = UUID('fbd8c934-0acb-4dd7-b81a-b9804876a143')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('544e3a23-1990-4b6b-b59a-5fc4959abfc6')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('87b6ee40-0254-4a87-817e-a1e2384c9e52')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('bb8fc014-e2c8-4531-8358-56e8b5337d06')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('aa9fb89e-557a-4609-b877-e2d0235e8a4d')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('2da9cb23-1eca-4e2b-8e7d-dbe8200c5084')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('b0e2e245-b7d9-433d-a142-1c5757e0aa1a')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('320ce40b-b838-4a4a-b018-5ecf276766cc')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('edc282d7-a9a1-4fff-a193-8b2ade55343d')

