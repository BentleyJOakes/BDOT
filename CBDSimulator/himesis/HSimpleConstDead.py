

from Server.TCore.core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HSimpleConstDead(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HSimpleConstDead.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSimpleConstDead, self).__init__(name='HSimpleConstDead', num_nodes=38, edges=[])
        
        # Add the edges
        self.add_edges([(0, 17), (17, 7), (1, 18), (18, 8), (1, 19), (19, 9), (1, 20), (20, 10), (2, 21), (21, 11), (2, 22), (22, 12), (2, 23), (23, 13), (3, 24), (24, 14), (5, 25), (25, 15), (6, 26), (26, 16), (4, 32), (32, 0), (4, 33), (33, 1), (4, 34), (34, 2), (4, 35), (35, 3), (4, 36), (36, 5), (4, 37), (37, 6), (16, 27), (27, 8), (16, 28), (28, 11), (10, 29), (29, 7), (14, 30), (30, 9), (15, 31), (31, 12)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HSimpleConstDead"""
        self["GUID__"] = UUID('b2bb0e2c-2176-45a5-99bb-f5ad9a3dd347')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Out1"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Outport"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F390
aF118
aF420
aF132
a.""")
        self.vs[0]["Port"] = 1
        self.vs[0]["GUID__"] = UUID('2786629c-3675-4d26-ab47-8c3c690183e6')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F305
aF132
aF335
aF163
a.""")
        self.vs[1]["GUID__"] = UUID('ff4ffdbf-6914-48e9-acdb-f7549e9b57b9')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F140
aF120
aF160
aF140
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('26220606-6ab7-44cb-9875-c2705afcb3ba')
        self.vs[3]["Name"] = """In1"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """Inport"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F170
aF178
aF200
aF192
a.""")
        self.vs[3]["Port"] = 1
        self.vs[3]["GUID__"] = UUID('3689b023-ed9f-46f7-9200-ebb3205e3f7d')
        self.vs[4]["Name"] = """HSimpleConstDead"""
        self.vs[4]["mm__"] = """SubSystem"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[4]["GUID__"] = UUID('3d60f01f-1ba7-4491-8bc2-ef9d5cb29893')
        self.vs[5]["Name"] = """Constant1"""
        self.vs[5]["SampleTime"] = inf
        self.vs[5]["value"] = 112.32
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Constant"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F85
aF168
aF135
aF202
a.""")
        self.vs[5]["GUID__"] = UUID('5590cdd4-2296-4968-aba6-802bf7d56f09')
        self.vs[6]["Name"] = """Constant2"""
        self.vs[6]["SampleTime"] = inf
        self.vs[6]["value"] = 433.22
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["mm__"] = """Constant"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
F50
aF82
aF105
aF118
a.""")
        self.vs[6]["GUID__"] = UUID('630fe897-abb5-4721-8c9f-adb310c2b356')
        self.vs[7]["Name"] = """1"""
        self.vs[7]["mm__"] = """Port_Input"""
        self.vs[7]["GUID__"] = UUID('5b417381-bcc0-4b9d-adc8-eaf26eb31a60')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Input"""
        self.vs[8]["GUID__"] = UUID('5e74f755-42bc-4497-9e42-2e94e1243b52')
        self.vs[9]["Name"] = """2"""
        self.vs[9]["mm__"] = """Port_Input"""
        self.vs[9]["GUID__"] = UUID('ef1dca5a-e814-499e-b794-27e7238b57d2')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('cc3efc10-3e3d-4a51-ae51-62d59ad424bc')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Input"""
        self.vs[11]["GUID__"] = UUID('307888a6-17ba-410f-8e04-5026c79aec6d')
        self.vs[12]["Name"] = """2"""
        self.vs[12]["mm__"] = """Port_Input"""
        self.vs[12]["GUID__"] = UUID('33ec8fe7-389b-42e1-844e-15d8a0837210')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('15b8e60f-9642-4132-92b9-0fd9a3a8a247')
        self.vs[14]["Name"] = """1"""
        self.vs[14]["mm__"] = """Port_Output"""
        self.vs[14]["GUID__"] = UUID('e4169261-ceca-4a46-96ca-2b9171a1a46f')
        self.vs[15]["Name"] = """1"""
        self.vs[15]["mm__"] = """Port_Output"""
        self.vs[15]["GUID__"] = UUID('66492617-9dc7-404e-ad08-f3e178565b03')
        self.vs[16]["Name"] = """1"""
        self.vs[16]["mm__"] = """Port_Output"""
        self.vs[16]["GUID__"] = UUID('f564acf5-5adf-4028-b47c-3588ad609f9d')
        self.vs[17]["mm__"] = """__Block_Inport__"""
        self.vs[17]["GUID__"] = UUID('73f3720f-177b-4130-a8af-1657076a5510')
        self.vs[18]["mm__"] = """__Block_Inport__"""
        self.vs[18]["GUID__"] = UUID('d877201a-b49d-4fa1-a6bc-dfdac3a9d800')
        self.vs[19]["mm__"] = """__Block_Inport__"""
        self.vs[19]["GUID__"] = UUID('2894a3a6-6217-4257-a134-fa8e0a0a6cb8')
        self.vs[20]["mm__"] = """__Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('b5ad22e8-0cef-47f5-b645-c23c8ad566ce')
        self.vs[21]["mm__"] = """__Block_Inport__"""
        self.vs[21]["GUID__"] = UUID('c2bd00f1-0ce1-471e-a83a-f3375b58c463')
        self.vs[22]["mm__"] = """__Block_Inport__"""
        self.vs[22]["GUID__"] = UUID('53b76e78-07a0-41ad-8956-e7ccf90e9c2c')
        self.vs[23]["mm__"] = """__Block_Outport__"""
        self.vs[23]["GUID__"] = UUID('eedc9af4-b8e9-4203-b4f5-ec754ca401ff')
        self.vs[24]["mm__"] = """__Block_Outport__"""
        self.vs[24]["GUID__"] = UUID('bdfb258e-6a29-4bec-8c96-6e6758fd11e0')
        self.vs[25]["mm__"] = """__Block_Outport__"""
        self.vs[25]["GUID__"] = UUID('cc3503c8-0d32-4ec2-9922-0635dd798565')
        self.vs[26]["mm__"] = """__Block_Outport__"""
        self.vs[26]["GUID__"] = UUID('32ca412c-6b23-4ddd-a412-dc4e92cfeb32')
        self.vs[27]["mm__"] = """__Relation__"""
        self.vs[27]["GUID__"] = UUID('9af174ae-b711-40f5-903b-4065c2ade80a')
        self.vs[28]["mm__"] = """__Relation__"""
        self.vs[28]["GUID__"] = UUID('0175598a-45b4-4907-b4d9-6eb9de77c10f')
        self.vs[29]["mm__"] = """__Relation__"""
        self.vs[29]["GUID__"] = UUID('029995bd-5011-420a-b73a-65abce3608ce')
        self.vs[30]["mm__"] = """__Relation__"""
        self.vs[30]["GUID__"] = UUID('71acf17b-5fce-415d-a2f6-686cc98d500a')
        self.vs[31]["mm__"] = """__Relation__"""
        self.vs[31]["GUID__"] = UUID('a166d687-d73c-4f01-bb78-34c77804b315')
        self.vs[32]["Name"] = """None"""
        self.vs[32]["mm__"] = """__Contains__"""
        self.vs[32]["GUID__"] = UUID('6fe50c66-2655-479c-8b05-43ad7a7c2371')
        self.vs[33]["Name"] = """None"""
        self.vs[33]["mm__"] = """__Contains__"""
        self.vs[33]["GUID__"] = UUID('dc0eb67c-f1aa-466f-a2c2-642db55f9ae8')
        self.vs[34]["Name"] = """None"""
        self.vs[34]["mm__"] = """__Contains__"""
        self.vs[34]["GUID__"] = UUID('d67ab269-6ea1-4403-9a54-704d37320a16')
        self.vs[35]["Name"] = """None"""
        self.vs[35]["mm__"] = """__Contains__"""
        self.vs[35]["GUID__"] = UUID('99d80e5a-482a-424f-9717-11801645bc9d')
        self.vs[36]["Name"] = """None"""
        self.vs[36]["mm__"] = """__Contains__"""
        self.vs[36]["GUID__"] = UUID('d5d2b8fe-8f5c-4d8d-a1a8-f85d1d2d7af9')
        self.vs[37]["Name"] = """None"""
        self.vs[37]["mm__"] = """__Contains__"""
        self.vs[37]["GUID__"] = UUID('d6758299-e49b-4f09-adbb-b407d4270f20')

