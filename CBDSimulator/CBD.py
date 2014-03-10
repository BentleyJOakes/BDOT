import matplotlib.pyplot as plt


class BaseBlock:

  # A base class for all types of CBD blocks

  def __init__(self, name):
    self.setBlockName(name)
    
    # The output signal produced by this block is encoded as an ordered list of values
    self.__signal = []
    
    # List of blocks that are linked to this block via indistinguishable inputs.
    # The time-delay (Delay, Integrator and Derivative) and Test blocks are different
    # as they have input ports that need to be distinguished
    # (IC for Delay/Integrator/Derivative blocks and TRUE_in/FALSE_in for Test blocks).
    # Each element of the list is a tuple containing 
    # (1) the block whose output this input is connected to, and 
    # (2) the name (a String) of the signal connecting the input block and self
    self.linksIN = []
    
    
    # List of blocks that are linked to this block via indistinguishable inputs.
    # Note that multiple connections may be made from the output of
    # any block. They will all have the same signal[] and the same name (that of the block)
    self.linksOUT = []


    self.Trigger = None

  def getBlockName(self):
    return self.__block_name
    
  def setBlockName(self, block_name):
    self.__block_name = block_name


  def getBlockType(self):
    return self.__class__.__name__

  def appendToSignal(self, value):
    self.__signal.append(value)

  def getSignal(self):
    return self.__signal

  def linkInput(self, in_block):
    self.linksIN.insert(0,in_block)
    
  def linkOutput(self, out_block):
    self.linksOUT.insert(0,out_block)


  def __repr__(self):
    repr = self.getBlockName() + ":" + self.getBlockType() + "\n"
    
    if len(self.linksIN) == 0:
      repr+= "  No incoming connections to IN port\n"
    else:
      for in_block in self.linksIN:
        repr += "  IN <- " + in_block.getBlockName() + ":" + in_block.getBlockType() + "\n"
        
    if len(self.linksOUT) == 0:
      repr+= "  No outgoing connections from OUT port\n"
    else:
      for in_block in self.linksOUT:
        repr += "  OUT <- " + in_block.getBlockName() + ":" + in_block.getBlockType() + "\n"
        
    if self.Trigger == None:
        repr += "  No incoming connections to Trigger port\n"
    else:
        repr += "  Trig <- " + self.Trigger.getBlockName() + ":" + self.Trigger.getBlockType() + "\n"
    return repr

class InputBlock(BaseBlock):
    def __init__(self, block_name):
        BaseBlock.__init__(self, block_name)

class OutputBlock(BaseBlock):
    def __init__(self, block_name):
        BaseBlock.__init__(self,block_name)

class SequenceRepeater(BaseBlock):
    def __init__(self, block_name, seq = 1):
        BaseBlock.__init__(self,block_name)
        if seq == 1:
            self.seq = [1,1,2,3]
        else:
            self.seq = [1,2,3,4]
        self.iteration = 0
class FloorBlock(BaseBlock):
    def __init__(self,block_name):
        BaseBlock.__init__(self,block_name)

class ScopeBlock(BaseBlock):
    def __init__(self, block_name):
        BaseBlock.__init__(self,block_name)

class ConstantBlock(BaseBlock):
  def __init__(self, block_name, value=0.0):

    BaseBlock.__init__(self, block_name)
    self.__value = value
  
  def getValue(self):
    return self.__value
    
  def setValue(self, value):
    self.__value = value
    
  def linkInput(self, in_block):
    print "Warning: Constant (block %s) does not accept input, ignoring extra connection" % self.getBlockName()

  def __repr__(self):    
    return BaseBlock.__repr__(self) + "  Value = " + str(self.getValue()) + "\n"
    

class NegatorBlock(BaseBlock):
  def __init__(self, block_name):
    BaseBlock.__init__(self, block_name)

  def linkInput(self, in_block):
    if len(self.linksIN) >= 1:
      print "Warning: Negator (block %s) takes exactly one input, ignoring extra connection (from block %s)"\
             % (self.getBlockName(), in_block.getBlockName())
    else:  
      self.linksIN.append(in_block)

class InverterBlock(BaseBlock):
  def __init__(self, block_name):
    BaseBlock.__init__(self, block_name)

  def linkInput(self, in_block):
    if len(self.linksIN) >= 1:
      print "Warning: Inverter (block %s) takes exactly one input, ignoring extra connection (from block %s)"\
             % (self.getBlockName(), in_block.getBlockName())
    else:  
      self.linksIN.append(in_block)
   

class AdderBlock(BaseBlock):
  def __init__(self, block_name):
    BaseBlock.__init__(self, block_name)
   

class ProductBlock(BaseBlock):
  def __init__(self, block_name):
    BaseBlock.__init__(self, block_name)

class GainBlock(BaseBlock):
  def __init__(self, block_name, gain = 1.0):

    BaseBlock.__init__(self, block_name)
    self.gain = gain

class PowerBlock(BaseBlock):
  def __init__(self, block_name, power=2.0):

    BaseBlock.__init__(self, block_name)
    self.power = power


class ModuloBlock(BaseBlock):
  def __init__(self, block_name, div = 2.0):
    BaseBlock.__init__(self, block_name)
    self.div = div


class GenericBlock(BaseBlock):
  def __init__(self, block_name, block_operator=None):
    # operator is the name (a string) of a Python function from the math library
    # which will be called when the block is evaluated
    # by default, initialized to None
    BaseBlock.__init__(self, block_name)
    self.__block_operator = block_operator
  
  def getBlockOperator(self):
    return self.__block_operator 

  def __repr__(self):    
    repr = BaseBlock.__repr__(self) 
    if self.__block_operator == None:
      repr += "  No operator given\n"
    else:
      repr += "  Operator :: " + self.__block_operator + "\n"
    return repr 

class DelayBlock(BaseBlock):
  def __init__(self, block_name):
    BaseBlock.__init__(self, block_name)

    # The block whose output is connected to the IC port, and 
    # None if no block connected to the IC port
    self.IC = None 

  def linkInput(self, in_block):
    if len(self.linksIN) >= 1:
      print "Warning: Delay (block %s) takes exactly one input, ignoring extra connection (from block %s)"\
             % (self.getBlockName(), in_block.getBlockName())
    else:  
      self.linksIN.append(in_block)

  def __repr__(self):
    repr = BaseBlock.__repr__(self)
    if self.IC == None:
      repr += "  No incoming connection to IC port\n"
    else:
      repr += "  IC <- " + self.IC.getBlockName() + ":" + self.IC.getBlockType() + "\n"
    return repr

class TimeDelayBlock(DelayBlock):
  # serves as a base class for Integrator and Derivative
  def __init__(self, block_name, time_increment=0.001):
    DelayBlock.__init__(self, block_name)
    self.__timeIncrement = time_increment
  
  def getTimeIncrement(self):
    return self.__timeIncrement
 
  def __repr__(self):
    return DelayBlock.__repr__(self) #+ "  Time increment :: " + str(self.__timeIncrement)
    

class IntegratorBlock(TimeDelayBlock):
  def __init__(self, block_name, time_increment=0.001):
    TimeDelayBlock.__init__(self, block_name, time_increment=time_increment)

  def __repr__(self):
     return TimeDelayBlock.__repr__(self)

class DerivativeBlock(TimeDelayBlock):
  def __init__(self, block_name, time_increment=0.001):
    TimeDelayBlock.__init__(self, block_name, time_increment=time_increment)

  def __repr__(self):
     return TimeDelayBlock.__repr__(self)

class TestBlock(BaseBlock):
  def __init__(self, block_name,expr = "=", switch_value = 0.0):
    BaseBlock.__init__(self, block_name)
    # The block whose output is connected to the TRUE_in port, and 
    # None if no block connected to the TRUE_in port
    self.TRUE_in = None
    # The block whose output is connected to the FALSE_in port, and 
    # None if no block connected to the FALSE_in port
    self.FALSE_in = None

    self.expr = expr # possible expressions = > < >= <=

    self.switch_value = switch_value
    
  def __repr__(self):    
    repr = BaseBlock.__repr__(self)
    if self.TRUE_in == None:
      repr += "  No incoming connection to TRUE_in port\n" 
    else:
      repr += "  TRUE_in <- " + self.TRUE_in.getBlockName() + ":" + self.TRUE_in.getBlockType() + "\n"
    if self.FALSE_in == None:
      repr += "  No incoming connection to FALSE_in port\n" 
    else:
      repr += "  FALSE_in <- " + self.FALSE_in.getBlockName() + ":" + self.FALSE_in.getBlockType() + "\n"
    return repr 

class CBD(BaseBlock):
  # The CBD class, contains an entire Causal Block Diagram 
  def __init__(self, block_name):
    BaseBlock.__init__(self, block_name)
    # The blocks in the CBD will be stored both 
    #  as an ordered list __blocks and   
    #  as a dictionary __blocksDict with the blocknames as keys for 
    #   fast name-based retrieval and 
    #   to ensure block names are unique within a single CBD
    self.__blocks = []
    self.__blocksDict = {}

    #TODO: move to flattening optimization
    self.__subsystems = []
    self.__inportsParentsDict = {} # dictionary of inportsParent with inportnames (== inputblock names) as keys

    self.__outportsDependentsDict = {} # dictionary of the parents of outports and the dependents of the outports. Outport names are keys


  def setBlocks(self, blocks):
    # blocks must be a list of BaseBlock (subclass) instances
    if type(blocks) == list:
      for block in blocks:
        if not isinstance(block, BaseBlock):
           exit("CBD.setBlocks() takes a list of BaseBlock (subclass) instances")
    else:
      exit("CBD.setBlocks() takes a list as argument, not a %s" % type(blocks))
   
  def getBlocks(self):
    return self.__blocks

  def getBlockByName(self, name):
    return self.__blocksDict[name]

  def addBlock(self, block):
    if not isinstance(block, BaseBlock):
      exit("Can only add BaseBlock (subclass) instances to a CBD")

    if not self.__blocksDict.has_key(block.getBlockName()):
      self.__blocks.append(block)
      self.__blocksDict[block.getBlockName()] = block
      if isinstance(block,CBD):
          self.__subsystems.append(block)
    else:
      print "Warning: did not add this block as it has the same name %s as an existing block" % block.getBlockName()

  def addConnection(self, from_block, to_block, inport_name=None, outport_name=None):
    if type(from_block) == str:
      from_block = self.getBlockByName(from_block)
    if type(to_block) == str:
      to_block = self.getBlockByName(to_block)
      
    #add the block to the output list
    from_block.linkOutput(to_block)
      
      
    if inport_name == None and outport_name == None:
      to_block.linkInput(from_block)

    elif isinstance(to_block, CBD) and isinstance(from_block,CBD):
        to_block.__inportsParentsDict[inport_name] = (from_block,outport_name)
        if outport_name in from_block.__outportsDependentsDict:
            from_block.__outportsDependentsDict[outport_name].append((to_block,inport_name))
        else:
            from_block.__outportsDependentsDict[outport_name] = [(to_block,inport_name)]
        to_block.linkInput(from_block)

    elif isinstance(to_block, CBD):# CBD block has multiple "unknown" inputblocks, they will be connected by name of inputport
        to_block.__inportsParentsDict[inport_name] = (from_block,outport_name)
        to_block.linkInput(from_block)

    elif isinstance(from_block,CBD):
        if inport_name == "Trig":
            to_block.Trigger = from_block
        else:
            if isinstance(to_block,DelayBlock):
                if inport_name == "IC":
                    to_block.IC = from_block
                else:
                    to_block.linkInput(from_block)
            elif isinstance(to_block,TestBlock):
                if inport_name == "TRUE":
                    to_block.TRUE_in = from_block
                elif inport_name == "FALSE":
                    to_block.FALSE_in = from_block
                else:
                    to_block.linkInput(from_block)
            else:
                to_block.linkInput(from_block)

        if outport_name in from_block.__outportsDependentsDict:
            from_block.__outportsDependentsDict[outport_name].append((to_block,inport_name))
        else:
            from_block.__outportsDependentsDict[outport_name] = ([(to_block,inport_name)])
    
    elif inport_name == "Trig":
        print "TrigConnect", from_block.getBlockName(), "Triggers", to_block.getBlockName()
        to_block.Trigger = from_block

    elif isinstance(to_block, DelayBlock): # DelayBlock, DerivativeBlock, IntegratorBlock have one named port
      if inport_name == "IC":
        to_block.IC = from_block
      else: exit("Invalid inport_name '%s' for DelayBlock\n should be IC" % inport_name)

    elif isinstance(to_block, TestBlock): # TestBlock has two named ports
      if inport_name == "TRUE":
        to_block.TRUE_in = from_block
      elif inport_name == "FALSE":
        to_block.FALSE_in = from_block
      else: exit("Invalid inport_name '%s' for TestBlock\n should be TRUE or FALSE" % inport_name)

    else:
      exit("addConnection to non-existing named port '%s'" % inport_name)


  def __repr__(self):
    if len(self.__inportsParentsDict) > 0:
        repr = self.getBlockName() + ":" + self.getBlockType() + "\n"
        for key in self.__inportsParentsDict:
            repr += "  " + key + "<-" + self.__inportsParentsDict[key][0].getBlockName() + ":" + self.__inportsParentsDict[key][0].getBlockType() + "\n"
    else:
        repr = BaseBlock.__repr__(self)
        for block in self.getBlocks():
            repr+= block.__repr__()
    return repr

  def dump(self):
    print "=========== Start of Model Dump ==========="
    print self
    print "=========== End of Model Dump =============\n"

  def dumpSignals(self):
    print "=========== Start of Signals Dump ==========="
    for block in self.getBlocks():
        print "%s:%s" % (block.getBlockName(), block.getBlockType())
        print str(block.getSignal()) + "\n"

    print "=========== End of Signals Dump =============\n"

  def showScopes(self,time):
      for block in self.getBlocks():
          #print "TIME len", len(time)
          #print "Signal len", len(block.getSignal())
          if isinstance(block,ScopeBlock):
              plt.plot(time,block.getSignal())
              plt.show()

  def getSignalDict(self):
    dict = {}
    for block in self.getBlocks():
       dict[block.getBlockName()] = block.getSignal()
    return dict

  def flatten(self):
    for subsystem in self.__subsystems:
       #print "SUB", subsystem.getBlockName()
       if len(subsystem.__subsystems) > 0:
           subsystem.flatten()

       for block in subsystem.getBlocks():
           #print "BLOCK", block.getBlockName()
           if isinstance(block, InputBlock)or isinstance(block,OutputBlock):
               pass
           else:
               block.setBlockName(subsystem.getBlockName()+"_"+block.getBlockName())
               self.addBlock(block)

       for block in subsystem.getBlocks():
                for influencer in block.linksIN:
                    if isinstance(influencer,InputBlock):
                        block.linksIN.remove(influencer)
                        if isinstance(subsystem.__inportsParentsDict[influencer.getBlockName()][0],CBD):
                            self.addConnection(subsystem.__inportsParentsDict[influencer.getBlockName()][0].getBlockName(),block.getBlockName(), outport_name= subsystem.__inportsParentsDict[influencer.getBlockName()][1])
                        else:
                            self.addConnection(subsystem.__inportsParentsDict[influencer.getBlockName()][0].getBlockName(),block.getBlockName())

                if isinstance(block,DelayBlock):
                    if isinstance(block.IC,InputBlock):
                        if isinstance(subsystem.__inportsParentsDict[block.IC.getBlockName()][0],CBD):
                            self.addConnection(subsystem.__inportsParentsDict[block.IC.getBlockName()][0].getBlockName(),block.getBlockName(),inport_name= "IC", outport_name= subsystem.__inportsParentsDict[influencer.getBlockName()][1])
                        else:
                            self.addConnection(subsystem.__inportsParentsDict[block.IC.getBlockName()][0].getBlockName(),block.getBlockName(), inport_name= "IC")

                elif isinstance(block, TestBlock):
                    if isinstance(block.TRUE_in, InputBlock):
                        if isinstance(subsystem.__inportsParentsDict[block.TRUE_in.getBlockName()][0],CBD):
                            self.addConnection(subsystem.__inportsParentsDict[block.TRUE_in.getBlockName()][0].getBlockName(),block.getBlockName(),inport_name= "TRUE", outport_name= subsystem.__inportsParentsDict[influencer.getBlockName()][1])
                        else:
                            self.addConnection(subsystem.__inportsParentsDict[block.TRUE_in.getBlockName()][0].getBlockName(),block.getBlockName(), inport_name= "TRUE")
                    elif isinstance(block.FALSE_in, InputBlock):
                        if isinstance(subsystem.__inportsParentsDict[block.FALSE_in.getBlockName()][0],CBD):
                            self.addConnection(subsystem.__inportsParentsDict[block.FALSE_in.getBlockName()][0].getBlockName(),block.getBlockName(),inport_name= "FALSE", outport_name= subsystem.__inportsParentsDict[influencer.getBlockName()][1])
                        else:
                            self.addConnection(subsystem.__inportsParentsDict[block.FALSE_in.getBlockName()][0].getBlockName(),block.getBlockName(), inport_name= "FALSE")

                elif isinstance(block, OutputBlock):
                    blockInfluencer = block.linksIN[0]
                    if block.getBlockName() in subsystem.__outportsDependentsDict.keys():
                        for (dependent, inport_name) in subsystem.__outportsDependentsDict[block.getBlockName()]:

                            if isinstance(dependent, CBD):
                                self.addConnection(blockInfluencer.getBlockName(),dependent.getBlockName(), inport_name= inport_name)
                            else:
                                if inport_name == None:
                                    dependent.linksIN.remove(subsystem)
                                    self.addConnection(blockInfluencer.getBlockName(),dependent.getBlockName())
                                else:
                                    if isinstance(dependent, DelayBlock) or isinstance(dependent,TestBlock):
                                        self.addConnection(blockInfluencer.getBlockName(),dependent.getBlockName(), inport_name = inport_name)

    for subsystem in self.__subsystems:
        self.__blocks.remove(subsystem)
        del self.__blocksDict[subsystem.getBlockName()]


  





# To add: extensive conformance check of a model with the CBD meta-model.
# This, to avoid building nonsense models and above all to avoid
# passing such a model to a simulator.
# Best to add a checkConformance() method to CBD to be called by the simulator
# before starting.


# A note on hierarchically nested blocks (HV 31/10/2012).
#
# This used to be implemented in the ChildBlock class.
#
# As an entire CBD is now also a class, which specializes
# Baseblock, there is no more need for ChildBlock.
#
# For hierarchical modelling, the following need to be added:
#
# 1. input- and output-ports for entire CBDs. These will 
#    be modelled as InputBlock and OutputBlock classes.
#
# 2. a flatten() method which takes as input a hierarchical
#    CBD and produces as output a flattended CBD.
#    A flattened CBD will have unique names for all blocks and signals
#    obtained by "_"-separated concatenation of all block
#    names, starting from the hierarchical model's root.
#    A flattened CBD will no longer have CBD instances in it.
#    All InputBlock and OutputBlock instances will have been
#    replaced by direct connections between blocks in the flattened model.
 
