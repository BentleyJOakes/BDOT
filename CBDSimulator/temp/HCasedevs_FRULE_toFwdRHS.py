

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_FRULE_toFwdRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_FRULE_toFwdRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_FRULE_toFwdRHS, self).__init__(name='HCasedevs_FRULE_toFwdRHS', num_nodes=31, edges=[])
        
        # Add the edges
        self.add_edges([(0, 26), (26, 21), (0, 27), (27, 22), (0, 13), (13, 5), (1, 28), (28, 23), (1, 29), (29, 24), (1, 14), (14, 6), (2, 30), (30, 25), (2, 15), (15, 7), (3, 16), (16, 8), (5, 17), (17, 25), (6, 18), (18, 21), (7, 19), (19, 22), (8, 20), (20, 24), (4, 9), (9, 0), (4, 10), (10, 1), (4, 11), (11, 2), (4, 12), (12, 3)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('022907b2-7ab3-47cb-bb90-3ab869d7de07')
        
        # Set the node attributes
        self.vs[0]["MT_post__Name"] = """return PreNode('1')['Name']+'Add'"""
        self.vs[0]["MT_post__Position"] = """return PreNode('1')['Position']"""
        self.vs[0]["MT_label__"] = """4"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_post__Sum"""
        self.vs[0]["GUID__"] = UUID('500fd9fb-a515-461d-b730-3325c081494f')
        self.vs[1]["MT_post__Name"] = """return PreNode('1')['Name']+'Product'"""
        self.vs[1]["MT_post__Position"] = """return PreNode('1')['Position']"""
        self.vs[1]["MT_label__"] = """3"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """MT_post__Product"""
        self.vs[1]["GUID__"] = UUID('f1a0b93b-fa7f-4b0a-9253-8b7fc5b5ef0d')
        self.vs[2]["MT_post__SampleTime"] = """return 0.001"""
        self.vs[2]["MT_post__Name"] = """return PreNode('1')['Name']+'Delay'"""
        self.vs[2]["MT_post__Position"] = """return PreNode('1')['Position']"""
        self.vs[2]["MT_post__InitialCondition"] = """return PreNode('1')['InitialCondition']"""
        self.vs[2]["MT_label__"] = """5"""
        self.vs[2]["BackgroundColor"] = """white"""
        self.vs[2]["mm__"] = """MT_post__UnitDelay"""
        self.vs[2]["GUID__"] = UUID('3ca7b477-93ca-4c4c-855f-d639291f0359')
        self.vs[3]["MT_post__Name"] = """return PreNode('1')['Name']+'gainconst'"""
        self.vs[3]["MT_post__Position"] = """return PreNode('1')['Position']"""
        self.vs[3]["MT_post__value"] = """return 0.001"""
        self.vs[3]["MT_label__"] = """6"""
        self.vs[3]["BackgroundColor"] = """white"""
        self.vs[3]["mm__"] = """MT_post__Constant"""
        self.vs[3]["GUID__"] = UUID('58b07f2c-d81b-497d-8a45-ff63178315ca')
        self.vs[4]["MT_post__Name"] = """return attr_value"""
        self.vs[4]["MT_label__"] = """99"""
        self.vs[4]["mm__"] = """MT_post__SubSystem"""
        self.vs[4]["GUID__"] = UUID('8cac1fd5-d10c-4abd-a51b-03817db98869')
        self.vs[5]["MT_post__Name"] = """return 1"""
        self.vs[5]["MT_label__"] = """451"""
        self.vs[5]["mm__"] = """MT_post__Port_Output"""
        self.vs[5]["GUID__"] = UUID('bc4ec429-edef-49fd-9049-b84d5c09cd97')
        self.vs[6]["MT_post__Name"] = """return 1"""
        self.vs[6]["MT_label__"] = """351"""
        self.vs[6]["mm__"] = """MT_post__Port_Output"""
        self.vs[6]["GUID__"] = UUID('c62c54a0-f7ae-4d7a-a81f-2088e1a2a3a5')
        self.vs[7]["MT_post__Name"] = """return 1"""
        self.vs[7]["MT_label__"] = """2"""
        self.vs[7]["mm__"] = """MT_post__Port_Output"""
        self.vs[7]["GUID__"] = UUID('3b58e844-508a-47e7-ad73-da2c1676e998')
        self.vs[8]["MT_post__Name"] = """return 1"""
        self.vs[8]["MT_label__"] = """651"""
        self.vs[8]["mm__"] = """MT_post__Port_Output"""
        self.vs[8]["GUID__"] = UUID('1d0133e7-dd86-4ff2-8de7-8f1742d6d18b')
        self.vs[9]["MT_post__Name"] = """return attr_value"""
        self.vs[9]["MT_label__"] = """9900000004"""
        self.vs[9]["mm__"] = """MT_post____Contains__"""
        self.vs[9]["GUID__"] = UUID('b1d390b6-1e49-48a9-b5f1-24e2f29e704a')
        self.vs[10]["MT_post__Name"] = """return attr_value"""
        self.vs[10]["MT_label__"] = """9900000003"""
        self.vs[10]["mm__"] = """MT_post____Contains__"""
        self.vs[10]["GUID__"] = UUID('981e428e-188f-47cc-af50-ce9024cf2804')
        self.vs[11]["MT_post__Name"] = """return attr_value"""
        self.vs[11]["MT_label__"] = """9900000005"""
        self.vs[11]["mm__"] = """MT_post____Contains__"""
        self.vs[11]["GUID__"] = UUID('c773f2c5-4be4-49d1-bbd4-e7d8cb31be5e')
        self.vs[12]["MT_post__Name"] = """return attr_value"""
        self.vs[12]["MT_label__"] = """9900000006"""
        self.vs[12]["mm__"] = """MT_post____Contains__"""
        self.vs[12]["GUID__"] = UUID('61e8cdc2-8796-42b8-ae83-bf9496beb320')
        self.vs[13]["MT_label__"] = """40000000451"""
        self.vs[13]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('01d4edae-0529-42f4-ac98-81dfb3dfdc49')
        self.vs[14]["MT_label__"] = """30000000351"""
        self.vs[14]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[14]["GUID__"] = UUID('0daa0cc0-212a-41f1-9e32-f85226fe491c')
        self.vs[15]["MT_label__"] = """50000000002"""
        self.vs[15]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[15]["GUID__"] = UUID('0cd554f1-5eac-4d93-8c06-ec8a5d7cdf8e')
        self.vs[16]["MT_label__"] = """60000000651"""
        self.vs[16]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('42a48e60-9496-4c44-a155-e3d2d11455e3')
        self.vs[17]["MT_label__"] = """5010451"""
        self.vs[17]["mm__"] = """MT_post____Relation__"""
        self.vs[17]["GUID__"] = UUID('1d284c6e-f107-47f9-a5e3-1a8d5421d320')
        self.vs[18]["MT_label__"] = """4010351"""
        self.vs[18]["mm__"] = """MT_post____Relation__"""
        self.vs[18]["GUID__"] = UUID('c654ec11-953c-4f02-bdd1-c566ce999799')
        self.vs[19]["MT_label__"] = """4020002"""
        self.vs[19]["mm__"] = """MT_post____Relation__"""
        self.vs[19]["GUID__"] = UUID('034e6653-d44e-413e-9268-5336b09a21a1')
        self.vs[20]["MT_label__"] = """3020651"""
        self.vs[20]["mm__"] = """MT_post____Relation__"""
        self.vs[20]["GUID__"] = UUID('8e5fe53d-8b18-4c8e-9182-58721dce3659')
        self.vs[21]["MT_post__Name"] = """return 1"""
        self.vs[21]["MT_label__"] = """401"""
        self.vs[21]["mm__"] = """MT_post__Port_Input"""
        self.vs[21]["GUID__"] = UUID('8b6e4e98-a2ae-4cf8-b570-6856c17fcbdc')
        self.vs[22]["MT_post__Name"] = """return 2"""
        self.vs[22]["MT_label__"] = """402"""
        self.vs[22]["mm__"] = """MT_post__Port_Input"""
        self.vs[22]["GUID__"] = UUID('f2951f66-b805-4d51-a50f-6cc4d6c7ad54')
        self.vs[23]["MT_post__Name"] = """return 1"""
        self.vs[23]["MT_label__"] = """0"""
        self.vs[23]["mm__"] = """MT_post__Port_Input"""
        self.vs[23]["GUID__"] = UUID('966a1867-6e98-4527-b5be-689e06f8cf86')
        self.vs[24]["MT_post__Name"] = """return 2"""
        self.vs[24]["MT_label__"] = """302"""
        self.vs[24]["mm__"] = """MT_post__Port_Input"""
        self.vs[24]["GUID__"] = UUID('2e3420f4-ce3f-4855-9de2-5fa603ba8f7f')
        self.vs[25]["MT_post__Name"] = """return 1"""
        self.vs[25]["MT_label__"] = """501"""
        self.vs[25]["mm__"] = """MT_post__Port_Input"""
        self.vs[25]["GUID__"] = UUID('261b3622-ba85-497f-b3ad-42c923e976b2')
        self.vs[26]["MT_label__"] = """40000000401"""
        self.vs[26]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[26]["GUID__"] = UUID('5b4993d6-8ff9-4be2-b447-87da4edca705')
        self.vs[27]["MT_label__"] = """40000000402"""
        self.vs[27]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[27]["GUID__"] = UUID('8902d9dc-8cad-4fd1-9dbf-a3a75c927680')
        self.vs[28]["MT_label__"] = """30000000000"""
        self.vs[28]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[28]["GUID__"] = UUID('29157d1b-841b-46cc-b090-d8f19318eee3')
        self.vs[29]["MT_label__"] = """30000000302"""
        self.vs[29]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[29]["GUID__"] = UUID('a85c2965-0f4e-4a25-bb3c-3bc7808324f5')
        self.vs[30]["MT_label__"] = """50000000501"""
        self.vs[30]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[30]["GUID__"] = UUID('df303058-d990-4df2-abec-8d07d2cf65cd')

        from HCasedevs_FRULE_toFwdLHS import HCasedevs_FRULE_toFwdLHS
        self.pre = HCasedevs_FRULE_toFwdLHS()
    
    def set_Name4(self, attr_value, PreNode, graph):
        return PreNode('1')['Name']+'Add'


    def set_Position4(self, attr_value, PreNode, graph):
        return PreNode('1')['Position']


    def set_Name401(self, attr_value, PreNode, graph):
        return 1


    def set_Name402(self, attr_value, PreNode, graph):
        return 2


    def set_Name451(self, attr_value, PreNode, graph):
        return 1


    def set_Name3(self, attr_value, PreNode, graph):
        return PreNode('1')['Name']+'Product'


    def set_Position3(self, attr_value, PreNode, graph):
        return PreNode('1')['Position']


    def set_Name0(self, attr_value, PreNode, graph):
        return 1


    def set_Name302(self, attr_value, PreNode, graph):
        return 2


    def set_Name351(self, attr_value, PreNode, graph):
        return 1


    def set_SampleTime5(self, attr_value, PreNode, graph):
        return 0.001


    def set_Name5(self, attr_value, PreNode, graph):
        return PreNode('1')['Name']+'Delay'


    def set_Position5(self, attr_value, PreNode, graph):
        return PreNode('1')['Position']


    def set_InitialCondition5(self, attr_value, PreNode, graph):
        return PreNode('1')['InitialCondition']


    def set_Name501(self, attr_value, PreNode, graph):
        return 1


    def set_Name2(self, attr_value, PreNode, graph):
        return 1


    def set_Name6(self, attr_value, PreNode, graph):
        return PreNode('1')['Name']+'gainconst'


    def set_Position6(self, attr_value, PreNode, graph):
        return PreNode('1')['Position']


    def set_value6(self, attr_value, PreNode, graph):
        return 0.001


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
        # Port_Input0
        try:
            graph.vs[labels['0']]['Name'] = self.set_Name0(graph.vs[labels['0']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['0']][Himesis.Constants.MT_DIRTY] = True
        # Port_Output2
        try:
            graph.vs[labels['2']]['Name'] = self.set_Name2(graph.vs[labels['2']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['2']][Himesis.Constants.MT_DIRTY] = True
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # Sum4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Sum'
        try:
            graph.vs[new_node]['Name'] = self.set_Name4(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        try:
            graph.vs[new_node]['Position'] = self.set_Position4(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        # Port_Input401
        new_node = graph.add_node()
        labels['401'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name401(None, lambda i: graph.vs[match[i]], graph)
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
        # Product3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Product'
        try:
            graph.vs[new_node]['Name'] = self.set_Name3(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        try:
            graph.vs[new_node]['Position'] = self.set_Position3(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        # Port_Input302
        new_node = graph.add_node()
        labels['302'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name302(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Port_Output351
        new_node = graph.add_node()
        labels['351'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name351(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # UnitDelay5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'UnitDelay'
        try:
            graph.vs[new_node]['SampleTime'] = self.set_SampleTime5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'SampleTime\'', e)
        try:
            graph.vs[new_node]['Name'] = self.set_Name5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        try:
            graph.vs[new_node]['Position'] = self.set_Position5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['InitialCondition'] = self.set_InitialCondition5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'InitialCondition\'', e)
        # Port_Input501
        new_node = graph.add_node()
        labels['501'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Input'
        try:
            graph.vs[new_node]['Name'] = self.set_Name501(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # Constant6
        new_node = graph.add_node()
        labels['6'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['Name'] = self.set_Name6(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        try:
            graph.vs[new_node]['Position'] = self.set_Position6(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['value'] = self.set_value6(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'value\'', e)
        # Port_Output651
        new_node = graph.add_node()
        labels['651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name651(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # __Contains__9900000004
        new_node = graph.add_node()
        labels['9900000004'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000003
        new_node = graph.add_node()
        labels['9900000003'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000005
        new_node = graph.add_node()
        labels['9900000005'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Contains__9900000006
        new_node = graph.add_node()
        labels['9900000006'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Block_Inport__40000000401
        new_node = graph.add_node()
        labels['40000000401'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Inport__40000000402
        new_node = graph.add_node()
        labels['40000000402'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__40000000451
        new_node = graph.add_node()
        labels['40000000451'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Inport__30000000000
        new_node = graph.add_node()
        labels['30000000000'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Inport__30000000302
        new_node = graph.add_node()
        labels['30000000302'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__30000000351
        new_node = graph.add_node()
        labels['30000000351'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Inport__50000000501
        new_node = graph.add_node()
        labels['50000000501'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__50000000002
        new_node = graph.add_node()
        labels['50000000002'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Block_Outport__60000000651
        new_node = graph.add_node()
        labels['60000000651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        # __Relation__5010451
        new_node = graph.add_node()
        labels['5010451'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__4010351
        new_node = graph.add_node()
        labels['4010351'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__4020002
        new_node = graph.add_node()
        labels['4020002'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        # __Relation__3020651
        new_node = graph.add_node()
        labels['3020651'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Relation__'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Product3 -> __Block_Inport__30000000000
        graph.add_edges((labels['3'], labels['30000000000']))
        # Product3 -> __Block_Inport__30000000302
        graph.add_edges((labels['3'], labels['30000000302']))
        # Product3 -> __Block_Outport__30000000351
        graph.add_edges((labels['3'], labels['30000000351']))
        # __Contains__9900000003 -> Product3
        graph.add_edges((labels['9900000003'], labels['3']))
        # __Block_Inport__30000000000 -> Port_Input0
        graph.add_edges((labels['30000000000'], labels['0']))
        # __Block_Inport__30000000302 -> Port_Input302
        graph.add_edges((labels['30000000302'], labels['302']))
        # __Block_Outport__30000000351 -> Port_Output351
        graph.add_edges((labels['30000000351'], labels['351']))
        # __Relation__3020651 -> Port_Input302
        graph.add_edges((labels['3020651'], labels['302']))
        # Port_Output651 -> __Relation__3020651
        graph.add_edges((labels['651'], labels['3020651']))
        # Port_Output351 -> __Relation__4010351
        graph.add_edges((labels['351'], labels['4010351']))
        # Sum4 -> __Block_Inport__40000000401
        graph.add_edges((labels['4'], labels['40000000401']))
        # Sum4 -> __Block_Inport__40000000402
        graph.add_edges((labels['4'], labels['40000000402']))
        # Sum4 -> __Block_Outport__40000000451
        graph.add_edges((labels['4'], labels['40000000451']))
        # __Contains__9900000004 -> Sum4
        graph.add_edges((labels['9900000004'], labels['4']))
        # __Block_Inport__40000000401 -> Port_Input401
        graph.add_edges((labels['40000000401'], labels['401']))
        # __Block_Inport__40000000402 -> Port_Input402
        graph.add_edges((labels['40000000402'], labels['402']))
        # __Block_Outport__40000000451 -> Port_Output451
        graph.add_edges((labels['40000000451'], labels['451']))
        # __Relation__4010351 -> Port_Input401
        graph.add_edges((labels['4010351'], labels['401']))
        # __Relation__4020002 -> Port_Input402
        graph.add_edges((labels['4020002'], labels['402']))
        # Port_Output2 -> __Relation__4020002
        graph.add_edges((labels['2'], labels['4020002']))
        # Port_Output451 -> __Relation__5010451
        graph.add_edges((labels['451'], labels['5010451']))
        # UnitDelay5 -> __Block_Inport__50000000501
        graph.add_edges((labels['5'], labels['50000000501']))
        # UnitDelay5 -> __Block_Outport__50000000002
        graph.add_edges((labels['5'], labels['50000000002']))
        # __Contains__9900000005 -> UnitDelay5
        graph.add_edges((labels['9900000005'], labels['5']))
        # __Block_Outport__50000000002 -> Port_Output2
        graph.add_edges((labels['50000000002'], labels['2']))
        # __Block_Inport__50000000501 -> Port_Input501
        graph.add_edges((labels['50000000501'], labels['501']))
        # __Relation__5010451 -> Port_Input501
        graph.add_edges((labels['5010451'], labels['501']))
        # Constant6 -> __Block_Outport__60000000651
        graph.add_edges((labels['6'], labels['60000000651']))
        # __Contains__9900000006 -> Constant6
        graph.add_edges((labels['9900000006'], labels['6']))
        # __Block_Outport__60000000651 -> Port_Output651
        graph.add_edges((labels['60000000651'], labels['651']))
        # SubSystem99 -> __Contains__9900000003
        graph.add_edges((labels['99'], labels['9900000003']))
        # SubSystem99 -> __Contains__9900000004
        graph.add_edges((labels['99'], labels['9900000004']))
        # SubSystem99 -> __Contains__9900000005
        graph.add_edges((labels['99'], labels['9900000005']))
        # SubSystem99 -> __Contains__9900000006
        graph.add_edges((labels['99'], labels['9900000006']))
        
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
        # __Block_Outport__10000000002, Integrator1, __Block_Inport__10000000000, __Contains__9900000001
        graph.delete_nodes([labels["10000000002"], labels["1"], labels["10000000000"], labels["9900000001"]])
    
