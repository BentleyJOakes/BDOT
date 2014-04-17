

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
        self["GUID__"] = UUID('923049c7-5c66-4da3-a8b5-a9e09afc456d')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F825
aF58
aF855
aF72
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('bf910204-2357-40bc-870a-80f855124639')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F640
aF47
aF670
aF78
a.""")
        self.vs[1]["GUID__"] = UUID('41995484-94dd-44ff-8b40-28dd9b59486e')
        self.vs[2]["Name"] = """HConstfolding"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('2737ada9-5d7e-4a0a-aacb-ea7accb71ab2')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay1"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F560
aF78
aF595
aF112
a.""")
        self.vs[3]["GUID__"] = UUID('03920cb3-4b32-4e75-ad28-fa41417f2806')
        self.vs[4]["InitialCondition"] = 0.0
        self.vs[4]["Name"] = """Unit Delay"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """UnitDelay"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F560
aF13
aF595
aF47
a.""")
        self.vs[4]["GUID__"] = UUID('d67bd51e-0bb8-4458-a027-bacc7f2bda33')
        self.vs[5]["Name"] = """Gain2"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["gain"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Gain"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F715
aF50
aF745
aF80
a.""")
        self.vs[5]["GUID__"] = UUID('4626d486-9080-4ba8-ab7a-f9368c9cc903')
        self.vs[6]["Name"] = """Gain3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["gain"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Gain"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F765
aF50
aF795
aF80
a.""")
        self.vs[6]["GUID__"] = UUID('ceed943b-5858-4a69-9880-d5d16ba6ff84')
        self.vs[7]["Name"] = """Constant50"""
        self.vs[7]["SampleTime"] = """inf"""
        self.vs[7]["value"] = 36.6
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["GUID__"] = UUID('db29ce22-8d5f-4912-96b7-7c2887e9deec')
        self.vs[8]["Name"] = """Constant51"""
        self.vs[8]["SampleTime"] = """inf"""
        self.vs[8]["value"] = 16.253
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["GUID__"] = UUID('839f05a5-055f-4f01-b1d8-0719cb59a58d')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('b01676a6-43d5-4bf3-99fe-2cb753ce36ae')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('0475e1ac-5bb8-4c61-843e-48467407e6d2')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('afc30c4c-4e9d-4dc5-8411-50b688155bcb')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('69a7916c-2469-40df-8fb4-bc14addc2e97')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('8a7dbb27-2b3e-4324-89a2-a47dc3bd6b9f')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('84009b76-a2ad-45cd-b9c7-2de7eeeae615')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('3ab89aad-2d54-48a7-8096-2fdceacb9594')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('54c3f15e-dfc5-4848-bdf0-4df2cb068e29')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('7479f976-0b4c-4ee1-8345-204b7ed892d9')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('f391a563-c98b-4f64-bf58-b48be9dbde82')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('aaf0eae4-7533-4434-91c1-42fafeb3a003')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('7228902b-0da3-4d38-8243-3a5847723b76')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('724363e9-fe3b-412b-b005-5973e0944011')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('bbbff50b-bf4a-4aa9-bdf1-b8e54c83f5bb')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('70337dab-dc1b-4a1e-abad-1caed80bb2a0')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('ca2d7ee8-ad4d-4425-9c6d-fd96dcbc30f2')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('6f37c674-0ab1-4dee-bc88-b14c709542ca')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('e2f784b9-12a7-4564-9a5c-6d39df8c29b3')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('e24d3155-ded2-4851-b226-d0abd38a3860')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('d935c14f-75cf-4b7b-ae0c-f7804442588f')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('4c0cc985-5cb3-499f-be3f-fdf832e854dd')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('3a7aa40c-dd13-4bc2-83bb-8f643ce80476')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('31fa2f79-0084-44cf-b296-22d29af5b17f')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('6e49c041-8bc3-4e04-9c48-be6c24cf38b1')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('5e980df2-25fc-420d-a509-8c3e9f257a1e')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('cae4163d-698b-472c-b638-c67eb0f8f46e')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('c3f1f759-662e-426c-a991-3f31527b4307')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('bdaeb941-416e-4687-b081-201b28c05619')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('b5560bab-b838-48df-9d6d-a3dbe6f70b68')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('a7d2b3f9-1720-4619-bc7b-6a0f175b1a9c')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('79d40268-f720-42f2-a99c-710318e48e88')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('ef0c763d-4c38-4dbb-9d8f-cc2fb1a77135')
        self.vs[41]["mm__"] = """__Relation__"""
        self.vs[41]["GUID__"] = UUID('fce9c66e-d8ed-4e50-a172-c0fa7f217132')
        self.vs[42]["mm__"] = """__Relation__"""
        self.vs[42]["GUID__"] = UUID('9c6b2377-fe63-4fd1-8170-91ab0bff1052')
        self.vs[43]["mm__"] = """__Relation__"""
        self.vs[43]["GUID__"] = UUID('64f90f91-97ec-4cf7-802a-be1baf786318')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('34fdd0ea-c29a-4e96-8d7a-ff2f5b42d43a')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('684449d7-9850-4d33-9fa9-5ec2cbe790c8')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('95ca7642-4952-43f6-a161-93e4e13a5264')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('f0f2e0f5-5ce3-4a23-b624-f1992717a1cf')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('f508538a-2d0a-4761-b261-24fc98afbaa6')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('dc378533-c197-4be7-b033-5d1a93ac08c9')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('e2f16de0-9228-4ee3-b174-ef0f295ffe0d')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('62622a96-01ea-4246-a56c-dad35d6adfe6')

