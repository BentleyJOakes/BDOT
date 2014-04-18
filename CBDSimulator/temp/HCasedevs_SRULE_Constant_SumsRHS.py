

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_SRULE_Constant_SumsRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_SRULE_Constant_SumsRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_SRULE_Constant_SumsRHS, self).__init__(name='HCasedevs_SRULE_Constant_SumsRHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(0, 4), (4, 1), (2, 3), (3, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('9d65d01e-4c5d-4d55-9f19-d8ad6ff83f12')
        
        # Set the node attributes
        self.vs[0]["MT_post__Name"] = """return 'folded_'+PreNode('1')['Name']+'_'+PreNode('2')['Name']"""
        self.vs[0]["MT_post__Position"] = """return PreNode('0')['Position']"""
        self.vs[0]["MT_post__value"] = """return PreNode('2')['value'] + PreNode('1')['value']"""
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_post__Constant"""
        self.vs[0]["GUID__"] = UUID('a04ed94b-1789-4b23-9c93-5b4a57b623bf')
        self.vs[1]["MT_post__Name"] = """return 1"""
        self.vs[1]["MT_label__"] = """4"""
        self.vs[1]["mm__"] = """MT_post__Port_Output"""
        self.vs[1]["GUID__"] = UUID('18523250-546f-47d9-91ee-169de00bd1ee')
        self.vs[2]["MT_post__Name"] = """return attr_value"""
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["mm__"] = """MT_post__SubSystem"""
        self.vs[2]["GUID__"] = UUID('54a76148-5167-4d7d-aa8d-d6d5f1a32b8c')
        self.vs[3]["MT_post__Name"] = """return attr_value"""
        self.vs[3]["MT_label__"] = """9900000005"""
        self.vs[3]["mm__"] = """MT_post____Contains__"""
        self.vs[3]["GUID__"] = UUID('2da57f6c-3acd-46bc-80a6-12af180bb45d')
        self.vs[4]["MT_label__"] = """50000000004"""
        self.vs[4]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[4]["GUID__"] = UUID('9c3eadbe-f3f0-4f05-a0c4-6e40a693c131')

        from HCasedevs_SRULE_Constant_SumsLHS import HCasedevs_SRULE_Constant_SumsLHS
        self.pre = HCasedevs_SRULE_Constant_SumsLHS()
    
    def set_Name5(self, attr_value, PreNode, graph):
        return 'folded_'+PreNode('1')['Name']+'_'+PreNode('2')['Name']


    def set_Position5(self, attr_value, PreNode, graph):
        return PreNode('0')['Position']


    def set_value5(self, attr_value, PreNode, graph):
        return PreNode('2')['value'] + PreNode('1')['value']


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
        # Port_Output4
        try:
            graph.vs[labels['4']]['Name'] = self.set_Name4(graph.vs[labels['4']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['4']][Himesis.Constants.MT_DIRTY] = True
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # Constant5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Constant'
        try:
            graph.vs[new_node]['Name'] = self.set_Name5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        try:
            graph.vs[new_node]['Position'] = self.set_Position5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Position\'', e)
        try:
            graph.vs[new_node]['value'] = self.set_value5(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'value\'', e)
        # __Contains__9900000005
        new_node = graph.add_node()
        labels['9900000005'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Contains__'
        # __Block_Outport__50000000004
        new_node = graph.add_node()
        labels['50000000004'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Constant5 -> __Block_Outport__50000000004
        graph.add_edges((labels['5'], labels['50000000004']))
        # __Contains__9900000005 -> Constant5
        graph.add_edges((labels['9900000005'], labels['5']))
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
        # Port_Output151, __Block_Outport__10000000151, __Relation__10251, __Block_Inport__1, Sum0, __Relation__20151, __Block_Inport__2, __Contains__9900000000, __Contains__9900000001, __Contains__9900000002, Port_Output251, __Block_Outport__20000000251
        graph.delete_nodes([labels["151"], labels["10000000151"], labels["10251"], labels["1"], labels["0"], labels["20151"], labels["2"], labels["9900000000"], labels["9900000001"], labels["9900000002"], labels["251"], labels["20000000251"]])
    
