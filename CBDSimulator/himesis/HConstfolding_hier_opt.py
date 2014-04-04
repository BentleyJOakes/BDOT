

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HConstfolding_hier_opt(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HConstfolding_hier_opt.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HConstfolding_hier_opt, self).__init__(name='HConstfolding_hier_opt', num_nodes=71, edges=[])
        
        # Add the edges
        self.add_edges([(0, 22), (1, 23), (2, 24), (3, 25), (4, 29), (5, 65), (5, 64), (5, 63), (5, 62), (5, 61), (5, 60), (5, 21), (8, 70), (8, 69), (8, 68), (8, 67), (8, 66), (9, 26), (10, 27), (11, 28), (12, 57), (13, 59), (14, 51), (15, 50), (16, 54), (16, 53), (17, 52), (18, 56), (19, 55), (20, 58), (21, 12), (22, 13), (23, 14), (24, 15), (25, 16), (26, 17), (27, 18), (28, 19), (29, 20), (40, 30), (41, 31), (42, 32), (43, 33), (44, 34), (45, 35), (46, 36), (47, 37), (48, 38), (49, 39), (5, 40), (5, 41), (6, 42), (1, 43), (1, 44), (2, 45), (2, 46), (3, 47), (4, 48), (7, 49), (50, 37), (51, 35), (52, 34), (53, 36), (54, 39), (55, 33), (56, 30), (57, 32), (58, 31), (59, 38), (60, 1), (61, 2), (62, 3), (63, 9), (64, 11), (65, 7), (66, 5), (67, 6), (68, 0), (69, 10), (70, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('843630bd-b401-4407-9942-e468175bdbae')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F125
aF125
aF155
aF155
a.""")
        self.vs[0]["GUID__"] = UUID('0186fce4-36ca-49b1-b051-58b1fc6261fa')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["GUID__"] = UUID('bb1c6705-3081-4534-82d5-e50b77f1eeb5')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F275
aF100
aF295
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('511473ce-0434-4032-9afa-a202e74d8899')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F325
aF93
aF360
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('75c4dfb3-ee3a-4e32-88c5-a22f73af646c')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F215
aF125
aF245
aF155
a.""")
        self.vs[4]["GUID__"] = UUID('c081b003-14d0-4420-ad24-2f1607374533')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F320
aF24
aF420
aF66
a.""")
        self.vs[5]["GUID__"] = UUID('19d28150-b637-4ab3-ac17-950e4a748826')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F485
aF38
aF515
aF52
a.""")
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('2c1c027f-fd7e-4121-b9ab-28fb0287dfb8')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F425
aF103
aF455
aF117
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('37d682f7-1901-4ccf-919a-83f37b5e5700')
        self.vs[8]["Name"] = """constfolding_hier"""
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["GUID__"] = UUID('28699197-37cf-48ae-a771-e60cce84c3e7')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F90
aF153
aF120
aF167
a.""")
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('ea085ab9-891e-46e3-8568-a57ff3c87235')
        self.vs[10]["Name"] = """In1"""
        self.vs[10]["BackgroundColor"] = """white"""
        self.vs[10]["mm__"] = """Inport"""
        self.vs[10]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[10]["Port"] = 1
        self.vs[10]["GUID__"] = UUID('1e2ea161-8296-4ab3-94cf-67e55c43bada')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('2b8ea402-57c2-4b2b-9b2c-3371657572d1')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('b3c6c324-ca0c-47ea-9d04-7f326d794004')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('eca4f978-be76-4427-a91c-98393e2006ef')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('2972d182-d143-480b-a107-402099c5f4bd')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('06713131-1d97-4771-898c-e041006531fe')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('02ff22be-eb60-4ed4-906f-de73ef25b12b')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('86330c31-b7c4-4231-a1fc-62f1edb510a9')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('d4a6fa7b-5a13-4f90-be25-ccd3ddeca1dc')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('f2c7bd8c-8e39-4895-aa27-6b212bf988c7')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('620e552e-d511-4414-952c-12b960ffe627')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('d78fded9-5a54-459f-9a0f-3796ee43951d')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('c7b2bbc2-bce9-4e50-9465-d8c89fb6d447')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('9e04d421-109b-4efb-8acc-a3b5fbd6bdc6')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('fb96b03d-4aec-41f4-9852-45658a969b57')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('c759c92b-c1c5-4b47-abee-c69d70a51fad')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('9116e4c2-38c5-4e3e-89a0-187a19464f71')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('5c8c4126-c22f-495b-9a38-8469639548f4')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('060179fe-0034-47c7-89a3-cc2bccaac553')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('aeeada97-2b25-4bf7-9e59-b77f963529d3')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('dbd8ce3d-a5c5-4d61-94e2-824a0e8bc684')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('8618ed33-bfec-4292-943e-246d17d3a15e')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('032dda51-4991-4c63-b265-6ac89818bac6')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('afdd5aaa-5c18-41b4-9a3c-9ae7f5f9bbed')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('ef94c080-4aea-4e3b-a342-14791125d97b')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('834dd969-618f-4346-aa5d-30e06ccd7d67')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('c870d9a2-330d-4d60-9363-e47adbcb12b4')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('412d4544-8f2e-4a09-b991-adb94f288e4b')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('9b78dd6b-e18b-4ce2-85e9-4cd4009c808a')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('10bec90b-38a7-4952-b274-d1523a762259')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('7e576174-b72e-41f4-8b95-0f67198d1c52')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('f84a4a4b-3e70-4c35-9193-9ce0351924ee')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('ac5e3d1f-d1fa-42af-9bfc-eddedcb1ef5a')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('1a660e08-6d0e-4b25-9901-465013e1e3c9')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('8ee50fc6-59ec-4d10-a10b-b694520065ab')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('6afb23f5-4005-4aae-b16d-a93c4997d42c')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('afd84a80-e5d4-4fba-8c3a-91481fb63f20')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('c1b64f67-b918-4a55-9892-e4c41e185fde')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('eb003904-1095-48c6-8554-8265f325061e')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('9bd0c6cb-d6a5-4833-993a-889a7ba3932f')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('91dee533-87f8-4913-bca5-2813f51222e0')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('217b9e18-b1dd-4c27-ba11-acf4337c2c9a')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('fa07ebe0-b9fe-48d6-b540-62243b290b6a')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('5392ea5c-cf2f-46dd-8977-8fccc6056d3a')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('2990c4ed-2750-4825-acba-54b9c6fa0950')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('b3c787c5-0b60-40dc-a560-8e6a6b18c925')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('b2ffecd0-a5db-40c9-85ce-28eecddeef1b')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('dc8abeb0-f297-4147-8589-7ccbada023d9')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('3933207f-478f-494e-9560-93c622f7806b')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('dbc02a5a-094d-48c1-9eb0-754b49c937af')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('1f46b748-8852-4b48-b16e-605352d6b545')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('d7f2def2-219b-4147-b179-a6ffc480d193')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('d5fe600c-0d28-413a-a6dc-4b3a104475be')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('b7c190fd-3684-45c7-9554-299f35aa79ad')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('69cdb9de-8cdb-4b9d-b282-2ae647913428')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('170ef43b-645a-4bab-9cb2-4836ba0bc857')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('0d9894ae-0533-45c6-bd9a-860f12fdf17c')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('54eecd3a-c785-4079-83b6-d4425a5b1f53')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('e6f06f05-b3b1-416f-8ffb-42dee4bb8427')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('cb5c5fa7-1106-4ca4-b829-eb7c0338e9f5')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('2be25674-40e0-4313-9e78-6fbf5bef40a4')

