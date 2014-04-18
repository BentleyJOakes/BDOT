

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_FRULE_toFwdLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_FRULE_toFwdLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_FRULE_toFwdLHS, self).__init__(name='HCasedevs_FRULE_toFwdLHS', num_nodes=7, edges=[])
        
        # Add the edges
        self.add_edges([(0, 5), (5, 1), (0, 6), (6, 2), (3, 4), (4, 0)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('ffaec2ce-e267-4d4a-a794-8194c6d07d42')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__InitialCondition"] = """return True"""
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre__Integrator"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('705ff93a-b8dc-4223-9fd0-4eb501727209')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """0"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["mm__"] = """MT_pre__Port_Input"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["GUID__"] = UUID('770b4d7c-696d-4b2a-b1e6-60897402538a')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """2"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__Port_Output"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('fa6ff3d8-609e-4e48-9442-fb739c94e739')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """99"""
        self.vs[3]["MT_subtypes__"] = """"""
        self.vs[3]["mm__"] = """MT_pre__SubSystem"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["MT_pre__Name"] = """return True"""
        self.vs[3]["GUID__"] = UUID('58efb542-a19d-459f-ad19-49ff6ac9d8c1')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """9900000001"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["mm__"] = """MT_pre____Contains__"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["MT_pre__Name"] = """return True"""
        self.vs[4]["GUID__"] = UUID('637e8db0-72e3-4a1c-95ec-436b436353d6')
        self.vs[5]["MT_label__"] = """10000000000"""
        self.vs[5]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[5]["GUID__"] = UUID('25e649f7-7b3f-473d-85d1-66a10aff3c66')
        self.vs[6]["MT_label__"] = """10000000002"""
        self.vs[6]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[6]["GUID__"] = UUID('d74b2754-001d-43fd-bb7b-fa32c0851805')

    def eval_InitialCondition1(self, attr_value, this):
        return True


    def eval_Position1(self, attr_value, this):
        return True


    def eval_Name1(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000001(self, attr_value, this):
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

