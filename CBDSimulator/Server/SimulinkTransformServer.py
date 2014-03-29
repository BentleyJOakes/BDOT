import SocketServer
import sys
import time
from Server.Core.MatlabHelper import MatlabHelper
from Server.Core.SimulinkExporter import SimulinkExporter
from Server.Core.SimulinkModelToHimesis import SimulinkModelToHimesis
from Server.Core.SimulinkTransformationToTCore import SimulinkTransformationToHimesis
from Server.TCore.core.himesis import Himesis
from Server.TCore.t_core.messages import Packet

__author__ = 'jdenil'

HOST = 'localhost'
PORT = 9999
POOLSIZE = 1


class SingleTCPHandler(SocketServer.StreamRequestHandler):
    """
    Thread to handle the request of a client. The protocol is Simple]
    Client connects
    Server gets a MATLAB helper from the pool of helpers
    Server Tx RDY
    Client response is a string: path;model;transformation\n
    Server responds OK
    Server executes transformation
    Server releases the helper to the pool
    Server Tx finished
    """
    def handle(self):
        """
        Handle the request. It should contain the directory, model name and tranformation name.
        The handle will make a Himesis of the model
        The handle will make a Himesis of the rules and a schedule
        The handle will execute the transformation
        The handle will export the transformed model to Simulink
        @return: None
        """
        sys.stdout.write( "started thread")
        self.mh =  self.server.getFromPool()
        self.wfile.write('RDY')
        data = self.rfile.readline().rstrip('\n')
        self.wfile.write('OK')
        sys.stdout.write(data)
        path,model,transformation = data.split(';')
        self.mh.chDir(path)
        # Model to Himesis
        modelToHimesis = SimulinkModelToHimesis(self.mh,model,path)
        modelToHimesis.SimulinkModelToHimesis()
        # Transfornation to T-Core
        transformationToHimesis = SimulinkTransformationToHimesis(transformation,path,self.mh)
        transformationToHimesis.SimulinkTransformationModelToHimesis()
        # Execute the Transformation
        exec("from Server.temp."+ Himesis.standardize_name(model) + " import "+ Himesis.standardize_name(model))
        exec("import Server.temp.T_" + transformation)
        packet = Packet()
        exec("packet.graph = "+ Himesis.standardize_name(model) + "()")
        exec('packet = Server.temp.T_'+ transformation +'.packet_in(packet)')
        #export:
        simulinkExport = SimulinkExporter(model,self.mh,packet.graph)
        simulinkExport.exportSimulink()
        self.wfile.write('finished')
    def finish(self):
        '''
        release the EngMat back to the pool for reuse
        @return: None
        '''
        self.server.returnToPool(self.mh)


class SimulinkServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    """
    Server class to accepts connections from clients
    """
    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address, requesthandlerClass):
        """
        Constructor, creates a pool of MATLAB helpers
        @param server_address: the address where the server will listen
        @param requesthandlerClass: The class to handle the request, separate thread
        @return: None
        """
        SocketServer.TCPServer.__init__(self,server_address,requesthandlerClass)
        self.pool = [MatlabHelper() for i in range(POOLSIZE)]
        self.initdir = self.pool[0].getCurrentDir()
        print self.initdir
        print 'ready'

    def getFromPool(self):
        """
        Get a worker from the pool of worker if there is a worker available
        @return: a member of the pool
        """
        if len(self.pool) > 0:
            return self.pool.pop()
        else:
            raise Exception('Oops, the pool was empty and a thread is requesting a connection to the so... This is wrong')

    def returnToPool(self, engmat):
        """
        Returns a helper to the pool
        @param engmat: the helper
        @return: None
        """
        print "Worker is ready for some more work"
        engmat.chDir(self.initdir)
        self.pool.append(engmat)

    def verify_request(self, request, client_address):
        """
        Check if a helper is available in the pool upon request. If no helper is available, deny the request
        @param request: the request
        @param client_address: the incoming address of the client
        @return:
        """
        if len(self.pool) > 0:
            print "request granted, thank you come again"
            return True
        else:
            print "request denied, all our operators are busy at the moment, try again later "
            return False

#if __name__ == "main":
server = SimulinkServer((HOST,PORT), SingleTCPHandler)
try:
    server.serve_forever()
except:
    sys.exit(0)