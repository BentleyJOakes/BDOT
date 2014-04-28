import math

from CBD import *

#the old CBD formalism simulator
#topological sorting needs to be extracted from this




class CBDsimulator:

  def __init__(self, model, curIteration=0):

      flattened = False
      self.__model = model

      self.__depGraph = None
      self.sortedGraph = None

      for block in model.getBlocks():
          if isinstance(block,CBD) and flattened == False:
              model.flatten()
              flattened = True

      self.__curIteration = curIteration

      #get de sortedlist of components to use for constant folding optimization
      """self.__depGraph = self.__createDepGraph()
      self.sortedGraph = self.__depGraph.getStrongComponents()
      model.foldConstants(self.sortedGraph)
      model.dump()"""
      self.__depGraph = None
      self.sortedGraph = None

  #return the dep graph
  #TODO: make sure this is safe to do
  def getDepGraph(self):
    if self.__depGraph == None:
        self.__depGraph = self.__createDepGraph()
  
    return self.__depGraph
  
  
    # to add: flattening of hierarchical CBDs before simulation starts 
    
  def getModel(self):
    return self.__model
                              
  def step(self):
    #print "Iteration", self.__curIteration
      
    if (self.__curIteration < 2):
      self.__depGraph = self.__createDepGraph()
      """print "----------------- Dependency Graph ---------------------"
      print self.__depGraph
      print "--------------------------------------------------------"""""
      self.sortedGraph = self.__depGraph.getStrongComponents()
      #print "-- Sorted collection of Strongly Connected Components --"
      #print self.sortedGraph # a list of lists
      #print "--------------------------------------------------------"
 
    self.__computeBlocks()
    self.__curIteration += 1

  # Constructs the dependency graph of the current state of the CBD
  def __createDepGraph(self):
    #self.__model.dump()
    blocks = self.__model.getBlocks()
    depGraph = DepGraph()
  
    for block in blocks:
      #print "Block before Depgraph", block
      depGraph.addMember(block)
  
    for block in blocks:
        
        if not block.Trigger == None:
            depGraph.setDependency(block,block.Trigger)
        if isinstance(block, DelayBlock):
            if (self.__curIteration == 0):
                if block.IC in blocks:
                    depGraph.setDependency(block,block.IC)
                else:
                    raise ValueError("No block linked to IC port of: ", block.getBlockName())
            else:
                pass

        else:
            for influencer in block.linksIN:
                if influencer in blocks:
                    depGraph.setDependency(block, influencer)
                else:
                    raise ValueError("No block linked to port of: ", block.getBlockName())

        if isinstance(block,TestBlock):
            if block.TRUE_in in blocks:
                depGraph.setDependency(block,block.TRUE_in)
            else:
                raise ValueError("No block linked to TRUE port of: ", block.getBlockName())

            if block.FALSE_in in blocks:
                depGraph.setDependency(block,block.FALSE_in)
            else:
                raise ValueError("No block linked to FALSE port of: ", block.getBlockName())

      # TO IMPLEMENT
      # Treat dependencies on memory blocks (Delay, Integrator, Derivative) differently: 
      # During the first iteration (time == 0.0), the block only depends on the IC; 
      # During later iterations, it depends on the block type. 
      #
      # use depGraph.setDependency(block, block_it_depends_on)
      #
    

    return depGraph
  
  def __computeGeneric(self, block):
    operator = getattr(math, block.getBlockOperator())
    output = operator(block.linksIN[0].getSignal()[self.__curIteration])
    block.appendToSignal(output)

  def __computeConstant(self, block):
    # TO IMPLEMENT
    block.appendToSignal(block.getValue())

  def __computeScope(self,block):
    influentBlock = block.linksIN[0]
    block.appendToSignal(influentBlock.getSignal()[self.__curIteration])


  def __computeNegator(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        influentBlock = block.linksIN[0]
        block.appendToSignal(-influentBlock.getSignal()[self.__curIteration])
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])

  def __computeGain(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        influentBlock = block.linksIN[0]
        block.appendToSignal(influentBlock.getSignal()[self.__curIteration]*block.gain)
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])

  def __computeInverter(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        influentBlock = block.linksIN[0]
        if influentBlock.getSignal()[self.__curIteration] == 0:
            raise ValueError("Can't divide by 0: ", block.getBlockName())
        else:
            block.appendToSignal(1/influentBlock.getSignal()[self.__curIteration])
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])

    
  def __computeAdder(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        sum = 0
        for influentBlock in block.linksIN:
            sum += influentBlock.getSignal()[self.__curIteration]
        block.appendToSignal(sum)
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])


  def __computeProduct(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        prod = 1
        for influentBlock in block.linksIN:
            prod *= influentBlock.getSignal()[self.__curIteration]
        block.appendToSignal(prod)
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])

  def __computePower(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:

        influentBlock = block.linksIN[0]
        block.appendToSignal(influentBlock.getSignal()[self.__curIteration] ** block.power)
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])


  def __computeModulo(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        influentBlock = block.linksIN[0]
        if block.div == 0:
            raise ValueError("Can't divide by 0: ", block.getBlockName())
        else:
            block.appendToSignal(influentBlock.getSignal()[self.__curIteration] % block.div)
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])


  def __computeDelay(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        
        if self.__curIteration == 0:
            block.appendToSignal(block.IC.getSignal()[self.__curIteration])
        else:
            block.appendToSignal(block.linksIN[0].getSignal()[self.__curIteration - 1])
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])


  def __computeDerivative(self, block):
    # Should never be used. Derivative blocks should be replaced 
    # by block diagrams using only Delay blocks
    if (self.__curIteration == 0):
      output = block.IC.getSignal()[self.__curIteration]
    else:
      influent_block = block.linksIN[0] # only one input
      influent_signal = influent_block.getSignal()
      output = (influent_signal[self.__curIteration] - \
                influent_signal[self.__curIteration-1]) / \
                block.getTimeIncrement()
    block.appendToSignal(output)

  def __computeIntegrator(self, block):
    # Should never be used. Integrator blocks should be replaced 
    # by block diagrams using only Delay blocks
    if (self.__curIteration == 0):
      output = block.IC.getSignal()[self.__curIteration]
    else:
      influent_block = block.linksIN[0] # only one input
      influent_signal = influent_block.getSignal()
      output = block.getSignal()[self.__curIteration-1] + \
                influent_signal[self.__curIteration-1] * \
                block.getTimeIncrement()
    block.appendToSignal(output)

  def __computeTest(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        influentBlock = block.linksIN[0]
        if block.expr == "=":
            if influentBlock.getSignal()[self.__curIteration] == block.switch_value:
                block.appendToSignal(block.TRUE_in.getSignal()[self.__curIteration])
            else:
                block.appendToSignal(block.FALSE_in.getSignal()[self.__curIteration])
        elif block.expr == ">":
            if influentBlock.getSignal()[self.__curIteration] > block.switch_value:
                block.appendToSignal(block.TRUE_in.getSignal()[self.__curIteration])
            else:
                block.appendToSignal(block.FALSE_in.getSignal()[self.__curIteration])
        elif block.expr == "<":
            if influentBlock.getSignal()[self.__curIteration] < block.switch_value:
                block.appendToSignal(block.TRUE_in.getSignal()[self.__curIteration])
            else:
                block.appendToSignal(block.FALSE_in.getSignal()[self.__curIteration])
        elif block.expr == "<=":
            if influentBlock.getSignal()[self.__curIteration] < block.switch_value or influentBlock.getSignal()[self.__curIteration] == block.switch_value:
                block.appendToSignal(block.TRUE_in.getSignal()[self.__curIteration])
            else:
                block.appendToSignal(block.FALSE_in.getSignal()[self.__curIteration])
        elif block.expr == ">=":
            if influentBlock.getSignal()[self.__curIteration] > block.switch_value or influentBlock.getSignal()[self.__curIteration] == block.switch_value:
                block.appendToSignal(block.TRUE_in.getSignal()[self.__curIteration])
            else:
                block.appendToSignal(block.FALSE_in.getSignal()[self.__curIteration])
        else:
            raise ValueError("Expression "+block.expr+" isn't a legal expression. Allowed expression are: =  >  <   >=   <=")
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])


  def __computeSequence(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        block.appendToSignal(block.seq[block.iteration])
        if self.__curIteration != 0:
            block.iteration += 1
        if block.iteration == len(block.seq):
            block.iteration = 0
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])

  def __computeFloor(self, block):
    if 1:
    #if block.Trigger.getSignal()[self.__curIteration]:
        influentBlock = block.linksIN[0]
        block.appendToSignal(math.floor(influentBlock.getSignal()[self.__curIteration]))
    else:
        block.appendToSignal(block.getSignal()[self.__curIteration-1])

  def __computeBlocks(self):

    for component in self.sortedGraph:

      if (not self.__hasCycle(component)):
        block = component[0]   # the strongly connected component has a single element
        #print "Block type + name:", block.getBlockType(),":",block.getBlockName()

        if isinstance(block, GenericBlock):
          self.__computeGeneric(block)
        elif isinstance(block, ConstantBlock):
          self.__computeConstant(block)
        elif isinstance(block, ScopeBlock):
          self.__computeScope(block)
        elif isinstance(block, NegatorBlock):
          self.__computeNegator(block)
        elif isinstance(block, InverterBlock):
          self.__computeInverter(block)
        elif isinstance(block, AdderBlock):
          self.__computeAdder(block)
        elif isinstance(block, ProductBlock):
          self.__computeProduct(block)
        elif isinstance(block, GainBlock):
          self.__computeGain(block)
        elif isinstance(block, FloorBlock):
          self.__computeFloor(block)
        elif isinstance(block, PowerBlock):
          self.__computePower(block)
        elif isinstance(block, ModuloBlock):
          self.__computeModulo(block)
        elif isinstance(block, DerivativeBlock):
          self.__computeDerivative(block)
        elif isinstance(block, IntegratorBlock):
          self.__computeIntegrator(block)
        elif isinstance(block, DelayBlock): # note that this needs to come AFTER Derivative and Integrator !
                                            # as they are sub-classes of DelayBlock
          self.__computeDelay(block)
        elif isinstance(block, TestBlock):
          self.__computeTest(block)
        elif isinstance(block,SequenceRepeater):
            self.__computeSequence(block)
        elif isinstance(block, CBD):
          raise ValueError("Hierachical blocks should have been flattened by now")
        else:
          raise ValueError("Unknown block type")
      else: #TODO what happens when blocks in loop have different rates?
        print "Component",component
        # Detected a strongly connected component
        assert self.__isLinear(component), "Cannot solve non-linear algebraic loop"
        solverInput = self.__constructLinearInput(component)
        print "########### Input matrix for linear solver -> ###########"
        self.__printLinearInputMatrices(component, solverInput)
        self.__gaussjLinearSolver(solverInput)
        solutionVector = solverInput[1]
        print "########### Solution from linear solver -> ###########"
        for block in component:
          blockIndex = component.index(block) 
          block.appendToSignal(solutionVector[blockIndex])
          print block.getBlockName(), "=", solutionVector[blockIndex], "\n"
    
  # Determine whether a component is cyclic 
  def __hasCycle(self, component):
    assert len(component)>=1, "A component should have at least one element"
    if len(component)>1:
      return True
    else: # a strong component of size one may still have a cycle: a self-loop
      if self.__depGraph.hasDependency(component[0], component[0]):
        return True
      else:
        return False

  # Determines if an algebraic loop describes a linear equation or not
  def __isLinear(self, strongComponent):
    # TO IMPLEMENT
    for block in strongComponent:
        if (isinstance(block, NegatorBlock) or isinstance(block, AdderBlock) or isinstance(block,GainBlock) ):
            pass
        elif isinstance(block, ProductBlock):
            strongInputs = 0
            for influentBlock in block.linksIN:
                if (influentBlock in strongComponent):
                    strongInputs += 1
            if (strongInputs >= 2):
                return False
        else:
            return False

    print "Linear algebraic loop detected"
    return True

  # Constructs input for a solver of systems of linear equations
  # Input consists of two matrices:
  # M1: coefficient matrix, where each row represents an equation of the system
  # M2: result matrix, where each element is the result for the corresponding equation in M1
  def __constructLinearInput(self, strongComponent):
    size = len(strongComponent)
    row = []
    M1 = [] 
    M2 = []
    
    # Initialize matrices with zeros
    i = 0
    while (i < size):
      j = 0
      row = []
      while (j < size):
        row.append(0)
        j += 1
      M1.append(row)
      M2.append(0)
      i += 1
    
    # TO IMPLEMENT

    for index in range(0, len(strongComponent)):
        print "index = ", index
        block = strongComponent[index]
        print "strongComponent.index = ", strongComponent.index(block)
        blockType = block.getBlockType()
        if isinstance(block, AdderBlock):
            for influentblock in block.linksIN:
                if  (not(influentblock in strongComponent)):
                    M2[index] = -influentblock.getSignal()[self.__curIteration]
                    print "I'm here ", influentblock.getSignal()[self.__curIteration], M2
                else:
                    print "influentblock index = ", strongComponent.index(influentblock)
                    print "M1 = ", M1
                    M1[index][index] = -1
                    M1[index][strongComponent.index(influentblock)] = 1
        elif isinstance(block, NegatorBlock):
            influentblock = block.linksIN[0]
            M2[index] = 0
            M1[index][index] = -1
            M1[index][strongComponent.index(influentblock)] = -1

        elif isinstance(block, ProductBlock):
            factor = 1
            infuentindex = 0
            for influentblock in block.linksIN:
                if  (not(influentblock in strongComponent)):
                    factor = influentblock.getSignal()[self.__curIteration]
                else:
                    infuentindex = strongComponent.index(influentblock)
            M2[index] = 0
            M1[index][index] = -1
            M1[index][infuentindex] = factor
        else:
            print "Fault in check linear"
    return [M1, M2]
   
  def __swap(self, a, b):
    t = a
    a = b
    b = t
    return (a, b)
  
  def __ivector(self, n):
    v = []
    for i in range(n):
      v.append(0)
    return v
    
  # Linear equation solution by Gauss-Jordan elimination
  def __gaussjLinearSolver(self, solverInput):
    M1 = solverInput[0]
    M2 = solverInput[1]
    n = len(M1)
    indxc = self.__ivector(n)
    indxr = self.__ivector(n)
    ipiv = self.__ivector(n)
    icol = 0
    irow = 0
    for i in range(n):
      big = 0.0
      for j in range(n):
        if (ipiv[j] != 1):
          for k in range(n):
            if (ipiv[k] == 0):
              if (math.fabs(M1[j][k]) >= big):
                big = math.fabs(M1[j][k])
                irow = j
                icol = k
            elif (ipiv[k] > 1): 
              raise ValueError("GAUSSJ: Singular Matrix-1")
      ipiv[icol] += 1
      if (irow != icol):
        for l in range(n):
          (M1[irow][l], M1[icol][l]) = self.__swap(M1[irow][l], M1[icol][l])
        (M2[irow], M2[icol]) = self.__swap(M2[irow], M2[icol])
      indxr[i] = irow
      indxc[i] = icol
      if (M1[icol][icol] == 0.0):
        raise ValueError("GAUSSJ: Singular Matrix-2")
      pivinv = 1.0/M1[icol][icol]
      M1[icol][icol] = 1.0
      for l in range(n):
        M1[icol][l] *= pivinv
      M2[icol] *= pivinv
      for ll in range(n):
        if (ll != icol):
          dum = M1[ll][icol]
          M1[ll][icol] = 0.0
          for l in range(n):
            M1[ll][l] -= M1[icol][l] * dum
          M2[ll] -= M2[icol] * dum
    l = n
    while (l > 0):
      l -= 1
      if (indxr[l] != indxc[l]):
        for k in range(n):
          (M1[k][indxr[l]], M1[k][indxc[l]]) = self.__swap(M1[k][indxr[l]], M1[k][indxc[l]])     
  
  # Print out the input matrices 
  def __printLinearInputMatrices(self, strongComponent, solverInput):
    print "Indices:"
    i = 0
    for block in strongComponent:
      print i, ":", block.getBlockName(), block.getBlockType()
      i += 1

    print "Matrices:"
    M1 = solverInput[0]
    M2 = solverInput[1]
    for row in M1:
      print row, "=", M2[M1.index(row)]

""" This module implements a dependency graph
    @author: Marc Provost
    @organization: McGill University
    @license: GNU General Public License
    @contact: marc.provost@mail.mcgill.ca
"""

import copy

class DepNode:
  """ Class implementing a node in the dependency graph.
  """
  
  def __init__(self, object):
    """ DepNode's constructor.
        @param object: Reference to a semantic object identifying the node
        @type object: Object
    """
    self.__object = object
    self.__isMarked   = False

  def mark(self):
    self.__isMarked = True
  
  def unMark(self):
    self.__isMarked = False
  
  def isMarked(self):
    return self.__isMarked 

  def getMappedObj(self):
    return self.__object
        
  def __repr__(self):
    return "DepNode :: "+str(self.__object)                 
          
class DepGraph:
  """ Class implementing dependency graph. 
  """

  def __init__(self):
    """ DepGraph's constructor.
    """
    #Dict holding a mapping "Object -> DepNode"
    self.__semanticMapping = {}
    
    #map object->list of objects depending on object
    self.__dependents = {}
    #map object->list of objects that influences object
    self.__influencers = {} 
 
  def __repr__(self):
    repr = "Dependents: \n"
    for dep in self.__dependents:
      repr += dep.getBlockName() + ":" + str(self.__dependents[dep]) + "\n"
    repr += "Influencers: \n"
    for infl in self.__influencers:
      repr += infl.getBlockName() + ":" + str(self.__influencers[infl]) + "\n"
    return repr

  def addMember(self, object):
    """ Add an object mapped to this graph.
        @param object: the object to be added
        @type object: Object
        @raise ValueError: If object is already in the graph
    """
    if not self.hasMember(object): 
      node = DepNode(object) 
      self.__dependents[object]                     = []
      self.__influencers[object]                    = []
      self.__semanticMapping[object] = node    
    else:
      raise ValueError("Specified object is already member of this graph")
      
  def hasMember(self, object):
    return self.__semanticMapping.has_key(object)      

  def removeMember(self, object):
    """ Remove a object from this graph.
        @param object: the object to be removed
        @type object: Object
        @raise ValueError: If object is not in the graph
    """  
    if self.hasMember(object):
      for dependent in self.getDependents(object):
        self.__influencers[dependent].remove(object)
      for influencer in self.getInfluencers(object):
        self.__dependents[influencer].remove(object)
      
      del self.__dependents[object]
      del self.__influencers[object]
      del self.__semanticMapping[object]       
    else:
      raise ValueError("Specified object is not member of this graph")

  def setDependency(self, dependent, influencer):
    """ Creates a dependency between two objects.
        @param dependent: The object which depends on the other
        @param influencer: The object which influences the other
        @type dependent: Object
        @type dependent: Object
        @raise ValueError: if dependent or influencer is not member of this graph
        @raise ValueError: if the dependency already exists
    """
    if self.hasMember(dependent) and self.hasMember(influencer): 
      if not influencer in self.__influencers[dependent] and\
         not dependent in self.__dependents[influencer]:
        self.__influencers[dependent].append(influencer) 
        self.__dependents[influencer].append(dependent)
      else:
        print "DEPENDENT", dependent
        print "influencer",influencer

        raise ValueError("Specified dependency already exists")
    else:
      if not self.hasMember(dependent):
        raise ValueError("Specified dependent object is not member of this graph")
      if not self.hasMember(influencer):
        raise ValueError("Specified influencer object is not member of this graph")
        
  def hasDependency(self, dependent, influencer):
    if self.hasMember(dependent) and self.hasMember(influencer):          
      return influencer in self.__influencers[dependent] and\
             dependent in self.__dependents[influencer]    
    else:
      if not self.hasMember(dependent):
        raise ValueError("Specified dependent object is not member of this graph")
      if not self.hasMember(influencer):
        raise ValueError("Specified influencer object is not member of this graph")        
        
  def unsetDependency(self, dependent, influencer):
    """ Removes a dependency between two objects.
        @param dependent: The object which depends on the other
        @param influencer: The object which influences the other
        @type dependent: Object
        @type dependent: Object
        @raise ValueError: if dependent or influencer is not member of this graph
        @raise ValueError: if the dependency does not exists
    """      
    if self.hasMember(dependent) and self.hasMember(influencer):   
      if influencer in self.__influencers[dependent] and\
         dependent in self.__dependents[influencer]:    
        self.__influencers[dependent].remove(influencer) 
        self.__dependents[influencer].remove(dependent)
      else:
        raise ValueError("Specified dependency does not exists")
    else:
      if not self.hasMember(dependent):
        raise ValueError("Specified dependent object is not member of this graph")
      if not self.hasMember(influencer):
        raise ValueError("Specified influencer object is not member of this graph")
                                                                                                                              
  def getDependents(self, object):
    if self.hasMember(object):
      return copy.copy(self.__dependents[object])
    else:
      raise ValueError("Specified object is not member of this graph") 

  def getInfluencers(self, object):
    if self.hasMember(object):
      return copy.copy(self.__influencers[object])
    else:
      raise ValueError("Specified object is not member of this graph") 
      
  def getStrongComponents(self):
    return self.__strongComponents()
      
  def __getDepNode(self, object):
    if self.hasMember(object):
      return self.__semanticMapping[object]
    else:
      raise ValueError("Specified object is not a member of this graph")      
      
  def __mark(self, object):
    self.__getDepNode(object).mark()
    
  def __unMark(self, object):
    self.__getDepNode(object).unMark()
    
  def __isMarked(self, object):
    return self.__getDepNode(object).isMarked()    
                                                      
  def __topoSort(self):
    """ Performs a topological sort on the graph.
    """
    for object in self.__semanticMapping.keys():
      self.__unMark(object)
    
    sortedList = []
      
    for object in self.__semanticMapping.keys():
      if not self.__isMarked(object):
        self.__dfsSort(object, sortedList)

    return sortedList
    
  def __dfsSort(self, object, sortedList):
    """ Performs a depth first search collecting
        the objects in topological order.
        @param object: the currently visited object.
        @param sortedList: partial sorted list of objects
        @type object: Object
        @type sortedList: list Of Object
    """
    
    if not self.__isMarked(object):
      self.__mark(object)
    
      for influencer in self.getInfluencers(object):      
        self.__dfsSort(influencer, sortedList)
    
      sortedList.append(object)

  def __strongComponents(self):
    """ Determine the strong components of the graph
        @rtype: list of list of Object
    """
    strongComponents = []
    sortedList = self.__topoSort()
    
    for object in self.__semanticMapping.keys():
      self.__unMark(object) 
          
    sortedList.reverse()
        
    for object in sortedList:
      if not self.__isMarked(object):
        component = []      
        self.__dfsCollect(object, component)
        strongComponents.append(component)
    
    strongComponents.reverse()         
    return strongComponents

  def __dfsCollect(self, object, component):
    """ Collects objects member of a strong component.
        @param object: Node currently visited
        @param component: current component
        @type object: Object
        @type component: List of Object
    """
    if not self.__isMarked(object):
      self.__mark(object)
                  
      for dependent in self.getDependents(object):
        self.__dfsCollect(dependent, component)
        
      component.append(object)
