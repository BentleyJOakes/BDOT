

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConst(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConst.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConst, self).__init__(name='HSimpleConst', num_nodes=38, edges=[])
        
        # Add the edges
        self.add_edges([(0, 17), (17, 7), (1, 18), (18, 8), (1, 19), (19, 9), (1, 20), (20, 10), (5, 21), (21, 11), (2, 22), (22, 12), (2, 23), (23, 13), (2, 24), (24, 14), (3, 25), (25, 15), (6, 26), (26, 16), (4, 32), (32, 0), (4, 33), (33, 1), (4, 34), (34, 5), (4, 35), (35, 2), (4, 36), (36, 3), (4, 37), (37, 6), (14, 27), (27, 8), (11, 28), (28, 12), (10, 29), (29, 7), (15, 30), (30, 9), (16, 31), (31, 13)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConst"""
        self["GUID__"] = UUID('c5ff4efe-fc9f-40b0-b51b-c02d39724df3')
        
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
        self.vs[0]["GUID__"] = UUID('99005180-3b52-40e5-8258-b2ff125ae418')
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
        self.vs[1]["GUID__"] = UUID('69bdfb3e-7f15-4bd9-8dbf-ed5979989f4d')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F220
aF110
aF240
aF130
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('82e2bcd1-a1a6-4204-8478-51d2beee6a37')
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
        self.vs[3]["GUID__"] = UUID('0765e57e-9c53-46aa-a1d7-bca34c4d23af')
        self.vs[4]["Name"] = """HSimpleConst"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('aaaae833-afa1-455a-b13f-210a86699134')
        self.vs[5]["Name"] = """Constant"""
        self.vs[5]["SampleTime"] = inf
        self.vs[5]["value"] = 433.22
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F85
aF102
aF140
aF138
a.""")
        self.vs[5]["GUID__"] = UUID('ed01000b-b08d-4592-950c-66739a09e3e9')
        self.vs[6]["Name"] = """Constant1"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 112.32
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F85
aF168
aF135
aF202
a.""")
        self.vs[6]["GUID__"] = UUID('3b2ac25e-194d-41f7-b538-fb9950c6f227')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('0a0e3c3b-ed2c-456d-933d-4125813503ed')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('e2dda52a-6e03-4632-8935-4f88057b50ec')
        self.vs[9]["Name"] = """2"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('65dc5186-54ec-4a96-bb34-3f4ee4f05cb8')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('23459806-1a8c-494f-b7ce-f94a78d726c8')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('d941af1a-30ea-4099-9e16-c33b2f2ba8d9')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('d084a56a-5987-4921-a86f-cad511dc46eb')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('72e32c62-5ce4-49a5-9f67-feba683d53a0')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('694e1ae4-27f8-4397-bf2e-bec9073039e2')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('e07834f9-c3ec-4548-80bc-cdb41f52ddb7')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('2e491fa7-2935-4da7-aa20-115602d80270')
        self.vs[17]["mm__"] = """__Block_Inport__"""
        self.vs[17]["GUID__"] = UUID('d0a3e164-aba9-427d-bff4-f84ae6bd5b44')
        self.vs[18]["mm__"] = """__Block_Inport__"""
        self.vs[18]["GUID__"] = UUID('29a24ebf-8d52-459c-890b-4960c7f25e77')
        self.vs[19]["mm__"] = """__Block_Inport__"""
        self.vs[19]["GUID__"] = UUID('8d20650b-5a78-43a5-948d-81701c73bf0b')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('c2dd2329-b55b-4ef6-aedb-37325ecd53f8')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('75f28e8d-c4bd-4dcd-8032-304be1c66aa3')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('43a4e10b-e9a0-4da2-a623-a7bd013d6098')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('e14a3874-198c-4207-8ee0-cf8175cad654')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('e4c44f10-2d99-4cba-826e-f0b223b53ad3')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('bed19cc8-9d5d-4639-9390-63bc38c97b05')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('0ab5d747-754c-4020-bd24-7c1d5855b747')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('1451b2fb-546c-4c7d-842a-2c9dcb155718')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('2b36da80-d476-4db3-b58c-947b87d46ef9')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('c79ba320-c4c4-4763-bc6d-b786fc83cf91')
        self.vs[30]["mm__"] = """__Relation__"""
        self.vs[30]["GUID__"] = UUID('25a5825e-144a-4a84-8b6c-05bba5f5ee1d')
        self.vs[31]["mm__"] = """__Relation__"""
        self.vs[31]["GUID__"] = UUID('e73cc8e9-091c-42a8-a531-4d0a0cb87592')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('e17586ae-b25b-4757-8409-0a4465fe7148')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('950fef18-6e3e-4851-8f98-8b3f263b03aa')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('6ebc7924-3efd-498e-8e3b-34ce6ca78a18')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('b9ab8545-faf5-4598-b285-714073a87f28')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('481d455c-30c6-4be9-b757-1015b3e2d82a')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('754dfe72-ed21-415b-bee7-ffbbcb86a9c2')

