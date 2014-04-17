from Server.Core.SimulinkLibItems import S2HConstants
from Server.Core.SimulinkParser import ParseModel, Block, OUTPORT, INPORT
from Server.TCore.core.himesis import Himesis

__author__ = 'jdenil'



class ContainsBlock(object):
    def __init__(self, block, subsystem):
        self.block = block
        self.subsystem = subsystem
        self._id= None
        self.fullPath = 'None/None'
        self.name = 'None'
        
        

    def getType(self):
        return S2HConstants.CONTAINMENT_RELATION

    def getParameters(self):
        return {}

class SimulinkModelToHimesis(object):
    def __init__(self, mh, modelname, path, outpath = './himesis/'):
        self.mh = mh
        self.modelname = modelname
        self.path = path
        self.output = outpath
        
        self.debugLevel = 0


    def SimulinkModelToHimesis(self):
        parser = ParseModel(self.modelname, self.mh)
        blocks = parser.blocks
        connections = parser.c
        if self.debugLevel > 0:
            print connections.conTable
        dividedblocks = {}
        for block in blocks:
            fullname = block.fullPath
            fullname = fullname.rsplit('/',1)
            if fullname[0] in dividedblocks:
                dividedblocks[fullname[0]].append(block)
            else:
                dividedblocks[fullname[0]] = [block]
        if self.debugLevel > 0:
            print dividedblocks
        # Go into the hierarchy and add subsystem links: There is one not yet created subsystem for the top node... Create it here as well
        for k,theBlockList in dividedblocks.iteritems():
            the_subSystem = k.rsplit('/',1)
            if self.debugLevel > 0:
                print the_subSystem
            if the_subSystem[0] in dividedblocks and len(the_subSystem) > 1:
                # it exists, we now find in this one the correct subsystem:
                blocks_one_above = dividedblocks[the_subSystem[0]]
                subsys = None
                for boa in blocks_one_above:
                    if boa.fullPath == k:
                        subsys = boa
                        break
                if subsys is None:
                    raise Exception('Could not locate the subsystem block')
                for block in theBlockList:
                    blocks.append(ContainsBlock(block, subsys))
            else:
                # These are the top level blocks normally:
                subsys = Block(the_subSystem[0],'None/'+the_subSystem[0],'SubSystem',self.mh)
                blocks.append(subsys)
                for block in theBlockList:
                    blocks.append(ContainsBlock(block,subsys))
        self.createSimulinkModel(blocks,connections,self.modelname,self.output)
        # close the model in SImulink:
        self.mh.closeWithoutSave(self.modelname)


    def getAllNodes(self,blocks):
        nodes = []
        nodeCounter = 0
        for block in blocks:
            block._id = nodeCounter
            nodeCounter += 1
            nodes.append(block)
            if not isinstance(block,ContainsBlock):
                for inport in block.inports.values():
                    inport._id = nodeCounter
                    nodeCounter += 1
                    nodes.append(inport)
                for outport in block.outports.values():
                    outport._id = nodeCounter
                    nodeCounter +=1
                    nodes.append(outport)
                for enable in block.enabled.values():
                    enable._id = nodeCounter
                    nodeCounter +=1
                    nodes.append(enable)
                for trigger in block.trigger.values():
                    trigger._id = nodeCounter
                    nodeCounter +=1
                    nodes.append(trigger)

        return nodes


    def createSimulinkModel(self, blocks, connections, name,outputfolder):
        allNodes = self.getAllNodes(blocks)
        # init Himesis:
        numberOfNodes = len(allNodes)
        himesis = Himesis(name=name, num_nodes=numberOfNodes)
        himesis[Himesis.Constants.META_MODEL] = ['Simulink']  # the meta-model type name
        himesis["name"] = str(name)
        # attributes
        for node in allNodes:
            himesis.vs[node._id][Himesis.Constants.META_MODEL] = str(node.getType())   # the meta-model type element
            #fullname = node.fullPath
            #fullname = fullname.rsplit('/',1)
            theName = str(node.name).rsplit('/',1)[-1]
            himesis.vs[node._id]['Name'] = str(theName)
            # do other attributes:
            parameters = node.getParameters()
            for k,v in parameters.iteritems():
                himesis.vs[node._id][k] = v
        for block in blocks:
            if not isinstance(block, ContainsBlock):
                himesis.vs[block._id]['Position'] = block.Position
        # edges, we have edges from block to port and from the containment relations
        for block in blocks:
            if not isinstance(block, ContainsBlock):
                for inport in block.inports.values():
                    blockportvertex = himesis.add_node()
                    himesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = S2HConstants.BLOCK_INPORT_RELATION
                    himesis.add_edge(block._id, blockportvertex)
                    himesis.add_edge(blockportvertex, inport._id)
                for outport in block.outports.values():
                    blockportvertex = himesis.add_node()
                    himesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = S2HConstants.BLOCK_OUTPORT_RELATION
                    himesis.add_edge(block._id, blockportvertex)
                    himesis.add_edge(blockportvertex, outport._id)
                for enableport in block.enabled.values():
                    blockportvertex = himesis.add_node()
                    himesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = S2HConstants.BLOCK_ENABLE_RELATION
                    himesis.add_edge(block._id, blockportvertex)
                    himesis.add_edge(blockportvertex, enableport._id)
                for triggerport in block.trigger.values():
                    blockportvertex = himesis.add_node()
                    himesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = S2HConstants.BLOCK_TRIGGER_RELATION
                    himesis.add_edge(block._id, blockportvertex)
                    himesis.add_edge(blockportvertex, triggerport._id)
            else:
                if self.debugLevel > 0:
                    print block.subsystem
                    print block.block
                himesis.add_edge(block.subsystem._id, block._id)
                himesis.add_edge(block._id,block.block._id)
        #and from outport to inport
        createdLines = []
        #del connections.conTable[None]
        for linename,connectionsdict in connections.conTable.iteritems():
            if linename is not None:
                doIdelete = True
                if self.debugLevel > 0:
                    print linename
                theOutports = connectionsdict[OUTPORT]
                theInports = connectionsdict[INPORT]
                for outportEndpoint in theOutports:
                    opid = None
                    if hasattr(outportEndpoint.port, '_id'):
                        opid = outportEndpoint.port._id
                    if opid is None or opid == -1: # the line is on another level, or even it is not there anymore
                        doIdelete = False
                        break
                    for inportEndpoint in theInports:
                        ipid = inportEndpoint.port._id
                        if ipid is None or ipid == -1: # the line is on another level, or even it is not there anymore
                            break
                        # use the assigned id of the
                        convertex = himesis.add_node()
                        himesis.vs[convertex][Himesis.Constants.META_MODEL] = S2HConstants.PORT2PORT_RELATION
                        himesis.add_edge(opid, convertex)
                        himesis.add_edge(convertex, ipid)
                        inportEndpoint.port._id = None # We created this line, so we do not need it anymore
                    outportEndpoint.port._id = None # We created this linem
                if doIdelete:
                    createdLines.append(linename)
        for linename in createdLines:
            del connections.conTable[linename]

        #compile
        himesis.compile(outputfolder)
