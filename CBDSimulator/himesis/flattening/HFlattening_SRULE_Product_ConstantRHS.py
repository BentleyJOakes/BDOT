

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattening_SRULE_Product_ConstantRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattening_SRULE_Product_ConstantRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattening_SRULE_Product_ConstantRHS, self).__init__(name='HFlattening_SRULE_Product_ConstantRHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(0, 4), (4, 1), (2, 3), (3, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('4df415d8-2d1c-4fcc-ac5b-8b27a142e78c')
        
        # Set the node attributes
        self.vs[0]["MT_post__Name"] = """return attr_value"""
        self.vs[0]["MT_post__Position"] = """return attr_value"""
        self.vs[0]["MT_post__value"] = """return attr_value"""
        self.vs[0]["MT_label__"] = """10"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_post__Constant"""
        self.vs[0]["GUID__"] = UUID('44e81b4c-24ae-4780-bb6c-0732229e65a9')
        self.vs[1]["MT_post__Name"] = """return 1"""
        self.vs[1]["MT_label__"] = """1051"""
        self.vs[1]["mm__"] = """MT_post__Port_Output"""
        self.vs[1]["GUID__"] = UUID('c808eae8-226a-458e-ab61-6254497ca2f2')
        self.vs[2]["MT_post__Name"] = """return attr_value"""
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["mm__"] = """MT_post__SubSystem"""
        self.vs[2]["GUID__"] = UUID('ce748fd4-ffde-482b-a146-623c5f1f39ce')
        self.vs[3]["MT_post__Name"] = """return attr_value"""
        self.vs[3]["MT_label__"] = """9900000010"""
        self.vs[3]["mm__"] = """MT_post____Contains__"""
        self.vs[3]["GUID__"] = UUID('1145c1c2-eab3-4070-945d-2bfe50116e72')
        self.vs[4]["MT_label__"] = """100000001051"""
        self.vs[4]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[4]["GUID__"] = UUID('52af7dd6-041b-4561-a6a1-2815fdbe80be')

        from HFlattening_SRULE_Product_ConstantLHS import HFlattening_SRULE_Product_ConstantLHS
        self.pre = HFlattening_SRULE_Product_ConstantLHS()
    
    def set_Name1051(self, attr_value, PreNode, graph):
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
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # Port_Output1051
        new_node = graph.add_node()
        labels['1051'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Port_Output'
        try:
            graph.vs[new_node]['Name'] = self.set_Name1051(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        # __Block_Outport__100000001051
        new_node = graph.add_node()
        labels['100000001051'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = '__Block_Outport__'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # Constant10 -> __Block_Outport__100000001051
        graph.add_edges((labels['10'], labels['100000001051']))
        # __Block_Outport__100000001051 -> Port_Output1051
        graph.add_edges((labels['100000001051'], labels['1051']))
        
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
    
