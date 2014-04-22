

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten1_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten1_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten1_opt, self).__init__(name='HFlatten1_opt', num_nodes=58, edges=[])
        
        # Add the edges
        self.add_edges([(3, 16), (4, 17), (5, 18), (6, 19), (7, 21), (8, 22), (1, 23), (1, 24), (1, 25), (1, 30), (1, 29), (1, 28), (1, 27), (1, 26), (2, 20), (9, 53), (9, 52), (10, 56), (10, 55), (11, 50), (12, 51), (13, 54), (14, 49), (15, 57), (16, 9), (17, 10), (18, 11), (19, 12), (20, 13), (21, 14), (22, 15), (40, 31), (41, 32), (42, 33), (43, 34), (44, 35), (45, 36), (46, 37), (47, 38), (48, 39), (23, 5), (24, 7), (25, 8), (26, 0), (27, 3), (28, 4), (29, 6), (30, 2), (0, 40), (3, 41), (3, 42), (6, 43), (6, 44), (7, 45), (7, 46), (8, 47), (8, 48), (49, 39), (50, 37), (51, 31), (52, 36), (53, 35), (54, 33), (55, 38), (56, 32), (57, 34)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlatten1_opt"""
        self["GUID__"] = UUID('8a267b43-3dfd-4abc-abc9-2e8737c2deed')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F470
aF123
aF500
aF137
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('3b401e16-68e3-4187-a854-175f1bf363af')
        self.vs[1]["Name"] = """Flatten1"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('726b075a-8a97-4c7e-b65d-b2aab0708ac8')
        self.vs[2]["Name"] = """In1"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Inport"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F15
aF183
aF45
aF197
a.""")
        self.vs[2]["Port"] = 1
        self.vs[2]["GUID__"] = UUID('17c09c93-e906-48b1-8679-7bcd20fb03f1')
        self.vs[3]["Name"] = """Product"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Product"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F155
aF147
aF185
aF178
a.""")
        self.vs[3]["GUID__"] = UUID('d7781063-41a7-4fbe-b486-f44223a79d97')
        self.vs[4]["Name"] = """Constant"""
        self.vs[4]["SampleTime"] = """inf"""
        self.vs[4]["value"] = 12.34
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Constant"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F25
aF102
aF70
aF138
a.""")
        self.vs[4]["GUID__"] = UUID('87987e60-90b7-43ab-8846-39c067e6d5a3')
        self.vs[5]["Name"] = """Constant2"""
        self.vs[5]["SampleTime"] = """inf"""
        self.vs[5]["value"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F125
aF235
aF155
aF265
a.""")
        self.vs[5]["GUID__"] = UUID('d02af974-e7c6-4bbf-a1ec-300d00705df5')
        self.vs[6]["Inputs"] = """|++"""
        self.vs[6]["Name"] = """Sum"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Sum"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F410
aF120
aF430
aF140
a.""")
        self.vs[6]["IconShape"] = """round"""
        self.vs[6]["GUID__"] = UUID('951d7c69-a0c6-4582-90ca-197323274e8b')
        self.vs[7]["Name"] = """Product2"""
        self.vs[7]["SampleTime"] = -1.0
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Product"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F215
aF167
aF245
aF198
a.""")
        self.vs[7]["GUID__"] = UUID('e5634ef6-e1f8-4ae2-9ce2-7c6288fbef53')
        self.vs[8]["Inputs"] = """++|"""
        self.vs[8]["Name"] = """Sum2"""
        self.vs[8]["SampleTime"] = -1.0
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Sum"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F275
aF125
aF295
aF145
a.""")
        self.vs[8]["IconShape"] = """round"""
        self.vs[8]["GUID__"] = UUID('2b020f4d-86a4-44d9-9d82-f804115457b5')
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('778fa55a-2121-49a7-9a33-17f0737fe665')
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('286fbbad-fa31-45e8-89d9-eef21ffaae24')
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('b644fd84-d3ff-4390-b72b-7ccbfe3bc68b')
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('3c699dd8-eec5-4afa-967b-e665927985c3')
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('ddf1167a-fc5c-41fd-9c59-a42353af92d5')
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('c2ee2d63-4ad4-4fa8-9b42-a2a174925727')
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('25e7ef6f-ad7c-42e2-b570-bb2660bc47d8')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('f79cfe7d-0b5b-4e78-9360-cda5471e384d')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('1fcabc23-4f7a-4aac-83a0-6e73b76e9961')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('55f0a28a-1e00-49c2-aa3c-2f93c496093b')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('970f8084-fbaa-4ce3-bff2-c0699ea0b403')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('cc63db70-090d-4421-acc5-b7d2f1f7a1a9')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('2ac50041-a8fb-4058-a757-1dff4ad66691')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('99d76fc8-881d-49e7-89c4-8ffe2f69eee8')
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('32519309-e8a2-47ae-9c3b-d1a78e24bd75')
        self.vs[24]["mm__"] = """__Contains__"""
        self.vs[24]["GUID__"] = UUID('e7c52492-f119-4d03-b358-03e286b5eda5')
        self.vs[25]["mm__"] = """__Contains__"""
        self.vs[25]["GUID__"] = UUID('a1351a33-a968-4d88-ac9b-7e5305919f1d')
        self.vs[26]["mm__"] = """__Contains__"""
        self.vs[26]["GUID__"] = UUID('a8d7b557-197f-48e1-8829-53fe28e23783')
        self.vs[27]["mm__"] = """__Contains__"""
        self.vs[27]["GUID__"] = UUID('713a6f64-a8ed-43c3-a1b1-90769c50cd07')
        self.vs[28]["mm__"] = """__Contains__"""
        self.vs[28]["GUID__"] = UUID('addb8b40-630b-449b-876a-c2cca15beeff')
        self.vs[29]["mm__"] = """__Contains__"""
        self.vs[29]["GUID__"] = UUID('e3da1bd2-0689-4e04-b729-b933a3a252a0')
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('a9aba6d1-970f-4e56-9974-1961547bf950')
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('64b5ce10-019f-40d7-b6d1-aa632994a8eb')
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('65d88670-38b2-403f-a3d8-67542f013f1d')
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('f3087fe0-41b4-4d2d-ab08-695ce5fc5cbf')
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('ef8894d6-5733-4e0a-b985-bf4d40ef9db3')
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('c0ae08c5-1bb6-42e0-a16c-b49f2575798f')
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('cdd3a1b9-3b6a-4e1e-90e9-b54f4237400f')
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('5c213fd4-dc3f-468e-943d-66e315243d0a')
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('9c5b749d-bbfa-47fc-b521-0d18d52d0ac8')
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('baa05b83-457c-42be-9c23-39bf8c5e4378')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('7ffd2b67-a0a6-4ff7-9a69-a83b8343eae1')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('810bb411-2d86-4841-a5b0-5660a40e8647')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('6e295e3c-7232-4292-be19-9d41e2a0a140')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('c1facd5d-40f5-4aed-9d5c-7459b7bbd792')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('5a2597b7-5be4-4f62-a98f-a4bf79ac87b9')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('7964d77b-dd2d-4fbb-9ddc-ec42e24f42e2')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('130a81f7-307a-47ba-afbe-32fdf493c488')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('6fe2f96c-2156-4dce-ab32-54ea994d49ea')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('176b8af8-e666-4130-adc2-35df865bb3c2')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('198e16ae-0d93-4e50-bd72-5565270bfb69')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('4ac82bd0-2546-4451-be7e-7e0a59aad876')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('ffba8fda-3752-4b88-8faa-96dd2e15a5f3')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('6c1c0663-e7e1-4ca9-b816-a9042c24dadb')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('a125c7fc-b675-41a3-a17b-5451929ef5b1')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('4ccde2f1-c6e1-4a3e-b448-f905ba268349')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('26ca2e44-c1a3-41ac-bbaa-623704168868')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('a2546270-7474-4fb0-bd38-49ca2be20598')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('b5da9ba1-e153-475a-b253-8ddb9fff890e')

