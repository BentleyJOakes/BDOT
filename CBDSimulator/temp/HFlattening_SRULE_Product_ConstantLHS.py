

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
        self["GUID__"] = UUID('18d83e27-2f7c-4cc6-b94f-67e6b30ebce6')
        
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
        self.vs[0]["GUID__"] = UUID('d5b60847-bb42-4bc9-abbf-470c669ee468')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_pre__Position"] = """return True"""
        self.vs[1]["MT_label__"] = """2"""
        self.vs[1]["MT_subtypes__"] = """"""
        self.vs[1]["BackgroundColor"] = """white"""
        self.vs[1]["mm__"] = """MT_pre__Product"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__Name"] = """return True"""
        self.vs[1]["GUID__"] = UUID('ea4a4d06-0911-427a-b814-cb919c8f601b')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """99"""
        self.vs[2]["MT_subtypes__"] = """"""
        self.vs[2]["mm__"] = """MT_pre__SubSystem"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__Name"] = """return True"""
        self.vs[2]["GUID__"] = UUID('9c34f09a-4c8e-448a-bbb6-626982528352')
        self.vs[3]["MT_label__"] = """2020151"""
        self.vs[3]["mm__"] = """MT_pre____Relation__"""
        self.vs[3]["GUID__"] = UUID('680675e5-4b09-42eb-9872-e49dbe246b0c')
        self.vs[4]["MT_subtypeMatching__"] = False
        self.vs[4]["MT_label__"] = """151"""
        self.vs[4]["MT_subtypes__"] = """"""
        self.vs[4]["mm__"] = """MT_pre__Port_Output"""
        self.vs[4]["MT_dirty__"] = False
        self.vs[4]["GUID__"] = UUID('56739230-22bf-40cc-812d-0595abf9df3b')
        self.vs[5]["MT_subtypeMatching__"] = False
        self.vs[5]["MT_label__"] = """0"""
        self.vs[5]["MT_subtypes__"] = """"""
        self.vs[5]["mm__"] = """MT_pre__Port_Input"""
        self.vs[5]["MT_dirty__"] = False
        self.vs[5]["GUID__"] = UUID('5cd4b9f3-f0fb-45a0-b8a1-afe2b61e8117')
        self.vs[6]["MT_subtypeMatching__"] = False
        self.vs[6]["MT_label__"] = """202"""
        self.vs[6]["MT_subtypes__"] = """"""
        self.vs[6]["mm__"] = """MT_pre__Port_Input"""
        self.vs[6]["MT_dirty__"] = False
        self.vs[6]["GUID__"] = UUID('ec25e33a-3db5-4d52-8d23-296531e470b8')
        self.vs[7]["MT_subtypeMatching__"] = False
        self.vs[7]["MT_label__"] = """4"""
        self.vs[7]["MT_subtypes__"] = """"""
        self.vs[7]["mm__"] = """MT_pre__Port_Output"""
        self.vs[7]["MT_dirty__"] = False
        self.vs[7]["GUID__"] = UUID('b8bda3c9-76f7-4f2d-9bc2-2a86a185fc8f')
        self.vs[8]["MT_subtypeMatching__"] = False
        self.vs[8]["MT_label__"] = """9900000001"""
        self.vs[8]["MT_subtypes__"] = """"""
        self.vs[8]["mm__"] = """MT_pre____Contains__"""
        self.vs[8]["MT_dirty__"] = False
        self.vs[8]["MT_pre__Name"] = """return True"""
        self.vs[8]["GUID__"] = UUID('704d55a7-9647-4d42-9ab9-f346fe18cec5')
        self.vs[9]["MT_subtypeMatching__"] = False
        self.vs[9]["MT_label__"] = """9900000002"""
        self.vs[9]["MT_subtypes__"] = """"""
        self.vs[9]["mm__"] = """MT_pre____Contains__"""
        self.vs[9]["MT_dirty__"] = False
        self.vs[9]["MT_pre__Name"] = """return True"""
        self.vs[9]["GUID__"] = UUID('7f2fd517-5924-4e08-ace9-22f603a4d82d')
        self.vs[10]["MT_label__"] = """10000000151"""
        self.vs[10]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[10]["GUID__"] = UUID('e5d5b270-e8e9-44d9-ab8b-6415ae8fe090')
        self.vs[11]["MT_label__"] = """20000000000"""
        self.vs[11]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[11]["GUID__"] = UUID('9346ff84-f38e-472d-a067-e9ba4272d783')
        self.vs[12]["MT_label__"] = """20000000202"""
        self.vs[12]["mm__"] = """MT_pre____Block_Inport__"""
        self.vs[12]["GUID__"] = UUID('e4d5be36-3e48-4262-b6d6-c279192069d8')
        self.vs[13]["MT_label__"] = """20000000004"""
        self.vs[13]["mm__"] = """MT_pre____Block_Outport__"""
        self.vs[13]["GUID__"] = UUID('59c25b75-72ee-40af-a92d-7ce0ec3b5205')

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

