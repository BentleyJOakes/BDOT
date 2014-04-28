from ctypes import *

# mxComplexity MatrixType
mxREAL=0
mxCOMPLEX=1
#Type of Matrix elements
#mxClassID

UNKNOWN=0
CELL=1
STRUCT=2
OBJECT=3
CHAR=4
SPARSE=5
DOUBLE=6
SINGLE=7
INT8=8
UINT8=9
INT16=10
UINT16=11
INT32=12
UINT32=13
INT64=14		# place holder - future enhancements
UINT64=15		#/* place holder - future enhancements */
FUNCTION=16
OPAQUE=17

class InvokeSharedObject:
    """
    Class to talk to MATLAB using the matlab shared libraries.
    This should be changed depending on the platform. TODO: Use os to make if, API remains
    """
    def __init__(self):
        """
        Constructor, initialize the connection with MATLAB
        @return:
        """
        self.libeng = cdll.LoadLibrary("libeng.so")
        self.libmx = cdll.LoadLibrary("libmx.so")
        self.libmat = cdll.LoadLibrary("libmat.so")

    def engOpen(self,startcmd):
        """
        Open connection with the shared library
        @param startcmd: Default None
        @return:
        """
        fun = self.libeng.engOpen
        fun.argtypes = [c_char_p]
        fun.restype = c_void_p
        return fun(startcmd)

    def engClose(self, pointer):
        """
        Close the connection with the shared lib
        @param pointer: the pointer ot the so
        @return:
        """
        fun = self.libeng.engClose
        fun.argtypes = [c_void_p]
        fun.restype = c_int
        return fun(pointer)

    def engEvalString(self, engine, cmd):
        """
        Evaluate command with engine
        @param engine: pointer to engine
        @param cmd: command string
        @return:
        """
        #print cmd
        #print type(cmd)
        #print len(cmd)
        fun = self.libeng.engEvalString
        fun.argtypes = [c_void_p, c_char_p]
        fun.restype = c_int
        cmd = create_string_buffer(cmd)
        #print cmd.raw
        #print repr(cmd.value)
        return fun(engine, cmd)

    def engOutputBuffer(self, engine, buffer):
        """
        Set the output buffer
        @param engine: the engine
        @param buffer: the buffer pointer
        @return:
        """
        fun = self.libeng.engOutputBuffer
        fun.argtypes = [c_void_p, c_char_p]
        fun.restype = c_int
        return fun(engine, buffer.buffer, buffer.length)

    def engSetVisible(self, engine, boolq):
        """
        Set the engine to visible
        @param engine: the engine
        @param boolq: boolean visible
        @return:
        """
        fun =self.libeng.engSetVisible
        fun.argtypes = [c_void_p, c_bool]
        fun.restype = c_int
        return fun(engine, boolq)

    def engIsVisible(self, engine):
        """
        Querry visibility
        @param engine: the engine
        @return:
        """
        fun = self.libeng.engIsVisible
        fun.argtypes = [c_void_p]
        fun.restype = c_int
        return fun(engine)

    def engPutVariable(self, engine, name, array):
        """
        set variable
        @param engine: engine
        @param name: name of var
        @param array: value
        @return:
        """
        fun = self.libeng.engPutVariable
        fun.argtypes = [c_void_p, c_char_p, c_void_p]
        return fun(engine, name, array)

    def engGetVariable(self, engine, name):
        """
        get variable
        @param engine: the engine
        @param name: var name
        @return: pointer to variable
        """
        fun = self.libeng.engGetVariable
        fun.argtypes = [c_void_p, c_char_p]
        fun.restype = c_void_p
        return fun(engine, name)

    def Type2ClassID(self, t):
        if(isinstance(t, c_ulong)):
            return UINT64
        elif(isinstance(t, c_long)):
            return INT64
        elif(isinstance(t, c_uint)):
            return UINT32
        elif(isinstance(t, c_int)):
            return INT32
        elif(isinstance(t, c_short)):
            return INT16
        elif(isinstance(t, c_ushort)):
            return UINT16
        elif(isinstance(t, c_ubyte)):
            return UINT8
        elif(isinstance(t, c_byte)):
            return INT8
        elif(isinstance(t, c_float)):
            return SINGLE
        elif(isinstance(t, c_double)):
            return DOUBLE
        else:
            return UNKNOWN

    def mxCreateDoubleMatrix(self, n, m, complexity):
        return self.libmx.mxCreateDoubleMatrix(n,m,complexity)

    def mxCreateNumericMatrix(self, n,m,classid, complexity):
        return self.libmx.mxCreateNumericMatrix(n, m, classid, complexity)

    def mxGetData(self, ptr):
        getdata = self.libmx.mxGetData
        getdata.argtypes = [c_void_p]
        getdata.restype = c_void_p
        return getdata(ptr)

    def mxGetN(self, ptr):
        fun = self.libmx.mxGetN
        fun.argtypes = [c_void_p]
        fun.restype = c_int
        return fun(ptr)

    def mxGetM(self, ptr):
        fun = self.libmx.mxGetM
        fun.argtypes = [c_void_p]
        fun.restype = c_int
        return fun(ptr)

    def mxGetClassID(self, ptr):
        fun = self.libmx.mxGetClassID
        fun.argtypes = [c_void_p]
        fun.restype = c_int
        return fun(ptr)

