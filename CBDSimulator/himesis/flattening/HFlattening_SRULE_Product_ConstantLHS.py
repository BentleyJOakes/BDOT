

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HFlattening_SRULE_Product_ConstantLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HFlattening_SRULE_Product_ConstantLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HFlattening_SRULE_Product_ConstantLHS, self).__init__(name='HFlattening_SRULE_Product_ConstantLHS', num_nodes=3, edges=[])
        
        # Add the edges
        self.add_edges([(1, 2), (2, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('5b0822f5-6d2f-42ea-9190-bdbdcdf1016b')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """10"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre_SubSystem"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('8ef6a86a-aa35-4cdd-ae0a-b55a2000e35b')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """99"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["mm__"] = """MT_pre__SubSystem"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__Name"] = """return True"""
        self.vs[1]["GUID__"] = UUID('7c2787f9-7db8-43eb-a218-556c51604293')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """9900000010"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre____Contains__"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__Name"] = """return True"""
        self.vs[2]["GUID__"] = UUID('0b308f21-fe28-46a1-935e-47b21f0c4a4b')

    def eval_Position10(self, attr_value, this):
        return True


    def eval_Name10(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000010(self, attr_value, this):
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

