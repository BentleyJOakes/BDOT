

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
        self["GUID__"] = UUID('df11176e-6702-4785-b607-7c53dd4cfa7c')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F920
aF63
aF950
aF77
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('152496ef-0f35-4761-ae88-035601143e60')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F685
aF47
aF715
aF78
a.""")
        self.vs[1]["GUID__"] = UUID('d0397c14-9d70-4ae1-a733-bd69e0ec87dd')
        self.vs[2]["Name"] = """HConstfolding"""
        self.vs[2]["mm__"] = """SubSystem"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[2]["GUID__"] = UUID('59d35f6b-4e03-4024-87bb-244e79a3ef84')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay1"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F605
aF78
aF640
aF112
a.""")
        self.vs[3]["GUID__"] = UUID('8c335900-af6a-4bd7-b3e6-7714d01701da')
        self.vs[4]["InitialCondition"] = 0.0
        self.vs[4]["Name"] = """Unit Delay"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """UnitDelay"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F605
aF13
aF640
aF47
a.""")
        self.vs[4]["GUID__"] = UUID('99952811-0f9c-4a83-b8e5-bfd11620454f')
        self.vs[5]["Name"] = """Gain2"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["gain"] = 1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Gain"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F775
aF55
aF805
aF85
a.""")
        self.vs[5]["GUID__"] = UUID('51dc357d-b2bc-4c4f-845e-7e5eb4954e52')
        self.vs[6]["Name"] = """Gain3"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["gain"] = 1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Gain"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F865
aF55
aF895
aF85
a.""")
        self.vs[6]["GUID__"] = UUID('22d49774-4459-455e-a104-cdbb83a633bc')
        self.vs[7]["Name"] = """Constant50"""
        self.vs[7]["SampleTime"] = """inf"""
        self.vs[7]["value"] = 36.6
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Constant"""
        self.vs[7]["GUID__"] = UUID('ca5246ee-4aba-4533-9b15-a5a377b182ee')
        self.vs[8]["Name"] = """Constant51"""
        self.vs[8]["SampleTime"] = """inf"""
        self.vs[8]["value"] = 16.253
        self.vs[8]["BackgroundColor"] = """white"""
        self.vs[8]["mm__"] = """Constant"""
        self.vs[8]["GUID__"] = UUID('ce420ae7-7b61-4a22-91a9-0340575a1f23')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('28c979cb-d1f1-44fa-a2c9-bf6c69140f0a')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('79f4b2ee-496c-46e1-9802-e4d1573f791f')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('b2905a18-f290-4d99-b02f-ade7687292f2')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('c9d30546-8f91-486c-9bfd-8b7fee2dfcea')
        self.vs[13]["Name"] = """2"""
        self.vs[13]["mm__"] = """Port_Input"""
        self.vs[13]["GUID__"] = UUID('e3dd3654-a5e6-42c3-bdbc-7ba9510cbfcd')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('3badc0ff-0fba-4c4e-bc94-233352ea3197')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Input"""
        self.vs[15]["GUID__"] = UUID('8de6ba5d-1aba-4b88-a1e0-50b3f66c54fc')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('1edb1b77-ed9a-43cd-8ff4-64dc67f48a17')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('cc048af3-0055-47dd-9982-9b0ef702a83e')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Input"""
        self.vs[18]["GUID__"] = UUID('f28261a9-57c9-4623-99ac-949edf69dd2d')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('710794da-95c5-4fac-a0f7-28964cf65fae')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('5ca872fe-026a-48e5-b226-696292969ee9')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('b4f4d341-b289-4b64-805f-104b455d1e69')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('53b04677-6ac5-46e8-b4c3-5469c298264e')
        self.vs[23]["mm__"] = """__Block_Inport__"""
        self.vs[23]["GUID__"] = UUID('ab136e83-709f-4ba5-a913-651bf431756b')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('ae929a24-91c0-4498-819b-3ce61bea96cf')
        self.vs[25]["mm__"] = """__Block_Inport__"""
        self.vs[25]["GUID__"] = UUID('51766230-e012-4ef9-9e49-c6d333fd3de8')
        self.vs[26]["mm__"] = """__Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('27dd2b82-8b10-4072-92b8-8e4b756841f2')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('3176de12-f4bf-46f4-b042-ebe9a89e5029')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('3cff21dd-c658-492f-84e2-b1bab92be41d')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('aa660fc0-9206-4744-990c-edbf2d64f173')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('a328bb82-c893-467c-8be7-38869cfeb8ac')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('f1aed844-21a1-4b80-ae23-79ff15ab20d7')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('9f71994f-7740-45f6-b010-8421349ebbd7')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('22323e6f-e810-4a69-af9d-df4642591b9c')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('74a2d343-95bc-4478-acb1-aa483adc4304')
        self.vs[35]["mm__"] = """__Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('3c39341c-b55b-420c-b58a-3154927284cc')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('5af21cd8-4ca0-4cde-87cb-fa172cf14058')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('4f183c4e-ea2a-4f49-9e95-964e11759218')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('b9e6c2e8-515b-463d-aa91-64a1d5929d1e')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('abc9a28e-523f-4daa-8920-f0a517a865cb')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('54c90f34-398d-4a95-aa34-49e3e84164da')
        self.vs[41]["mm__"] = """__Relation__"""
        self.vs[41]["GUID__"] = UUID('a7580782-f8e4-40d4-93af-c0cbfc04c441')
        self.vs[42]["mm__"] = """__Relation__"""
        self.vs[42]["GUID__"] = UUID('309a5f29-5e59-45f7-9115-3a62577be3dd')
        self.vs[43]["mm__"] = """__Relation__"""
        self.vs[43]["GUID__"] = UUID('b170ba72-c781-471b-8e51-27ed652b2c48')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('5a89b932-1f19-4f21-b0c0-c7a2690edb45')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('e23f97ef-589b-49b0-bfdc-e46a9409e100')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('745833a7-bff4-4315-a866-67b4199b29ce')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('0cbf29dc-b482-44d0-b6b2-5fa0a9f959b0')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('14f8bd4e-6cb2-4769-beb2-b44b324971df')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('51e94020-dac1-45ee-a502-d68eec064eed')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('b71ffd83-e3cf-40e3-a897-5ec54e76c1e1')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('3ce12d88-3827-4959-9986-84c61ddc5182')

