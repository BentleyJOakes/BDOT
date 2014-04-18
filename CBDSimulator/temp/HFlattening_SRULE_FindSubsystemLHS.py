

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattening_SRULE_FindSubsystemLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattening_SRULE_FindSubsystemLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattening_SRULE_FindSubsystemLHS, self).__init__(name='HFlattening_SRULE_FindSubsystemLHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(0, 4), (4, 1), (2, 3), (3, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('da3ef30f-e75d-4abf-9b36-1666b1e8d4b2')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre__Constant"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__value"] = """return True"""
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('994febc8-9f1b-49a6-a68a-d6afe32fe762')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """51"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["mm__"] = """MT_pre__Port_Output"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('a1570e84-4246-43a2-b1d5-4db9d4f8a70b')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__SubSystem"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__Name"] = """return True"""
        self.vs[2]["GUID__"] = UUID('f0a5954d-149c-491e-b3b9-a4a2518f1812')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """9900000000"""
        self.vs[3]["MT_subtypes__"] = """"""
        self.vs[3]["mm__"] = """MT_pre____Contains__"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__Name"] = """return True"""
        self.vs[3]["GUID__"] = UUID('58366cc2-1888-4a68-bc77-28a4d9e4e37d')
        self.vs[4]["MT_label__"] = """51"""
        self.vs[4]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[4]["GUID__"] = UUID('16b1c71f-7ca8-46eb-a519-0d0e1fcaa01a')

    def eval_Position0(self, attr_value, this):
        return True


    def eval_value0(self, attr_value, this):
        return True


    def eval_Name0(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000000(self, attr_value, this):
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

