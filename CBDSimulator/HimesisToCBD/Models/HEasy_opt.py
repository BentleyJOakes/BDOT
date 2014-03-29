

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
        
        super(HEasy_opt, self).__init__(name='HEasy_opt', num_nodes=38, edges=[])
        
        # Add the edges
        self.add_edges([(0, 11), (1, 13), (2, 37), (2, 36), (2, 35), (2, 34), (2, 33), (2, 32), (5, 12), (6, 14), (7, 28), (8, 31), (9, 27), (10, 30), (10, 29), (11, 7), (12, 8), (13, 9), (14, 10), (17, 22), (18, 23), (19, 24), (20, 25), (21, 26), (22, 0), (23, 0), (24, 3), (25, 1), (26, 4), (27, 19), (28, 21), (29, 18), (30, 20), (31, 17), (32, 15), (32, 0), (33, 3), (34, 5), (35, 16), (35, 1), (36, 4), (37, 6), (15, 11), (16, 13)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HEasy_opt"""
        self["GUID__"] = UUID('24946a68-4e87-4c9a-a37c-66d36a76240e')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Product"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["mm__"] = """Product"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F240
aF82
aF270
aF113
a.""")
        self.vs[0]["GUID__"] = UUID('bcb62404-e5f9-4bac-bdd9-ab79f4265346')
        self.vs[1]["Name"] = """Gain"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["gain"] = 1.0
        self.vs[1]["BackgroundColor"] = """yellow"""
        self.vs[1]["mm__"] = """Gain"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F250
aF185
aF280
aF215
a.""")
        self.vs[1]["GUID__"] = UUID('6ead8eec-7716-442c-b8b6-844c1e85aebc')
        self.vs[2]["Name"] = """easy"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('f75f2060-f4c6-483f-b693-8a3cad944b85')
        self.vs[3]["NumInputPorts"] = """1"""
        self.vs[3]["Name"] = """Scope1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Scope"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F345
aF184
aF375
aF216
a.""")
        self.vs[3]["LimitDataPoints"] = """on"""
        self.vs[3]["GUID__"] = UUID('245e12c7-b4e9-457f-8efd-03d933b9e6ff')
        self.vs[4]["NumInputPorts"] = """1"""
        self.vs[4]["Name"] = """Scope"""
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Scope"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F345
aF79
aF375
aF111
a.""")
        self.vs[4]["LimitDataPoints"] = """on"""
        self.vs[4]["GUID__"] = UUID('4c02392b-a654-4b83-bd79-7651cb7a68a7')
        self.vs[5]["Name"] = """Constant"""
        self.vs[5]["SampleTime"] = """inf"""
        self.vs[5]["value"] = 1.0
        self.vs[5]["Tag"] = """1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F155
aF75
aF185
aF105
a.""")
        self.vs[5]["GUID__"] = UUID('1ee33570-aa47-4324-842a-1e13858e4a20')
        self.vs[6]["Name"] = """Constant1"""
        self.vs[6]["SampleTime"] = """inf"""
        self.vs[6]["value"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F150
aF125
aF180
aF155
a.""")
        self.vs[6]["GUID__"] = UUID('882507a6-4ab9-450e-9b27-62781d9f080b')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Output"""
        self.vs[7]["GUID__"] = UUID('2ed921af-2dd5-46d0-91c0-9ab367bc0452')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('4b40105c-83e1-4d8e-88b3-00167fd7bf33')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('47982257-1733-4c77-a8f5-7d162029e014')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('0c54468e-27fd-4aa1-a291-9bda6b60d85e')
        self.vs[11]["mm__"] = """__Block_Outport__"""
        self.vs[11]["GUID__"] = UUID('54cce490-a4b5-4aca-ba8b-e7e208c50833')
        self.vs[12]["mm__"] = """__Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('8d9141d3-0920-4572-85bd-dab2ed9557b5')
        self.vs[13]["mm__"] = """__Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('978c160a-3b56-4bd9-a606-aa71d7708431')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('b282b3dc-a99b-45b3-b97e-4bdd611940b2')
        self.vs[15]["value"] = 1.0
        self.vs[15]["mm__"] = """Constant"""
        self.vs[15]["GUID__"] = UUID('cb473bf1-2e54-4a0a-b389-55ea96bc56d5')
        self.vs[16]["value"] = 1.0
        self.vs[16]["mm__"] = """Constant"""
        self.vs[16]["GUID__"] = UUID('cb80787b-c2cd-449f-b6d8-79c25c45f04b')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('19f42a0f-10b3-497b-b81e-14b4f2a98d31')
        self.vs[18]["Name"] = """2"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('0439788b-b4a4-435b-acb4-b0304efcf043')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Input"""
        self.vs[19]["GUID__"] = UUID('be17c4d9-6f97-405e-aeda-ff578ba55dac')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Input"""
        self.vs[20]["GUID__"] = UUID('b1245d6c-5563-44fb-b5ec-e7ad9b468ee0')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('fa822fa1-bfea-4661-bc1b-14bd10dad5f9')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('3b1e57ee-cf1a-49ba-89f6-e108ca49bf4d')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('90b98d8a-be80-4ed8-bb84-ba4c31cd614f')
        self.vs[24]["mm__"] = """__Block_Inport__"""
        self.vs[24]["GUID__"] = UUID('6f6f7021-1917-4f33-a092-1295eaf83c41')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('208258fb-37f9-4f4f-9077-34059e301ff7')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('f28e0672-5384-4e60-a940-c5ee096f56f3')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('5af27738-6c63-4c8f-808b-3d7bedb0ee77')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('36046084-f9d8-47bc-b798-fa294718bd5e')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('b9ec2aab-ecc7-4bd0-bf92-5c24a45cdb43')
        self.vs[30]["mm__"] = """__Relation__"""
        self.vs[30]["GUID__"] = UUID('63d5a4ff-b336-48ae-b1f4-5403bd4278a1')
        self.vs[31]["mm__"] = """__Relation__"""
        self.vs[31]["GUID__"] = UUID('66e12de4-7b05-4f0b-86e5-8c246844576a')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('d4334dce-d094-4fa1-96b4-72019f8e5f41')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('386b047d-2bd4-4995-8ac6-9c21de06c649')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('09a997e5-6aaf-4eaf-a7fc-311dee5c6a1d')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('a2982d21-92fd-42eb-80b4-d1b21c950df1')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('65800dc1-a327-4fd3-bd80-1d44e508181d')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('89560133-8363-4d93-87f7-5bb0f5ca1303')

