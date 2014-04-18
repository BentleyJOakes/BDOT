

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
        self["GUID__"] = UUID('19c68527-906d-4381-8d59-05729f9b5e07')
        
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
        self.vs[0]["GUID__"] = UUID('2bf47ed1-b257-4a2d-9c11-4830558233fc')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__Position"] = """return True"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """MT_pre__Product"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__Name"] = """return True"""
        self.vs[1]["GUID__"] = UUID('2cbecc2c-8ef7-4881-b507-eefa4c8a08f3')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__SubSystem"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__Name"] = """return True"""
        self.vs[2]["GUID__"] = UUID('e254143b-ceaa-44fc-b0e3-16e94c03a063')
        self.vs[3]["MT_label__"] = """2020151"""
        self.vs[3]["mm__"] = """MT_pre____Relation__"""
        self.vs[3]["GUID__"] = UUID('6df6b56e-8a2f-4eaa-8e31-0bc91d0894f8')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """151"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["mm__"] = """MT_pre__Port_Output"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('6252f1b9-844a-4ce3-9a50-3838300af534')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """0"""
        self.vs[5]["MT_subtypes__"] = """"""
        self.vs[5]["mm__"] = """MT_pre__Port_Input"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('77a34214-0ac2-45c3-bfba-d85cc4d20537')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """202"""
        self.vs[6]["MT_subtypes__"] = """"""
        self.vs[6]["mm__"] = """MT_pre__Port_Input"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('5f9f0534-9219-4092-aac8-67f5144905de')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """4"""
        self.vs[7]["MT_subtypes__"] = """"""
        self.vs[7]["mm__"] = """MT_pre__Port_Output"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('a074a15e-a088-4321-a53e-4537d8fcd4e4')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """9900000001"""
        self.vs[8]["MT_subtypes__"] = """"""
        self.vs[8]["mm__"] = """MT_pre____Contains__"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["MT_pre__Name"] = """return True"""
        self.vs[8]["GUID__"] = UUID('c826b67c-f3bc-4ce5-ab1a-8c8e4fe58201')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """9900000002"""
        self.vs[9]["MT_subtypes__"] = """"""
        self.vs[9]["mm__"] = """MT_pre____Contains__"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["MT_pre__Name"] = """return True"""
        self.vs[9]["GUID__"] = UUID('823d63bf-27d0-438a-a992-873e5b93c858')
        self.vs[10]["MT_label__"] = """10000000151"""
        self.vs[10]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[10]["GUID__"] = UUID('eeb832ef-e8a0-439c-9c88-b68fe8ea5713')
        self.vs[11]["MT_label__"] = """20000000000"""
        self.vs[11]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('24b9b0dc-8984-4b7e-a412-4c0dd2c56d6c')
        self.vs[12]["MT_label__"] = """20000000202"""
        self.vs[12]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('6d244212-3fe3-4469-8990-127e80c078bf')
        self.vs[13]["MT_label__"] = """20000000004"""
        self.vs[13]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('6f351493-cd7e-4bc4-a23a-53b88d2e13f1')

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

