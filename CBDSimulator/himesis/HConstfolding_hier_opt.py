

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
        self.add_edges([(0, 22), (1, 23), (2, 24), (3, 25), (4, 29), (5, 65), (5, 64), (5, 63), (5, 62), (5, 61), (5, 60), (5, 21), (8, 70), (8, 69), (8, 68), (8, 67), (8, 66), (9, 26), (10, 27), (11, 28), (12, 59), (13, 58), (14, 55), (15, 54), (16, 53), (16, 52), (17, 51), (18, 57), (19, 50), (20, 56), (21, 12), (22, 13), (23, 14), (24, 15), (25, 16), (26, 17), (27, 18), (28, 19), (29, 20), (40, 30), (41, 31), (42, 32), (43, 33), (44, 34), (45, 35), (46, 36), (47, 37), (48, 38), (49, 39), (5, 40), (5, 41), (6, 42), (1, 43), (1, 44), (2, 45), (2, 46), (3, 47), (4, 48), (7, 49), (50, 33), (51, 34), (52, 36), (53, 39), (54, 37), (55, 35), (56, 31), (57, 30), (58, 38), (59, 32), (60, 1), (61, 2), (62, 3), (63, 9), (64, 11), (65, 7), (66, 5), (67, 6), (68, 0), (69, 10), (70, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('43002890-8aaf-4b4f-a4fe-9df2e439c8a6')
        
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
        self.vs[0]["GUID__"] = UUID('804c40c9-2ebb-4a2e-aa26-441f3819ab35')
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
        self.vs[1]["GUID__"] = UUID('45c66f4f-ae86-4b0f-a114-65af6f835394')
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
        self.vs[2]["GUID__"] = UUID('ecd01f99-4244-41af-b71e-aeed8ab3ec16')
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
        self.vs[3]["GUID__"] = UUID('7a08030d-ce67-4ee3-ad2d-33bcb6ab07fd')
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
        self.vs[4]["GUID__"] = UUID('55201f7c-ea9b-4350-b76e-74aef3d638ed')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F320
aF24
aF420
aF66
a.""")
        self.vs[5]["GUID__"] = UUID('2c7519b4-ce4f-4af4-95ea-3ecb8ae1a78b')
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
        self.vs[6]["GUID__"] = UUID('7e5d79a4-80bd-4979-ba09-dec738e7250e')
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
        self.vs[7]["GUID__"] = UUID('e96139c6-9820-4a90-8898-0c3aa92928ea')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["GUID__"] = UUID('e0acbcb3-855e-4ed1-afe2-fc9262839377')
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
        self.vs[9]["GUID__"] = UUID('de5311bc-1dbb-40b5-87c7-952362d58d3c')
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
        self.vs[10]["GUID__"] = UUID('4a0932a6-6a12-4387-ab7c-c72b7f2bde3b')
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
        self.vs[11]["GUID__"] = UUID('3ea5f228-8b5d-4fe4-beab-441ddace71af')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('f8fe6769-2899-437b-ab5d-6792b9eeac30')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('69ae298e-b412-42a9-839b-b162a3fe6b39')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('fb477f64-c7a8-4e5d-a8ef-85be7688ae31')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('22b6d8d6-ec82-4517-86aa-ae3ba9a460e1')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('9296f988-9395-46e3-9f6b-bf7304053de8')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('98857e4e-59d4-41b5-95d0-4ab157cd0f7c')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('e42f3358-58fd-4aaa-bf33-511f8a132ae8')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('6bf7929c-bcc0-407d-816e-6df7a62fb6f5')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('fd05b8e7-8526-4b05-ae2a-55a77d44015b')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('3618bcdc-5f13-41be-a0a9-95937648e615')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('7d5fef0d-8a83-4b31-9517-68ddd44e401e')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('92726bec-f19b-4968-b090-156115cb5a53')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('58fed9c1-aafb-4880-b5f9-cc54abc508b4')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('b6dbdf78-6846-4849-9f48-cf0733575fdb')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('81d6962b-f710-4fcb-9e24-79ca263df2fa')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('f491b55e-8473-457f-9b4d-b7c0c477d652')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('9851759f-4c86-4b68-8551-d8a8c81c25f8')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('0d7385c0-17aa-45c6-b9c2-3f1ada87da00')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('efcc670b-e1cf-4a71-ac36-5520ea9c0c0b')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('fbec7219-6d4f-4da7-88ce-57402b456fe1')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('6f87b7d2-3064-4730-922d-e15d7508a913')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('8281150d-210f-4620-8cc3-1aae236fc5aa')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('525bba1c-2d39-4092-bbcc-03472cbaf5ac')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('7bf2d4fe-cf32-43d8-9430-426f36e8adeb')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('408b6da2-3ed2-4ce7-947a-d9a03caba716')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('d3f6f2d8-9d9a-4e00-93ee-925b2d37546f')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('238fce68-758a-4d25-b52c-d583d9c1ae3e')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('5cafe6fb-79a3-4824-a356-df72f9a88c84')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('0fc2115e-293e-47bd-858e-45036ff875c4')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('eebbaba3-dbb3-4b1e-80b7-e7d13a2e85c8')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('192fcb57-7bd1-4118-addb-ab1259ce4c7d')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('4aedd2ae-04e5-4626-8046-079a89989c53')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('7fded142-5cfa-4aeb-bfca-208de4577fa7')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('b5c69fa9-035c-4936-9f01-962e91c007dd')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('e7872e38-acf7-4664-974c-85de522dce71')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('326ef68c-e7ee-4797-8a22-1493ec5ff775')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('c6609d29-ffe2-4bdf-8a3a-09d01062ce57')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('c93da69e-523a-419b-8e0c-9b76cdb95042')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('9f07a7fd-eafe-4dd6-80dd-885053dcfba2')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('d4238079-3dec-48b4-9f1e-c13d09cd1adb')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('50b94d43-4078-432c-b001-c5299a0120f0')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('d2fde735-5c78-488a-8959-9e81e5fe4eb0')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('971bf6f1-4960-44a6-87c0-a6614baf2b91')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('53a01732-8508-4662-aef0-65f92521a9da')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('560052ee-b011-400c-ab69-f247d9d228c0')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('aee4c6c6-87ca-445c-9112-d88f32e8aabb')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('bdd8df3f-7907-469f-a0e5-c03e72d177a6')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('63c5c07b-722e-43d1-87eb-dafa2ae18e8a')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('2d4bc541-88d2-4759-9b42-4a572b048540')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('7b5fb2ee-17c8-43c4-85ba-32ebae6f6944')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('2b18a913-4295-458e-9149-7002f5f5fb6f')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('6df181a1-ac8e-432d-99b9-b81f796f19f6')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('7b8cd210-88e1-4e17-89e3-5f41d1c65607')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('ffc7caa5-b265-4b06-8939-1b5649df4e5f')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('393ddd3b-7975-463a-ab94-4370c4832673')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('1cba3f3d-08f5-4016-b1aa-94070e804b75')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('46bddd26-cf07-4299-8290-22c419e0fc32')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('1abf651d-dc2f-4ea5-8665-7e91e4583ff5')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('716b5cd2-3a5f-4393-a43e-2edbd88c0538')

