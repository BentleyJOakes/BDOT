

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConstDead(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConstDead.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConstDead, self).__init__(name='HSimpleConstDead', num_nodes=38, edges=[])
        
        # Add the edges
        self.add_edges([(0, 17), (17, 7), (1, 18), (18, 8), (1, 19), (19, 9), (1, 20), (20, 10), (2, 21), (21, 11), (2, 22), (22, 12), (2, 23), (23, 13), (3, 24), (24, 14), (5, 25), (25, 15), (6, 26), (26, 16), (4, 32), (32, 0), (4, 33), (33, 1), (4, 34), (34, 2), (4, 35), (35, 3), (4, 36), (36, 5), (4, 37), (37, 6), (16, 27), (27, 8), (16, 28), (28, 11), (10, 29), (29, 7), (14, 30), (30, 9), (15, 31), (31, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConstDead"""
        self["GUID__"] = UUID('ff8b7810-8a19-4b51-bfce-ed424f263385')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F390
aF118
aF420
aF132
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('a93633c9-6c18-4a4f-b0c5-399251442009')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F305
aF132
aF335
aF163
a.""")
        self.vs[1]["GUID__"] = UUID('f95fa9db-0fc2-4863-bc94-d09c9aedb4a0')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F140
aF120
aF160
aF140
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('c5558c38-ca7c-4c88-9370-4e47bc0d8485')
        self.vs[3]["Name"] = """In1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Inport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F170
aF178
aF200
aF192
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('9cec2301-adab-4b87-a170-eae0173be6e0')
        self.vs[4]["Name"] = """HSimpleConstDead"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('b3b9664c-38e2-4eef-a7e6-ca9e04b2cd6a')
        self.vs[5]["Name"] = """Constant1"""
        self.vs[5]["SampleTime"] = inf
        self.vs[5]["value"] = 112.32
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F85
aF168
aF135
aF202
a.""")
        self.vs[5]["GUID__"] = UUID('f70b7b57-4d27-4b8f-84c1-77282272c958')
        self.vs[6]["Name"] = """Constant2"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 433.22
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F50
aF82
aF105
aF118
a.""")
        self.vs[6]["GUID__"] = UUID('dd5829ac-bee4-45b6-8ff2-471037a4c99a')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('49c3c7d1-176f-4270-9107-f73173bae60b')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('55b84147-a17b-4f53-80a5-6af46535d9cf')
        self.vs[9]["Name"] = """2"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('98e6703b-bb4c-460a-a15d-aae2d988ea01')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('4a4de4c8-41a1-4cb8-b4e5-3ed410270057')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('69b5823e-c04f-42b9-8a60-008cff89a714')
        self.vs[12]["Name"] = """2"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('feff2ff9-cd40-4891-9fe7-4ed282500451')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('63f29131-9443-4d81-9eb0-548782ed2d90')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('557c0b21-5285-409a-81c5-a3a7c0aa2ed2')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('fff9876a-481e-45eb-bbe1-937b1f2300b0')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('c56b1de6-9013-4854-a895-e85be7a9ea8f')
        self.vs[17]["mm__"] = """__Block_Inport__"""
        self.vs[17]["GUID__"] = UUID('c4df8999-fa79-4181-9972-23877f6fd21a')
        self.vs[18]["mm__"] = """__Block_Inport__"""
        self.vs[18]["GUID__"] = UUID('d27962c0-4f1a-45ca-b86b-0087b951c1d3')
        self.vs[19]["mm__"] = """__Block_Inport__"""
        self.vs[19]["GUID__"] = UUID('d1d018fe-5c0b-4fb8-abfd-4c562a60de18')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('094cb734-cd14-46bf-9c3a-038d6ea8260a')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('26425291-7f9f-4e47-919b-cbfa019b5b46')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('3fa716b9-4cbc-457d-bdcd-f5b9e61ba87c')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('3817e0f6-fae3-4801-80a5-04bff8aaa6a5')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('7b452f35-890d-4e8b-ab2a-dbf2106bdbd6')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('2338abb3-5776-46bd-b6d9-bdc93b0c6a1d')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('d1ae9d57-6e74-4d71-8905-5e17a4b77f29')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('4cac7a97-8289-439a-bb49-051cb208fb1c')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('cd7348a2-e1ab-4be7-b916-c69f98f7e964')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('89e31d5f-430a-415d-be62-193e2f442db6')
        self.vs[30]["mm__"] = """__Relation__"""
        self.vs[30]["GUID__"] = UUID('3e243bff-6466-47b4-8e54-60ba3c2d55ed')
        self.vs[31]["mm__"] = """__Relation__"""
        self.vs[31]["GUID__"] = UUID('df3345fb-a79c-45cd-a58f-a6d86c488dab')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('012c4209-522a-4614-9feb-a0b84ed58069')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('9a6dee01-e8e8-4fba-a73b-a18d7a4039ef')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('6d1e38ed-e258-4311-aaaf-f5aff99395a5')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('4fcfe7fe-0249-4c89-a455-e8b5c0c981d7')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('d42f8e41-a2c1-44ff-b755-fce6dd8304be')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('bceb5adb-55a8-465f-84db-fa45defd45ed')

