from MatlabHelper import MatlabHelper
import sys
from Server.Core.SimulinkLibItems import SimulinkBlocks, CommonParameters

"""
Make sure your matlab so path is set: export LD_LIBRARY_PATH=/usr/local/pkgs/MATLAB/R2012a/bin/glnx86/ for example on the ubuntu of cs.mcgill.ca
"""

__author__ = 'jdenil'


INPORT = 1
OUTPORT = 2
ENABLED = 3
TRIGGER = 4
STATE = 5
LCONN = 6
RCONN = 7
IFACTION = 8

'''
to get line segments: TODO
>> lines_h = find_system('test_hier', 'SearchDepth', 1, 'FindAll', 'on', 'Type', 'line', 'Name', 'line2')

lines_h =

   1.9480e+03

>> get_param(lines_h,'Points')

ans =

   180   125
   255   125
   255    65
   340    65
'''

class Port(object):
    def __init__(self, name, type, line, parent, parentfullpath):
        self.name = name
        self.type = type
        self.line = line
        self.id = -1
        self.x = -1
        self.y = -1
        self.parent = parent
        self.parameters = {}
        self.fullPath = parentfullpath

    def __str__(self):
        return str(self.name)

    def getType(self):
        if self.type == INPORT:
            return "Port_Input"
        elif self.type == OUTPORT:
            return "Port_Output"
        else:
            return "Port_" + str(self.type)

    def getParameters(self):
        return self.parameters

class EndPoint(object):
    def __init__(self, block, port):
        self.block = block
        self.port = port

    def __str__(self):
        return str(self.block.name) + "/" + str(self.port)

    def __repr__(self):
        return str(self.block.name) + "/" + str(self.port)

class Connections(object):
    def __init__(self, helper):
        self.conTable = {}
        self.helper = helper

    def add(self, lineName, block, port, type):
        if lineName in self.conTable:
            line = self.conTable[lineName]
            if type in line:
                self.conTable[lineName][type].append(EndPoint(block, port))
            else:
                self.conTable[lineName][type] = [EndPoint(block, port)]
        else:
            self.conTable[lineName] = {}
            self.conTable[lineName][type] = [EndPoint(block, port)]

    def buildConnectionTable(self, blockList):
        for block in blockList:
            for inportname,inport in block.inports.iteritems():
                if inport.line is not None:
                    self.add(inport.line, block, inport, INPORT)
            for outportname, outport in block.outports.iteritems():
                if outport.line is not None:
                    self.add(outport.line, block, outport, OUTPORT)
            for triggerportname,triggerport in block.trigger.iteritems():
                if triggerport.line is not None:
                    self.add(triggerport.line, block, triggerport, INPORT)
            for enablename,enableport in block.enabled.iteritems():
                if enableport.line is not None:
                    self.add(enableport.line, block, enableport, INPORT)

    def getLineSegments(self, systemName):
        m = self.helper
        for k in self.conTable.iterkeys():
            m.getLinePoints(systemName,k)

class Block(object):
    def __init__(self, name, fullPath, type, helper):
        self.name = " ".join(name.split())
        self.fullPath = " ".join(fullPath.split())
        self.type = " ".join(type.split())
        self.Position = []
        self.id = -1
        self.x = -1
        self.y = -1
        self.inports = {}
        self.outports = {}
        self.enabled = {}
        self.parameters = {}
        self.trigger = {}
        self.helper = helper

    def __str__(self):
        return self.name

    def getType(self):
        return self.type

    def getLocation(self):
        m = self.helper
        self.Position = m.getParameter(self.fullPath, "Position")[0]
        for coor in self.Position:
            coor = int(coor)
        print self.Position


    def getPorts(self):
        """
        Gets all the ports of a block / subsystem, fills the datastructure
        @return: None
        """
        m = self.helper
        self.portsraw = m.getParameter(self.fullPath, "Ports")
        print self.portsraw
        m.mat.evaluate("porthandle = get_param('{0}', 'PortHandles')",self.fullPath)
        m.mat.evaluate("inports = porthandle.Inport")
        for i in range(1,int(self.portsraw[0][0]+1)):
            m.mat.evaluate("lname = ''")
            m.mat.evaluate("lh = get_param(porthandle.Inport({0}), 'line')",i)
            err = m.mat.evaluate("lname = get_param(lh,'Name')")
            if not err:
                linename = None
                linename = m.mat.getString("lname")
                self.inports[i] = Port(i,INPORT,linename, self, self.fullPath)
            else:
                self.inports[i] = Port(i,INPORT,None, self, self.fullPath)
        for i in range(1,int(self.portsraw[0][1]+1)):
            m.mat.evaluate("lname = ''")
            m.mat.evaluate("lh = get_param(porthandle.Outport({0}), 'line')",i)
            err = m.mat.evaluate("lname = get_param(lh,'Name')")
            if not err:
                linename = None
                linename = m.mat.getString("lname")
                self.outports[i] = Port(i,OUTPORT,linename, self, self.fullPath)
            else:
                self.outports[i] = Port(i,OUTPORT,None, self, self.fullPath)
        for i in range(1,int(self.portsraw[0][2]+1)):
            m.mat.evaluate("lname = ''")
            m.mat.evaluate("lh = get_param(porthandle.Enable({0}), 'line')",i)
            err = m.mat.evaluate("lname = get_param(lh,'Name')")
            if not err:
                linename = None
                linename = m.mat.getString("lname")
                theport = Port(i,ENABLED,linename, self, self.fullPath)
                self.enabled[i] = theport
            else:
                self.enabled[i] = Port(i,ENABLED,None, self, self.fullPath)
        for i in range(1,int(self.portsraw[0][3]+1)):
            m.mat.evaluate("lname = ''")
            m.mat.evaluate("lh = get_param(porthandle.Trigger({0}), 'line')",i)
            err = m.mat.evaluate("lname = get_param(lh,'Name')")
            if not err:
                linename = None
                linename = m.mat.getString("lname")
                theport = Port(i,TRIGGER,linename, self, self.fullPath)
                self.trigger[i] = theport
            else:
                self.trigger[i] = Port(i,TRIGGER,None, self, self.fullPath)


    def getAllParameters(self):
        self.getLocation()
        self.getPorts()
        #print self.inports
        #print self.outports

        # do the common properties

        for simeq,attrType in CommonParameters:
            theVal = self.helper.getParameter(self.fullPath, simeq)
            try:
                if theVal is None:
                    pass
                elif attrType == 'string':
                    theVal = str(theVal)
                elif attrType == 'integer':
                    theVal = int(theVal)
                elif attrType == 'float':
                    theVal = float(theVal)
                elif attrType == 'list':
                    rv = []
                    theVal = theVal[1:-1]
                    split = theVal.split(' ')
                    for val in split:
                        rv.append(float(val))
                    theVal = rv
            except ValueError:
                theVal = str(theVal)
            self.parameters[simeq] = theVal

        # do the block specific parameters

        if self.type in SimulinkBlocks:
            parameters = SimulinkBlocks[self.type]
            for param,simeq,attrType in parameters:
                theVal = self.helper.getParameter(self.fullPath, simeq)
                try:
                    if theVal is None:
                        pass
                    elif attrType == 'string':
                        theVal = str(theVal)
                    elif attrType == 'integer':
                        theVal = int(theVal)
                    elif attrType == 'float':
                        theVal = float(theVal)
                    elif attrType == 'list':
                        rv = []
                        theVal = theVal[1:-1]
                        split = theVal.split(' ')
                        for val in split:
                            rv.append(float(val))
                        theVal = rv
                except ValueError:
                    theVal = str(theVal)
                self.parameters[param] = theVal


    def getParameters(self):
        return self.parameters

class SimulinkParser(object):
    def __init__(self, modelname, helper):
        self.modelname = modelname
        #self.fullPath = fullPath
        self.matlabHelper = helper
        #self.matlabHelper.chDir(fullPath) no longer needed since this is done by the worker
        self.matlabHelper.renameAllLines(self.modelname)

    def parseBlocks(self):
        blocks = self.matlabHelper.getContainedBlocksTopLevel(self.modelname)
        blocklist = []
        for name,v in blocks.iteritems():
            type,fullpath = v
            block = Block(name,fullpath,type,self.matlabHelper)
            block.getAllParameters()
            blocklist.append(block)
            print type
        return blocklist

class ParseModel(object):
    def __init__(self, modelname, mh):
        self.c = Connections(mh)
        theParser = SimulinkParser(modelname, mh)
        self.blocks = theParser.parseBlocks()
        self.c.buildConnectionTable(self.blocks)
        #self.c.getLineSegments(modelname)



