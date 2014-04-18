

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_FRULE_toCanonical_no_plantLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_FRULE_toCanonical_no_plantLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_FRULE_toCanonical_no_plantLHS, self).__init__(name='HCasedevs_FRULE_toCanonical_no_plantLHS', num_nodes=9, edges=[])
        
        # Add the edges
        self.add_edges([(0, 3), (3, 1), (0, 4), (4, 2), (6, 7), (7, 5), (5, 8), (8, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('a05915c1-0397-405c-ae27-52983025a197')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__Numerator"] = """return True"""
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre__TransferFcn"""
        self.vs[0]["MT_pre__Denominator"] = """return True"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('bb171c50-3739-4075-a557-c2113ac8b436')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["mm__"] = """MT_pre__Port_Input"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('98e4b21a-4ac2-4e5d-adc2-5cb4a0471bb7')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__Port_Output"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('57729201-2490-4114-b2fe-267855d6af1f')
        self.vs[3]["MT_label__"] = """20000000001"""
        self.vs[3]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[3]["GUID__"] = UUID('4e369f43-1cf1-4bf0-9bda-2494dbe649f0')
        self.vs[4]["MT_label__"] = """20000000003"""
        self.vs[4]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[4]["GUID__"] = UUID('0bf862ff-afd5-4fef-883c-36aeb0ec51c3')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """9"""
        self.vs[5]["MT_subtypes__"] = """"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """MT_pre__SubSystem"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["MT_pre__Name"] = """return False if 'plant' in attr_value else True"""
        self.vs[5]["GUID__"] = UUID('3562b2b1-3168-40fa-90c3-91de916df16f')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """99"""
        self.vs[6]["MT_subtypes__"] = """"""
        self.vs[6]["mm__"] = """MT_pre__SubSystem"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["MT_pre__Name"] = """return True"""
        self.vs[6]["GUID__"] = UUID('1db1be34-7e4d-4f46-a095-428246bc7178')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """9900000009"""
        self.vs[7]["MT_subtypes__"] = """"""
        self.vs[7]["mm__"] = """MT_pre____Contains__"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["MT_pre__Name"] = """return True"""
        self.vs[7]["GUID__"] = UUID('06a2dcfe-cf7d-4355-bd91-d81ec4b256ac')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """900000002"""
        self.vs[8]["MT_subtypes__"] = """"""
        self.vs[8]["mm__"] = """MT_pre____Contains__"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["MT_pre__Name"] = """return True"""
        self.vs[8]["GUID__"] = UUID('c54f2415-e62e-44a3-8edf-f35856805534')

    def eval_Name9(self, attr_value, this):
        return False if 'plant' in attr_value else True


    def eval_Numerator2(self, attr_value, this):
        return True


    def eval_Position2(self, attr_value, this):
        return True


    def eval_Denominator2(self, attr_value, this):
        return True


    def eval_Name2(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000009(self, attr_value, this):
        return True


    def eval_Name900000002(self, attr_value, this):
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

