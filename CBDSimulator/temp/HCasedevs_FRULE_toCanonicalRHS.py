

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_FRULE_toCanonicalRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_FRULE_toCanonicalRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_FRULE_toCanonicalRHS, self).__init__(name='HCasedevs_FRULE_toCanonicalRHS', num_nodes=38, edges=[])
        
        # Add the edges
        self.add_edges([(3, 32), (32, 26), (3, 16), (16, 6), (4, 33), (33, 27), (4, 17), (17, 7), (0, 34), (34, 28), (0, 35), (35, 29), (0, 18), (18, 8), (5, 36), (36, 30), (5, 19), (19, 9), (1, 37), (37, 31), (1, 20), (20, 10), (6, 21), (21, 31), (7, 22), (22, 29), (8, 23), (23, 26), (10, 24), (24, 27), (10, 25), (25, 30), (2, 11), (11, 3), (2, 12), (12, 4), (2, 13), (13, 0), (2, 14), (14, 5), (2, 15), (15, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('68cdfdb4-7c6d-47e8-91c5-0dd2fc8135e8')
        
        # Set the node attributes
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[0]["MT_label__"] = """4"""
        self.vs[0]["MT_post__Name"] = """return PreNode('2')['Name']+'_add1'"""
        self.vs[0]["mm__"] = """MT_post__Sum"""
        self.vs[0]["GUID__"] = UUID('5fda17f0-84f2-403f-80ac-bf9d30987a83')
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[1]["MT_post__InitialCondition"] = """return 0"""
        self.vs[1]["MT_label__"] = """6"""
        self.vs[1]["MT_post__Name"] = """return PreNode('2')['Name']+'_int'"""
        self.vs[1]["mm__"] = """MT_post__Integrator"""
        self.vs[1]["GUID__"] = UUID('60599514-3f37-418e-95d6-ed6f0a5553f8')
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["MT_post__Name"] = """return attr_value"""
        self.vs[2]["mm__"] = """MT_post__SubSystem"""
        self.vs[2]["GUID__"] = UUID('e3bd5850-8626-4856-bb34-070eedabc4fd')
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[3]["MT_label__"] = """5"""
        self.vs[3]["MT_post__gain"] = """return PreNode('2')['Denominator'][0]"""
        self.vs[3]["MT_post__Name"] = """return PreNode('2')['Name']+'_Gain_D2'"""
        self.vs[3]["mm__"] = """MT_post__Gain"""
        self.vs[3]["GUID__"] = UUID('597ec653-ee26-4380-8ec4-af17644f60f2')
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[4]["MT_label__"] = """8"""
        self.vs[4]["MT_post__gain"] = """return -PreNode('2')['Denominator'][1]"""
        self.vs[4]["MT_post__Name"] = """return PreNode('2')['Name']+'_Gain_D1'"""
        self.vs[4]["mm__"] = """MT_post__Gain"""
        self.vs[4]["GUID__"] = UUID('7c8854e5-cbd6-4c01-ab3e-e72103584eea')
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["MT_post__Position"] = """return PreNode('2')['Position']"""
        self.vs[5]["MT_label__"] = """7"""
        self.vs[5]["MT_post__gain"] = """return PreNode('2')['Numerator'][0]"""
        self.vs[5]["MT_post__Name"] = """return PreNode('2')['Name']+'Gain_N_1'"""
        self.vs[5]["mm__"] = """MT_post__Gain"""
        self.vs[5]["GUID__"] = UUID('7216c2db-8f3d-48de-a64c-805b460c2192')
        self.vs[6]["MT_label__"] = """551"""
        self.vs[6]["MT_post__Name"] = """return 1"""
        self.vs[6]["mm__"] = """MT_post__Port_Output"""
        self.vs[6]["GUID__"] = UUID('50e9ba77-9229-41e9-a769-1ed8a93617a5')
        self.vs[7]["MT_label__"] = """851"""
        self.vs[7]["MT_post__Name"] = """return 1"""
        self.vs[7]["mm__"] = """MT_post__Port_Output"""
        self.vs[7]["GUID__"] = UUID('14464877-979f-4c32-b074-b0837536502e')
        self.vs[8]["MT_label__"] = """451"""
        self.vs[8]["MT_post__Name"] = """return 1"""
        self.vs[8]["mm__"] = """MT_post__Port_Output"""
        self.vs[8]["GUID__"] = UUID('f73c5879-bf82-401b-bece-f693407cc1a4')
        self.vs[9]["MT_label__"] = """3"""
        self.vs[9]["MT_post__Name"] = """return 1"""
        self.vs[9]["mm__"] = """MT_post__Port_Output"""
        self.vs[9]["GUID__"] = UUID('a013b2c0-9e9c-4fd9-b23f-7b8490c467f8')
        self.vs[10]["MT_label__"] = """651"""
        self.vs[10]["MT_post__Name"] = """return 1"""
        self.vs[10]["mm__"] = """MT_post__Port_Output"""
        self.vs[10]["GUID__"] = UUID('dbf808b5-0a56-403b-9181-fa2c9d89078f')
        self.vs[11]["MT_label__"] = """9900000005"""
        self.vs[11]["MT_post__Name"] = """return attr_value"""
        self.vs[11]["mm__"] = """MT_post____Contains__"""
        self.vs[11]["GUID__"] = UUID('02fae37f-a17b-4985-9385-1aa1266860d9')
        self.vs[12]["MT_label__"] = """9900000008"""
        self.vs[12]["MT_post__Name"] = """return attr_value"""
        self.vs[12]["mm__"] = """MT_post____Contains__"""
        self.vs[12]["GUID__"] = UUID('9c5e2b83-7a22-4c86-a02c-a936861e5544')
        self.vs[13]["MT_label__"] = """9900000004"""
        self.vs[13]["MT_post__Name"] = """return attr_value"""
        self.vs[13]["mm__"] = """MT_post____Contains__"""
        self.vs[13]["GUID__"] = UUID('44ba8d09-254b-4bb1-8aa3-806b280713cf')
        self.vs[14]["MT_label__"] = """9900000007"""
        self.vs[14]["MT_post__Name"] = """return attr_value"""
        self.vs[14]["mm__"] = """MT_post____Contains__"""
        self.vs[14]["GUID__"] = UUID('41964236-3f4e-4be4-b74e-54e9cbeedbf5')
        self.vs[15]["MT_label__"] = """9900000006"""
        self.vs[15]["MT_post__Name"] = """return attr_value"""
        self.vs[15]["mm__"] = """MT_post____Contains__"""
        self.vs[15]["GUID__"] = UUID('c4d8b291-820e-4c71-858a-7cfae359030b')
        self.vs[16]["MT_label__"] = """50000000551"""
        self.vs[16]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('7c7d7c49-4b59-48f2-8fe7-2a578b0ba986')
        self.vs[17]["MT_label__"] = """80000000851"""
        self.vs[17]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('a3bb7d7b-8545-4e28-af73-21384eda7cfd')
        self.vs[18]["MT_label__"] = """40000000451"""
        self.vs[18]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('3db51621-4ff8-43c0-91f5-3e96bc079948')
        self.vs[19]["MT_label__"] = """70000000003"""
        self.vs[19]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[19]["GUID__"] = UUID('183dc181-09df-4e81-8758-d75397a14a4e')
        self.vs[20]["MT_label__"] = """60000000651"""
        self.vs[20]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[20]["GUID__"] = UUID('a82d438f-423d-42c4-94a6-2e22e9921cf6')
        self.vs[21]["MT_label__"] = """6010551"""
        self.vs[21]["mm__"] = """MT_post____Relation__"""
        self.vs[21]["GUID__"] = UUID('ae15f89e-8110-4def-8d98-043eec063367')
        self.vs[22]["MT_label__"] = """4020851"""
        self.vs[22]["mm__"] = """MT_post____Relation__"""
        self.vs[22]["GUID__"] = UUID('514780ab-8540-423c-9be9-cc6dabf58cdb')
        self.vs[23]["MT_label__"] = """5010451"""
        self.vs[23]["mm__"] = """MT_post____Relation__"""
        self.vs[23]["GUID__"] = UUID('45eedc8a-a96b-4161-87a1-02436ba3f395')
        self.vs[24]["MT_label__"] = """8010651"""
        self.vs[24]["mm__"] = """MT_post____Relation__"""
        self.vs[24]["GUID__"] = UUID('6000745e-1e7b-40dd-a627-dcee161a904f')
        self.vs[25]["MT_label__"] = """7010651"""
        self.vs[25]["mm__"] = """MT_post____Relation__"""
        self.vs[25]["GUID__"] = UUID('9e28e464-8def-43f2-854a-656abb80bfdd')
        self.vs[26]["MT_label__"] = """501"""
        self.vs[26]["MT_post__Name"] = """return 1"""
        self.vs[26]["mm__"] = """MT_post__Port_Input"""
        self.vs[26]["GUID__"] = UUID('223b6bbe-36ca-4a78-bb8a-43962d1b2266')
        self.vs[27]["MT_label__"] = """801"""
        self.vs[27]["MT_post__Name"] = """return 1"""
        self.vs[27]["mm__"] = """MT_post__Port_Input"""
        self.vs[27]["GUID__"] = UUID('96211d4c-006e-4535-81c6-2b326ec3363f')
        self.vs[28]["MT_label__"] = """1"""
        self.vs[28]["MT_post__Name"] = """return 1"""
        self.vs[28]["mm__"] = """MT_post__Port_Input"""
        self.vs[28]["GUID__"] = UUID('049eaa7c-e9bb-451b-bdef-2fd147ddc845')
        self.vs[29]["MT_label__"] = """402"""
        self.vs[29]["MT_post__Name"] = """return 2"""
        self.vs[29]["mm__"] = """MT_post__Port_Input"""
        self.vs[29]["GUID__"] = UUID('5b25848e-d2f7-401c-be2a-1794f0a27158')
        self.vs[30]["MT_label__"] = """701"""
        self.vs[30]["MT_post__Name"] = """return 1"""
        self.vs[30]["mm__"] = """MT_post__Port_Input"""
        self.vs[30]["GUID__"] = UUID('73241ac3-0560-4279-ac47-adae41717773')
        self.vs[31]["MT_label__"] = """601"""
        self.vs[31]["MT_post__Name"] = """return 1"""
        self.vs[31]["mm__"] = """MT_post__Port_Input"""
        self.vs[31]["GUID__"] = UUID('d3d032dc-612d-4b17-bb4c-b5e24d879019')
        self.vs[32]["MT_label__"] = """50000000501"""
        self.vs[32]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[32]["GUID__"] = UUID('119bf05f-d8d4-440f-8a7c-f6a1e44c40cb')
        self.vs[33]["MT_label__"] = """80000000801"""
        self.vs[33]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[33]["GUID__"] = UUID('97c10c6d-4e9d-4c7c-99c5-414ff8955ecd')
        self.vs[34]["MT_label__"] = """40000000001"""
        self.vs[34]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[34]["GUID__"] = UUID('94fe2814-c374-48b4-b626-203c961255d3')
        self.vs[35]["MT_label__"] = """40000000402"""
        self.vs[35]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[35]["GUID__"] = UUID('0afdff75-2d4e-448d-ad61-7df44ad02ba0')
        self.vs[36]["MT_label__"] = """70000000701"""
        self.vs[36]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[36]["GUID__"] = UUID('bd1aec9b-b721-4528-b5dc-f8659398627f')
        self.vs[37]["MT_label__"] = """60000000601"""
        self.vs[37]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[37]["GUID__"] = UUID('0f5ada12-3c28-4d64-a59a-7ee92a7e0805')

        from HCasedevs_FRULE_toCanonicalLHS import HCasedevs_FRULE_toCanonicalLHS
        self.pre = HCasedevs_FRULE_toCanonicalLHS()
    
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
        # __Contains__9900000005
        new_node = graph.add_node()
        labels['9900000005'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000008
        new_node = graph.add_node()
        labels['9900000008'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000004
        new_node = graph.add_node()
        labels['9900000004'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000007
        new_node = graph.add_node()
        labels['9900000007'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000006
        new_node = graph.add_node()
        labels['9900000006'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
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
        # __Relation__8010651
        new_node = graph.add_node()
        labels['8010651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__7010651
        new_node = graph.add_node()
        labels['7010651'] = new_node
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
        # __Contains__9900000004 -> Sum4
        graph.add_edges((labels['9900000004'], labels['4']))
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
        # __Contains__9900000005 -> Gain5
        graph.add_edges((labels['9900000005'], labels['5']))
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
        # __Contains__9900000006 -> Integrator6
        graph.add_edges((labels['9900000006'], labels['6']))
        # __Block_Inport__60000000601 -> Port_Input601
        graph.add_edges((labels['60000000601'], labels['601']))
        # __Block_Outport__60000000651 -> Port_Output651
        graph.add_edges((labels['60000000651'], labels['651']))
        # __Relation__6010551 -> Port_Input601
        graph.add_edges((labels['6010551'], labels['601']))
        # Port_Output651 -> __Relation__8010651
        graph.add_edges((labels['651'], labels['8010651']))
        # Port_Output651 -> __Relation__7010651
        graph.add_edges((labels['651'], labels['7010651']))
        # Gain7 -> __Block_Inport__70000000701
        graph.add_edges((labels['7'], labels['70000000701']))
        # Gain7 -> __Block_Outport__70000000003
        graph.add_edges((labels['7'], labels['70000000003']))
        # __Contains__9900000007 -> Gain7
        graph.add_edges((labels['9900000007'], labels['7']))
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
        # __Contains__9900000008 -> Gain8
        graph.add_edges((labels['9900000008'], labels['8']))
        # __Block_Inport__80000000801 -> Port_Input801
        graph.add_edges((labels['80000000801'], labels['801']))
        # __Block_Outport__80000000851 -> Port_Output851
        graph.add_edges((labels['80000000851'], labels['851']))
        # __Relation__8010651 -> Port_Input801
        graph.add_edges((labels['8010651'], labels['801']))
        # SubSystem99 -> __Contains__9900000004
        graph.add_edges((labels['99'], labels['9900000004']))
        # SubSystem99 -> __Contains__9900000005
        graph.add_edges((labels['99'], labels['9900000005']))
        # SubSystem99 -> __Contains__9900000006
        graph.add_edges((labels['99'], labels['9900000006']))
        # SubSystem99 -> __Contains__9900000007
        graph.add_edges((labels['99'], labels['9900000007']))
        # SubSystem99 -> __Contains__9900000008
        graph.add_edges((labels['99'], labels['9900000008']))
        
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
        # __Block_Inport__20000000001, __Block_Outport__20000000003, TransferFcn2, __Contains__9900000002
        graph.delete_nodes([labels["20000000001"], labels["20000000003"], labels["2"], labels["9900000002"]])
    
