

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
        self["GUID__"] = UUID('753310a9-582c-4e71-9c16-f8f21f41af7d')
        
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
        self.vs[0]["GUID__"] = UUID('a9170c9f-cdcf-43c0-8436-1c44cdafa331')
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
        self.vs[1]["GUID__"] = UUID('bea41a7f-138c-4522-b731-3e3af0c89c7c')
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
        self.vs[2]["GUID__"] = UUID('130ba0de-e4fd-4304-84da-e55117b98cec')
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
        self.vs[3]["GUID__"] = UUID('0e7cc859-19e8-40dc-b8ff-e3265f07cc59')
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
        self.vs[4]["GUID__"] = UUID('f02e7ffc-fe06-4a51-99d0-d9af74e2915e')
        self.vs[5]["Name"] = """Const1"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[5]["GUID__"] = UUID('6e9a96ef-cf07-4c5b-b9d6-1846e5e31a5b')
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
        self.vs[6]["GUID__"] = UUID('846d8b00-5ab9-4b84-9a82-4146a3097870')
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
        self.vs[7]["GUID__"] = UUID('183466cc-7a4a-4e13-9e08-ed4d65868a77')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('4c627527-8edd-4805-be63-7f1282583c4a')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('bf61d9fe-1439-4be1-8cf0-c6aa773893a3')
        self.vs[10]["Name"] = """2"""
        self.vs[10]["mm__"] = """Port_Input"""
        self.vs[10]["GUID__"] = UUID('19d0fdd4-38f5-489d-9c2c-055554230239')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('d49be00d-faed-444b-aa67-e1d48ff11ad9')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('3bfeb1b2-d7d4-4ebd-87db-4a1a53db000e')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('38305a23-5f4a-4fd7-b755-f6e8fa277adb')
        self.vs[14]["Name"] = """2"""
        self.vs[14]["mm__"] = """Port_Input"""
        self.vs[14]["GUID__"] = UUID('daee2cbe-5377-479e-9cd4-9ecd11f268bc')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('c03469ca-932c-4304-be36-1bfd144718a9')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('7e4e9bea-3d3b-439f-ace0-286f378db35d')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Input"""
        self.vs[17]["GUID__"] = UUID('abb173a9-ffc3-46d4-ba48-d346bf09d3b3')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('b55becd3-b13d-422a-af90-b370ce630d24')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('be5ed201-94ba-411f-a2f7-bb6641795b7b')
        self.vs[20]["mm__"] = """__Block_Inport__"""
        self.vs[20]["GUID__"] = UUID('1474cb1d-fb03-46e9-97fd-6ecb20382055')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('4efc132b-b4ba-4405-97f9-625dd93426da')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('15c60313-8b86-4e91-8e51-38164e111438')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('3f82eea1-9717-483d-bdfc-264746a6a375')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('f138e250-3c0c-4c78-a5b3-5d8c79e194b3')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('3d307e18-6627-4a71-8e00-a741bf23097d')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('0d01ecbc-d8b1-4de9-a2a7-46ad7c877804')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('66d665d4-aff9-482d-b79a-b9c831abd0d6')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('6040a449-0b0f-4820-9fb1-096ac3bdb0c4')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('392d1e61-7081-4816-a336-b90f79bfa150')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('d513a328-47a4-467e-b97e-fd060fae056c')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('d590a201-a5e9-4ab9-99e8-4771f94e433b')
        self.vs[32]["mm__"] = """__Relation__"""
        self.vs[32]["GUID__"] = UUID('6956a45f-68ec-4084-bd8e-0198fe23b070')
        self.vs[33]["mm__"] = """__Relation__"""
        self.vs[33]["GUID__"] = UUID('713103e9-7151-4487-bfcd-8c0c42b43e6c')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('750d1b7e-8dca-4036-b42c-6d776c194303')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('d799f014-5538-4dfc-a9a7-daaa5ab92501')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('4756c233-8ec0-4e3f-8310-9f1ffe278570')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('5fba715a-5113-4083-b43e-94245ee77eb4')
        self.vs[38]["Name"] = """None"""
        self.vs[38]["mm__"] = """__Contains__"""
        self.vs[38]["GUID__"] = UUID('c7fe3a35-995d-42f6-a18e-7e6f5466879e')
        self.vs[39]["Name"] = """None"""
        self.vs[39]["mm__"] = """__Contains__"""
        self.vs[39]["GUID__"] = UUID('465500a0-bbad-44c8-94ff-3b7ccd6489ae')
        self.vs[40]["Name"] = """None"""
        self.vs[40]["mm__"] = """__Contains__"""
        self.vs[40]["GUID__"] = UUID('899a2b45-b4cf-4370-916f-6e68c147dea9')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('77fe2ca4-3d1e-4c8b-a8a3-6f1a5caebbb3')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('66f599a8-7b46-4649-a566-5f0025e6e5a9')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('b0727e54-7e62-4738-9103-3abe04bb6c90')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('3a41bc8d-399c-44dd-9837-8a67058f4501')

