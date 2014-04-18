

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_SRULE_Product_ConstantRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_SRULE_Product_ConstantRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_SRULE_Product_ConstantRHS, self).__init__(name='HCasedevs_SRULE_Product_ConstantRHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(0, 5), (5, 1), (0, 6), (6, 2), (3, 4), (4, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('8ab52923-2f70-4e12-b37d-34fd67e4fc32')
        
        # Set the node attributes
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["MT_post__Position"] = """return PreNode('1')['Position']"""
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["MT_post__gain"] = """return PreNode('1')['value']"""
        self.vs[0]["MT_post__Name"] = """return PreNode('1')['Name']+'Gain'"""
        self.vs[0]["mm__"] = """MT_post__Gain"""
        self.vs[0]["GUID__"] = UUID('60f35582-b51b-43d5-a0c3-55f842600986')
        self.vs[1]["MT_label__"] = """0"""
        self.vs[1]["MT_post__Name"] = """return 1"""
        self.vs[1]["mm__"] = """MT_post__Port_Input"""
        self.vs[1]["GUID__"] = UUID('9125eae6-3773-4dfe-8821-ba8eb955f268')
        self.vs[2]["MT_label__"] = """4"""
        self.vs[2]["MT_post__Name"] = """return 1"""
        self.vs[2]["mm__"] = """MT_post__Port_Output"""
        self.vs[2]["GUID__"] = UUID('9202ab21-ff8e-4178-8ff0-eb353a2a4009')
        self.vs[3]["MT_label__"] = """99"""
        self.vs[3]["MT_post__Name"] = """return attr_value"""
        self.vs[3]["mm__"] = """MT_post__SubSystem"""
        self.vs[3]["GUID__"] = UUID('72db13e2-d0ee-4b6f-988e-64773f238db3')
        self.vs[4]["MT_label__"] = """9900000005"""
        self.vs[4]["MT_post__Name"] = """return attr_value"""
        self.vs[4]["mm__"] = """MT_post____Contains__"""
        self.vs[4]["GUID__"] = UUID('1a6a2d8c-9db9-42ca-a063-a8f65e52a7d7')
        self.vs[5]["MT_label__"] = """50000000000"""
        self.vs[5]["mm__"] = """MT_post____Block_Inport__"""
        self.vs[5]["GUID__"] = UUID('8bbdbe4f-b0d4-45a7-a81f-5ce4080c762b')
        self.vs[6]["MT_label__"] = """50000000004"""
        self.vs[6]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[6]["GUID__"] = UUID('f219f10e-713e-4e92-9c63-0b5417182c56')

        from HCasedevs_SRULE_Product_ConstantLHS import HCasedevs_SRULE_Product_ConstantLHS
        self.pre = HCasedevs_SRULE_Product_ConstantLHS()
    
    def set_Position5(self, attr_value, PreNode, graph):
        return PreNode('1')['Position']


    def set_gain5(self, attr_value, PreNode, graph):
        return PreNode('1')['value']


    def set_Name5(self, attr_value, PreNode, graph):
        return PreNode('1')['Name']+'Gain'


    def set_Name0(self, attr_value, PreNode, graph):
        return 1


    def set_Name4(self, attr_value, PreNode, graph):
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
        # Port_Output4
        try:
            graph.vs[labels['4']]['Name'] = self.set_Name4(graph.vs[labels['4']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['4']][Himesis.Constants.MT_DIRTY] = True
        
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
        # __Contains__9900000005
        new_node = graph.add_node()
        labels['9900000005'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Block_Inport__50000000000
        new_node = graph.add_node()
        labels['50000000000'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Inport__'
        # __Block_Outport__50000000004
        new_node = graph.add_node()
        labels['50000000004'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Gain5 -> __Block_Inport__50000000000
        graph.add_edges((labels['5'], labels['50000000000']))
        # Gain5 -> __Block_Outport__50000000004
        graph.add_edges((labels['5'], labels['50000000004']))
        # __Contains__9900000005 -> Gain5
        graph.add_edges((labels['9900000005'], labels['5']))
        # __Block_Inport__50000000000 -> Port_Input0
        graph.add_edges((labels['50000000000'], labels['0']))
        # __Block_Outport__50000000004 -> Port_Output4
        graph.add_edges((labels['50000000004'], labels['4']))
        # SubSystem99 -> __Contains__9900000005
        graph.add_edges((labels['99'], labels['9900000005']))
        
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
        # Port_Output151, Port_Input202, __Block_Inport__20000000000, __Block_Outport__20000000004, Constant1, Product2, __Relation__2020151, __Block_Inport__20000000202, __Contains__9900000001, __Contains__9900000002, __Block_Outport__10000000151
        graph.delete_nodes([labels["151"], labels["202"], labels["20000000000"], labels["20000000004"], labels["1"], labels["2"], labels["2020151"], labels["20000000202"], labels["9900000001"], labels["9900000002"], labels["10000000151"]])
    
