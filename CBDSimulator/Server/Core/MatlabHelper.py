
import pdb
from Server.Core import InvokeSo
from Server.Core.EngMatLabLib import EngMatAccess

__author__ = 'jdenil'



class MatLabFieldType:
    String = 0
    Real = 1
    Enum = 2
    Ports = 3
    Rectangle = 4
    Boolean = 5
    Matrix = 6
    List = 7
    Int = 8
    Unknown = 9
    Object = 10
    Handle = 11

    def __init__(self, type):
        self.type = type
        #self.defaultValue=defaultValue
        #self.readonly = readonly

class MatlabHelper:
    def __init__(self):
        """
        Constructor, opens Simulink
        @return:
        """
        self.mat = EngMatAccess()
        self.mat.evaluate("load_system simulink")

    def loadSystem(self,name):
        self.mat.evaluate('load_system {0}', name)

    def chDir(self,fullPath):
        self.mat.evaluate("chdir '{0}'", fullPath)

    def openSystem(self,name):
        self.mat.evaluate("load_system '{0}'", name)

    def saveSystem(self,name):
        self.mat.evaluate("save_system('{0}',[],'OverwriteIfChangedOnDisk',true)", name)

    def closeSystem(self,name):
        self.mat.evaluate("close_system '{0}'", name)

    def closeWithoutSave(self,name):
        self.mat.evaluate("bdclose '{0}'", name)

    def createSystem(self, name):
        self.mat.evaluate("new_system '{0}'", name)
        self.mat.evaluate("save_system '{0}'", name)
        self.mat.evaluate("close_system '{0}'", name)

    def createSubSystem(self, name, model):
        self.mat.evaluate("new_system '{0}', '{1}'", name, model)

    def openLibrary(self):
        self.mat.evaluate("libbrowse('create')")

    def endLib(self):
        self.mat.close()

    def getCurrentDir(self):
        self.mat.evaluate("pwd")
        return self.mat.getString("ans")


    def addBlock(self, fullType, fullpath):
        """
        stores block handle in the newblock:
        theBlock = add_block('Simulink/Commonly Used Blocks/Product', 'testCreate/prd2')
        """
        b = self.mat.evaluate("newblock = add_block('{0}', '{1}')", fullType, fullpath)
        return b


    def setParameterOnNewCreatedBlock(self, param, value):
        """
        add parameter to the previous created block
        set_param(theBlock, 'Position', '[235 297 265 328]')
        """
        b = self.mat.evaluate("set_param(newblock, '{0}', '{1}')", param, value)
        return b

    def getPositionOfNew(self):
        b  = self.mat.evaluate("pos = get_param(newblock, 'Position')")
        return self.mat.getMatrix("pos").asVector()
    """
    add parameter to a block with path:
     set_param('testCreate/int', 'Position', '[135 197 165 228]')
    """
    def setParameter(self, fullpath, param, value):
        b = self.mat.evaluate("set_param('{0}', '{1}', '{2}')", fullpath,param, value)
        return b
    """
    add_line('testCreate', 'gain/1', 'ud/1','autorouting','on' )
    """
    def addConnection(self, model, outFullPath, outPortNr, inFullPath, inPortNr):
        b = self.mat.evaluate("add_line('{0}','{1}/{2}','{3}/{4}', 'autorouting','on')", model, outFullPath, outPortNr, inFullPath, inPortNr)

    def deleteBlock(self, system, path):
        parts = path.split('/')
        name = parts[len(parts) - 1]
        c = ""
        if len(parts) < 2 :
            c = ""
        else:
            parts = parts[:-1]
            for p in parts:
                c += p + '/'
            c = c[:-1]
        self.mat.evaluate("delete_block('{0}{1}/{2}')", system, c, name)

    def getLinePoints(self, system, lineName):
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

        self.openSystem(system)
        self.mat.evaluate("r = sfroot")
        self.mat.evaluate("active = r.find('-depth', 1, 'Name', '{0}')", system)
        self.mat.evaluate("lines_h = active.find('Type', 'line', 'Name', '{0}')", lineName)
        self.mat.evaluate("seg_nrs = size(lines_h)")
        size = self.mat.getMatrix("seg_nrs").asMatrix()[0][0]
        print size
        self.mat.evaluate("get(lines_h,'Points')")
        points =  self.mat.getMatrix("ans").asVector()
        for e in points:
            print e

    def renameAllLines(self, system):
        self.openSystem(system)
        self.mat.evaluate("r = sfroot")
        self.mat.evaluate("active = r.find('-depth', 1, 'Name', '{0}')", system)
        self.mat.evaluate("lines = active.find('Type', 'line')")
        self.mat.evaluate("cnt = size(lines)")
        cnt = int(self.mat.getMatrix("cnt").asMatrix()[0][0])
        print cnt
        for i in range(1,cnt+1):
            self.mat.evaluate("line = lines({0})", i)
            self.mat.evaluate("line.Name")
            name =  self.mat.getString("ans")
            if name is None or name == "":
                self.mat.evaluate("line.Name = 'line{0}'", i)
            else:
                self.mat.evaluate("line.Name = '{0}_line{1}'",name,i)
        # ok we have unique names for our lines now so now we can use the port handles to get the line for connections

    def deleteContentofSubsys(self,subsys):
        self.mat.evaluate("Simulink.SubSystem.deleteContents('{0}');", subsys)

    def findElementAndStoreIntoBlk(self, system, blockPath):
        print "blockpath: " + blockPath
        parts = blockPath.split('/')
        blockName = parts[len(parts) - 1]
        print "blockname: " + blockName
        c = ""
        if len(parts) < 2 :
            c = ""
        else:
            parts = parts[:-1]
            for p in parts:
                c += p + '/'
            c = c[:-1]
        expectedFullName = "{0}{1}/{2}".format(system, c, blockName)
        print "expectedFullName: "+expectedFullName

        self.mat.evaluate("r = sfroot")
        self.mat.evaluate("active = r.find('-depth', 1, 'Name', '{0}')", system)
        if blockName == "":
            self.mat.evaluate("blks = active.find('Type', 'block')")
        else:
            self.mat.evaluate("blks = active.find('Type', 'block', 'Name', '{0}')", blockName)
        self.mat.evaluate("cnt = size(blks)")
        cnt = int(self.mat.getMatrix("cnt").asMatrix()[0][0])
        print cnt
        for i in range(1,cnt+1):
            self.mat.evaluate("fullName = blks({0}).getFullName()", i)
            fullName = self.mat.getString("fullName")
            print fullName
            if (fullName == expectedFullName):
                self.mat.evaluate("blk = blks({0})", i)

    def getBlocks(self, system):
        self.openSystem(system)
        self.mat.evaluate("r = sfroot")
        self.mat.evaluate("active = r.find('-depth', 1, 'Name', '{0}')", system)
        self.mat.evaluate("blks = active.find('Type', 'block')")
        return self.processBlksNodeArray(system)

    def getContainedBlocks(self, system, containerPath):
        self.openSystem(system)
        self.findElementAndStoreIntoBlk(system, containerPath)
        self.mat.evaluate("blks = blk.getChildren()")
        return self.processBlksNodeArray(system)

    def getContainedBlocksTopLevel(self, system):
        self.openSystem(system)
        self.mat.evaluate("r = sfroot")
        self.mat.evaluate("active = r.find('-depth', 1, 'Name', '{0}')", system)
        self.mat.evaluate("blks = active.find('Type', 'block')")
        return self.processBlksNodeArray(system)

    def processBlksNodeArray(self,system):
        ret = {}
        self.mat.evaluate("cnt = size(blks)")
        cnt = int(self.mat.getMatrix("cnt").asMatrix()[0][0])
        for i in range(1,cnt+1):
            self.mat.evaluate("blks({0}).Type", i)
            if self.mat.getString("ans") != "block":
                continue
            if (self.getParentReferenceBlock("blks({0})", i)) != "":
                continue
            type = self.getReferenceBlock("blks({0})", i)
            if type is None or type == "":
                type = self.mat.evaluate("blks({0}).BlockType", i)
                type = self.mat.getString("ans")
                type = type.strip()
            self.mat.evaluate("blks({0}).getFullName", i)
            fullname = self.mat.getString("ans")
            print fullname
            name = fullname[len(system) + 1:]
            print name
            ret[name] = (type.replace(".", "/"),fullname)
        return ret

    def getParameter(self, fullPath, parameter):
        err = self.mat.evaluate("val = get_param('{0}', '{1}')", fullPath, parameter)
        if not err:
            type = self.mat.getValueType("val")
            if type == InvokeSo.CHAR:
                return self.mat.getString("val")
            elif type == InvokeSo.DOUBLE:
                return self.mat.getMatrix("val").asMatrix()
            else:
                return self.mat.getString("val")
        else:
            return None

    def getReferenceBlock(self, varName, *args):
        varName = varName.format(*args)
        self.mat.evaluate("{0}.ReferenceBlock", varName)
        referenceBlock = self.mat.getString("ans")
        if referenceBlock is not None:
            referenceBlock = referenceBlock.strip()
        return referenceBlock

    def getParentReferenceBlock(self, varName, *args):
        varName = varName.format(*args)
        parentName = self.mat.evaluate("{0}.getParent", varName)
        parentName = self.mat.getString("ans")
        print "parentName: " + str(parentName)
        if parentName is None or "Simulink.BlockDiagram" in parentName :
            return ""
        self.mat.evaluate("{0}.getParent().ReferenceBlock", varName)
        referenceBlock = self.mat.getString("ans").strip()
        return referenceBlock

    def getLibraryTree(self):
        root = LibraryNode("root", None)
        self.mat.evaluate("level0 = libbrowse('create'); cnt = size(level0); cnt = cnt(1);")
        self.traverse(0,root)
        return root

    def traverse(self, level, parent):
        self.mat.evaluate("cnt = size(level{0}); cnt = cnt(1);", level)
        cnt = self.mat.getMatrix("cnt")
        cnt = int(cnt.asVector()[0])
        print "cnt " + str(cnt)
        for i in range(1,cnt+1):
            self.mat.evaluate("act = level{0}{{{1}}}", level, i)
            if self.mat.getValueType("act") == InvokeSo.CHAR:
                LibraryLeaf(self.mat.getString("act"), parent)
            else:
                self.mat.evaluate("t = level{0}({1});t = t{{1}};name=t(1);name=name{{1}};sub=t(2);level{2}=sub{{1}};first=level{2}{{1}};", level ,i, level+1)
                name = self.mat.getString("name")
                self.traverse(level+1, LibraryNode(name,parent))

    def getCommonProperties(self, fullpath, blockType):
        self.mat.evaluate("blockType = get_param('{0}', 'BlockType');" ,fullpath)
        blockType = self.mat.getString("blockType")
        self.mat.evaluate("fields = get_param('{0}', 'ObjectParameters');fns = fieldnames(fields);", fullpath)
        cnt = self.mat.getElementCount("fns")
        diction = {}
        for i in range(1,cnt+1):
            self.mat.evaluate("fns{{{0}}}", i)
            fieldName = self.mat.getString("ans")
            self.mat.evaluate("fields." + fieldName + ".Type")
            type = self.mat.getString("ans")
            print type
            #self.mat.evaluate("fields." + fieldName + ".Attributes")
            #attributes = self.mat.getString("ans")
            #print attributes
            #isReadOnly = "read-only" in attributes or "never-save" in attributes
            #self.mat.evaluate("get_param('{0}', '{1}')", fullpath, fieldName)
            if type == "string":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.String)
            elif type == "real":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Real)
            elif type == "int":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Int)
            elif type == "enum":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Enum)
            elif type == "ports":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Ports)
            elif type == "rectangle":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Rectangle)
            elif type == "boolean":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Boolean)
            elif type == "matrix":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Matrix)
            elif type == "list":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.List)
            elif type == "object":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Object)
            elif type == "handle vector":
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Handle)
            else:
                diction[fieldName] = MatLabFieldType(MatLabFieldType.Unknown)
        #print diction
        return diction

class LibraryNode:
    def __init__(self, name, parent):
        self.name = name
        self.nodes = []
        self.parent = parent
        if parent is not None:
            parent.nodes.append(self)
        self.fullPath = ""
        if parent is not None:
            self.fullPath=parent.fullPath + "/" + name.strip('/')
            #print self.fullPath

    def __str__(self):
        return self.name

    def getPath(self):
        return self.fullPath[1:]

class LibraryLeaf(LibraryNode):
    def __init__(self, name, parent, helper):
        LibraryNode.__init__(self, name, parent)
        self.parameters = None
        self.customParameters = None
        self.blockType = ""
        self.helper = helper

    def getParameters(self):
        if self.parameters is None:
            self.parameters = self.FillProps()
        return self.parameters

    def FillProps(self):
        return self.helper.getCommonProperties(self.getPath(), self.blockType)