

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
        self["GUID__"] = UUID('6ffa8ab0-cd75-4065-a650-ddae21a9fb4f')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F140
aF65
aF170
aF95
a.""")
        self.vs[0]["GUID__"] = UUID('3659c2ca-382a-41fa-b1c5-c3d64e30e36c')
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
        self.vs[1]["GUID__"] = UUID('8526ad8a-7650-47f1-98eb-db38749fa7c2')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('f64e7c14-387c-4fdc-bc68-ce27e0e6619a')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('2dd31819-269c-4c1e-a8c2-91345f22f9c6')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F205
aF65
aF235
aF95
a.""")
        self.vs[4]["GUID__"] = UUID('6482f27f-5464-4109-8701-220cd0d6662c')
        self.vs[5]["Name"] = """Subsystem"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """SubSystem"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F260
aF24
aF305
aF66
a.""")
        self.vs[5]["GUID__"] = UUID('f11fe1ec-5a5d-4e0b-9850-9020cf463866')
        self.vs[6]["Name"] = """Out1"""
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Outport"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[6]["Port"] = 1
        self.vs[6]["GUID__"] = UUID('f179b4b4-2918-4965-a058-0787a08bac50')
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
        self.vs[7]["GUID__"] = UUID('627d38e6-3572-4d51-b32b-0b365d24f482')
        self.vs[8]["Name"] = """HConstfolding_hier"""
        self.vs[8]["mm__"] = """SubSystem"""
        self.vs[8]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[8]["GUID__"] = UUID('dee92175-21e2-4cf1-bf15-c17837b81768')
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
        self.vs[9]["GUID__"] = UUID('879fbead-b6a1-4b9c-8a1e-59bfad5c8b11')
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
        self.vs[10]["GUID__"] = UUID('d0d7833c-f5f4-4d59-a8b2-5c007e06b645')
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
        self.vs[11]["GUID__"] = UUID('d97efeb7-9739-4770-a250-a85ce147c7a4')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('d56dbe4c-c339-4b63-98e3-1ac65065a45c')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('5fd9cfbd-0592-4f7b-8622-f9c31a2401e3')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('33d62b74-1aa5-45f1-8faf-e68928d56646')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('d99cea76-7362-418b-8999-e3c009802f6d')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('955b47a2-c04f-498f-95f1-7d7585b9c309')
        self.vs[17]["Name"] = """1"""
        self.vs[17]["mm__"] = """Port_Output"""
        self.vs[17]["GUID__"] = UUID('0042e3f2-8bb8-4b99-be2b-9aa4cc3523d4')
        self.vs[18]["Name"] = """1"""
        self.vs[18]["mm__"] = """Port_Output"""
        self.vs[18]["GUID__"] = UUID('33c4ae59-5d78-495b-99a3-09eed33dc1ab')
        self.vs[19]["Name"] = """1"""
        self.vs[19]["mm__"] = """Port_Output"""
        self.vs[19]["GUID__"] = UUID('8ae493b7-4328-4ae2-9d5a-1b645b7bf4dd')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Output"""
        self.vs[20]["GUID__"] = UUID('340ec685-a8cf-4a59-9863-e85027cf1434')
        self.vs[21]["mm__"] = """__Block_Outport__"""
        self.vs[21]["GUID__"] = UUID('df8abb3c-d362-4f42-8d06-19378de8a53d')
        self.vs[22]["mm__"] = """__Block_Outport__"""
        self.vs[22]["GUID__"] = UUID('f43ea105-0751-4bf2-97c5-f4cc918775a3')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('260b8fe0-4156-4867-8624-139b9bddb540')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('0ae7429a-709d-4083-b0ba-b44cbc47c383')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('8b9b9afb-6975-443c-a4b7-a87ad5460080')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('40dbee7e-bdf8-4838-ae62-099c2e25c5ad')
        self.vs[27]["mm__"] = """__Block_Outport__"""
        self.vs[27]["GUID__"] = UUID('69e456d5-1a24-4bc4-b840-a7bc6219a243')
        self.vs[28]["mm__"] = """__Block_Outport__"""
        self.vs[28]["GUID__"] = UUID('0a9ed894-8fce-4550-af02-26e8217e3d3a')
        self.vs[29]["mm__"] = """__Block_Outport__"""
        self.vs[29]["GUID__"] = UUID('2bc54a0b-7f1f-4e5f-9363-8e97f2c441a4')
        self.vs[30]["Name"] = """1"""
        self.vs[30]["mm__"] = """Port_Input"""
        self.vs[30]["GUID__"] = UUID('b9bcfc5f-18d9-4f5b-b1a0-fa0a3a4c1ce0')
        self.vs[31]["Name"] = """2"""
        self.vs[31]["mm__"] = """Port_Input"""
        self.vs[31]["GUID__"] = UUID('c801e1da-d4bc-4c99-be07-792edbe29ec3')
        self.vs[32]["Name"] = """1"""
        self.vs[32]["mm__"] = """Port_Input"""
        self.vs[32]["GUID__"] = UUID('457c614e-9e2f-46c2-93fa-134c0d9996c0')
        self.vs[33]["Name"] = """1"""
        self.vs[33]["mm__"] = """Port_Input"""
        self.vs[33]["GUID__"] = UUID('5870f340-60f5-49dc-9772-9d418257f825')
        self.vs[34]["Name"] = """2"""
        self.vs[34]["mm__"] = """Port_Input"""
        self.vs[34]["GUID__"] = UUID('aa6ff387-ab03-4ce0-bf27-30e82c2b0b34')
        self.vs[35]["Name"] = """1"""
        self.vs[35]["mm__"] = """Port_Input"""
        self.vs[35]["GUID__"] = UUID('03046569-293a-43ff-9210-34e25a2c235c')
        self.vs[36]["Name"] = """2"""
        self.vs[36]["mm__"] = """Port_Input"""
        self.vs[36]["GUID__"] = UUID('d0168662-a7bb-438c-907d-b50c652184ad')
        self.vs[37]["Name"] = """1"""
        self.vs[37]["mm__"] = """Port_Input"""
        self.vs[37]["GUID__"] = UUID('c1d2a29c-63e3-43c2-bc2d-5e430f30cc72')
        self.vs[38]["Name"] = """1"""
        self.vs[38]["mm__"] = """Port_Input"""
        self.vs[38]["GUID__"] = UUID('b6cc2410-f2eb-43d0-ad4f-7721b64af1ab')
        self.vs[39]["Name"] = """1"""
        self.vs[39]["mm__"] = """Port_Input"""
        self.vs[39]["GUID__"] = UUID('476748b9-2516-4b0b-ae76-e3f56f90d527')
        self.vs[40]["mm__"] = """__Block_Inport__"""
        self.vs[40]["GUID__"] = UUID('29e2d085-5958-4829-b5e4-f116d7083808')
        self.vs[41]["mm__"] = """__Block_Inport__"""
        self.vs[41]["GUID__"] = UUID('f69789d3-21b8-4173-b6c3-08ec6b3bf402')
        self.vs[42]["mm__"] = """__Block_Inport__"""
        self.vs[42]["GUID__"] = UUID('30bd5a81-31bc-4f79-a5da-0676e8edf198')
        self.vs[43]["mm__"] = """__Block_Inport__"""
        self.vs[43]["GUID__"] = UUID('cd9392e8-0e29-47d3-aaf1-cfd0220c7acd')
        self.vs[44]["mm__"] = """__Block_Inport__"""
        self.vs[44]["GUID__"] = UUID('247691e0-df3b-4391-920e-8454e06a240e')
        self.vs[45]["mm__"] = """__Block_Inport__"""
        self.vs[45]["GUID__"] = UUID('077aabe0-4e4c-474a-9b30-85f8fa7df307')
        self.vs[46]["mm__"] = """__Block_Inport__"""
        self.vs[46]["GUID__"] = UUID('725087a3-9de7-489a-8ff0-ea5e2dc3c4b4')
        self.vs[47]["mm__"] = """__Block_Inport__"""
        self.vs[47]["GUID__"] = UUID('b0cbeba6-e510-4c05-8ac1-f7e3b8435078')
        self.vs[48]["mm__"] = """__Block_Inport__"""
        self.vs[48]["GUID__"] = UUID('ff8a27fb-b234-4e43-8979-e8b165ef67bc')
        self.vs[49]["mm__"] = """__Block_Inport__"""
        self.vs[49]["GUID__"] = UUID('8b6a23fd-6e3c-44f1-918a-d06dd026d077')
        self.vs[50]["mm__"] = """__Relation__"""
        self.vs[50]["GUID__"] = UUID('43ba4f0f-a850-4aed-af0d-2debf26ad277')
        self.vs[51]["mm__"] = """__Relation__"""
        self.vs[51]["GUID__"] = UUID('27cdf9a6-f4dd-43ac-8d4b-325175727ea2')
        self.vs[52]["mm__"] = """__Relation__"""
        self.vs[52]["GUID__"] = UUID('6da6577d-5fc0-4d7f-93a5-ae8906956884')
        self.vs[53]["mm__"] = """__Relation__"""
        self.vs[53]["GUID__"] = UUID('e172c522-3be4-4cc9-8ce4-c38065817f33')
        self.vs[54]["mm__"] = """__Relation__"""
        self.vs[54]["GUID__"] = UUID('2db665dd-143a-4a6f-bbde-60b7cd533cb8')
        self.vs[55]["mm__"] = """__Relation__"""
        self.vs[55]["GUID__"] = UUID('59feec8a-1ef8-4d57-b4e6-2c732faa3b9a')
        self.vs[56]["mm__"] = """__Relation__"""
        self.vs[56]["GUID__"] = UUID('0284e822-9b45-4d76-98d5-4a9cff4e5fa2')
        self.vs[57]["mm__"] = """__Relation__"""
        self.vs[57]["GUID__"] = UUID('1d87975c-500f-4b69-bd02-fda9f5d328e1')
        self.vs[58]["mm__"] = """__Relation__"""
        self.vs[58]["GUID__"] = UUID('764a2625-bde1-48cd-8f89-dc5a681ad9a7')
        self.vs[59]["mm__"] = """__Relation__"""
        self.vs[59]["GUID__"] = UUID('4a593715-0b3b-4a3a-909b-43988351b457')
        self.vs[60]["Name"] = """None"""
        self.vs[60]["mm__"] = """__Contains__"""
        self.vs[60]["GUID__"] = UUID('540832a3-addc-4051-9f6a-b335d3092e77')
        self.vs[61]["Name"] = """None"""
        self.vs[61]["mm__"] = """__Contains__"""
        self.vs[61]["GUID__"] = UUID('0944b602-8371-4166-9334-9f784fbab567')
        self.vs[62]["Name"] = """None"""
        self.vs[62]["mm__"] = """__Contains__"""
        self.vs[62]["GUID__"] = UUID('754748d5-bc16-47e2-9ff1-c3bf49937178')
        self.vs[63]["Name"] = """None"""
        self.vs[63]["mm__"] = """__Contains__"""
        self.vs[63]["GUID__"] = UUID('9d5f8649-ee54-4ff5-bdb0-08af3d63e061')
        self.vs[64]["Name"] = """None"""
        self.vs[64]["mm__"] = """__Contains__"""
        self.vs[64]["GUID__"] = UUID('d5e3f136-d722-464e-b582-55dafbf876de')
        self.vs[65]["Name"] = """None"""
        self.vs[65]["mm__"] = """__Contains__"""
        self.vs[65]["GUID__"] = UUID('b7742763-4f16-4037-88a4-6857331194ca')
        self.vs[66]["Name"] = """None"""
        self.vs[66]["mm__"] = """__Contains__"""
        self.vs[66]["GUID__"] = UUID('584cf275-def8-4aad-829d-aad52ea37211')
        self.vs[67]["Name"] = """None"""
        self.vs[67]["mm__"] = """__Contains__"""
        self.vs[67]["GUID__"] = UUID('7ecdc812-8c4a-479a-b256-28c5f8259a18')
        self.vs[68]["Name"] = """None"""
        self.vs[68]["mm__"] = """__Contains__"""
        self.vs[68]["GUID__"] = UUID('2abc4008-c233-43cf-adaa-16cd06cc003b')
        self.vs[69]["Name"] = """None"""
        self.vs[69]["mm__"] = """__Contains__"""
        self.vs[69]["GUID__"] = UUID('3e84f26d-86e6-41c5-892c-7d78e1147532')
        self.vs[70]["Name"] = """None"""
        self.vs[70]["mm__"] = """__Contains__"""
        self.vs[70]["GUID__"] = UUID('5922054d-fa65-48c7-ba43-a51bd1da69d8')

