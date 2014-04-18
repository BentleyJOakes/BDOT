

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_SRULE_Product_ConstantLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_SRULE_Product_ConstantLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_SRULE_Product_ConstantLHS, self).__init__(name='HCasedevs_SRULE_Product_ConstantLHS', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([(0, 10), (10, 4), (1, 11), (11, 5), (1, 12), (12, 6), (1, 13), (13, 7), (4, 3), (3, 6), (2, 8), (8, 0), (2, 9), (9, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('f7b27601-743c-48b1-b11e-eab1c61c201d')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre__Constant"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__value"] = """return True"""
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('ac280244-1c63-4c38-86a8-605f9c588daf')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__Position"] = """return True"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """MT_pre__Product"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__Name"] = """return True"""
        self.vs[1]["GUID__"] = UUID('74d44114-e356-49f7-88a5-c0c71c30e939')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__SubSystem"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__Name"] = """return True"""
        self.vs[2]["GUID__"] = UUID('803cd103-1873-477e-b10b-81d3c91afa59')
        self.vs[3]["MT_label__"] = """2020151"""
        self.vs[3]["mm__"] = """MT_pre____Relation__"""
        self.vs[3]["GUID__"] = UUID('4d82597b-b563-4576-b5b1-e77155f234cf')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """151"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["mm__"] = """MT_pre__Port_Output"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('247c0316-3962-4ffa-93df-8575b2b42f86')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """0"""
        self.vs[5]["MT_subtypes__"] = """"""
        self.vs[5]["mm__"] = """MT_pre__Port_Input"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('b92bc12e-6c69-47c4-ae6f-1da3b04dd0d2')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """202"""
        self.vs[6]["MT_subtypes__"] = """"""
        self.vs[6]["mm__"] = """MT_pre__Port_Input"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('78f941f4-b86e-4e62-9932-b8859eed018d')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """4"""
        self.vs[7]["MT_subtypes__"] = """"""
        self.vs[7]["mm__"] = """MT_pre__Port_Output"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('69022e70-0416-4a79-8c38-54b8adcabf66')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """9900000001"""
        self.vs[8]["MT_subtypes__"] = """"""
        self.vs[8]["mm__"] = """MT_pre____Contains__"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["MT_pre__Name"] = """return True"""
        self.vs[8]["GUID__"] = UUID('f0f6d51e-e917-4db6-ab1d-6e165cc59741')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """9900000002"""
        self.vs[9]["MT_subtypes__"] = """"""
        self.vs[9]["mm__"] = """MT_pre____Contains__"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["MT_pre__Name"] = """return True"""
        self.vs[9]["GUID__"] = UUID('56acd116-5aea-4e01-a60b-385041c93909')
        self.vs[10]["MT_label__"] = """10000000151"""
        self.vs[10]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[10]["GUID__"] = UUID('15c68534-200b-4338-8f39-646741020061')
        self.vs[11]["MT_label__"] = """20000000000"""
        self.vs[11]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('e7ab18ac-41bb-4a87-aa63-352c5dde775e')
        self.vs[12]["MT_label__"] = """20000000202"""
        self.vs[12]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('817fddb8-3131-42c0-bfcd-75f826695cac')
        self.vs[13]["MT_label__"] = """20000000004"""
        self.vs[13]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('c2646e13-47e6-45c3-b6e3-ac530e254f20')

    def eval_Position1(self, attr_value, this):
        return True


    def eval_value1(self, attr_value, this):
        return True


    def eval_Name1(self, attr_value, this):
        return True


    def eval_Position2(self, attr_value, this):
        return True


    def eval_Name2(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000001(self, attr_value, this):
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

