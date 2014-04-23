

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
        self["GUID__"] = UUID('090caaad-1264-4836-a837-9a4e27169148')
        
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
        self.vs[0]["GUID__"] = UUID('cf886619-57b1-4ffd-974d-186e924f8ebd')
        self.vs[1]["Name"] = """Flatten1"""
        self.vs[1]["mm__"] = """SubSystem"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[1]["GUID__"] = UUID('8334f64b-d882-4c73-98d0-893a3f5c1e54')
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
        self.vs[2]["GUID__"] = UUID('ab0535f2-5dcc-4fa4-8f97-2872c930b91b')
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
        self.vs[3]["GUID__"] = UUID('f60e2f7e-0ea7-4ae7-b50e-9532e235f601')
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
        self.vs[4]["GUID__"] = UUID('867e3f1b-366c-40b5-91d4-697be27b9139')
        self.vs[5]["Name"] = """Constant2"""
        self.vs[5]["SampleTime"] = """inf"""
        self.vs[5]["value"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F110
aF170
aF140
aF200
a.""")
        self.vs[5]["GUID__"] = UUID('294785b6-ae75-472d-89ad-5d9401c5b5f1')
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
        self.vs[6]["GUID__"] = UUID('7657871f-439d-4f77-93d2-86527536eeb1')
        self.vs[7]["Name"] = """Product2"""
        self.vs[7]["SampleTime"] = -1.0
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Product"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F210
aF117
aF240
aF148
a.""")
        self.vs[7]["GUID__"] = UUID('9462e8ca-31d2-42e4-9793-8c981d90d908')
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
        self.vs[8]["GUID__"] = UUID('f78e061e-fc30-4bcd-8b4c-532dcec9ae86')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('a6f66d22-2473-4deb-84cc-c8e075287ce9')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('1140fea2-a98e-4c37-baaa-f0ea68b24078')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('de325c95-8d13-44af-ab00-c03712bab023')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('05b5a80c-53eb-42cc-8cb7-9a6474995056')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('d922e292-6fd6-4b97-bb5b-bfb812578dc2')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('6335291e-1f52-4ce3-829f-24b750937bbc')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('15686c17-c3d7-4ebb-a596-99f144bd6ed0')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('6e28377a-397a-4d6f-807c-21075696a07a')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('3576aacb-6763-496c-bbde-04f4ba7cf15c')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('16db8b85-85ea-48d5-8a86-05c1eae6db73')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('3e5749ce-9921-448e-a002-196af3f47930')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('c6893ad6-9c3d-400f-bcea-aac434d17f2f')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('4f72928c-a1f6-4ca5-9607-8ac0c7d6914a')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('30a403e5-40be-4936-a66d-173e12f02660')
        self.vs[23]["Name"] = """None"""
        self.vs[23]["mm__"] = """__Contains__"""
        self.vs[23]["GUID__"] = UUID('49427837-ca44-4497-9fe2-2978f1ed06f5')
        self.vs[24]["Name"] = """None"""
        self.vs[24]["mm__"] = """__Contains__"""
        self.vs[24]["GUID__"] = UUID('d4ccc768-2de4-4ce9-bbcf-fbc451d0346a')
        self.vs[25]["Name"] = """None"""
        self.vs[25]["mm__"] = """__Contains__"""
        self.vs[25]["GUID__"] = UUID('47906554-9c32-463c-a262-d4bc242f5938')
        self.vs[26]["Name"] = """None"""
        self.vs[26]["mm__"] = """__Contains__"""
        self.vs[26]["GUID__"] = UUID('95555f74-2549-42f9-a35f-9a294aeaed45')
        self.vs[27]["Name"] = """None"""
        self.vs[27]["mm__"] = """__Contains__"""
        self.vs[27]["GUID__"] = UUID('fe112df3-529e-480f-b982-89c7a32a1610')
        self.vs[28]["Name"] = """None"""
        self.vs[28]["mm__"] = """__Contains__"""
        self.vs[28]["GUID__"] = UUID('2b8c79f1-3848-47b9-b2dc-cbd76bb3df63')
        self.vs[29]["Name"] = """None"""
        self.vs[29]["mm__"] = """__Contains__"""
        self.vs[29]["GUID__"] = UUID('eec95365-6b37-4d0a-af41-1b03a7d8d518')
        self.vs[30]["Name"] = """None"""
        self.vs[30]["mm__"] = """__Contains__"""
        self.vs[30]["GUID__"] = UUID('24e3e6e3-7923-48cb-8f34-79a1b2629288')
        self.vs[31]["Name"] = """1"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('33246905-a20c-431f-ad3d-60d3c9fd7f55')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('39f096c7-9fc3-4b19-9c50-e17dc31d919a')
        self.vs[33]["Name"] = """2"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('f0fb0d30-dac5-48f4-b084-1561a3ebbac0')
        self.vs[34]["Name"] = """1"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('86be1234-b38f-45f6-9b1e-d823cab7b38d')
        self.vs[35]["Name"] = """2"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('3545bfa4-2282-4666-8d47-42e33f7d8b66')
        self.vs[36]["Name"] = """1"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('ca618eb9-2d5d-4628-9211-353b7f3b503e')
        self.vs[37]["Name"] = """2"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('a79205cb-4c7e-419b-97a8-58389df70e6b')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('8b6a516c-21c2-4778-88de-3d46a3ec1678')
        self.vs[39]["Name"] = """2"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('f6524db5-21b6-4fe7-92f6-ecdac8febac2')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('d0296be5-80d0-4860-aca8-a201ba183ffd')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('0d641750-719e-4361-b6ad-cc03b9807d3e')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('cb589a40-ab41-457e-ba6e-bd832ee72e8f')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('edab673f-e3d9-41ae-8e66-9c677565c4e8')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('6b05585e-481c-4db8-aa02-ce813340e396')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('067372cb-418c-4425-afd5-380c6930d3a5')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('a22fe3ab-b91b-4e87-a901-5af210faf224')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('e66d40c0-a8f9-4e45-80fb-ec01dc8ed630')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('a21ca5b9-d6a3-4ca2-a306-59c02be62531')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('94bcd7a0-cf32-46fd-9b29-c482eaa17311')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('7218e45e-bd9e-45db-bd09-ffb5eac187a0')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('86e204d6-61c2-4024-bc09-d2fe7869cee2')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('93c2bac8-77df-4a3b-a254-2614537015f7')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('ace1bd36-7c61-43f7-805e-2a5b908ffb9d')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('3dcc2f91-aa94-4869-853c-2a595916c537')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('f1bfdf43-26f0-4054-8e15-3a71c8e5ce64')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('df9d19ca-b372-467b-acb6-3252c728e1b0')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('30bd259b-8b17-4761-a65f-eb03f97c8392')

