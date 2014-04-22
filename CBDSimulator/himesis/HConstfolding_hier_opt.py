

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
        
        super(HConstfolding_hier_opt, self).__init__(name='HConstfolding_hier_opt', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([(0, 14), (1, 15), (2, 16), (3, 17), (4, 19), (6, 41), (6, 42), (6, 43), (6, 47), (6, 46), (6, 45), (6, 44), (7, 18), (8, 40), (9, 37), (10, 36), (11, 35), (11, 34), (12, 39), (13, 38), (14, 8), (15, 9), (16, 10), (17, 11), (18, 12), (19, 13), (27, 20), (28, 21), (29, 22), (30, 23), (31, 24), (32, 25), (33, 26), (5, 27), (1, 28), (1, 29), (2, 30), (2, 31), (3, 32), (4, 33), (34, 24), (35, 20), (36, 25), (37, 23), (38, 22), (39, 21), (40, 26), (41, 1), (42, 2), (43, 3), (44, 5), (45, 0), (46, 7), (47, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('451183ee-6510-4150-ace4-1fed70573496')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F140
aF65
aF170
aF95
a.""")
        self.vs[0]["GUID__"] = UUID('8ee134a7-e383-4656-a8b0-91bde8541f83')
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
        self.vs[1]["GUID__"] = UUID('351ee50b-84d5-42f4-a2e6-06e37ab57dd9')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('20722a6c-ce2b-4c41-b3a9-6c3e28308b7c')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('3f3ef515-abd8-4e11-9b44-9c2bdcb77a0f')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F205
aF65
aF235
aF95
a.""")
        self.vs[4]["GUID__"] = UUID('4d4c2828-a284-4af7-be12-cf6fb959bf12')
        self.vs[5]["Name"] = """Out1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Outport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('5fde2710-1ad6-469d-988c-b15eb3a2cbf1')
        self.vs[6]["Name"] = """HConstfolding_hier"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('b6dc645f-5b60-4bba-80eb-6aa75d4d95b3')
        self.vs[7]["Name"] = """In1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Inport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('fb235a90-eb67-418b-bfe0-4a19f37d34ca')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('9b8e4e04-363e-4c21-9a6e-097e92e2020a')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('fd746df5-ff1b-4994-9e57-36c6edd4147b')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('f469b898-c0be-448d-b788-c920f576d3f9')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('c7a6d73e-8f54-4ac5-bb4c-effff82ebc06')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('476eea07-6e34-4eec-8f22-118238dad775')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('d9969e7e-731a-4bb6-a6d6-9ef7074ca922')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('f2e2f0d3-a21d-4f9c-ad13-994939ecf13f')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('9aad16b4-6da0-4a29-af69-eea24ed2472b')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('c8fb8011-fb57-499d-a67b-f3f582633aae')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('2c11f242-1ae7-4847-8c70-0ca4b8480575')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('f1cd1db8-952b-4dc8-9d20-264450556b74')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('a9033af6-f593-4c70-b372-7706d2990916')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Input"""
        self.vs[20]["GUID__"] = UUID('8cdbd579-9915-420c-a7d5-0fb4a4e443ef')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('78effcef-5db9-4ec7-a62b-4b1a1fc67f57')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('2d9d4143-d0cc-49c2-882a-62f319a06ace')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('97f03684-72b4-41a3-ada2-1c17aabec36a')
        self.vs[24]["Name"] = """2"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('eb44f3ab-9dd6-4332-a758-e356fbac5587')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('502bd7d1-0877-45cf-8b9f-c094061be276')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('806fe04d-91a9-483f-98d7-3277ba263761')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('5edfb9fe-19a5-4f78-96a8-c0782c831be7')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('e6063422-4748-4288-9c3c-6e3ce6fa8d3e')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('fa770d85-a140-4f09-aa94-037521a6ab91')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('d947cd12-aece-44c1-b3df-6828420b79a3')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('25a7f9d2-25a7-44b8-86d3-fde7a7003e51')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('1d35f46d-fa0c-4ea7-8c1c-bb484e2b716b')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('7bc9ac4d-5f81-4489-aa3f-cd44b02531ef')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('2f6a36e9-d9ed-4ee8-8e74-10ed4c3dd35f')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('561e4138-0c63-4fb0-89d3-b13da50fbadc')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('5daf6859-c918-4767-8bdc-1c9f00890064')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('2ea57f3d-558f-4b18-a26d-04422f29aea6')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('e2d99698-389f-4302-aa46-5867e1b593be')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('33ada074-f3a4-497a-811f-ec100f4e2068')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('f962b893-1de7-4f0b-82fc-c444896e0b45')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('6a02d620-7b35-43cf-8115-e9b11cd94763')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('2cf5f2df-fb20-46e7-a9ca-593ceda3e7c1')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('51630d36-e4a7-4726-b511-8578baafc398')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('257b1e13-2577-4124-b41c-c63f07d4de0c')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('b240bf89-f6ec-4bf7-bf3c-dae5f7fa6f8a')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('961bebf5-00b0-4d9e-911a-3a5bfc0d6c25')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('0805da75-6c14-4f9a-a90d-612d28cb2d36')

