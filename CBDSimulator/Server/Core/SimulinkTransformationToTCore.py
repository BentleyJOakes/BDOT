import os
from Server.Core.SimulinkLibItems import TypeMapperLHS, TypeMapperRHs, getPreSubTypes, S2HConstants
from Server.Core.SimulinkParser import Block, INPORT, OUTPORT, ParseModel
from Server.TCore.core.himesis import Himesis, HimesisPreConditionPatternLHS, HimesisPostConditionPattern


"""
For the transformation multiple blocks (ports, contains, block_to_port, etc.) with multiple labels have to be added to the Himesis model
Labels should return the same in pre and post if the created block maps to the same otherwise it should return some other label
Therefore this is the system:
blocks labels = 1 -98 (max of 98 user blocks in a transformation, is this enough? Otherwise new label system has to found)
Inport of blocks: label *100 + portnr (but can also be something given by user bu using the port block...)
Outport of blocks: label * 100 + 50 + portnr
__Relation__ between input and output port: label should be based on inport*10000 + outport
Top Subsystem of the transformation: label 99
__Contains__ relation between block and subsystems: should be based on the label of the subsystem and the label of the block (block range: 1-99):
    subsys*100 000 000 + blocklabel
relation between block and port: blocklabel * 10 000 000 000 + portlabel (I hope T-core can handle this... )
"""


__author__ = 'jdenil'


class PreContainsBlock(object):
    def __init__(self, block, subsystem):
        self.block = block
        self.subsystem = subsystem
        self._id= None
        self.fullPath = 'None/None'
        self.parameters = {'MT_pre__Name' : 'return True'}


    def getType(self):
        return Himesis.Constants.MT_PRECOND_PREFIX+S2HConstants.CONTAINMENT_RELATION

    def getParameters(self):
        return self.parameters


class PostContainsBlock(object):
    def __init__(self, block, subsystem):
        self.block = block
        self.subsystem = subsystem
        self._id= None
        self.fullPath = 'None/None'
        self.parameters = {'MT_post__Name' : 'return attr_value'}

    def getType(self):
        return Himesis.Constants.MT_POSTCOND_PREFIX+S2HConstants.CONTAINMENT_RELATION

    def getParameters(self):
        return self.parameters

"""
test comment for checkin
"""
class TransfromationRule(object):

    portStubs = ['Post_CommonlyUsedBlocks/Post_OutportOfBlock','Post_CommonlyUsedBlocks/Post_InportOfBlock','Pre_CommonlyUsedBlocks/Pre_InportOfBlock','Pre_CommonlyUsedBlocks/Pre_OutportOfBlock']

    def createPreBlockTopSubSystem(self):
        block = Block('top', 'none', 'SubSystem',None)
        block.parameters = {'MT_label__':'99', 'MT_pre__Name': 'return True'}
        return block

    def createPostBlockTopSubSystem(self):
        block = Block('top', 'none', 'SubSystem', None)
        block.parameters = {'MT_label__':'99', 'MT_post__Name': 'return attr_value'}
        return block

    def __init__(self, name, path, connections):
        self.LHS = []
        self.LHSHimesis = None
        self.RHS = []
        self.RHSHimesis = None
        self.NACs = []
        self.NACsHimesis = []
        self.name = name
        self.path = path
        self.connections = connections
        self.pre_label_MM_mapping={}


    def existsAnOutport(self, outport):
        """
        This returns the outport ID of block if it exist in the rule: Post and Pre_InportOfBlock
        @param inport:
        @return: the ID or None
        """
        linename = outport.line
        if linename in self.connections:
            inports = self.connections[linename][INPORT]
            for endpoint in inports:
                if endpoint.block.getType() == 'Post_CommonlyUsedBlocks/Post_OutportOfBlock' or endpoint.block.getType() == 'Pre_CommonlyUsedBlocks/Pre_OutportOfBlock':
                    return endpoint.block
            return None
        else:
            return None

    def existsAnInport(self, inport):
        """
        This returns the inport ID of block if it exist in the rule: Post and Pre_InportOfBlock
        @param inport:
        @return: the ID or None
        """
        linename = inport.line
        if linename in self.connections:
            inports = self.connections[linename][OUTPORT]
            for endpoint in inports:
                if endpoint.block.getType() == 'Post_CommonlyUsedBlocks/Post_InportOfBlock' or endpoint.block.getType() == 'Pre_CommonlyUsedBlocks/Pre_InportOfBlock':
                    return endpoint.block
            return None
        else:
            return None

    def getAllNodes(self,blocks, lhs):
        """
        Get all the nodes except for the Relation nodes in hierarchy
        @param blocks:
        @param lhs: is it a LHS or RHS
        @return:
        """
        nodes = []
        nodeCounter = 0
        divided = {}

        #add the contain relationships:
        for block in blocks:
            fullpath = block.fullPath.rsplit('/',1)
            print fullpath
            if fullpath[0] in divided:
                divided[fullpath[0]].append(block)
            else:
                divided[fullpath[0]] = [block]
        # Do the Hierarchies
        for hierarchy,blocklist in divided.iteritems():
            print 'doing hierarchy ' + str(hierarchy) + ' with # of blocks: ' + str(len(blocklist))
            # find the level above and the block that contains these:
            levelabove  = hierarchy.rsplit('/',1)
            print 'levelabove:' +str(levelabove)
            if levelabove[0] in divided:
                # it exists, this is not the toplevel!
                # find the subsystems:
                print "Hierarchy level exists"
                subsys = None
                for bla in divided[levelabove[0]]:
                    print '---assign subs---'
                    print divided[levelabove[0]]
                    name = bla.name.rsplit('/',1)[1]
                    if bla.getType() == 'SubSystem' and name == levelabove[1]:
                        subsys = bla
                        break
                # we found the subsystem, now we have to add the relationship
                for b in blocklist:
                    if not b.getType() in self.portStubs:
                        if lhs:
                            toadd = PreContainsBlock(b,subsys)
                            toadd.parameters[Himesis.Constants.MT_LABEL] = str(int(b.getParameters()[Himesis.Constants.MT_LABEL]) + int(subsys.getParameters()[Himesis.Constants.MT_LABEL])*100000000)
                            blocks.append(toadd)
                        elif not lhs:
                            toadd = PostContainsBlock(b,subsys)
                            toadd.parameters[Himesis.Constants.MT_LABEL] = str(int(b.getParameters()[Himesis.Constants.MT_LABEL]) + int(subsys.getParameters()[Himesis.Constants.MT_LABEL])*100000000)
                            blocks.append(toadd)
            else:
                print "Hierarchy level at top"
                # these are top level blocks:
                # create a subsystem:
                subsys = None
                if lhs:
                    subsys = self.createPreBlockTopSubSystem()
                else:
                    subsys = self.createPostBlockTopSubSystem()
                blocks.append(subsys)
                for b in blocklist:
                    if not b.getType() in self.portStubs:
                        if lhs :
                            toadd = PreContainsBlock(b,subsys)
                            toadd.parameters[Himesis.Constants.MT_LABEL] = str(int(b.getParameters()[Himesis.Constants.MT_LABEL]) + int(subsys.getParameters()[Himesis.Constants.MT_LABEL])*100000000)
                            blocks.append(toadd)
                        elif not lhs and not b.getType() in self.portStubs:
                            toadd = PostContainsBlock(b,subsys)
                            toadd.parameters[Himesis.Constants.MT_LABEL] = str(int(b.getParameters()[Himesis.Constants.MT_LABEL]) + int(subsys.getParameters()[Himesis.Constants.MT_LABEL])*100000000)
                            blocks.append(toadd)
        # Do the Ports:
        for block in blocks:
            if not block.getType() in self.portStubs:
                parameters = block.getParameters()
                label = int(parameters[Himesis.Constants.MT_LABEL])
                block._id = nodeCounter
                nodeCounter += 1
                nodes.append(block)
                if not isinstance(block, PostContainsBlock) and not isinstance(block, PreContainsBlock):
                    for inport in block.inports.values():
                        inport._id = nodeCounter
                        #Assign unique label to port!
                        if self.existsAnInport(inport) is None:
                            inport.parameters[Himesis.Constants.MT_LABEL] = str(label *100 + int(inport.name))
                        else:
                            inport.parameters[Himesis.Constants.MT_LABEL] = str(self.existsAnInport(inport).getParameters()[Himesis.Constants.MT_LABEL])
                        nodeCounter += 1
                        nodes.append(inport)
                    for outport in block.outports.values():
                        outport._id = nodeCounter
                        if self.existsAnOutport(outport) is None:
                            outport.parameters[Himesis.Constants.MT_LABEL] = str( label * 100 + 50 + int(outport.name))
                        else:
                            outport.parameters[Himesis.Constants.MT_LABEL] = str(self.existsAnOutport(outport).getParameters()[Himesis.Constants.MT_LABEL])
                        nodeCounter +=1
                        nodes.append(outport)
        return nodes

    def doLHS(self):
        print '---LHS---'
        for block in self.LHS:
            print block.getType()
            print block.getParameters()
        nodes = self.getAllNodes(self.LHS, True)
        self.LHSHimesis = HimesisPreConditionPatternLHS(name=self.name + 'LHS', num_nodes=len(nodes))
        NAC_names = []
        for i in range(len(self.NACs)):
            NAC_names.append(self.name + 'NAC' + str(i))
        self.LHSHimesis.NACs = NAC_names
        self.LHSHimesis[Himesis.Constants.META_MODEL] = ['Simulink']  # the meta-model type name
        self.LHSHimesis["name"] = ""
        for node in nodes:
            self.LHSHimesis.vs[node._id][Himesis.Constants.META_MODEL] = TypeMapperLHS[node.getType()]   # the meta-model type element
            self.pre_label_MM_mapping[node.getParameters()[Himesis.Constants.MT_LABEL]] = TypeMapperLHS[node.getType()].replace(Himesis.Constants.MT_PRECOND_PREFIX,'')
            self.LHSHimesis.vs[node._id][Himesis.Constants.MT_DIRTY] = False
            #self.LHSHimesis.vs[node._id][Himesis.Constants.MT_PIVOT_IN] = ''
            #self.LHSHimesis.vs[node._id][Himesis.Constants.MT_PIVOT_OUT] = ''
            if TypeMapperLHS[node.getType()] == 'MT_pre__AbstractBlock':
                self.LHSHimesis.vs[node._id][Himesis.Constants.MT_SUBTYPE_MATCH] = True
                self.LHSHimesis.vs[node._id][Himesis.Constants.MT_SUBTYPES] = getPreSubTypes()
            else:
                self.LHSHimesis.vs[node._id][Himesis.Constants.MT_SUBTYPE_MATCH] = False
                self.LHSHimesis.vs[node._id][Himesis.Constants.MT_SUBTYPES] = ''
            parameters = node.getParameters()
            for k,v in parameters.iteritems():
                self.LHSHimesis.vs[node._id][k] = v
        # the connections between ports and blocks: Special case on the 2 ports for connection to other blocks TODO enable and trigger
        for block in self.LHS:
            if not block.getType() in self.portStubs and not isinstance(block,PreContainsBlock):
                for inport in block.inports.values():
                    blockportvertex = self.LHSHimesis.add_node()
                    self.LHSHimesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = Himesis.Constants.MT_PRECOND_PREFIX + S2HConstants.BLOCK_INPORT_RELATION
                    self.LHSHimesis.vs[blockportvertex][Himesis.Constants.MT_LABEL] = str(int(block.getParameters()[Himesis.Constants.MT_LABEL])*10000000000 + int(inport.parameters[Himesis.Constants.MT_LABEL]))
                    self.pre_label_MM_mapping[self.LHSHimesis.vs[blockportvertex][Himesis.Constants.MT_LABEL]] = S2HConstants.BLOCK_INPORT_RELATION
                    self.LHSHimesis.add_edge(block._id, blockportvertex)
                    self.LHSHimesis.add_edge(blockportvertex,inport._id)
                for outport in block.outports.values():
                    blockportvertex = self.LHSHimesis.add_node()
                    self.LHSHimesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = Himesis.Constants.MT_PRECOND_PREFIX + S2HConstants.BLOCK_OUTPORT_RELATION
                    self.LHSHimesis.vs[blockportvertex][Himesis.Constants.MT_LABEL] = str(int(block.getParameters()[Himesis.Constants.MT_LABEL])*10000000000 + int(outport.parameters[Himesis.Constants.MT_LABEL]))
                    self.pre_label_MM_mapping[self.LHSHimesis.vs[blockportvertex][Himesis.Constants.MT_LABEL]] = S2HConstants.BLOCK_OUTPORT_RELATION
                    self.LHSHimesis.add_edge(block._id, blockportvertex)
                    self.LHSHimesis.add_edge(blockportvertex,outport._id)
        #between ports and ports:
        # loop over all outputports and create the link:
        for node in nodes:
            # set the hierarchy level:
            if isinstance(node,PreContainsBlock):
                print node.block.name
                print node.subsystem.name
                self.LHSHimesis.add_edge(node.subsystem._id, node._id)
                self.LHSHimesis.add_edge(node._id, node.block._id)
            # do the connection between in and outports. Create the relation,
            if node.getType() == 'Port_Output' and node.line is not None:
                line = node.line
                print line
                # lookup the line:
                theLineRecord = self.connections[line][INPORT]
                for inport in theLineRecord:
                    if hasattr(inport.port, '_id'):
                        # add the connection to here
                        conid = self.LHSHimesis.add_node()
                        self.LHSHimesis.vs[conid][Himesis.Constants.META_MODEL] = Himesis.Constants.MT_PRECOND_PREFIX+S2HConstants.PORT2PORT_RELATION
                        self.LHSHimesis.vs[conid][Himesis.Constants.MT_LABEL] = str(int(self.LHSHimesis.vs[inport.port._id][Himesis.Constants.MT_LABEL])*10000+int(self.LHSHimesis.vs[node._id][Himesis.Constants.MT_LABEL]))
                        self.pre_label_MM_mapping[self.LHSHimesis.vs[conid][Himesis.Constants.MT_LABEL]] = S2HConstants.PORT2PORT_RELATION # no need to add and then replace the pre_condition_pattern MT_PRECOND_PREFIX
                        self.LHSHimesis.add_edge(node._id, conid)
                        self.LHSHimesis.add_edge(conid, inport.port._id)
        #compile:
        self.LHSHimesis.compile(self.path)

    def doRHS(self):
        print '---RHS---'
        for block in self.RHS:
            print block.getType()
            print block.getParameters()
        nodes = self.getAllNodes(self.RHS, False)
        self.RHSHimesis = HimesisPostConditionPattern(name=self.name + 'RHS', num_nodes=len(nodes))
        self.RHSHimesis.pre = self.LHSHimesis.name
        self.RHSHimesis[Himesis.Constants.META_MODEL] = ['Simulink']  # the meta-model type name
        self.RHSHimesis["name"] = ""
        for node in nodes:
            print "********************************"
            # set a parameter to the real value of the port
            print node.getType()
            if node.getType() in ['Port_Input','Port_Output']: #TODO if the port exists in the LHS, return attr_value
                node.parameters[Himesis.Constants.MT_POSTCOND_PREFIX+'Name'] = 'return ' + str(node.name)
            self.RHSHimesis.vs[node._id][Himesis.Constants.META_MODEL] = TypeMapperRHs[node.getType()]
            # parameters
            parameters = node.getParameters()
            for k,v in parameters.iteritems():
                print k
                print v
                self.RHSHimesis.vs[node._id][k] = v
            #self.RHSHimesis.vs[node._id][Himesis.Constants.MT_PIVOT_OUT] = ''
        for block in self.RHS:
            if not block.getType() in self.portStubs and not isinstance(block,PostContainsBlock): #this if os obsolete ?
                for inport in block.inports.values():
                    #self.RHSHimesis.add_edge(block._id, inport._id)
                    blockportvertex = self.RHSHimesis.add_node()
                    self.RHSHimesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = Himesis.Constants.MT_POSTCOND_PREFIX + S2HConstants.BLOCK_INPORT_RELATION
                    self.RHSHimesis.vs[blockportvertex][Himesis.Constants.MT_LABEL] = str(int(block.getParameters()[Himesis.Constants.MT_LABEL])*10000000000 + int(inport.parameters[Himesis.Constants.MT_LABEL]))
                    self.RHSHimesis.add_edge(block._id, blockportvertex)
                    self.RHSHimesis.add_edge(blockportvertex,inport._id)
                for outport in block.outports.values():
                    #self.RHSHimesis.add_edge(block._id, outport._id)
                    blockportvertex = self.RHSHimesis.add_node()
                    self.RHSHimesis.vs[blockportvertex][Himesis.Constants.META_MODEL] = Himesis.Constants.MT_POSTCOND_PREFIX + S2HConstants.BLOCK_OUTPORT_RELATION
                    self.RHSHimesis.vs[blockportvertex][Himesis.Constants.MT_LABEL] = str(int(block.getParameters()[Himesis.Constants.MT_LABEL])*10000000000 + int(outport.parameters[Himesis.Constants.MT_LABEL]))
                    self.RHSHimesis.add_edge(block._id, blockportvertex)
                    self.RHSHimesis.add_edge(blockportvertex,outport._id)
        for node in nodes:
            # do the hierarchy
            if isinstance(node,PostContainsBlock):
                self.RHSHimesis.add_edge(node.subsystem._id, node._id)
                self.RHSHimesis.add_edge(node._id, node.block._id)
            if node.getType() == 'Port_Output' and node.line is not None:
                line = node.line
                print line
                # lookup the line:
                theLineRecord = self.connections[line][INPORT]
                for inport in theLineRecord:
                    if hasattr(inport.port, '_id'):
                        # add the connection to here
                        conid = self.RHSHimesis.add_node()
                        self.RHSHimesis.vs[conid][Himesis.Constants.META_MODEL] = Himesis.Constants.MT_POSTCOND_PREFIX+S2HConstants.PORT2PORT_RELATION
                        self.RHSHimesis.vs[conid][Himesis.Constants.MT_LABEL] = str(int(self.RHSHimesis.vs[inport.port._id][Himesis.Constants.MT_LABEL])*10000+int(self.RHSHimesis.vs[node._id][Himesis.Constants.MT_LABEL]))
                        self.RHSHimesis.add_edge(node._id, conid)
                        self.RHSHimesis.add_edge(conid, inport.port._id)
        self.RHSHimesis.compile(self.path, self.pre_label_MM_mapping)

    def doNAC(self):
        pass

class SimulinkTransformationToHimesis(object):

    def __init__(self, name, path, mh, outpath = './temp/'):
        self.name = name
        self.path = path
        self.mh = mh
        self.outpath = outpath


    def doSchedule(self, name, path, blocks, contable):
        for block in blocks:
            print block
        print "----= Schedule =----"
        file_path = path
        if os.path.isfile(file_path):
            file_path = os.path.dirname(file_path)
        if not os.path.isdir(file_path):
            e = IOError(2, 'Output path does not exist')
            e.filename = file_path
            raise e
        # open file:
        theFile = open(path +'/T_'+name+'.py', 'w')
        #Imports:
        theFile.write('from Server.TCore.t_core.messages import Packet' + os.linesep)
        theFile.write('from Server.TCore.t_core.composer import Composer' + os.linesep)
        theFile.write('from Server.TCore.tc_python.frule import FRule' + os.linesep)
        theFile.write('from Server.TCore.tc_python.arule import ARule' + os.linesep)
        theFile.write('from Server.TCore.tc_python.srule import SRule' + os.linesep)
        # do Imports of LHS and RHS blocks:
        for block in blocks:
            if block.getType() == 'SubSystem':
                theName = 'H%s%s' % (name[0].capitalize(), name[1:])
                theFile.write('from '+theName+'_'+block.name+'LHS import '+theName+'_'+block.name+'LHS'+os.linesep)
                theFile.write('from '+theName+'_'+block.name+'RHS import '+theName+'_'+block.name+'RHS'+os.linesep)
        theFile.write(os.linesep)

        for block in blocks:
            if block.getType() == 'SubSystem':
                theFile.write('class '+ block.name+'(Composer):'+os.linesep)
                theFile.write('    def __init__(self):'+os.linesep)
                if block.getType() == 'SubSystem':
                    theName = 'H%s%s' % (name[0].capitalize(), name[1:])
                    if 'ARULE' in block.name:
                        theFile.write('        self.rule = ARule('+theName+'_'+block.name+'LHS(), '+theName+'_'+block.name+'RHS())'+os.linesep)
                    elif 'FRULE' in block.name:
                        theFile.write('        self.rule = FRule('+theName+'_'+block.name+'LHS(), '+theName+'_'+block.name+'RHS())'+os.linesep)
                    elif 'SRULE' in block.name:
                        theFile.write('        self.rule = SRule('+theName+'_'+block.name+'LHS(), '+theName+'_'+block.name+'RHS())'+os.linesep)
                theFile.write(os.linesep)
                theFile.write('    def packet_in(self, packet):' + os.linesep)
                theFile.write("         return self.rule.packet_in(packet)" + os.linesep + os.linesep)
        # go over the blocks and add the onSuccess things
        #now order, look for the start:
        orderstring = 'transOrder = {'
        for block in blocks:
            if block.getType() == 'SubSystem':
                print block.outports.keys()
                for v in block.outports.values():
                    print v.line
                orderstring+= "\""+block.name+"\"" + ':['

                if 1 in block.outports:
                    onSuccessLine = block.outports[1].line
                    print onSuccessLine
                    if onSuccessLine is not None and onSuccessLine != "":
                        inpo = contable[onSuccessLine][INPORT]
                        for ipo in inpo:
                            if ipo.block.getType() == 'SubSystem' and len(ipo.block.name.split('/')) == 1:
                                orderstring+="\""+ipo.block.name+"\""+','
                                break

                    else:
                        orderstring+='None,'
                if 2 in block.outports:
                    onFailure = block.outports[2].line
                    print onFailure
                    if onFailure is not None and onFailure != "":
                        inpo = contable[onFailure][INPORT]
                        for ipo in inpo:
                            if ipo.block.getType() == 'SubSystem' and len(ipo.block.name.split('/')) == 1:
                                orderstring+="\"" + ipo.block.name+"\""+','
                                break

                    else:
                        orderstring+='None,'
                if 3 in block.outports:
                    onNA = block.outports[3].line
                    print onNA
                    if onNA is not None and onNA != "":
                        inpo = contable[onNA][INPORT]
                        for ipo in inpo:
                            if ipo.block.getType() == 'SubSystem' and len(ipo.block.name.split('/')) == 1:
                                orderstring+="\"" + ipo.block.name +"\""
                                break

                    else:
                        orderstring+='None'
                orderstring+= '],'
        theFile.write(orderstring[:-1] + '}' + os.linesep)
        theFile.write("def packet_in(packet):"+ os.linesep)
        for block in blocks:
            if 'start' in block.name:
                linename = block.outports.values()[0].line
                print linename
                startBlocks = contable[linename][INPORT][0].block
                theFile.write("    current = \"" + startBlocks.name +"\""+ os.linesep)
                theFile.write("    while current is not None:"+ os.linesep)
                theFile.write("        exec(\"trans = \" + current + \"()\")"+ os.linesep)
                theFile.write("        exec(\"packet = trans.packet_in(packet)\")"+ os.linesep)
                theFile.write("        packet.clear_state()" + os.linesep)
                theFile.write("        if trans.rule.is_success:"+ os.linesep)
                theFile.write("            current = transOrder[current][0]"+ os.linesep)
                theFile.write("        elif not trans.rule.is_success:"+ os.linesep)
                theFile.write("            current = transOrder[current][2]"+ os.linesep)
                theFile.write("        else:"+ os.linesep)
                theFile.write("            current = transOrder[current][1]"+ os.linesep)
        theFile.write("    return packet"+ os.linesep+ os.linesep)
        theFile.close()
        print "----=End Schedule=----"

    def SimulinkTransformationModelToHimesis(self):

        parser = ParseModel(self.name, self.mh)
        blocks = parser.blocks
        connections = parser.c

        scheduleBlocks = []
        rules = {}
        for block in blocks:
            fullPathSplited = block.fullPath.split('/')
            if len(fullPathSplited) == 1:
                pass
            elif len(fullPathSplited) == 2:
                scheduleBlocks.append(block)
                if not fullPathSplited[1] in rules:
                    rules[fullPathSplited[1]] = TransfromationRule(fullPathSplited[1], self.outpath, connections.conTable)
            elif len(fullPathSplited) == 3:
                pass
            else:
                # if not yet exists in rules:
                if not fullPathSplited[1] in rules:
                    rules[fullPathSplited[1]] = TransfromationRule(fullPathSplited[0]+'_'+fullPathSplited[1], self.outpath, connections.conTable)
                # if LHS add to LHS, RHS, add to RHS, etc
                if 'LHS' in fullPathSplited[2]:
                    rules[fullPathSplited[1]].LHS.append(block)
                elif 'NAC' in fullPathSplited[2]:
                    rules[fullPathSplited[1]].NACs.append(block)
                elif  'RHS' in fullPathSplited[2]:
                    rules[fullPathSplited[1]].RHS.append(block)

        self.doSchedule(self.name,self.outpath,scheduleBlocks, connections.conTable)
        print rules
        for k,v in rules.iteritems():
            v.doLHS()
            v.doRHS()
        self.mh.closeWithoutSave(self.name)


