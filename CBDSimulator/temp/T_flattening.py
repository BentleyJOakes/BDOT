from Server.TCore.t_core.messages import Packet
from Server.TCore.t_core.composer import Composer
from Server.TCore.tc_python.frule import FRule
from Server.TCore.tc_python.arule import ARule
from Server.TCore.tc_python.srule import SRule
from HFlattening_SRULE_Product_ConstantLHS import HFlattening_SRULE_Product_ConstantLHS
from HFlattening_SRULE_Product_ConstantRHS import HFlattening_SRULE_Product_ConstantRHS

class SRULE_Product_Constant(Composer):
    def __init__(self):
        self.rule = SRule(HFlattening_SRULE_Product_ConstantLHS(), HFlattening_SRULE_Product_ConstantRHS())

    def packet_in(self, packet):
         return self.rule.packet_in(packet)

transOrder = {"SRULE_Product_Constant":[None,None,None]}
def packet_in(packet):
    current = "SRULE_Product_Constant"
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

