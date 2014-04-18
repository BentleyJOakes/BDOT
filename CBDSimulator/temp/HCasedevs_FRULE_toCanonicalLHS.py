

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_FRULE_toCanonicalLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_FRULE_toCanonicalLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_FRULE_toCanonicalLHS, self).__init__(name='HCasedevs_FRULE_toCanonicalLHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(0, 5), (5, 1), (0, 6), (6, 2), (3, 4), (4, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('6805fe88-3787-4cd3-a721-9fe302f806a7')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__Denominator"] = """return True"""
        self.vs[0]["MT_pre__Numerator"] = """return True"""
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre__TransferFcn"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('b1b905a4-1326-46ea-995d-a8c82454bfa8')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["mm__"] = """MT_pre__Port_Input"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('aeba5793-fd7f-4cad-bd54-5f88283d1b0e')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__Port_Output"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('ab678b95-2b1b-493d-a6b6-bbdac7124d06')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """99"""
        self.vs[3]["MT_subtypes__"] = """"""
        self.vs[3]["mm__"] = """MT_pre__SubSystem"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__Name"] = """return True"""
        self.vs[3]["GUID__"] = UUID('0a1c2031-6764-49d8-82ac-facf8459e954')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """9900000002"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["mm__"] = """MT_pre____Contains__"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["MT_pre__Name"] = """return True"""
        self.vs[4]["GUID__"] = UUID('67893c99-ce88-4572-81d1-62004a511ab0')
        self.vs[5]["MT_label__"] = """20000000001"""
        self.vs[5]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[5]["GUID__"] = UUID('5ea556e7-fc86-497e-8c07-15dca30ce340')
        self.vs[6]["MT_label__"] = """20000000003"""
        self.vs[6]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[6]["GUID__"] = UUID('0508b535-c400-482d-84e1-dcd6a642930f')

    def eval_Denominator2(self, attr_value, this):
        return True


    def eval_Numerator2(self, attr_value, this):
        return True


    def eval_Position2(self, attr_value, this):
        return True


    def eval_Name2(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000002(self, attr_value, this):
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

