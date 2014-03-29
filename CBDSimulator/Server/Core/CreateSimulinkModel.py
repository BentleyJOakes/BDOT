from Server.Core.MatlabHelper import MatlabHelper

__author__ = 'jdenil'


class SimulinkCreator(object):
    def __init__(self, modelname, helper, directory=None):
        self.modelName = modelname
        self.mat = helper
        print self.mat.getCurrentDir()
        if dir is not None or dir !="":
            self.mat.chDir(directory)
        print self.mat.getCurrentDir()
        self.mat.createSystem(modelname)
        self.mat.openSystem(modelname)

    def saveAndClose(self):
        self.mat.saveSystem(self.modelName)
        self.mat.closeSystem(self.modelName)

    """
    blockname: can be hierarchical, automatically adds the top level
    """
    def createBlock(self, blockname, type):
        self.mat.addBlock(type, self.modelName+"/"+blockname)
        if type == "Simulink/Commonly Used Blocks/Subsystem":
            self.mat.deleteContentofSubsys(self.modelName+'/'+blockname)

    def addParameterToNewBlock(self, parameter, value):
        self.mat.setParameterOnNewCreatedBlock(parameter,value)

    def addConnection(self, outFullPath, outPortNr, inFullPath, inPortNr):
        outpath = outFullPath.rsplit('/',1)
        intpath = inFullPath.rsplit('/',1)
        if len(outpath) > 1:
            self.mat.addConnection(self.modelName+'/'+outpath[0], outpath[1], outPortNr, intpath[1], inPortNr)
        else:
            self.mat.addConnection(self.modelName
                , outFullPath, outPortNr, inFullPath, inPortNr)

    def addPositionToNewBlock(self, position):
        if position is not None:
            self.mat.setParameterOnNewCreatedBlock('Position', "[{0} {1} {2} {3}]".format(int(position[0]),int(position[1]),int(position[2]),int(position[3])))
