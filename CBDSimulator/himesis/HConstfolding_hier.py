

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_hier(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_hier.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_hier, self).__init__(name='HConstfolding_hier', num_nodes=71, edges=[])
        
        # Add the edges
        self.add_edges([(5, 40), (40, 30), (5, 41), (41, 31), (5, 21), (21, 12), (6, 42), (42, 32), (0, 22), (22, 13), (1, 43), (43, 33), (1, 44), (44, 34), (1, 23), (23, 14), (2, 45), (45, 35), (2, 46), (46, 36), (2, 24), (24, 15), (3, 47), (47, 37), (3, 25), (25, 16), (9, 26), (26, 17), (10, 27), (27, 18), (11, 28), (28, 19), (4, 48), (48, 38), (4, 29), (29, 20), (7, 49), (49, 39), (5, 60), (60, 1), (5, 61), (61, 2), (5, 62), (62, 3), (5, 63), (63, 9), (5, 64), (64, 11), (5, 65), (65, 7), (8, 66), (66, 5), (8, 67), (67, 6), (8, 68), (68, 0), (8, 69), (69, 10), (8, 70), (70, 4), (19, 50), (50, 33), (17, 51), (51, 34), (16, 52), (52, 36), (16, 53), (53, 39), (15, 54), (54, 37), (14, 55), (55, 35), (20, 56), (56, 31), (18, 57), (57, 30), (13, 58), (58, 38), (12, 59), (59, 32)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier"""
        self["GUID__"] = UUID('472e57a8-5d86-4a9a-b863-7fc2a3feb980')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F135
aF65
aF165
aF95
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('c1fbf467-153c-4044-a45e-b962a2fdca38')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """yellow"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F205
aF92
aF235
aF123
a.""")
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["GUID__"] = UUID('ab2ace1e-536a-4cc5-a91c-d315c0e5d72c')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """yellow"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F250
aF100
aF270
aF120
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('26245164-899d-4dec-87c5-a51a1329ce95')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["GUID__"] = UUID('0414137d-bb02-4a8c-a830-67b246b3b22c')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F200
aF64
aF240
aF96
a.""")
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["GUID__"] = UUID('be4f4e7b-94a4-44a2-9aa0-3fb3e3190551')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """yellow"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["GUID__"] = UUID('94a2decb-71f6-4c78-a798-f72aebd65d69')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('94ba6c08-692d-4e92-b373-7af422c94f1c')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """yellow"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F365
aF103
aF395
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('2266697d-b53d-4152-8fe8-23dea8f17d17')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('a172f642-dbe5-41bc-87f4-d17a2940b867')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """yellow"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F145
aF118
aF175
aF132
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('00cb20c1-f309-4555-b6b3-a1644a6df048')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('77540dfc-f183-4997-b2a7-d4cc376bd19d')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """yellow"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F145
aF88
aF175
aF102
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('aefc16d4-e1f2-45d8-ade5-a5eaea54d6d0')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('9fa827be-0264-4e9a-86bd-747054adf5ad')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('58180195-bb7c-40cd-90d1-468131683327')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('c019c997-edc2-42a3-8faa-a25b6309e715')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('1130e66a-6cbf-4a39-8c2a-4e8830cfcaa1')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('147a12f1-d451-4937-96ee-8380bd04209a')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('d26a180d-56c2-4735-a3fb-f420727deb43')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('e9e50393-afff-4764-8427-3e2a195ec63c')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('a076e856-ec82-4778-84b9-8e9c23273ab9')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('874c1cde-905d-4ff7-9a1b-9a4e8427ce81')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('680706ec-c108-40b2-8fe0-7934071b1e20')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('4cb9ea64-c579-4b4c-b8b1-aa0d744a804d')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('f5e427fd-0098-4fa9-8833-e9bb3b1768b6')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('870ea00c-2aee-434a-bef8-21f242a56e08')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('82e42d6b-debe-43c2-9b1f-0428005c1a03')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('75871fbf-e3a7-4ca4-91fa-b4fe2b136857')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('a5e27d0c-ba11-4a63-951a-e9b214c83080')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('cb088b5c-9bc1-4812-b325-2f60f76e5034')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('8c98326b-992f-4f60-8da9-0f790528e39f')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('4b7634b3-fa1b-4931-99d4-3bb1aa388fee')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('3401699e-7df2-441f-9553-18f7e4a13520')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('2b4c0fec-d4ca-467d-8891-2b231ef61e52')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('01515a8b-a234-438c-957f-7ee26b4c0787')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('c1b649ba-1e71-4600-8c66-9c00823eb8b9')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('2e62ca59-a86a-4ec9-9d18-a45f2a649efb')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('ed1062a1-346f-4fe3-aac6-68a3f748c210')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('d6fd4692-b68d-475e-b05d-ed7d98b5ad8e')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('6b14435f-dad3-447d-9353-3c171752a4c2')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('6ac515c7-9101-4b84-9ad6-f95c59c9a39d')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('73a2aa04-f85e-497a-b247-a63e7b1b6e6f')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('d4d0108b-a0ae-483b-a074-31038acfdc65')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('2f15839e-a27c-4042-b64a-8c41fdcd5c93')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('a7b294d9-8f46-48c8-bcc7-53782e153e7d')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('4d18147a-0298-4290-842d-aa642ebffb85')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('36e2083e-3b2c-46c6-b06c-f137ed4731e7')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('63ad4350-c941-46d7-9e6d-428ef3deb3cb')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('1950e5be-6272-4543-aacd-b6493b11d7d9')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('0d1ff08f-b626-48c3-8a36-cd61ac68f0ff')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('c7442e51-14e2-490b-8314-d365a01ec427')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('81142741-6ecd-40ac-85ae-c88367ee21eb')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('557a7737-e62b-4504-8159-daa485ba553a')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('741629d7-6064-4ff6-b0e2-3e671942e2e1')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('3aa967cb-eac1-46f9-9ebb-d95e04106f91')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('f1a50761-eb6b-4c5a-8a8c-4089558395ae')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('87692c59-6151-45fe-b882-a6df28bf9768')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('7a6c130b-d298-4e47-b76d-417b0f20eff9')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('14babdfd-8a88-4b63-8b2c-a9fc5b74ffae')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('662e967d-5c57-4333-9775-73050641c36c')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('ca3646a7-2418-4a3a-bff9-da17f6d221f3')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('61de8882-a17b-4046-8b3a-7d28939832ad')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('6b4bd740-49c8-4aad-9034-4a0325376039')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('72396714-dca0-4fc3-98cf-9327307995b5')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('d5784ec5-7774-46a6-8b88-d816ad41df47')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('ea21c211-c587-474f-8ac7-a076cd925dc7')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('1907e4ed-c9bb-4133-8522-0cce00c97e6b')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('962cc8f4-a658-4beb-8109-7b5ebc1cd168')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('fa688312-d606-43f4-ad63-5476065cccbe')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('c0664078-1421-4f44-867b-7424c9620209')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('ea254807-594a-4261-aab6-e6bdcf933e52')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('ab00e328-d71e-4a0d-956e-e3541a961eae')

