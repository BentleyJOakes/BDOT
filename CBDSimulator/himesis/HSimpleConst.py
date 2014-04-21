

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
        self["GUID__"] = UUID('308f412b-6fd8-443d-b2a0-f26f5c2df69b')
        
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
        self.vs[0]["GUID__"] = UUID('e8208fe4-d77a-4ca9-a10c-06e4c248cf3e')
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
        self.vs[1]["GUID__"] = UUID('be7cf68d-4a00-4d94-9a59-f2864946fbf9')
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
        self.vs[2]["GUID__"] = UUID('9dbc3b76-ae88-494a-baf3-4f1fe98ee409')
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
        self.vs[3]["GUID__"] = UUID('520e0868-72c4-448b-a163-d86fac272d5a')
        self.vs[4]["Name"] = """HSimpleConst"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('954c7049-aa8e-445a-bede-f29ee94bdeb2')
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
        self.vs[5]["GUID__"] = UUID('7cdc9d91-3140-48cd-8a29-63baacf25dc4')
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
        self.vs[6]["GUID__"] = UUID('186720b4-9e17-4f76-84f9-74f063c08351')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('d38eaa83-4995-49eb-83cb-b9a081ce9040')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('695e1a88-8407-4299-b4a2-5a1af70c66f4')
        self.vs[9]["Name"] = """2"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('2400eddf-781a-426f-9278-f2eeba9629e3')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('695e3635-1a9d-4b66-809c-5143ef4cf75d')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('1cfe6486-e58b-45c0-9468-2bb280c743f5')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('c7a0851c-257d-4ebd-a155-400fa711da89')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('b4d18800-fdd3-4ec8-8600-fae456f4130c')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('c59be3bd-da45-4d3c-ac59-06704ffeb919')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('33aabcb9-946a-4467-8455-53b365c5d768')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('438175f7-9ccb-4e59-b3dc-c136f38c42ef')
        self.vs[17]["mm__"] = """__Block_Inport__"""
        self.vs[17]["GUID__"] = UUID('0ebe7e82-bf89-4c97-aa9d-39317fa07236')
        self.vs[18]["mm__"] = """__Block_Inport__"""
        self.vs[18]["GUID__"] = UUID('061f9a36-ef35-47b0-9e5a-fc638fb2d28a')
        self.vs[19]["mm__"] = """__Block_Inport__"""
        self.vs[19]["GUID__"] = UUID('8a9c9b3b-e0f0-4f3d-8f47-210e468c88b3')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('5217e3fd-1420-48e3-b5c0-fbc6cb92cd44')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('7d93c49b-f111-4359-bccf-4751a5bec204')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('77a0b2bc-065f-4e79-9926-8d0925d7844b')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('7655df7a-9d69-4002-aec6-6011a4d2b820')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('a5df883a-b08a-4162-bf72-ae5d949f91c3')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('d2949001-2caa-437f-8e33-088b70035b30')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('2462c254-4061-4c28-8116-d0872d65de1a')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('930483a2-9fc0-453a-896d-291b234f70cd')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('833aaa74-c2e8-41be-ab4b-e354dc1b0ad5')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('9ce33b63-fff2-4f1e-ae48-de60a958f91a')
        self.vs[30]["mm__"] = """__Relation__"""
        self.vs[30]["GUID__"] = UUID('5bae6f28-3ce3-4ac0-9210-81d9051811c1')
        self.vs[31]["mm__"] = """__Relation__"""
        self.vs[31]["GUID__"] = UUID('81b0a895-ea6f-481c-913e-ef36a1eebc03')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('c560890d-fc40-4757-bdb2-c38ba46ec25e')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('5ad6ac34-af4c-414b-9eec-5a4cfe86a0f8')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('ef6026e7-f507-484e-903a-ec406da17891')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('05277b56-2ac9-43b3-895c-76289ed7d5e0')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('e32553e8-0234-4c23-a388-299e3a470358')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('53b42008-f28d-4c44-ae94-5ff08a546626')

