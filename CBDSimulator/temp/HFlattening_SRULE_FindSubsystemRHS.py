

from Server.TCore.core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattening_SRULE_FindSubsystemRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattening_SRULE_FindSubsystemRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattening_SRULE_FindSubsystemRHS, self).__init__(name='HFlattening_SRULE_FindSubsystemRHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(0, 4), (4, 1), (2, 3), (3, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('663313b2-ce81-4bb2-8a5f-1ed654fa052e')
        
        # Set the node attributes
        self.vs[0]["MT_post__Name"] = """return attr_value + '_after'"""
        self.vs[0]["MT_post__Position"] = """return attr_value"""
        self.vs[0]["MT_post__value"] = """return attr_value"""
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_post__Constant"""
        self.vs[0]["GUID__"] = UUID('a72dac3f-c54b-4b4a-a88c-da34d030a9c3')
        self.vs[1]["MT_post__Name"] = """return 1"""
        self.vs[1]["MT_label__"] = """51"""
        self.vs[1]["mm__"] = """MT_post__Port_Output"""
        self.vs[1]["GUID__"] = UUID('39e050ac-cb81-4aff-9472-1e21e643e8fd')
        self.vs[2]["MT_post__Name"] = """return attr_value"""
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["mm__"] = """MT_post__SubSystem"""
        self.vs[2]["GUID__"] = UUID('0df15252-927a-406d-a6e5-ca79b1cba89e')
        self.vs[3]["MT_post__Name"] = """return attr_value"""
        self.vs[3]["MT_label__"] = """9900000000"""
        self.vs[3]["mm__"] = """MT_post____Contains__"""
        self.vs[3]["GUID__"] = UUID('142d1851-76ea-4445-b509-12cebe15d99d')
        self.vs[4]["MT_label__"] = """51"""
        self.vs[4]["mm__"] = """MT_post____Block_Outport__"""
        self.vs[4]["GUID__"] = UUID('28f2fa47-f3a5-44e5-9a72-c5c31cd9856f')

        from HFlattening_SRULE_FindSubsystemLHS import HFlattening_SRULE_FindSubsystemLHS
        self.pre = HFlattening_SRULE_FindSubsystemLHS()
    
    def set_Name0(self, attr_value, PreNode, graph):
        return attr_value + '_after'


    def set_Name51(self, attr_value, PreNode, graph):
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
        # Constant0
        try:
            graph.vs[labels['0']]['Name'] = self.set_Name0(graph.vs[labels['0']]['Name'], lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'Name\'', e)
        
        graph.vs[labels['0']][Himesis.Constants.MT_DIRTY] = True
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        
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
    
