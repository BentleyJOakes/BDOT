

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
        
        super(HConstfolding_hier_opt, self).__init__(name='HConstfolding_hier_opt', num_nodes=48, edges=[])
        
        # Add the edges
        self.add_edges([(0, 14), (1, 15), (2, 16), (3, 17), (4, 19), (6, 41), (6, 42), (6, 43), (6, 47), (6, 46), (6, 45), (6, 44), (7, 18), (8, 40), (9, 37), (10, 36), (11, 35), (11, 34), (12, 39), (13, 38), (14, 8), (15, 9), (16, 10), (17, 11), (18, 12), (19, 13), (27, 20), (28, 21), (29, 22), (30, 23), (31, 24), (32, 25), (33, 26), (5, 27), (1, 28), (1, 29), (2, 30), (2, 31), (3, 32), (4, 33), (34, 24), (35, 20), (36, 25), (37, 23), (38, 22), (39, 21), (40, 26), (41, 1), (42, 2), (43, 3), (44, 5), (45, 0), (46, 7), (47, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """HConstfolding_hier_opt"""
        self["GUID__"] = UUID('673459bf-5566-4e4c-ad17-071efba1d6aa')
        
        # Set the node attributes
        self.vs[0]["Name"] = """Constant"""
        self.vs[0]["SampleTime"] = """inf"""
        self.vs[0]["value"] = 1.0
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """Constant"""
        self.vs[0]["Position"] = pickle.loads("""(lp1
F135
aF65
aF165
aF95
a.""")
        self.vs[0]["GUID__"] = UUID('8e7690f0-fb5b-4641-b811-de170ebb94b8')
        self.vs[1]["Name"] = """Product"""
        self.vs[1]["SampleTime"] = -1.0
        self.vs[1]["BackgroundColor"] = """yellow"""
        self.vs[1]["mm__"] = """Product"""
        self.vs[1]["Position"] = pickle.loads("""(lp1
F210
aF92
aF240
aF123
a.""")
        self.vs[1]["GUID__"] = UUID('a6b72548-8674-4b07-949a-fc1528e18395')
        self.vs[2]["Inputs"] = """|++"""
        self.vs[2]["Name"] = """Sum"""
        self.vs[2]["SampleTime"] = -1.0
        self.vs[2]["BackgroundColor"] = """yellow"""
        self.vs[2]["mm__"] = """Sum"""
        self.vs[2]["Position"] = pickle.loads("""(lp1
F260
aF100
aF280
aF120
a.""")
        self.vs[2]["IconShape"] = """round"""
        self.vs[2]["GUID__"] = UUID('75ec2801-4434-42ce-b807-3b0f29b7c5b8')
        self.vs[3]["InitialCondition"] = 0.0
        self.vs[3]["Name"] = """Unit Delay"""
        self.vs[3]["SampleTime"] = -1.0
        self.vs[3]["BackgroundColor"] = """yellow"""
        self.vs[3]["mm__"] = """UnitDelay"""
        self.vs[3]["Position"] = pickle.loads("""(lp1
F290
aF93
aF325
aF127
a.""")
        self.vs[3]["GUID__"] = UUID('124cd720-c0ea-48c9-9cfe-e34c09c240a9')
        self.vs[4]["Name"] = """Gain"""
        self.vs[4]["SampleTime"] = -1.0
        self.vs[4]["gain"] = 0.01
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """Gain"""
        self.vs[4]["Position"] = pickle.loads("""(lp1
F200
aF64
aF240
aF96
a.""")
        self.vs[4]["GUID__"] = UUID('f6ebbd27-0664-4f8f-b37e-a3a2f9bf5ed4')
        self.vs[5]["Name"] = """Out1"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """Outport"""
        self.vs[5]["Position"] = pickle.loads("""(lp1
F335
aF38
aF365
aF52
a.""")
        self.vs[5]["Port"] = 1
        self.vs[5]["GUID__"] = UUID('b95002ff-45f2-4990-9731-460ec5b62b43')
        self.vs[6]["Name"] = """HConstfolding_hier"""
        self.vs[6]["mm__"] = """SubSystem"""
        self.vs[6]["Position"] = pickle.loads("""(lp1
.""")
        self.vs[6]["GUID__"] = UUID('db030682-6353-481f-b3ce-4ee829138a53')
        self.vs[7]["Name"] = """In1"""
        self.vs[7]["BackgroundColor"] = """white"""
        self.vs[7]["mm__"] = """Inport"""
        self.vs[7]["Position"] = pickle.loads("""(lp1
F170
aF28
aF200
aF42
a.""")
        self.vs[7]["Port"] = 1
        self.vs[7]["GUID__"] = UUID('fe2ff181-1a99-4db7-a100-54c7ba8405b3')
        self.vs[8]["Name"] = """1"""
        self.vs[8]["mm__"] = """Port_Output"""
        self.vs[8]["GUID__"] = UUID('f1a529b0-9cfa-4364-ab8c-4f4d0a37279b')
        self.vs[9]["Name"] = """1"""
        self.vs[9]["mm__"] = """Port_Output"""
        self.vs[9]["GUID__"] = UUID('f9d89e96-2950-40ae-a35e-76446cec1b01')
        self.vs[10]["Name"] = """1"""
        self.vs[10]["mm__"] = """Port_Output"""
        self.vs[10]["GUID__"] = UUID('e72b4d16-a32e-465e-be11-0dcd3402a3cf')
        self.vs[11]["Name"] = """1"""
        self.vs[11]["mm__"] = """Port_Output"""
        self.vs[11]["GUID__"] = UUID('f86ac6ed-d342-42f9-b656-b21549373413')
        self.vs[12]["Name"] = """1"""
        self.vs[12]["mm__"] = """Port_Output"""
        self.vs[12]["GUID__"] = UUID('8cdba424-6ca3-41ec-92bf-b1140b7431cb')
        self.vs[13]["Name"] = """1"""
        self.vs[13]["mm__"] = """Port_Output"""
        self.vs[13]["GUID__"] = UUID('3f6ae472-f6ef-47c2-8f46-a8dc9dacb0c5')
        self.vs[14]["mm__"] = """__Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('2a4bfee5-e51c-4675-a95a-2e07aa9bd57a')
        self.vs[15]["mm__"] = """__Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('bc43efee-ad74-4eac-b88b-580f2f735724')
        self.vs[16]["mm__"] = """__Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('4928a4c2-606b-48ed-9b1d-7bf4407b014b')
        self.vs[17]["mm__"] = """__Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('3dfb2b62-1392-4d90-84e7-9b9490f4ac4b')
        self.vs[18]["mm__"] = """__Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('e38441b4-1899-41d8-9b2f-c88d876431c9')
        self.vs[19]["mm__"] = """__Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('a22777ca-afb3-440e-b564-bb00db002a97')
        self.vs[20]["Name"] = """1"""
        self.vs[20]["mm__"] = """Port_Input"""
        self.vs[20]["GUID__"] = UUID('1b0c03ba-8ebc-4428-b876-d3a93fa70828')
        self.vs[21]["Name"] = """1"""
        self.vs[21]["mm__"] = """Port_Input"""
        self.vs[21]["GUID__"] = UUID('aa38cc75-5001-4d1c-bb06-c866cd9ae745')
        self.vs[22]["Name"] = """2"""
        self.vs[22]["mm__"] = """Port_Input"""
        self.vs[22]["GUID__"] = UUID('3d6b1715-811b-44fb-a434-3096fa79060e')
        self.vs[23]["Name"] = """1"""
        self.vs[23]["mm__"] = """Port_Input"""
        self.vs[23]["GUID__"] = UUID('247dd097-bf9d-4cfd-9b58-609879ed0e32')
        self.vs[24]["Name"] = """2"""
        self.vs[24]["mm__"] = """Port_Input"""
        self.vs[24]["GUID__"] = UUID('c1413430-7ee7-4dcd-a6ef-91e25944b796')
        self.vs[25]["Name"] = """1"""
        self.vs[25]["mm__"] = """Port_Input"""
        self.vs[25]["GUID__"] = UUID('5a8d6ac9-0fd4-4a6c-9c24-9e78add7a639')
        self.vs[26]["Name"] = """1"""
        self.vs[26]["mm__"] = """Port_Input"""
        self.vs[26]["GUID__"] = UUID('e3d7bb40-0af6-4a39-9016-6ad55f6e3d71')
        self.vs[27]["mm__"] = """__Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('baf40ff3-ea1a-4c53-b2fd-446a4febbe69')
        self.vs[28]["mm__"] = """__Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('f69a03f2-edb9-42ed-bf2f-50b06ed492de')
        self.vs[29]["mm__"] = """__Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('551526d7-1a73-40a6-b8fa-b1ab4019550c')
        self.vs[30]["mm__"] = """__Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('0c382eb4-76ba-4b59-99d0-5425b92e24bc')
        self.vs[31]["mm__"] = """__Block_Inport__"""
        self.vs[31]["GUID__"] = UUID('3ac70b58-83f7-437e-b165-1cec57ddbf67')
        self.vs[32]["mm__"] = """__Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('8371b48e-899d-4d68-b728-ab93047edbd6')
        self.vs[33]["mm__"] = """__Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('badf18b9-358e-4508-8c61-f62992b2ca54')
        self.vs[34]["mm__"] = """__Relation__"""
        self.vs[34]["GUID__"] = UUID('2cfbd0ea-57ab-4f22-a868-235ebe6e422f')
        self.vs[35]["mm__"] = """__Relation__"""
        self.vs[35]["GUID__"] = UUID('0aeb486e-cf59-4681-8283-fdf697984dc1')
        self.vs[36]["mm__"] = """__Relation__"""
        self.vs[36]["GUID__"] = UUID('a137b3ff-827b-4202-b218-4b5fa6cf8431')
        self.vs[37]["mm__"] = """__Relation__"""
        self.vs[37]["GUID__"] = UUID('4b2c8068-f39a-42b0-88fd-830b42110782')
        self.vs[38]["mm__"] = """__Relation__"""
        self.vs[38]["GUID__"] = UUID('6c6014bd-de01-4f82-bdb4-96d4a71f97c9')
        self.vs[39]["mm__"] = """__Relation__"""
        self.vs[39]["GUID__"] = UUID('122bd0ca-30b0-4e7e-ad77-450a38690450')
        self.vs[40]["mm__"] = """__Relation__"""
        self.vs[40]["GUID__"] = UUID('a8429b8f-7fff-47a3-b02e-92a337d8486b')
        self.vs[41]["Name"] = """None"""
        self.vs[41]["mm__"] = """__Contains__"""
        self.vs[41]["GUID__"] = UUID('e15def97-9bc7-4e15-af8d-8198d3045c39')
        self.vs[42]["Name"] = """None"""
        self.vs[42]["mm__"] = """__Contains__"""
        self.vs[42]["GUID__"] = UUID('e3375ace-8f3b-4e5c-8a22-6d12108fc228')
        self.vs[43]["Name"] = """None"""
        self.vs[43]["mm__"] = """__Contains__"""
        self.vs[43]["GUID__"] = UUID('18ac96e2-3544-4ace-8671-878b3a1a288b')
        self.vs[44]["Name"] = """None"""
        self.vs[44]["mm__"] = """__Contains__"""
        self.vs[44]["GUID__"] = UUID('9ce28e48-7109-4c72-be65-ced29b81854b')
        self.vs[45]["Name"] = """None"""
        self.vs[45]["mm__"] = """__Contains__"""
        self.vs[45]["GUID__"] = UUID('cfd44d89-b004-432b-93ad-cec5a1916b2c')
        self.vs[46]["Name"] = """None"""
        self.vs[46]["mm__"] = """__Contains__"""
        self.vs[46]["GUID__"] = UUID('aa19d4ce-2777-4ada-bd2e-9f3ed0b9ddca')
        self.vs[47]["Name"] = """None"""
        self.vs[47]["mm__"] = """__Contains__"""
        self.vs[47]["GUID__"] = UUID('c6c83a2d-09c6-420a-8d43-558a73ba2c6e')

