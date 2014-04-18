from Server.TCore.t_core.messages import Packet
from Server.TCore.t_core.composer import Composer
from Server.TCore.tc_python.frule import FRule
from Server.TCore.tc_python.arule import ARule
from Server.TCore.tc_python.srule import SRule
from HCasedevs_SRULE_Constant_SumsLHS import HCasedevs_SRULE_Constant_SumsLHS
from HCasedevs_SRULE_Constant_SumsRHS import HCasedevs_SRULE_Constant_SumsRHS
from HCasedevs_FRULE_toCanonicalLHS import HCasedevs_FRULE_toCanonicalLHS
from HCasedevs_FRULE_toCanonicalRHS import HCasedevs_FRULE_toCanonicalRHS
from HCasedevs_SRULE_Product_ConstantLHS import HCasedevs_SRULE_Product_ConstantLHS
from HCasedevs_SRULE_Product_ConstantRHS import HCasedevs_SRULE_Product_ConstantRHS
from HCasedevs_FRULE_toFwdLHS import HCasedevs_FRULE_toFwdLHS
from HCasedevs_FRULE_toFwdRHS import HCasedevs_FRULE_toFwdRHS
from HCasedevs_FRULE_toCanonical_no_plantLHS import HCasedevs_FRULE_toCanonical_no_plantLHS
from HCasedevs_FRULE_toCanonical_no_plantRHS import HCasedevs_FRULE_toCanonical_no_plantRHS

class SRULE_Constant_Sums(Composer):
    def __init__(self):
        self.rule = SRule(HCasedevs_SRULE_Constant_SumsLHS(), HCasedevs_SRULE_Constant_SumsRHS())

    def packet_in(self, packet):
         return self.rule.packet_in(packet)

class FRULE_toCanonical(Composer):
    def __init__(self):
        self.rule = FRule(HCasedevs_FRULE_toCanonicalLHS(), HCasedevs_FRULE_toCanonicalRHS())

    def packet_in(self, packet):
         return self.rule.packet_in(packet)

class SRULE_Product_Constant(Composer):
    def __init__(self):
        self.rule = SRule(HCasedevs_SRULE_Product_ConstantLHS(), HCasedevs_SRULE_Product_ConstantRHS())

    def packet_in(self, packet):
         return self.rule.packet_in(packet)

class FRULE_toFwd(Composer):
    def __init__(self):
        self.rule = FRule(HCasedevs_FRULE_toFwdLHS(), HCasedevs_FRULE_toFwdRHS())

    def packet_in(self, packet):
         return self.rule.packet_in(packet)

class FRULE_toCanonical_no_plant(Composer):
    def __init__(self):
        self.rule = FRule(HCasedevs_FRULE_toCanonical_no_plantLHS(), HCasedevs_FRULE_toCanonical_no_plantRHS())

    def packet_in(self, packet):
         return self.rule.packet_in(packet)

transOrder = {"SRULE_Constant_Sums":[None,None,None],"FRULE_toCanonical":[None,None,None],"SRULE_Product_Constant":["SRULE_Constant_Sums",None,None],"FRULE_toFwd":["SRULE_Product_Constant",None,None],"FRULE_toCanonical_no_plant":["FRULE_toFwd",None,None]}
def packet_in(packet):
    current = "FRULE_toCanonical_no_plant"
    while current is not None:
        exec("trans = " + current + "()")
        exec("packet = trans.packet_in(packet)")
        packet.clear_state()
        if trans.rule.is_success:
            current = transOrder[current][0]
        elif not trans.rule.is_success:
            current = transOrder[current][2]
        else:
            current = transOrder[current][1]
    return packet

