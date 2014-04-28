

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConst1(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConst1.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConst1, self).__init__(name='HConst1', num_nodes=45, edges=[])
        
        # Add the edges
        self.add_edges([(0, 20), (20, 8), (1, 21), (21, 9), (1, 22), (22, 10), (1, 23), (23, 11), (6, 24), (24, 12), (2, 25), (25, 13), (2, 26), (26, 14), (2, 27), (27, 15), (3, 28), (28, 16), (4, 29), (29, 17), (4, 30), (30, 18), (7, 31), (31, 19), (5, 38), (38, 0), (5, 39), (39, 1), (5, 40), (40, 6), (5, 41), (41, 2), (5, 42), (42, 3), (5, 43), (43, 4), (5, 44), (44, 7), (15, 32), (32, 8), (18, 33), (33, 10), (12, 34), (34, 17), (11, 35), (35, 14), (16, 36), (36, 13), (19, 37), (37, 9)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """Const1"""
        self["GUID__"] = UUID('11194996-20c0-41ef-8dc4-a8dfbc0c6021')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F415
aF138
aF445
aF152
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('fb9fcd25-ac2e-41c8-bf0a-1166663b4e86')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F215
aF127
aF245
aF158
a.""")
        self.vs[1]["GUID__"] = UUID('8298bafc-ecca-481b-aed4-3899b8ebd77b')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F300
aF95
aF320
aF115
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('296f0b36-e3e0-4c1b-9e0e-ac65f6118410')
        self.vs[3]["Name"] = """In1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Inport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F90
aF48
aF120
aF62
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('63374654-771a-44f4-9139-2274db77aac9')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 5.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F135
aF155
aF165
aF185
a.""")
        self.vs[4]["GUID__"] = UUID('3d5de9a7-063b-4d0b-837f-950ab6fb70d2')
        self.vs[5]["Name"] = """Const1"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[5]["GUID__"] = UUID('da481de2-9f43-42bd-a80d-866040342d85')
        self.vs[6]["Name"] = """Constant"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 12.34
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F45
aF152
aF90
aF188
a.""")
        self.vs[6]["GUID__"] = UUID('430c9a93-351b-4171-8a48-eb87b23b5f38')
        self.vs[7]["Name"] = """Constant1"""
        self.vs[7]["SampleTime"] = inf
        self.vs[7]["value"] = 7.12
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F40
aF80
aF70
aF110
a.""")
        self.vs[7]["GUID__"] = UUID('998f155f-dde8-42a4-b3e6-db4295c4952c')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('617c0037-376d-429c-b0ab-cb4240219380')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('c1733e04-b0f1-453d-ad0f-f4d42c7aa7a7')
        self.vs[10]["Name"] = """2"""
        self.vs[10]["mm__"] = """Port_Input"""
        self.vs[10]["GUID__"] = UUID('cb0a6f14-c42e-421c-a108-4ab99d5f7378')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('1a5aeefd-f37c-4d62-9315-e8eee2cd95dc')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('32824f8c-8854-4421-994d-4ed2edbcb37c')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('08fce00e-f250-4287-8934-7384a64d5923')
        self.vs[14]["Name"] = """2"""
        self.vs[14]["mm__"] = """Port_Input"""
        self.vs[14]["GUID__"] = UUID('0a7ce2c2-eacd-462e-9694-21e275824680')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('d8850888-9704-41da-bdf5-9ed980c3f92e')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('321c0ebc-58ab-44c8-95e7-848431586de8')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('96cd036f-20e1-4047-9d25-b4c841ed1737')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('e7c36f3f-61d0-4cc5-a4dc-14d2157ff64a')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('ddfb736e-a4b7-4766-9caf-c5db5ead6bbd')
        self.vs[20]["mm__"] = """__Block_Inport__"""
        self.vs[20]["GUID__"] = UUID('caaf4860-d9c6-4c38-b823-50539b6d13e1')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('0470b753-3ed1-49f7-9326-aa5496c3df7c')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('c6045526-635d-412d-8c44-37e7124a45eb')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('a8b5b0f8-f6e4-463f-9f08-a887564234e3')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('fabaa08e-a52c-4097-b21a-365be94ea967')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('7655e4c6-deb6-460d-b433-9ee8b3129dc7')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('4b1a50b2-8f2f-444d-861d-696e355b3086')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('f5fc190a-ef54-4e7c-bf4d-301c8f28bb59')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('7144eb99-2e80-43d7-a5c3-e09f5078e05b')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('41cfe002-8938-4b34-8fd9-814c07c04418')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('1a6d8ed1-2b0a-4ce2-a94c-b954b75a5fbf')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('ef2d3ddf-1dd4-4a0b-8c8e-ba38e8bc3ca9')
        self.vs[32]["mm__"] = """__Relation__"""
        self.vs[32]["GUID__"] = UUID('bbddd1de-9788-49ae-9afb-0d956eb178fa')
        self.vs[33]["mm__"] = """__Relation__"""
        self.vs[33]["GUID__"] = UUID('ee8c0510-9d88-4a48-898f-13251cfe2ab2')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('f2de112e-e04a-4369-afcf-c161ac82a047')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('ca5afde3-1929-431b-be44-284ddf4eec56')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('843104a3-1fe7-4e52-b5f7-ae1b9342459c')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('bab0eeda-2bad-4ac3-9b58-f7696d607ebd')
        self.vs[38]["Name"] = """None"""
        self.vs[38]["mm__"] = """__Contains__"""
        self.vs[38]["GUID__"] = UUID('d6531c44-e9d1-4459-9a0a-226cfe21425e')
        self.vs[39]["Name"] = """None"""
        self.vs[39]["mm__"] = """__Contains__"""
        self.vs[39]["GUID__"] = UUID('7af84b2a-38d6-4c27-8803-23b34ae66e6e')
        self.vs[40]["Name"] = """None"""
        self.vs[40]["mm__"] = """__Contains__"""
        self.vs[40]["GUID__"] = UUID('6374b2b6-4884-4090-a0df-a0e6343c69a7')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('f2783d9f-17f8-4521-8433-de77b02dcb55')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('e1b964af-ee02-4b2e-85d9-138545151591')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('2ddd3138-96c8-4775-b407-abe22c06f955')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('7ea8f20c-e095-40d2-a5d6-29b69fefb3c8')

