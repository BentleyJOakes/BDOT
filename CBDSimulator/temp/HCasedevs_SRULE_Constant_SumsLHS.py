

from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle
from uuid import UUID

inf = "inf"

class HCasedevs_SRULE_Constant_SumsLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the Simulink model HCasedevs_SRULE_Constant_SumsLHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HCasedevs_SRULE_Constant_SumsLHS, self).__init__(name='HCasedevs_SRULE_Constant_SumsLHS', num_nodes=19, edges=[])
        
        # Add the edges
        self.add_edges([(0, 6), (6, 2), (0, 7), (7, 3), (0, 16), (16, 10), (4, 17), (17, 11), (5, 18), (18, 12), (11, 8), (8, 2), (12, 9), (9, 3), (1, 13), (13, 0), (1, 14), (14, 4), (1, 15), (15, 5)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Simulink'
p2
a.""")
        self["name"] = """"""
        self["GUID__"] = UUID('ba0575f3-1958-45db-80ce-c54fb28e3b5a')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__Position"] = """return True"""
        self.vs[0]["MT_label__"] = """0"""
        self.vs[0]["MT_subtypes__"] = """"""
        self.vs[0]["BackgroundColor"] = """white"""
        self.vs[0]["mm__"] = """MT_pre__Sum"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__Name"] = """return True"""
        self.vs[0]["GUID__"] = UUID('280c82cd-5146-4669-84f7-9e633d39f94f')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """99"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["mm__"] = """MT_pre__SubSystem"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__Name"] = """return True"""
        self.vs[1]["GUID__"] = UUID('22a3ba0f-90bf-4521-ac35-e0c77ed3eabd')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__Port_Input"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["GUID__"] = UUID('3388be33-111f-4f96-9d78-ff8933ed4700')
        self.vs[3]["MT_subtypeMatching__"] = False
        self.vs[3]["MT_label__"] = """2"""
        self.vs[3]["MT_subtypes__"] = """"""
        self.vs[3]["mm__"] = """MT_pre__Port_Input"""
        self.vs[3]["MT_dirty__"] = False
        self.vs[3]["GUID__"] = UUID('4d6467cd-ad44-40e8-b70e-71f992aad2e8')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_pre__Position"] = """return True"""
        self.vs[4]["MT_label__"] = """2"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["BackgroundColor"] = """white"""
        self.vs[4]["mm__"] = """MT_pre__Constant"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["MT_pre__value"] = """return True"""
        self.vs[4]["MT_pre__Name"] = """return True"""
        self.vs[4]["GUID__"] = UUID('7bd5e15e-3b08-4c53-b07d-a0584682525a')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_pre__Position"] = """return True"""
        self.vs[5]["MT_label__"] = """1"""
        self.vs[5]["MT_subtypes__"] = """"""
        self.vs[5]["BackgroundColor"] = """white"""
        self.vs[5]["mm__"] = """MT_pre__Constant"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["MT_pre__value"] = """return True"""
        self.vs[5]["MT_pre__Name"] = """return True"""
        self.vs[5]["GUID__"] = UUID('0c53b973-509a-4b82-a5bd-36689f0deb70')
        self.vs[6]["MT_label__"] = """1"""
        self.vs[6]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[6]["GUID__"] = UUID('75bd1e16-54e8-497b-829c-50de2743e60f')
        self.vs[7]["MT_label__"] = """2"""
        self.vs[7]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[7]["GUID__"] = UUID('e4b8b3c9-a17f-4da1-b578-52d88125d0db')
        self.vs[8]["MT_label__"] = """10251"""
        self.vs[8]["mm__"] = """MT_pre____Relation__"""
        self.vs[8]["GUID__"] = UUID('090ebdf7-59e1-41e8-acbc-9c51552818ab')
        self.vs[9]["MT_label__"] = """20151"""
        self.vs[9]["mm__"] = """MT_pre____Relation__"""
        self.vs[9]["GUID__"] = UUID('54ce7790-b94b-4a0a-ab73-617ea2443af6')
        self.vs[10]["MT_subtypeMatching__"] = False
        self.vs[10]["MT_label__"] = """4"""
        self.vs[10]["MT_subtypes__"] = """"""
        self.vs[10]["mm__"] = """MT_pre__Port_Output"""
        self.vs[10]["MT_dirty__"] = False
        self.vs[10]["GUID__"] = UUID('11ca6239-2587-4d87-828a-61afd42cda4b')
        self.vs[11]["MT_subtypeMatching__"] = False
        self.vs[11]["MT_label__"] = """251"""
        self.vs[11]["MT_subtypes__"] = """"""
        self.vs[11]["mm__"] = """MT_pre__Port_Output"""
        self.vs[11]["MT_dirty__"] = False
        self.vs[11]["GUID__"] = UUID('7eac3dfe-1e61-419b-89be-f8a732c63438')
        self.vs[12]["MT_subtypeMatching__"] = False
        self.vs[12]["MT_label__"] = """151"""
        self.vs[12]["MT_subtypes__"] = """"""
        self.vs[12]["mm__"] = """MT_pre__Port_Output"""
        self.vs[12]["MT_dirty__"] = False
        self.vs[12]["GUID__"] = UUID('ecd40243-b054-4d11-b63a-c8ee424f6d86')
        self.vs[13]["MT_subtypeMatching__"] = False
        self.vs[13]["MT_label__"] = """9900000000"""
        self.vs[13]["MT_subtypes__"] = """"""
        self.vs[13]["mm__"] = """MT_pre____Contains__"""
        self.vs[13]["MT_dirty__"] = False
        self.vs[13]["MT_pre__Name"] = """return True"""
        self.vs[13]["GUID__"] = UUID('0cd339c5-aa10-46be-86b9-30876968443a')
        self.vs[14]["MT_subtypeMatching__"] = False
        self.vs[14]["MT_label__"] = """9900000002"""
        self.vs[14]["MT_subtypes__"] = """"""
        self.vs[14]["mm__"] = """MT_pre____Contains__"""
        self.vs[14]["MT_dirty__"] = False
        self.vs[14]["MT_pre__Name"] = """return True"""
        self.vs[14]["GUID__"] = UUID('c5f0b85c-36bc-4cb3-a936-46c3965b9380')
        self.vs[15]["MT_subtypeMatching__"] = False
        self.vs[15]["MT_label__"] = """9900000001"""
        self.vs[15]["MT_subtypes__"] = """"""
        self.vs[15]["mm__"] = """MT_pre____Contains__"""
        self.vs[15]["MT_dirty__"] = False
        self.vs[15]["MT_pre__Name"] = """return True"""
        self.vs[15]["GUID__"] = UUID('10867b72-58f0-4607-87ca-a54b43b24270')
        self.vs[16]["MT_label__"] = """4"""
        self.vs[16]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[16]["GUID__"] = UUID('0c2de88d-16f2-4f42-bb23-be5224fe9e71')
        self.vs[17]["MT_label__"] = """20000000251"""
        self.vs[17]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[17]["GUID__"] = UUID('bf47914d-7502-46ac-8285-f9f049347f86')
        self.vs[18]["MT_label__"] = """10000000151"""
        self.vs[18]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[18]["GUID__"] = UUID('97237877-d8f6-4097-ba53-9257b7ac9fb0')

    def eval_Position0(self, attr_value, this):
        return True


    def eval_Name0(self, attr_value, this):
        return True


    def eval_Position2(self, attr_value, this):
        return True


    def eval_value2(self, attr_value, this):
        return True


    def eval_Name2(self, attr_value, this):
        return True


    def eval_Position1(self, attr_value, this):
        return True


    def eval_value1(self, attr_value, this):
        return True


    def eval_Name1(self, attr_value, this):
        return True


    def eval_Name99(self, attr_value, this):
        return True


    def eval_Name9900000000(self, attr_value, this):
        return True


    def eval_Name9900000002(self, attr_value, this):
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

