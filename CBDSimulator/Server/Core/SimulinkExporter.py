from Server.Core.SimulinkLibItems import SimulinkTypes, CommonParameters, S2HConstants
from Server.TCore.core.himesis import Himesis

__author__ = 'jdenil'

from CreateSimulinkModel import SimulinkCreator



class SimulinkExporter(object):
    def __init__(self, model, mh, himesis):
        self.name = model
        self.mh = mh
        self.himesis = himesis

    def getBlock(self,port):
        # watch out inports have multiple in connections:
        incoming = port.predecessors()
        for innode in incoming:
        
            if innode[Himesis.Constants.META_MODEL] in [S2HConstants.BLOCK_INPORT_RELATION,S2HConstants.BLOCK_OUTPORT_RELATION,S2HConstants.BLOCK_ENABLE_RELATION,S2HConstants.BLOCK_TRIGGER_RELATION]:
                the_blocks = innode.predecessors()
                # should be only one... but to be sure:
                for proposedblock in the_blocks:
                    if proposedblock[Himesis.Constants.META_MODEL] in SimulinkTypes:
                        return proposedblock
        return None

    #### Add emulated hierarchy here: Work from top level to bottom

    def getSinglePredOfType(self, vs,type):
        listOfpred = vs.predecessors()
        for pred in listOfpred:
            if pred[Himesis.Constants.META_MODEL] == type:
                return pred
        return None

    def getNextHier(self,vs):
        pred = self.getSinglePredOfType(vs, '__Contains__')
        if pred is None:
            return None
        pred = self.getSinglePredOfType(pred,'SubSystem')
        return pred

    def getFullPathList(self,vs):
        rv = []
        currentNode = vs
        while(True):
            currentNode = self.getNextHier(currentNode)
            if currentNode is None:
                return rv
            else:
                rv.insert(0,currentNode['Name'])

    def exportSimulink(self):
        print "Starting export to Simulink MDL"
        himesisgraph = self.himesis
        #print himesisgraph.vcount()
        self.name+="_export"
        blocksPerHierLevel = {}
        # Create the true fullname used for hierarchy:
        for vs in himesisgraph.vs:
        
            if vs[Himesis.Constants.META_MODEL] in SimulinkTypes:
                path = self.getFullPathList(vs)
                if len(path) in blocksPerHierLevel:
                    blocksPerHierLevel[len(path)].append(vs)
                else:
                    blocksPerHierLevel[len(path)] = [vs]
                theStringPath = "/"
                for p in path[1:]:
                    theStringPath+="/"+p
                vs['SimulinkFullName'] = theStringPath[1:]+'/'+vs['Name']
                vs['SimulinkFullName'] = vs['SimulinkFullName'][1:]
                print("Simulink Full Name: " + vs['SimulinkFullName'])
                
                
        creator = SimulinkCreator(self.name,self.mh)
        
        for key in sorted(blocksPerHierLevel.iterkeys()):
            nodes = blocksPerHierLevel[key]
            if key !=0:
                for node in nodes:
                    if node[Himesis.Constants.META_MODEL] in SimulinkTypes:
                        fullname,parameters = SimulinkTypes[node[Himesis.Constants.META_MODEL]]
                        creator.createBlock(node['SimulinkFullName'], fullname)
                        if node['Position'] is not None:
                            creator.addPositionToNewBlock(node['Position'])
                        for parameter in parameters:
                            if node[parameter[0]] is not None:
                                creator.addParameterToNewBlock(parameter[1],node[parameter[0]])
                        for parameter in CommonParameters:
                            if node[parameter[0]] is not None:
                                creator.addParameterToNewBlock(parameter[0], node[parameter[0]])
     
        
        for es in himesisgraph.es:
        
            source = self.himesis.vs[es.source]
            target = self.himesis.vs[es.target]
            
            if source[Himesis.Constants.META_MODEL] == 'Port_Output' and target[Himesis.Constants.META_MODEL] == '__Relation__' :
                thesuccessors = target.successors()
                # there can only be one successor of a relation and that is the port where we need to connect to:
                target=thesuccessors[0]
                if source[Himesis.Constants.META_MODEL] == 'Port_Output' and target[Himesis.Constants.META_MODEL] == 'Port_Input':
                    sourceBlock = self.getBlock(source)
                    targetBlock = self.getBlock(target)                    
                    if sourceBlock is not None and targetBlock is not None:
                        print '1' + sourceBlock['SimulinkFullName']+'/'+str(source['Name'])
                        print '1' + targetBlock['SimulinkFullName']+ '/'+str(target['Name'])
                        creator.addConnection(sourceBlock['SimulinkFullName'], source['Name'], targetBlock['SimulinkFullName'], target['Name'])
                elif source[Himesis.Constants.META_MODEL] == 'Port_Output' and target[Himesis.Constants.META_MODEL] == 'Port_4':
                    sourceBlock = self.getBlock(source)
                    targetBlock = self.getBlock(target)
                    if sourceBlock is not None and targetBlock is not None:
                        print '2' + sourceBlock['SimulinkFullName']+'/'+str(source['Name'])
                        print '2' + targetBlock['SimulinkFullName']+ '/'+str(target['Name'])
                        creator.addConnection(sourceBlock['SimulinkFullName'], source['Name'], targetBlock['SimulinkFullName'], 'Trigger')
                elif source[Himesis.Constants.META_MODEL] == 'Port_Output' and target[Himesis.Constants.META_MODEL] == 'Port_3':
                    sourceBlock = self.getBlock(source)
                    targetBlock = self.getBlock(target)
                    if sourceBlock is not None and targetBlock is not None:
                        print '3' + sourceBlock['SimulinkFullName']+'/'+str(source['Name'])
                        print '3' + targetBlock['SimulinkFullName']+ '/'+str(target['Name'])
                        creator.addConnection(sourceBlock['SimulinkFullName'], source['Name'], targetBlock['SimulinkFullName'], 'Enable')

        creator.saveAndClose()
