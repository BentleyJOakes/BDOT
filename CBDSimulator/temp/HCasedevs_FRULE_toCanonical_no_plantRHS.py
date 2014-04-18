

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_FRULE_toCanonical_no_plantRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_FRULE_toCanonical_no_plantRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_FRULE_toCanonical_no_plantRHS, self).__init__(name='HCasedevs_FRULE_toCanonical_no_plantRHS', num_nodes=40, edges=[])
        
        # Add the edges
        self.add_edges([(4, 34), (34, 22), (4, 12), (12, 7), (0, 35), (35, 23), (0, 13), (13, 8), (5, 36), (36, 24), (5, 14), (14, 9), (6, 37), (37, 25), (6, 15), (15, 10), (1, 38), (38, 26), (1, 39), (39, 27), (1, 16), (16, 11), (8, 17), (17, 22), (8, 18), (18, 25), (9, 19), (19, 23), (10, 20), (20, 27), (11, 21), (21, 24), (3, 28), (28, 2), (2, 29), (29, 4), (2, 30), (30, 0), (2, 31), (31, 5), (2, 32), (32, 6), (2, 33), (33, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('356cc416-659d-4575-8eac-5bb6114afc1b')
        
        # Set the node attributes
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[0]["MT_post__InitialCondition"] = """return 0"""
        self.vs[0]["MT_label__"] = """6"""
        self.vs[0]["MT_post__Name"] = """return PreNode('2')['Name']+'_int'"""
        self.vs[0]["mm__"] = """MT_post__Integrator"""
        self.vs[0]["GUID__"] = UUID('8203adf6-641b-4dbd-a91f-05e54704c78f')
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[1]["MT_label__"] = """4"""
        self.vs[1]["MT_post__Name"] = """return PreNode('2')['Name']+'_add1'"""
        self.vs[1]["mm__"] = """MT_post__Sum"""
        self.vs[1]["GUID__"] = UUID('2abdd17e-dbeb-4507-ad87-556ac69ae4ca')
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["MT_label__"] = """9"""
        self.vs[2]["MT_post__Name"] = """return attr_value"""
        self.vs[2]["mm__"] = """MT_post__SubSystem"""
        self.vs[2]["GUID__"] = UUID('e8a22e88-4215-466b-805a-89b53a392038')
        self.vs[3]["MT_label__"] = """99"""
        self.vs[3]["MT_post__Name"] = """return attr_value"""
        self.vs[3]["mm__"] = """MT_post__SubSystem"""
        self.vs[3]["GUID__"] = UUID('1e353349-66ef-4543-9b15-31357a036ea5')
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[4]["MT_label__"] = """7"""
        self.vs[4]["MT_post__gain"] = """return PreNode('2')['Numerator'][0]"""
        self.vs[4]["MT_post__Name"] = """return PreNode('2')['Name']+'Gain_N_1'"""
        self.vs[4]["mm__"] = """MT_post__Gain"""
        self.vs[4]["GUID__"] = UUID('31bc2b71-5ace-4995-a756-f2baf53dddc6')
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[5]["MT_label__"] = """5"""
        self.vs[5]["MT_post__gain"] = """return PreNode('2')['Denominator'][0]"""
        self.vs[5]["MT_post__Name"] = """return PreNode('2')['Name']+'_Gain_D2'"""
        self.vs[5]["mm__"] = """MT_post__Gain"""
        self.vs[5]["GUID__"] = UUID('dd3a0968-0b29-43fc-9fd8-093c19c119e3')
        self.vs[6]["BackgroundColor"] = """white"""
        self.vs[6]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[6]["MT_label__"] = """8"""
        self.vs[6]["MT_post__gain"] = """return -PreNode('2')['Denominator'][1]"""
        self.vs[6]["MT_post__Name"] = """return PreNode('2')['Name']+'_Gain_D1'"""
        self.vs[6]["mm__"] = """MT_post__Gain"""
        self.vs[6]["GUID__"] = UUID('14b23327-d5af-4ca2-b0b1-06ce98a66223')
        self.vs[7]["MT_label__"] = """3"""
        self.vs[7]["MT_post__Name"] = """return 1"""
        self.vs[7]["mm__"] = """MT_post__Port_Output"""
        self.vs[7]["GUID__"] = UUID('17642504-73cb-4173-94b6-208b4ea5ce5a')
        self.vs[8]["MT_label__"] = """651"""
        self.vs[8]["MT_post__Name"] = """return 1"""
        self.vs[8]["mm__"] = """MT_post__Port_Output"""
        self.vs[8]["GUID__"] = UUID('9fb9d0a6-d84e-4696-be44-9c6a9cfb508d')
        self.vs[9]["MT_label__"] = """551"""
        self.vs[9]["MT_post__Name"] = """return 1"""
        self.vs[9]["mm__"] = """MT_post__Port_Output"""
        self.vs[9]["GUID__"] = UUID('b3ce1714-d213-4597-a2a6-d5aee2ae0da7')
        self.vs[10]["MT_label__"] = """851"""
        self.vs[10]["MT_post__Name"] = """return 1"""
        self.vs[10]["mm__"] = """MT_post__Port_Output"""
        self.vs[10]["GUID__"] = UUID('abed0575-97ca-4eb8-a5d9-e16065ef5977')
        self.vs[11]["MT_label__"] = """451"""
        self.vs[11]["MT_post__Name"] = """return 1"""
        self.vs[11]["mm__"] = """MT_post__Port_Output"""
        self.vs[11]["GUID__"] = UUID('5e0091a3-a40e-4ac1-b72b-46fa949530e9')
        self.vs[12]["MT_label__"] = """70000000003"""
        self.vs[12]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[12]["GUID__"] = UUID('2948582d-59db-4c2f-93b8-fc518aeec0b3')
        self.vs[13]["MT_label__"] = """60000000651"""
        self.vs[13]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('07279973-d08b-4670-b0f8-1ca1ceb4ae78')
        self.vs[14]["MT_label__"] = """50000000551"""
        self.vs[14]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('7c0012ca-1297-4ce4-b988-6dbdca460d12')
        self.vs[15]["MT_label__"] = """80000000851"""
        self.vs[15]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('2fda6c6d-8086-4f41-9e4a-d0b10516bd32')
        self.vs[16]["MT_label__"] = """40000000451"""
        self.vs[16]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('20167224-0661-428f-b27e-445211de5ddb')
        self.vs[17]["MT_label__"] = """7010651"""
        self.vs[17]["mm__"] = """MT_post____Relation__"""
        self.vs[17]["GUID__"] = UUID('bd6afa87-ec95-48ca-bb48-8e457d14577d')
        self.vs[18]["MT_label__"] = """8010651"""
        self.vs[18]["mm__"] = """MT_post____Relation__"""
        self.vs[18]["GUID__"] = UUID('84d701e9-e177-4afc-beb3-cfba0952b098')
        self.vs[19]["MT_label__"] = """6010551"""
        self.vs[19]["mm__"] = """MT_post____Relation__"""
        self.vs[19]["GUID__"] = UUID('9d2323fc-adeb-4ebf-b2cb-96c7f59c0bff')
        self.vs[20]["MT_label__"] = """4020851"""
        self.vs[20]["mm__"] = """MT_post____Relation__"""
        self.vs[20]["GUID__"] = UUID('c1ff2534-484d-4d99-a8af-cc7e6a8d8217')
        self.vs[21]["MT_label__"] = """5010451"""
        self.vs[21]["mm__"] = """MT_post____Relation__"""
        self.vs[21]["GUID__"] = UUID('eaa25fd3-6a8b-4979-89c3-1202f29774b3')
        self.vs[22]["MT_label__"] = """701"""
        self.vs[22]["MT_post__Name"] = """return 1"""
        self.vs[22]["mm__"] = """MT_post__Port_Input"""
        self.vs[22]["GUID__"] = UUID('a541b2c3-797a-4abb-bbcb-87bb281bed07')
        self.vs[23]["MT_label__"] = """601"""
        self.vs[23]["MT_post__Name"] = """return 1"""
        self.vs[23]["mm__"] = """MT_post__Port_Input"""
        self.vs[23]["GUID__"] = UUID('1d1a03b1-393a-44e4-91c5-23e390324e0f')
        self.vs[24]["MT_label__"] = """501"""
        self.vs[24]["MT_post__Name"] = """return 1"""
        self.vs[24]["mm__"] = """MT_post__Port_Input"""
        self.vs[24]["GUID__"] = UUID('8a478463-88d4-4382-9f13-eb2875957033')
        self.vs[25]["MT_label__"] = """801"""
        self.vs[25]["MT_post__Name"] = """return 1"""
        self.vs[25]["mm__"] = """MT_post__Port_Input"""
        self.vs[25]["GUID__"] = UUID('705dc9c7-eef8-4e4a-9e02-ee3b29611585')
        self.vs[26]["MT_label__"] = """1"""
        self.vs[26]["MT_post__Name"] = """return 1"""
        self.vs[26]["mm__"] = """MT_post__Port_Input"""
        self.vs[26]["GUID__"] = UUID('0c36c5b3-0a22-441a-83c5-1217a769f9e7')
        self.vs[27]["MT_label__"] = """402"""
        self.vs[27]["MT_post__Name"] = """return 2"""
        self.vs[27]["mm__"] = """MT_post__Port_Input"""
        self.vs[27]["GUID__"] = UUID('6393e246-110a-4734-a3fb-fdf18a904e16')
        self.vs[28]["MT_label__"] = """9900000009"""
        self.vs[28]["MT_post__Name"] = """return attr_value"""
        self.vs[28]["mm__"] = """MT_post____Contains__"""
        self.vs[28]["GUID__"] = UUID('49c58056-8108-4409-8585-2856325e57c5')
        self.vs[29]["MT_label__"] = """900000007"""
        self.vs[29]["MT_post__Name"] = """return attr_value"""
        self.vs[29]["mm__"] = """MT_post____Contains__"""
        self.vs[29]["GUID__"] = UUID('477655d3-70fe-48fa-81ca-8801b69d0842')
        self.vs[30]["MT_label__"] = """900000006"""
        self.vs[30]["MT_post__Name"] = """return attr_value"""
        self.vs[30]["mm__"] = """MT_post____Contains__"""
        self.vs[30]["GUID__"] = UUID('605e7f23-9524-4a1e-9060-4a26d246bcce')
        self.vs[31]["MT_label__"] = """900000005"""
        self.vs[31]["MT_post__Name"] = """return attr_value"""
        self.vs[31]["mm__"] = """MT_post____Contains__"""
        self.vs[31]["GUID__"] = UUID('2a194768-4a52-4422-b4ef-4625e1d8c143')
        self.vs[32]["MT_label__"] = """900000008"""
        self.vs[32]["MT_post__Name"] = """return attr_value"""
        self.vs[32]["mm__"] = """MT_post____Contains__"""
        self.vs[32]["GUID__"] = UUID('29a89ebe-fbb4-41e3-aca3-978357ba4a49')
        self.vs[33]["MT_label__"] = """900000004"""
        self.vs[33]["MT_post__Name"] = """return attr_value"""
        self.vs[33]["mm__"] = """MT_post____Contains__"""
        self.vs[33]["GUID__"] = UUID('abf07f27-c107-4942-842b-fa5fe41fd5d6')
        self.vs[34]["MT_label__"] = """70000000701"""
        self.vs[34]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[34]["GUID__"] = UUID('74577f46-ace6-4cf2-b556-314ae1e3d857')
        self.vs[35]["MT_label__"] = """60000000601"""
        self.vs[35]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('a442267b-9a3a-4bf3-a570-acd74c38d1c6')
        self.vs[36]["MT_label__"] = """50000000501"""
        self.vs[36]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[36]["GUID__"] = UUID('69fd9903-ae5c-4f80-ba28-3921942be3d4')
        self.vs[37]["MT_label__"] = """80000000801"""
        self.vs[37]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('9ee80a89-128a-455f-bad1-d66b04b3b891')
        self.vs[38]["MT_label__"] = """40000000001"""
        self.vs[38]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[38]["GUID__"] = UUID('112be667-ae04-4a3b-a88c-d45049ac45ee')
        self.vs[39]["MT_label__"] = """40000000402"""
        self.vs[39]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[39]["GUID__"] = UUID('7e1bcbb0-bdcf-436c-90ea-6fc9320338ae')

        from HCasedevs_FRULE_toCanonical_no_plantLHS import HCasedevs_FRULE_toCanonical_no_plantLHS
        self.pre = HCasedevs_FRULE_toCanonical_no_plantLHS()
    
    def set_Position7(self, attr_value, PreNode, graph):
        return PreNode('2')['Position']


    def set_gain7(self, attr_value, PreNode, graph):
        return PreNode('2')['Numerator'][0]


    def set_Name7(self, attr_value, PreNode, graph):
        return PreNode('2')['Name']+'Gain_N_1'


    def set_Name701(self, attr_value, PreNode, graph):
        return 1


    def set_Name3(self, attr_value, PreNode, graph):
        return 1


    def set_Position6(self, attr_value, PreNode, graph):
        return PreNode('2')['Position']


    def set_InitialCondition6(self, attr_value, PreNode, graph):
        return 0


    def set_Name6(self, attr_value, PreNode, graph):
        return PreNode('2')['Name']+'_int'


    def set_Name601(self, attr_value, PreNode, graph):
        return 1


    def set_Name651(self, attr_value, PreNode, graph):
        return 1


    def set_Position5(self, attr_value, PreNode, graph):
        return PreNode('2')['Position']


    def set_gain5(self, attr_value, PreNode, graph):
        return PreNode('2')['Denominator'][0]


    def set_Name5(self, attr_value, PreNode, graph):
        return PreNode('2')['Name']+'_Gain_D2'


    def set_Name501(self, attr_value, PreNode, graph):
        return 1


    def set_Name551(self, attr_value, PreNode, graph):
        return 1


    def set_Position8(self, attr_value, PreNode, graph):
        return PreNode('2')['Position']


    def set_gain8(self, attr_value, PreNode, graph):
        return -PreNode('2')['Denominator'][1]


    def set_Name8(self, attr_value, PreNode, graph):
        return PreNode('2')['Name']+'_Gain_D1'


    def set_Name801(self, attr_value, PreNode, graph):
        return 1


    def set_Name851(self, attr_value, PreNode, graph):
        return 1


    def set_Position4(self, attr_value, PreNode, graph):
        return PreNode('2')['Position']


    def set_Name4(self, attr_value, PreNode, graph):
        return PreNode('2')['Name']+'_add1'


    def set_Name1(self, attr_value, PreNode, graph):
        return 1


    def set_Name402(self, attr_value, PreNode, graph):
        return 2


    def set_Name451(self, attr_value, PreNode, graph):
        return 1


    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        pass

    def execute(self, packet, match):
        """
            Transforms the current match of the packet according to the rule %s.
            Pivots are also assigned, if any.
            @param packet: The input packet.
            @param match: The match to rewrite.
        """
        graph = packet.graph
        
        # Build a dictionary {label: node index} mapping each label of the pattern to a node in the graph to rewrite.
        # Because of the uniqueness property of labels in a rule, we can store all LHS labels
        # and subsequently add the labels corresponding to the nodes to be created.
        labels = match.copy()
        
        #===============================================================================
        # Update attribute values
        #===============================================================================
        # Port_Input1
        try:
            graph.vs[labels['1']]['Name'] = self.set_Name1(graph.vs[labels['1']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['1']][Himesis.Constants.MT_DIRTY] = True
        # Port_Output3
        try:
            graph.vs[labels['3']]['Name'] = self.set_Name3(graph.vs[labels['3']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['3']][Himesis.Constants.MT_DIRTY] = True
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # Gain7
        new_node = graph.add_node()
        labels['7'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Gain'
        try:
            graph.vs[new_node]['Position'] = self.set_Position7(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['gain'] = self.set_gain7(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'gain\'', e)
        try:
            graph.vs[new_node]['Name'] = self.set_Name7(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Input701
        new_node = graph.add_node()
        labels['701'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name701(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Integrator6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Integrator'
        try:
            graph.vs[new_node]['Position'] = self.set_Position6(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['InitialCondition'] = self.set_InitialCondition6(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'InitialCondition\'', e)
        try:
            graph.vs[new_node]['Name'] = self.set_Name6(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Input601
        new_node = graph.add_node()
        labels['601'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name601(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Output651
        new_node = graph.add_node()
        labels['651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name651(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Gain5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Gain'
        try:
            graph.vs[new_node]['Position'] = self.set_Position5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['gain'] = self.set_gain5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'gain\'', e)
        try:
            graph.vs[new_node]['Name'] = self.set_Name5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Input501
        new_node = graph.add_node()
        labels['501'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name501(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Output551
        new_node = graph.add_node()
        labels['551'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name551(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Gain8
        new_node = graph.add_node()
        labels['8'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Gain'
        try:
            graph.vs[new_node]['Position'] = self.set_Position8(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['gain'] = self.set_gain8(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'gain\'', e)
        try:
            graph.vs[new_node]['Name'] = self.set_Name8(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Input801
        new_node = graph.add_node()
        labels['801'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name801(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Output851
        new_node = graph.add_node()
        labels['851'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name851(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Sum4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Sum'
        try:
            graph.vs[new_node]['Position'] = self.set_Position4(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['Name'] = self.set_Name4(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Input402
        new_node = graph.add_node()
        labels['402'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name402(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Output451
        new_node = graph.add_node()
        labels['451'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name451(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # __Contains__900000007
        new_node = graph.add_node()
        labels['900000007'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__900000006
        new_node = graph.add_node()
        labels['900000006'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__900000005
        new_node = graph.add_node()
        labels['900000005'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__900000008
        new_node = graph.add_node()
        labels['900000008'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__900000004
        new_node = graph.add_node()
        labels['900000004'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Block_Inport__70000000701
        new_node = graph.add_node()
        labels['70000000701'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__70000000003
        new_node = graph.add_node()
        labels['70000000003'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Inport__60000000601
        new_node = graph.add_node()
        labels['60000000601'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__60000000651
        new_node = graph.add_node()
        labels['60000000651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Inport__50000000501
        new_node = graph.add_node()
        labels['50000000501'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__50000000551
        new_node = graph.add_node()
        labels['50000000551'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Inport__80000000801
        new_node = graph.add_node()
        labels['80000000801'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__80000000851
        new_node = graph.add_node()
        labels['80000000851'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Inport__40000000001
        new_node = graph.add_node()
        labels['40000000001'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Inport__40000000402
        new_node = graph.add_node()
        labels['40000000402'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__40000000451
        new_node = graph.add_node()
        labels['40000000451'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Relation__7010651
        new_node = graph.add_node()
        labels['7010651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__8010651
        new_node = graph.add_node()
        labels['8010651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__6010551
        new_node = graph.add_node()
        labels['6010551'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__4020851
        new_node = graph.add_node()
        labels['4020851'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__5010451
        new_node = graph.add_node()
        labels['5010451'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Sum4 -> __Block_Inport__40000000001
        graph.add_edges((labels['4'], labels['40000000001']))
        # Sum4 -> __Block_Inport__40000000402
        graph.add_edges((labels['4'], labels['40000000402']))
        # Sum4 -> __Block_Outport__40000000451
        graph.add_edges((labels['4'], labels['40000000451']))
        # __Contains__900000004 -> Sum4
        graph.add_edges((labels['900000004'], labels['4']))
        # __Block_Inport__40000000001 -> Port_Input1
        graph.add_edges((labels['40000000001'], labels['1']))
        # __Block_Inport__40000000402 -> Port_Input402
        graph.add_edges((labels['40000000402'], labels['402']))
        # __Block_Outport__40000000451 -> Port_Output451
        graph.add_edges((labels['40000000451'], labels['451']))
        # __Relation__4020851 -> Port_Input402
        graph.add_edges((labels['4020851'], labels['402']))
        # Port_Output851 -> __Relation__4020851
        graph.add_edges((labels['851'], labels['4020851']))
        # Port_Output451 -> __Relation__5010451
        graph.add_edges((labels['451'], labels['5010451']))
        # Gain5 -> __Block_Inport__50000000501
        graph.add_edges((labels['5'], labels['50000000501']))
        # Gain5 -> __Block_Outport__50000000551
        graph.add_edges((labels['5'], labels['50000000551']))
        # __Contains__900000005 -> Gain5
        graph.add_edges((labels['900000005'], labels['5']))
        # __Block_Inport__50000000501 -> Port_Input501
        graph.add_edges((labels['50000000501'], labels['501']))
        # __Block_Outport__50000000551 -> Port_Output551
        graph.add_edges((labels['50000000551'], labels['551']))
        # __Relation__5010451 -> Port_Input501
        graph.add_edges((labels['5010451'], labels['501']))
        # Port_Output551 -> __Relation__6010551
        graph.add_edges((labels['551'], labels['6010551']))
        # Integrator6 -> __Block_Inport__60000000601
        graph.add_edges((labels['6'], labels['60000000601']))
        # Integrator6 -> __Block_Outport__60000000651
        graph.add_edges((labels['6'], labels['60000000651']))
        # __Contains__900000006 -> Integrator6
        graph.add_edges((labels['900000006'], labels['6']))
        # __Block_Inport__60000000601 -> Port_Input601
        graph.add_edges((labels['60000000601'], labels['601']))
        # __Block_Outport__60000000651 -> Port_Output651
        graph.add_edges((labels['60000000651'], labels['651']))
        # __Relation__6010551 -> Port_Input601
        graph.add_edges((labels['6010551'], labels['601']))
        # Port_Output651 -> __Relation__7010651
        graph.add_edges((labels['651'], labels['7010651']))
        # Port_Output651 -> __Relation__8010651
        graph.add_edges((labels['651'], labels['8010651']))
        # Gain7 -> __Block_Inport__70000000701
        graph.add_edges((labels['7'], labels['70000000701']))
        # Gain7 -> __Block_Outport__70000000003
        graph.add_edges((labels['7'], labels['70000000003']))
        # __Contains__900000007 -> Gain7
        graph.add_edges((labels['900000007'], labels['7']))
        # __Block_Outport__70000000003 -> Port_Output3
        graph.add_edges((labels['70000000003'], labels['3']))
        # __Block_Inport__70000000701 -> Port_Input701
        graph.add_edges((labels['70000000701'], labels['701']))
        # __Relation__7010651 -> Port_Input701
        graph.add_edges((labels['7010651'], labels['701']))
        # Gain8 -> __Block_Inport__80000000801
        graph.add_edges((labels['8'], labels['80000000801']))
        # Gain8 -> __Block_Outport__80000000851
        graph.add_edges((labels['8'], labels['80000000851']))
        # __Contains__900000008 -> Gain8
        graph.add_edges((labels['900000008'], labels['8']))
        # __Block_Inport__80000000801 -> Port_Input801
        graph.add_edges((labels['80000000801'], labels['801']))
        # __Block_Outport__80000000851 -> Port_Output851
        graph.add_edges((labels['80000000851'], labels['851']))
        # __Relation__8010651 -> Port_Input801
        graph.add_edges((labels['8010651'], labels['801']))
        # SubSystem9 -> __Contains__900000004
        graph.add_edges((labels['9'], labels['900000004']))
        # SubSystem9 -> __Contains__900000005
        graph.add_edges((labels['9'], labels['900000005']))
        # SubSystem9 -> __Contains__900000006
        graph.add_edges((labels['9'], labels['900000006']))
        # SubSystem9 -> __Contains__900000007
        graph.add_edges((labels['9'], labels['900000007']))
        # SubSystem9 -> __Contains__900000008
        graph.add_edges((labels['9'], labels['900000008']))
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        
        #===============================================================================
        # Perform the post-action
        #===============================================================================
        try:
            self.action(lambda i: graph.vs[labels[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while applying the post-action', e)
        #===============================================================================
        # Finally, delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        # __Block_Inport__20000000001, __Block_Outport__20000000003, __Contains__900000002, TransferFcn2
        graph.delete_nodes([labels["20000000001"], labels["20000000003"], labels["900000002"], labels["2"]])
    
