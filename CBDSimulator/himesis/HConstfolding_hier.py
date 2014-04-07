

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
        
        super(HConstfolding_hier, self).__init__(name='HConstfolding_hier', num_nodes=68, edges=[])
        
        # Add the edges
        self.add_edges([(5, 47), (47, 37), (5, 48), (48, 38), (5, 28), (28, 19), (6, 49), (49, 39), (0, 29), (29, 20), (1, 50), (50, 40), (1, 51), (51, 41), (1, 30), (30, 21), (2, 52), (52, 42), (2, 53), (53, 43), (2, 31), (31, 22), (3, 54), (54, 44), (3, 32), (32, 23), (9, 33), (33, 24), (10, 34), (34, 25), (11, 35), (35, 26), (4, 55), (55, 45), (4, 36), (36, 27), (7, 56), (56, 46), (5, 57), (57, 1), (5, 58), (58, 2), (5, 59), (59, 3), (5, 60), (60, 9), (5, 61), (61, 11), (5, 62), (62, 7), (8, 63), (63, 5), (8, 64), (64, 6), (8, 65), (65, 0), (8, 66), (66, 10), (8, 67), (67, 4), (23, 12), (12, 43), (23, 13), (13, 46), (22, 14), (14, 44), (21, 15), (15, 42), (27, 16), (16, 38), (20, 17), (17, 45), (19, 18), (18, 39)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier"""
        self["GUID__"] = UUID('97164dbe-b7c6-4b37-a1e9-a144bb27ad1b')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = inf
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F125
aF125
aF155
aF155
a.""")
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["GUID__"] = UUID('9a1b9c76-656b-48f7-86bc-88a08d289705')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["GUID__"] = UUID('83dcc29e-7602-47f3-990b-c2b5f9974ef9')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F275
aF100
aF295
aF120
a.""")
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('4135a0cc-31bc-4066-823e-2626db00cd2d')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F325
aF93
aF360
aF127
a.""")
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["GUID__"] = UUID('e5b13792-28ab-4be7-84b5-f01860b22e4d')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F215
aF125
aF245
aF155
a.""")
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["GUID__"] = UUID('bb6c7e3f-75b4-4d94-88ee-32990dd22314')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F320
aF24
aF420
aF66
a.""")
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["GUID__"] = UUID('475f338d-8107-4f8a-96a8-cd4640d4ae81')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F485
aF38
aF515
aF52
a.""")
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('70d4945a-e9be-4ea4-8892-76fb4db57a8b')
        self.vs[7]["Name"] = """Out1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F425
aF103
aF455
aF117
a.""")
        self.vs[7]["mm__"] = """Outport"""
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('b674c207-372e-422a-a1ed-4b15d50bdfba')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["GUID__"] = UUID('f2cab1b1-dc7d-40ca-aa23-4c1c24613ff0')
        self.vs[9]["Name"] = """In2"""
        self.vs[9]["BackgroundColor"] = """white"""
        self.vs[9]["Position"] = pickle.loads("""(lp1
F90
aF153
aF120
aF167
a.""")
        self.vs[9]["mm__"] = """Inport"""
        self.vs[9]["Port"] = 2
        self.vs[9]["GUID__"] = UUID('79cc87dc-37d5-4760-bec5-b8936c7459c7')
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
        self.vs[10]["GUID__"] = UUID('9e68eaec-0461-43f5-a708-a020f707ebbd')
        self.vs[11]["Name"] = """In1"""
        self.vs[11]["BackgroundColor"] = """white"""
        self.vs[11]["Position"] = pickle.loads("""(lp1
F110
aF103
aF140
aF117
a.""")
        self.vs[11]["mm__"] = """Inport"""
        self.vs[11]["Port"] = 1
        self.vs[11]["GUID__"] = UUID('62cff7b4-8a9e-480b-8d95-61534d393bae')
        self.vs[12]["mm__"] = """__Relation__"""
        self.vs[12]["GUID__"] = UUID('556067fa-c97b-412c-b17e-085f19eb0a02')
        self.vs[13]["mm__"] = """__Relation__"""
        self.vs[13]["GUID__"] = UUID('dd2424ed-186b-4b3a-bf18-0c431dc58b0b')
        self.vs[14]["mm__"] = """__Relation__"""
        self.vs[14]["GUID__"] = UUID('12c9cece-725e-43fb-8ef6-eeee73248698')
        self.vs[15]["mm__"] = """__Relation__"""
        self.vs[15]["GUID__"] = UUID('75ff7306-4958-4a43-bf42-f02b33d955fd')
        self.vs[16]["mm__"] = """__Relation__"""
        self.vs[16]["GUID__"] = UUID('85cb9666-d464-4488-8df8-eebef79e98f9')
        self.vs[17]["mm__"] = """__Relation__"""
        self.vs[17]["GUID__"] = UUID('008b3072-85f2-4b3d-83dc-eec95839a32f')
        self.vs[18]["mm__"] = """__Relation__"""
        self.vs[18]["GUID__"] = UUID('f3139a56-0578-42ac-8e56-252bf6556520')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('bc0a0464-24aa-4b4d-ac10-0787fe8535c6')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('ede93010-343d-46a0-9151-a450f5733626')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Output"""
        self.vs[21]["GUID__"] = UUID('457123f5-9fd6-4970-95ef-d583fddeacd8')
        self.vs[22]["Name"] = """1"""
        self.vs[22]["mm__"] = """Port_Output"""
        self.vs[22]["GUID__"] = UUID('68d3cd54-645e-431d-8291-d88bb68a1eef')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Output"""
        self.vs[23]["GUID__"] = UUID('79140a30-30bb-49aa-9d31-11e10a3ff745')
        self.vs[24]["Name"] = """1"""
        self.vs[24]["mm__"] = """Port_Output"""
        self.vs[24]["GUID__"] = UUID('3ac77406-8e5b-48af-90d2-ac7fa2af0c79')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Output"""
        self.vs[25]["GUID__"] = UUID('920a2100-eb82-4243-bdd9-af61e4102526')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Output"""
        self.vs[26]["GUID__"] = UUID('e4fe0731-b6e5-46ec-94f2-6b91bf1325a5')
        self.vs[27]["Name"] = """1"""
        self.vs[27]["mm__"] = """Port_Output"""
        self.vs[27]["GUID__"] = UUID('f128cd9a-f691-4c28-a450-585ae14211b9')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('ffef2614-f097-4514-a7ec-c00eb8faf5ee')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('74dccd6f-adbc-4617-af5c-de88a697520b')
        self.vs[30]["mm__"] = """__Block_Outport__"""
        self.vs[30]["GUID__"] = UUID('e18b00fc-9a99-47c1-afbb-9970fdd72ce2')
        self.vs[31]["mm__"] = """__Block_Outport__"""
        self.vs[31]["GUID__"] = UUID('390a431e-7e7b-43ad-9b57-e3e3ab47d257')
        self.vs[32]["mm__"] = """__Block_Outport__"""
        self.vs[32]["GUID__"] = UUID('d180407f-0862-4299-bcb1-4e09df1d2786')
        self.vs[33]["mm__"] = """__Block_Outport__"""
        self.vs[33]["GUID__"] = UUID('d682c28c-90c6-4dbc-aa49-fb2d20c8cecd')
        self.vs[34]["mm__"] = """__Block_Outport__"""
        self.vs[34]["GUID__"] = UUID('456cc30b-e249-4f18-9753-a0b897d49616')
        self.vs[35]["mm__"] = """__Block_Outport__"""
        self.vs[35]["GUID__"] = UUID('66c92064-c656-4e3a-a384-3efdfc0211cb')
        self.vs[36]["mm__"] = """__Block_Outport__"""
        self.vs[36]["GUID__"] = UUID('7b746cd7-542d-476b-9635-8e8adb2b4bf0')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('b544697f-1612-4b9e-be56-db60831c8e70')
        self.vs[38]["Name"] = """2"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('2b0fee03-a867-4928-a60d-b3e133cade80')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('8220e68e-f382-4594-8df0-5e48a8607f07')
        self.vs[40]["Name"] = """1"""
        self.vs[40]["mm__"] = """Port_Input"""
        self.vs[40]["GUID__"] = UUID('167c8979-6c59-461e-8147-83ebfd2ac7be')
        self.vs[41]["Name"] = """2"""
        self.vs[41]["mm__"] = """Port_Input"""
        self.vs[41]["GUID__"] = UUID('ce2c72ba-c219-4c19-841b-e3a70437225f')
        self.vs[42]["Name"] = """1"""
        self.vs[42]["mm__"] = """Port_Input"""
        self.vs[42]["GUID__"] = UUID('56e34f11-ec4a-474b-abc3-9d58506b82cb')
        self.vs[43]["Name"] = """2"""
        self.vs[43]["mm__"] = """Port_Input"""
        self.vs[43]["GUID__"] = UUID('11e6bb4b-4d3e-4a3d-8ee3-d543b385b6f9')
        self.vs[44]["Name"] = """1"""
        self.vs[44]["mm__"] = """Port_Input"""
        self.vs[44]["GUID__"] = UUID('175fa6b8-8d69-454a-b359-437d8f2e4de2')
        self.vs[45]["Name"] = """1"""
        self.vs[45]["mm__"] = """Port_Input"""
        self.vs[45]["GUID__"] = UUID('b9035820-931d-4ba5-9cc4-572b41153eeb')
        self.vs[46]["Name"] = """1"""
        self.vs[46]["mm__"] = """Port_Input"""
        self.vs[46]["GUID__"] = UUID('2eb33d19-61e4-483b-aa41-14e446c503b6')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('11cada30-99ca-40ae-8d0d-293eac088a45')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('dca50589-618e-45ad-83e1-94cf6b855e09')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('6c7c0890-e666-44c7-97b4-0158a3edb676')
        self.vs[50]["mm__"] = """__Block_Inport__"""
        self.vs[50]["GUID__"] = UUID('e5085383-578b-4c86-9e43-3874def4d8c4')
        self.vs[51]["mm__"] = """__Block_Inport__"""
        self.vs[51]["GUID__"] = UUID('f08a372b-0c71-4c34-9a84-f0d09216e222')
        self.vs[52]["mm__"] = """__Block_Inport__"""
        self.vs[52]["GUID__"] = UUID('40b625f6-69d8-4e31-b848-c70c8a5cc8af')
        self.vs[53]["mm__"] = """__Block_Inport__"""
        self.vs[53]["GUID__"] = UUID('9ef00c7c-9770-46ee-a584-f55b25926057')
        self.vs[54]["mm__"] = """__Block_Inport__"""
        self.vs[54]["GUID__"] = UUID('8a9c4b19-7e2c-4c9f-953c-0d7f1c68ab49')
        self.vs[55]["mm__"] = """__Block_Inport__"""
        self.vs[55]["GUID__"] = UUID('f35904ea-b6c3-46d6-bdfd-d4c5d2bb6cb5')
        self.vs[56]["mm__"] = """__Block_Inport__"""
        self.vs[56]["GUID__"] = UUID('96a04d7e-f8e2-44c3-a4ae-794757eccda2')
        self.vs[57]["Name"] = """None"""
        self.vs[57]["mm__"] = """__Contains__"""
        self.vs[57]["GUID__"] = UUID('efefc1e3-4708-4c33-8a6f-5cdf18822d77')
        self.vs[58]["Name"] = """None"""
        self.vs[58]["mm__"] = """__Contains__"""
        self.vs[58]["GUID__"] = UUID('25ab47d0-0ddd-4ff8-8e19-1d861d99440f')
        self.vs[59]["Name"] = """None"""
        self.vs[59]["mm__"] = """__Contains__"""
        self.vs[59]["GUID__"] = UUID('2a5e9322-4870-4797-8013-26055efe3e80')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('6e9978ae-e8cc-4110-b8d8-e76f24ffbb7c')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('ec622fbb-f990-4666-9a4a-41765d9fbe6b')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('db6a3059-53ca-4656-abfa-76b3f842b0b7')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('8b836d28-cd6d-4ba7-a440-df62ad5e5514')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('8016c007-c2cc-4928-b4c0-06070833e246')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('3bf1ecb8-5c61-434f-b9b7-962fdbe021c0')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('9c221e16-0c32-4b90-ad57-3551fd951c0c')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('c47945bf-9632-42ac-af4e-48b04ae131ca')

