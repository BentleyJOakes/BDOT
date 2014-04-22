

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
        
        super(HFlattening_SRULE_Product_ConstantLHS, self).__init__(name='HFlattening_SRULE_Product_ConstantLHS', num_nodes=14, edges=[])
        
        # Add the edges
        self.add_edges([(0, 10), (10, 4), (1, 11), (11, 5), (1, 12), (12, 6), (1, 13), (13, 7), (4, 3), (3, 6), (2, 8), (8, 0), (2, 9), (9, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('1fedec71-ab97-43f1-9756-61696d8d4726')
        
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
        self.vs[0]["GUID__"] = UUID('1b5027aa-4710-4703-b7ee-ef2a4ee014e6')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__Position"] = """return True"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """MT_pre__Product"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__Name"] = """return True"""
        self.vs[1]["GUID__"] = UUID('e2771b43-0826-47ab-8b77-3aa6434ee8d3')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__SubSystem"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__Name"] = """return True"""
        self.vs[2]["GUID__"] = UUID('38874930-0c1e-443d-9de3-a02cd8dff138')
        self.vs[3]["MT_label__"] = """2020151"""
        self.vs[3]["mm__"] = """MT_pre____Relation__"""
        self.vs[3]["GUID__"] = UUID('02de59fa-8b5c-4960-a438-d9d2638cdf5b')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """151"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["mm__"] = """MT_pre__Port_Output"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('62a1eb0b-6a9d-4228-aafa-7b59934d5eef')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """0"""
        self.vs[5]["MT_subtypes__"] = """"""
        self.vs[5]["mm__"] = """MT_pre__Port_Input"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('089aab84-6470-4a23-8e12-cabdd9a59c6b')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """202"""
        self.vs[6]["MT_subtypes__"] = """"""
        self.vs[6]["mm__"] = """MT_pre__Port_Input"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('71ff2ccd-0d4b-4f61-996d-9f2974d4897f')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """4"""
        self.vs[7]["MT_subtypes__"] = """"""
        self.vs[7]["mm__"] = """MT_pre__Port_Output"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('7d9e26ad-ba03-459f-a3d6-7a9f7ee88671')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """9900000001"""
        self.vs[8]["MT_subtypes__"] = """"""
        self.vs[8]["mm__"] = """MT_pre____Contains__"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["MT_pre__Name"] = """return True"""
        self.vs[8]["GUID__"] = UUID('4a378714-ed84-4a35-9295-bb24ad7d5039')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """9900000002"""
        self.vs[9]["MT_subtypes__"] = """"""
        self.vs[9]["mm__"] = """MT_pre____Contains__"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["MT_pre__Name"] = """return True"""
        self.vs[9]["GUID__"] = UUID('23fc7dba-1262-41b4-a560-c34b72c5d7b8')
        self.vs[10]["MT_label__"] = """10000000151"""
        self.vs[10]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[10]["GUID__"] = UUID('71db2dc1-900a-44a0-8751-53a01b90fb58')
        self.vs[11]["MT_label__"] = """20000000000"""
        self.vs[11]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('3c736294-c01a-4f25-8606-7f2fdf5226e2')
        self.vs[12]["MT_label__"] = """20000000202"""
        self.vs[12]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('cd70b90b-4247-4dfb-8266-3c9e325c6f8c')
        self.vs[13]["MT_label__"] = """20000000004"""
        self.vs[13]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('d9c725d4-973a-473e-bb13-25ded7103089')

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

