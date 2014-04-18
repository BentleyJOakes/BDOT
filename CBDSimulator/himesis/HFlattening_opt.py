

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattening_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattening_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattening_opt, self).__init__(name='HFlattening_opt', num_nodes=74, edges=[])
        
        # Add the edges
        self.add_edges([(0, 23), (1, 25), (2, 26), (3, 46), (3, 45), (3, 44), (3, 43), (3, 42), (3, 41), (3, 21), (5, 22), (6, 24), (8, 51), (8, 50), (8, 49), (8, 48), (8, 47), (9, 27), (10, 28), (11, 29), (12, 73), (13, 69), (14, 72), (15, 68), (16, 67), (17, 66), (17, 65), (18, 64), (19, 71), (19, 70), (20, 63), (21, 12), (22, 13), (23, 14), (24, 15), (25, 16), (26, 17), (27, 18), (28, 19), (29, 20), (52, 30), (53, 31), (54, 32), (55, 33), (56, 34), (57, 35), (58, 36), (59, 37), (60, 38), (61, 39), (62, 40), (41, 6), (42, 1), (43, 2), (44, 9), (45, 11), (46, 7), (47, 3), (48, 4), (49, 5), (50, 0), (51, 10), (3, 52), (3, 53), (4, 54), (5, 55), (5, 56), (6, 57), (6, 58), (1, 59), (1, 60), (2, 61), (7, 62), (63, 35), (64, 36), (65, 38), (66, 40), (67, 39), (68, 37), (69, 31), (70, 30), (71, 33), (72, 34), (73, 32)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HFlattening_opt"""
        self["GUID__"] = UUID('3c43b0f7-da2f-4209-9f07-cd368fb4569b')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F40
aF105
aF70
aF135
a.""")
        self.vs[0]["GUID__"] = UUID('286fe725-2065-41bb-b855-ea95487e4c4a')
        self.vs[1]["Inputs"] = """|++"""
        self.vs[1]["Name"] = """Sum"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Sum"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[1]["IconShape"] = """round"""
        self.vs[1]["GUID__"] = UUID('77cdf4f1-3288-4a3a-acc0-909573405283')
        self.vs[2]["InitialCondition"] = 0.0
        self.vs[2]["Name"] = """Unit Delay"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """UnitDelay"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[2]["GUID__"] = UUID('116598df-5c9f-4242-a642-ff9ffafd8b4c')
        self.vs[3]["Name"] = """Subsystem"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """SubSystem"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[3]["GUID__"] = UUID('8ebfe51d-0e8e-4249-95a1-030d40eae978')
        self.vs[4]["Name"] = """Out1"""
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Outport"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[4]["Port"] = 1
        self.vs[4]["GUID__"] = UUID('6d39cc57-9eda-47e5-b7e3-d032e66e72c7')
        self.vs[5]["Name"] = """Product"""
        self.vs[5]["SampleTime"] = -1.0
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Product"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F170
aF67
aF200
aF98
a.""")
        self.vs[5]["GUID__"] = UUID('8977f96a-3c3f-4b2c-8c25-87f1b06234c7')
        self.vs[6]["Name"] = """Product"""
        self.vs[6]["SampleTime"] = -1.0
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Product"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[6]["GUID__"] = UUID('bbe60af3-b77e-4e90-84f5-f87ce30f4c6d')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F365
aF103
aF395
aF117
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('8696f5b2-4550-4fd1-8e21-1cb0d79a9dc3')
        self.vs[8]["Name"] = """HFlattening"""
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["GUID__"] = UUID('5e449c43-49b0-48be-8871-363a4f0f2549')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F150
aF118
aF180
aF132
a.""")
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('21cfb17f-e14d-4340-be17-32326d476635')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F60
aF48
aF90
aF62
a.""")
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('d13ef6f1-4efd-4f93-b8d0-86c07884c255')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F150
aF88
aF180
aF102
a.""")
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('8187f330-3d8f-4140-87c3-6546f35155cb')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('a6e473c0-abb6-4d14-8b42-6b2aaffebee6')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('7c6af1a7-4715-4a3a-a754-feca13e87ea6')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('49e3283f-e95b-4404-a935-b84a4e9eaf06')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('d7e72116-982e-4783-a80a-bc367c399cc6')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('964f0b98-f374-4fe4-b5a9-7f284d273d5b')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('e9d36267-573d-49d0-8542-1087a929f8ad')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('b9b4da19-78f0-4b7d-9972-0e0b7e99fa7d')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('6198cab6-9d4e-474b-ac69-f8dfc1f7de62')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('17664c82-9c56-4440-b2c7-84330e1075a4')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('737dd95f-aada-44b9-affb-989345ca13b6')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('f512acef-d48c-4424-8e9b-f5846ee61fca')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('6145bd86-cdf8-4a63-acb7-6e8093c07a2a')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('120a4ec2-5cee-46c5-b00b-37a9d6fe3334')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('47e87f67-78ba-4232-868b-f3093cce158c')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('9e41e3a5-b4a6-461f-8a65-4cb7b065fe8e')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('75060fb4-042c-4e87-9710-c2c84fabd7fa')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('78c4d1fd-8855-4e37-aa97-76a9f70594b7')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('cff6d806-7b2c-411e-b921-569634fc9d21')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('d9fc8c24-4ae5-4f49-ac98-ba79eaa135d4')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('e29b8abd-208d-4313-9914-f5c5266439c5')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('528bcda6-3d47-4964-89f6-2ad5781cc041')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('b759dd39-f9ac-46fc-ba80-1fd339773357')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('ac153b18-81d4-40c8-8830-70b862bba2e1')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('c3ccafa1-ac55-4eb7-beb0-384c9bebc6c9')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('aac1832e-95f9-4bd5-a47b-48156c8b0cfc')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('5cc15965-bd36-4f3d-ba16-5273546e2d90')
        self.vs[38]["Name"] = """2"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('0e209565-f86f-45dd-98c0-0923c6e34a03')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('0d13d4b5-20be-4aac-bf45-52ac74ee06ae')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('3292bd9e-d070-412a-b296-a7da99d4a7e9')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('990dc5ef-1099-48ec-ae25-9406623971fd')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('cf5b094b-018b-4593-9a9a-7ac5dc1d9951')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('410f488e-1ef9-403a-a3ff-4ff466858138')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('41c9e729-a37f-4e0c-ab2c-b22cc6dbd750')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('5c0bf22d-b892-42e1-8fda-8ea049adc03d')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('b756589c-15fa-4183-9de7-ba5605c00e4e')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('8a7fe532-4304-4f84-84f1-3aa1c8d9a3a0')
        self.vs[48]["Name"] = """None"""
        self.vs[48]["mm__"] = """__Contains__"""
        self.vs[48]["GUID__"] = UUID('a8cfdc04-d261-43fb-acd8-588beab607e2')
        self.vs[49]["Name"] = """None"""
        self.vs[49]["mm__"] = """__Contains__"""
        self.vs[49]["GUID__"] = UUID('6e8ffdb4-fdc9-4b7a-bf08-74c43c90a22c')
        self.vs[50]["Name"] = """None"""
        self.vs[50]["mm__"] = """__Contains__"""
        self.vs[50]["GUID__"] = UUID('be1ad5e8-57c0-4291-8ded-7f6253657de6')
        self.vs[51]["Name"] = """None"""
        self.vs[51]["mm__"] = """__Contains__"""
        self.vs[51]["GUID__"] = UUID('9770a3dc-f22c-42c4-80db-60ee921aeedd')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('f21c286e-637b-40d1-b778-336107d1be94')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('9411ddd2-de91-4a10-9afa-35571e2b505a')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('ef2bc278-717d-4aa2-a871-99190b0df275')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('780f277b-f7d0-4e0d-8bb4-633db9f60591')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('e3e20a77-a940-42f6-89cc-eab89cc93382')
        self.vs[57]["mm__"] = """__Block_Inport__"""
        self.vs[57]["GUID__"] = UUID('2e5181e6-2780-4c00-a80c-f212095c2439')
        self.vs[58]["mm__"] = """__Block_Inport__"""
        self.vs[58]["GUID__"] = UUID('e926e904-dda2-4d6d-a417-d403e529381a')
        self.vs[59]["mm__"] = """__Block_Inport__"""
        self.vs[59]["GUID__"] = UUID('fd6a1bce-ef36-4c7a-b5c0-594b87c5ef78')
        self.vs[60]["mm__"] = """__Block_Inport__"""
        self.vs[60]["GUID__"] = UUID('30581a9d-57b1-4ed7-b8ec-45e5cc398d3e')
        self.vs[61]["mm__"] = """__Block_Inport__"""
        self.vs[61]["GUID__"] = UUID('44df906f-650b-4384-8db9-2f062d6e040b')
        self.vs[62]["mm__"] = """__Block_Inport__"""
        self.vs[62]["GUID__"] = UUID('94b0ac62-60a6-491a-ae05-f1aac43cd503')
        self.vs[63]["mm__"] = """__Relation__"""
        self.vs[63]["GUID__"] = UUID('8ce29eb3-0936-487c-a202-bbb9ee21aced')
        self.vs[64]["mm__"] = """__Relation__"""
        self.vs[64]["GUID__"] = UUID('a859f5b7-1048-42f8-be62-804cda1c864d')
        self.vs[65]["mm__"] = """__Relation__"""
        self.vs[65]["GUID__"] = UUID('58a551bb-4755-4576-92e3-917c4f6fc716')
        self.vs[66]["mm__"] = """__Relation__"""
        self.vs[66]["GUID__"] = UUID('a527e60d-5c8d-4830-9f6d-0beab48028a8')
        self.vs[67]["mm__"] = """__Relation__"""
        self.vs[67]["GUID__"] = UUID('07ae8c3a-f899-4f74-b81d-2fbba833fc0b')
        self.vs[68]["mm__"] = """__Relation__"""
        self.vs[68]["GUID__"] = UUID('607cb54e-a77d-4d88-9680-8f1d61c3f3eb')
        self.vs[69]["mm__"] = """__Relation__"""
        self.vs[69]["GUID__"] = UUID('a5e9e2ec-87b5-4127-a168-490041281e03')
        self.vs[70]["mm__"] = """__Relation__"""
        self.vs[70]["GUID__"] = UUID('de76f320-3f54-4c53-a834-83eea3ecb013')
        self.vs[71]["mm__"] = """__Relation__"""
        self.vs[71]["GUID__"] = UUID('0d8374cd-8ecf-4339-93f2-e2b8f75154d8')
        self.vs[72]["mm__"] = """__Relation__"""
        self.vs[72]["GUID__"] = UUID('33546945-8e5c-42cd-9948-8715b01d8fe4')
        self.vs[73]["mm__"] = """__Relation__"""
        self.vs[73]["GUID__"] = UUID('355f8ef9-ad8a-4b56-9667-67705a9bad84')

