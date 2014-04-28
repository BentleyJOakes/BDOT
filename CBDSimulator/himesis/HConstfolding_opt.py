

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_opt, self).__init__(name='HConstfolding_opt', num_nodes=52, edges=[])
        
        # Add the edges
        self.add_edges([(1, 28), (2, 51), (2, 50), (2, 49), (2, 48), (2, 47), (2, 46), (2, 45), (2, 44), (3, 33), (4, 36), (5, 24), (6, 30), (23, 9), (10, 42), (25, 11), (26, 12), (27, 13), (14, 41), (29, 15), (16, 40), (17, 39), (32, 18), (19, 38), (20, 37), (35, 21), (22, 43), (44, 5), (45, 0), (46, 1), (47, 6), (48, 7), (49, 3), (50, 8), (51, 4), (5, 23), (24, 10), (0, 25), (1, 26), (1, 27), (28, 14), (6, 29), (30, 16), (31, 17), (3, 32), (33, 19), (34, 20), (4, 35), (36, 22), (37, 21), (38, 13), (39, 18), (40, 11), (41, 9), (42, 15), (43, 12), (7, 31), (8, 34)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_opt"""
        self["GUID__"] = UUID('e88c8b75-6a2f-466e-af4c-4cda8f9f2b5c')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F620
aF58
aF650
aF72
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('5e0cefed-2319-4ab4-be34-531a955b8aaa')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F435
aF47
aF465
aF78
a.""")
        self.vs[1]["GUID__"] = UUID('20cb1868-29fc-4d38-93df-f940b7c4ad56')
        self.vs[2]["Name"] = """HConstfolding"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('8c915adf-46c7-4766-85ba-8d5cd9044299')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay1"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F355
aF78
aF390
aF112
a.""")
        self.vs[3]["GUID__"] = UUID('7a2e268d-e9f5-45ea-8e60-5834d92409d0')
        self.vs[4]["InitialCondition"] = 0.0
        self.vs[4]["Name"] = """Unit Delay"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """UnitDelay"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F355
aF13
aF390
aF47
a.""")
        self.vs[4]["GUID__"] = UUID('5efbabb9-21d7-46e9-9d00-daba1ab05cc4')
        self.vs[5]["Name"] = """Gain2"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["gain"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Gain"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F510
aF50
aF545
aF80
a.""")
        self.vs[5]["GUID__"] = UUID('cd4dd0be-e018-425c-8e99-f995b85f9328')
        self.vs[6]["Name"] = """Gain3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["gain"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Gain"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F560
aF50
aF605
aF80
a.""")
        self.vs[6]["GUID__"] = UUID('c19f9419-0985-484f-81df-5751c1ae897b')
        self.vs[7]["Name"] = """Constant50"""
        self.vs[7]["SampleTime"] = """inf"""
        self.vs[7]["value"] = 36.6
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["GUID__"] = UUID('c11a9881-5a96-48a6-95af-ef9d51c051d1')
        self.vs[8]["Name"] = """Constant51"""
        self.vs[8]["SampleTime"] = """inf"""
        self.vs[8]["value"] = 16.253
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["GUID__"] = UUID('f942f8c1-cdec-4c47-8610-02f214cc83d2')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('78b54b2e-52ed-40b6-b06b-bdfe8cb001c6')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('b82f5550-42fe-4682-a688-1fe0f2bc4759')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('6541851a-dd99-44ed-b0a1-4efbc98e797c')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('eacd4a4b-f335-43a8-90e8-1ea1d2e408c4')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('ca0088e3-6433-4174-bd8c-d8ab04ca764a')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('833fbf37-4d69-4e0e-8b24-ecacd5f5aee4')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('eb3067b4-3121-4f7b-a0e2-6ad3afb7bcec')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('97780d87-7dc4-4cf1-9360-3d363b85fc40')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('6e6bd7cc-6907-4617-b58a-0890ac669fa5')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('5a47ef6b-e5c9-4476-ae31-4537cdd351bc')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('20f755e7-9a97-43bc-9637-4082957eabe2')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('b7e34617-5eea-42b5-9d00-5c1a87ea8a8c')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('714bc628-5a51-424e-a52e-d194183d3df7')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('e3e81256-516d-4b47-8a86-840ea05b0212')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('7585afd9-37d8-4352-aab9-b470b798e2e8')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('0b6e03fc-e8ea-4a26-ada8-960ff989c93c')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('c24e55ed-e409-47fe-affd-c65ed9151a65')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('75eb2b39-d1f6-4e3b-b1f0-5c5d43c629ae')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('b9d48010-eb85-4628-894d-ff55d2eddce5')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('211b5ce6-4e72-4644-af4a-b7c4b945cd1e')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('0e0b388f-1e6f-43f0-b373-1f981a86ca15')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('98cf2966-d063-45bd-9436-5699a3397987')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('6523a374-5627-4151-a5cd-8357ec2c6cd6')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('5a3ab84a-4dc2-4705-98bb-9f2d3545ae07')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('e7145c2d-358d-44a4-96de-76602d8b9339')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('849ee8db-7817-4e6f-bda6-ff8c41c4db44')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('233201ac-e881-4b8a-976f-da5dddf123af')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('44332566-fa00-4f4b-9586-9fd6973cd15a')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('686c4a92-e4a4-421d-ad76-774f9ae4bd7c')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('fe4c3d2e-b41b-4176-80e1-86b943af5108')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('9067ff20-996a-4562-8634-acb40d23aeba')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('02473d36-cae8-4ba1-a2e9-5fb8d6ef74d0')
        self.vs[41]["mm__"] = """__Relation__"""
        self.vs[41]["GUID__"] = UUID('dc157e85-24e8-4713-8f36-9d4afa40bc28')
        self.vs[42]["mm__"] = """__Relation__"""
        self.vs[42]["GUID__"] = UUID('5c194bfb-51b7-42cd-98ff-1ec7f50b2539')
        self.vs[43]["mm__"] = """__Relation__"""
        self.vs[43]["GUID__"] = UUID('a00b8086-1750-4169-9119-02b68bdc9830')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('10d5e9bb-4b43-4cf1-9122-c558bf28148d')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('f30ab25a-1bda-4326-851c-56e89b12dec9')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('17258987-a651-4c60-81ed-58aa73c9d99a')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('6aa8f178-53cf-4b1c-902b-7ef8794d93ea')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('a71a9614-6afa-4be9-9a9a-38d00d739613')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('ecc82786-f321-4ef9-b092-d454c1b9fcab')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('d23ec4c8-4808-4fe5-ac4e-5a7a41b43492')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('ad0a871a-3740-497a-a0ee-e144ee3f4666')

