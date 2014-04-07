

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
        
        super(HConstfolding_hier_opt, self).__init__(name='HConstfolding_hier_opt', num_nodes=54, edges=[])
        
        # Add the edges
        self.add_edges([(0, 15), (1, 16), (2, 17), (3, 18), (4, 20), (7, 30), (7, 29), (7, 28), (8, 28), (8, 29), (8, 30), (8, 35), (8, 34), (8, 33), (8, 32), (8, 31), (6, 19), (9, 27), (10, 22), (11, 21), (12, 24), (12, 23), (13, 25), (14, 26), (15, 9), (16, 10), (17, 11), (18, 12), (19, 13), (20, 14), (45, 36), (46, 37), (47, 38), (48, 39), (49, 40), (50, 41), (51, 42), (52, 43), (53, 44), (7, 45), (7, 46), (5, 47), (1, 48), (1, 49), (2, 50), (2, 51), (3, 52), (4, 53), (21, 43), (22, 41), (23, 42), (24, 38), (25, 39), (26, 40), (27, 44), (28, 1), (29, 2), (30, 3), (31, 7), (32, 5), (33, 0), (34, 6), (35, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('a8dd2c52-dedd-4f63-998d-f8295f70480a')
        
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
        self.vs[0]["GUID__"] = UUID('3a5ecffa-038b-488d-91a5-cf013b0a2e6f')
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
        self.vs[1]["GUID__"] = UUID('3286fa10-535e-4492-99cb-57a94644a8fa')
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
        self.vs[2]["GUID__"] = UUID('9636b42a-6334-401f-8698-22468a37c7b2')
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
        self.vs[3]["GUID__"] = UUID('37e8cbdf-70fc-4a7d-ab4b-d14aa3b8e5ff')
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
        self.vs[4]["GUID__"] = UUID('76d64ce8-d31c-4c07-8c12-9a7ba8826290')
        self.vs[5]["Name"] = """Out1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Outport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F485
aF38
aF515
aF52
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('1ab417bd-1b1a-455c-9966-1e4bf5e663ac')
        self.vs[6]["Name"] = """In1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Inport"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('2d8f8841-8160-48e0-898e-3676be01cd25')
        self.vs[7]["Name"] = """Subsystem"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """SubSystem"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F320
aF24
aF420
aF66
a.""")
        self.vs[7]["GUID__"] = UUID('a04ce056-eb6b-4600-859f-c59214d26ce7')
        self.vs[8]["Name"] = """constfolding_hier"""
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["GUID__"] = UUID('be2bb6de-e737-4180-8582-9328412f6b58')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('96982df6-78cd-4339-a316-df30582a2e06')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('eeec8fc8-bc2a-4dde-9709-c6f6c5dad97b')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('0c1089a0-0b85-472e-a55c-8b5f6b0f0d06')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('c66b08bf-83c7-4c45-9e47-5d1b3739cb73')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('b56db3c5-240a-4191-b900-82a732cd03b1')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('7d62e14d-abd6-4fa9-bde7-8b3acbf5ed48')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('4427cd55-dccb-4f87-ad5a-370b23077534')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('5ba6a136-e795-4be5-a246-5b7885d16194')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('00cb26e6-feca-405f-8e1d-e14f774bb735')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('95842c61-7ec0-45b6-8f4f-ae2623d48541')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('99eb8849-88f8-419a-b244-1f9fe004080e')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('f75a9d71-3d1f-4c61-9596-a0bf22ca997d')
        self.vs[21]["mm__"] = """__Relation__"""
        self.vs[21]["GUID__"] = UUID('fca246b9-944e-4457-8765-845a2b13c00e')
        self.vs[22]["mm__"] = """__Relation__"""
        self.vs[22]["GUID__"] = UUID('3ce951dc-2286-4eda-bf47-d8fc106dbc32')
        self.vs[23]["mm__"] = """__Relation__"""
        self.vs[23]["GUID__"] = UUID('a20668f0-9fc0-42a1-bf17-12d7b4d0a73b')
        self.vs[24]["mm__"] = """__Relation__"""
        self.vs[24]["GUID__"] = UUID('6d1f5ea8-2bad-442d-8cc2-7b2bf0627a9f')
        self.vs[25]["mm__"] = """__Relation__"""
        self.vs[25]["GUID__"] = UUID('d8d41d8e-b3ee-44e5-80cd-56409fecdb77')
        self.vs[26]["mm__"] = """__Relation__"""
        self.vs[26]["GUID__"] = UUID('5f9b697f-832f-4a09-a611-3a35cb89aa93')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('f3ca5825-a59f-4ccb-9ec3-975a2da89e52')
        self.vs[28]["Name"] = """None"""
        self.vs[28]["mm__"] = """__Contains__"""
        self.vs[28]["GUID__"] = UUID('f2dfba04-e566-426b-8b5e-895f562e0425')
        self.vs[29]["Name"] = """None"""
        self.vs[29]["mm__"] = """__Contains__"""
        self.vs[29]["GUID__"] = UUID('7ca98333-b264-4940-ae9a-38b89719f13c')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('73a498ca-a1b2-4a41-b39f-f3cce1a44642')
        self.vs[31]["Name"] = """None"""
        self.vs[31]["mm__"] = """__Contains__"""
        self.vs[31]["GUID__"] = UUID('f0d66d7a-8b8a-442e-9e57-37b0a36a4b09')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('08230bdb-f046-4a37-9d87-459882ea4b06')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('661c77f9-8010-4c2c-84d3-12fa8be6cf3b')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('244730c7-e60f-41e8-91c0-3a290f69ec05')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('770f0485-b763-448b-bd1f-633813b8a347')
        self.vs[36]["Name"] = """1"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('f13f2875-64a3-436a-a4c8-7a15b4320dda')
        self.vs[37]["Name"] = """2"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('df72b947-1216-427b-877f-1ac5fd28e765')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('34dff1b0-db76-49f8-a6ea-f339b4d80bbb')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('98cb0795-193c-41c8-8614-d99a2a835881')
        self.vs[40]["Name"] = """2"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('5f85d681-fa85-4e0f-b918-6f6807542f3b')
        self.vs[41]["Name"] = """1"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('0dea862f-e8b5-4cef-bf59-7e547be7e7f2')
        self.vs[42]["Name"] = """2"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('3b65b562-47ee-4646-bc70-cb287d8ac776')
        self.vs[43]["Name"] = """1"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('ae9c189b-ebcb-4840-bfbe-c9df42b100a3')
        self.vs[44]["Name"] = """1"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('cbea2b6b-98fe-4d2d-a634-678f0c736305')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('37f7107b-969a-43d5-b411-d223da13ad4f')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('96ab9dd9-a4dc-4210-84e5-79f66c0f9477')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('cf5808f8-e8d3-49e8-b31c-1f38adf3a1f1')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('cb753d54-08c3-446d-8561-11b732073c1e')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('c2ce96d7-547e-41e9-a6a5-e6e3f4c6e296')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('3f410f7f-93b5-40aa-8206-2f994dd06281')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('8dff8897-91b9-44f2-9bf8-7a1920688b32')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('24ae9fbd-0a65-462d-89cd-c84b8fb806e7')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('b339ebc7-6888-4b66-98b9-990adb48ac94')

