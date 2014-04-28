

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlatten2_export_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlatten2_export_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlatten2_export_opt, self).__init__(name='HFlatten2_export_opt', num_nodes=64, edges=[])
        
        # Add the edges
        self.add_edges([(0, 19), (2, 25), (6, 22), (7, 23), (4, 61), (4, 62), (4, 63), (4, 60), (4, 59), (4, 58), (4, 57), (4, 56), (4, 55), (4, 54), (8, 20), (5, 21), (9, 24), (10, 26), (11, 50), (11, 49), (12, 47), (13, 51), (14, 46), (15, 48), (16, 53), (17, 45), (18, 52), (19, 11), (20, 12), (21, 13), (22, 14), (23, 15), (24, 16), (25, 17), (26, 18), (36, 27), (37, 28), (38, 29), (39, 30), (40, 31), (41, 32), (42, 33), (43, 34), (44, 35), (3, 36), (0, 37), (6, 38), (6, 39), (7, 40), (7, 41), (1, 42), (2, 43), (2, 44), (45, 28), (46, 35), (47, 34), (48, 30), (49, 27), (50, 33), (51, 31), (52, 29), (53, 32), (54, 3), (55, 0), (56, 5), (57, 7), (58, 1), (59, 9), (60, 10), (61, 8), (62, 6), (63, 2)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlatten2_export_opt"""
        self["GUID__"] = UUID('1f214b2c-06ba-452c-a41a-c06cd1d4c159')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Gain2"""
        self.vs[0]["SampleTime"] = -1.0
        self.vs[0]["gain"] = 5.4
        self.vs[0]["BackgroundColor"] = """yellow"""
        self.vs[0]["mm__"] = """Gain"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F405
aF99
aF445
aF131
a.""")
        self.vs[0]["GUID__"] = UUID('b4a0392b-fbcc-4726-b0cb-4d113735e96e')
        self.vs[1]["NumInputPorts"] = """1"""
        self.vs[1]["Name"] = """Scope"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Scope"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F345
aF129
aF375
aF161
a.""")
        self.vs[1]["LimitDataPoints"] = """on"""
        self.vs[1]["GUID__"] = UUID('3eaebf52-2608-4487-82e5-ce13f106447c')
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """lightBlue"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F280
aF90
aF300
aF110
a.""")
        self.vs[2]["GUID__"] = UUID('cf8f13ed-c214-4bf3-93df-0e4659712e29')
        self.vs[3]["Name"] = """Out1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Outport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F355
aF98
aF385
aF112
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('e0d7e35f-eb96-434e-a6fc-1ea7c11d727e')
        self.vs[4]["Name"] = """Flatten2_export"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('de7b2170-6918-47c9-b94e-14b3dc33c57d')
        self.vs[5]["Name"] = """In1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Inport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F40
aF48
aF70
aF62
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('956dcc40-3ccc-4402-b5e1-15c28b8efc0f')
        self.vs[6]["Name"] = """Product3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """lightBlue"""
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F225
aF127
aF255
aF158
a.""")
        self.vs[6]["GUID__"] = UUID('34487c72-2ed7-4170-9488-026f43a92794')
        self.vs[7]["Name"] = """Product2"""
        self.vs[7]["SampleTime"] = -1.0
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["mm__"] = """Product"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F185
aF177
aF215
aF208
a.""")
        self.vs[7]["GUID__"] = UUID('599c5e82-ba7f-4091-8b81-abc7a8e2f599')
        self.vs[8]["Name"] = """Constant"""
        self.vs[8]["SampleTime"] = """inf"""
        self.vs[8]["value"] = 66598.0
        self.vs[8]["BackgroundColor"] = """lightBlue"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
F205
aF69
aF250
aF101
a.""")
        self.vs[8]["GUID__"] = UUID('be3c3374-fa37-4032-8af6-38fa5b482174')
        self.vs[9]["Name"] = """Constant"""
        self.vs[9]["SampleTime"] = """inf"""
        self.vs[9]["value"] = 134.67
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Constant"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F30
aF127
aF80
aF163
a.""")
        self.vs[9]["GUID__"] = UUID('41600bdc-f880-426c-85e2-c9aa814fce4b')
        self.vs[10]["Name"] = """Constant2"""
        self.vs[10]["SampleTime"] = """inf"""
        self.vs[10]["value"] = 12.34
        self.vs[10]["BackgroundColor"] = """yellow"""
        self.vs[10]["mm__"] = """Constant"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F175
aF120
aF220
aF150
a.""")
        self.vs[10]["GUID__"] = UUID('8ab8b140-ef06-46b4-b230-1b7f56cc9ecf')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('66ff7894-e299-4eb7-9ce1-0d5ba9f06175')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('feff959c-613d-45dc-8781-1e6fb103868f')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('c9746902-1652-485e-9f41-c3e2858b1392')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('1677d8a8-beed-493d-89f1-46413e8afcdf')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('6d247c4b-7698-44d1-ae0d-bf3e22e84370')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('23888ae8-8d8b-4357-af18-39dcf2bb387a')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('7a9dcd5c-d80a-4ea7-b2ca-6df4ef2fc9d6')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('05c69303-27f7-4614-a8a9-d8bff141c404')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('4fa620d9-a099-4893-9f66-28cbc827c653')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('d848ca35-1b55-4ac5-bc99-89f6debb3ce0')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('d3da97de-e934-4543-b62b-58b50e697a1f')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('c14b1248-057c-463d-9964-c0a6a4822602')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('0651f2b1-0e92-448e-8dc4-a71534e96303')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('e191b7ab-f899-439e-a1a5-1de18282d132')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('f4ebd7ce-0770-427d-a8e4-87514270967d')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('73322464-5908-479d-8a53-6fe1c703f6bc')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Input"""
        self.vs[27]["GUID__"] = UUID('87ffb758-194d-4ea7-8e66-3473b43bd99e')
        self.vs[28]["Name"] = """1"""
        self.vs[28]["mm__"] = """Port_Input"""
        self.vs[28]["GUID__"] = UUID('91b84637-1c25-4e45-b8f3-341e1608020e')
        self.vs[29]["Name"] = """1"""
        self.vs[29]["mm__"] = """Port_Input"""
        self.vs[29]["GUID__"] = UUID('95b1a2e2-8561-4b52-bcda-5f0a99855a06')
        self.vs[30]["Name"] = """2"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('0b9f6a10-51d3-4c63-a1b2-e12158a61b40')
        self.vs[31]["Name"] = """1"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('ddba4969-aacb-4823-b43d-58fdbfb79469')
        self.vs[32]["Name"] = """2"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('ea77e99d-c292-4cf4-826a-8b77dd401fae')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('c553208c-bdda-4a7e-9992-25f8bc2c0b9a')
        self.vs[34]["Name"] = """1"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('bb2dcd45-06d4-4e1e-85ba-e93d050921f9')
        self.vs[35]["Name"] = """2"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('af311b5c-acac-4935-b56f-b1b67ed49629')
        self.vs[36]["mm__"] = """__Block_Inport__"""
        self.vs[36]["GUID__"] = UUID('bba17a1e-43cc-4370-8448-5b594a1c5e81')
        self.vs[37]["mm__"] = """__Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('3a94e3cf-78eb-4f72-8ee1-23bd0e133741')
        self.vs[38]["mm__"] = """__Block_Inport__"""
        self.vs[38]["GUID__"] = UUID('284f93c5-4499-4407-9a05-cf918c344f33')
        self.vs[39]["mm__"] = """__Block_Inport__"""
        self.vs[39]["GUID__"] = UUID('d4375929-da43-431e-b430-35add62e4179')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('1bf27c1e-ddcb-484c-acce-dbaba615132b')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('a4f6891c-c4aa-429c-81a2-5bf583278266')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('03370f64-d1ce-4099-b71c-91acd2c03e41')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('79c284ba-0dba-424d-b189-d879cb64a23c')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('e1063708-95a9-4617-b30d-c19ca0229e7c')
        self.vs[45]["mm__"] = """__Relation__"""
        self.vs[45]["GUID__"] = UUID('64cb205e-9579-446e-a255-1a442bc0efd9')
        self.vs[46]["mm__"] = """__Relation__"""
        self.vs[46]["GUID__"] = UUID('bc38be6a-1af9-40b6-b83c-288c17b1dc10')
        self.vs[47]["mm__"] = """__Relation__"""
        self.vs[47]["GUID__"] = UUID('bcde7da1-2b2c-41ce-9308-1512e3cb59f4')
        self.vs[48]["mm__"] = """__Relation__"""
        self.vs[48]["GUID__"] = UUID('80b77110-74c0-4977-9a97-5ebf8c33e0b6')
        self.vs[49]["mm__"] = """__Relation__"""
        self.vs[49]["GUID__"] = UUID('e6564455-6d43-4e95-a6dc-6a81a1c10ba1')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('c9418213-98be-4238-9195-b6fa8e7b39c1')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('c955dca0-552e-4afd-a903-ccd397ee16db')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('31cefcf7-82c0-4218-8a27-4db9ed9bddf5')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('d07a0f2f-a64d-4d4d-ae3d-f64ecd999e4a')
        self.vs[54]["Name"] = """None"""
        self.vs[54]["mm__"] = """__Contains__"""
        self.vs[54]["GUID__"] = UUID('0223f91f-34cc-4635-8331-74edcd664d9c')
        self.vs[55]["Name"] = """None"""
        self.vs[55]["mm__"] = """__Contains__"""
        self.vs[55]["GUID__"] = UUID('8336470d-6fa9-448b-8167-643af1cf3234')
        self.vs[56]["Name"] = """None"""
        self.vs[56]["mm__"] = """__Contains__"""
        self.vs[56]["GUID__"] = UUID('e98e0776-7fbf-4342-91e7-64073b3239bb')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('926905f8-87a9-49a2-90b1-7c037ad969f9')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('b38b74c1-62fe-43a3-a7bd-b48027be1e1f')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('26e83f35-b501-4cf2-a191-e348ffbc636b')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('24ff8660-3b3a-479e-96fa-f8112aea43a7')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('1d0ccb5b-ac08-470e-b422-ff0f082854bd')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('de8ea71d-3493-4c9f-9e59-906aeba7d994')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('7d65bcfa-b2ef-41f8-be3f-cc97b9857c85')

