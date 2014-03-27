from InvokeSo import InvokeSharedObject
from Server.Core import InvokeSo

__author__ = 'jdenil'

from ctypes import *

class Buffer:
    def __init__(self, buffersize):
        self.buffer = create_string_buffer('',size=buffersize)
        self.length = buffersize

'''
Instantiate this only once per thread!!!! It contains the reference to the shared object
'''

class EngMatAccess:
    def __init__(self, buffersize = 128):
        self.so = InvokeSharedObject()
        self.engine = self.so.engOpen(None)
        self.buffer = Buffer(buffersize)
        self.resultBuffer = False
        self.bufferSize = buffersize
        self.bufferingActive = True
        self.so.engOutputBuffer(self.engine, self.buffer)
        self.so.engSetVisible(self.engine,True)
        
        self.print_commands = False

    def close(self):
        self.so.engClose(self.engine)
        self.engine = None
        self.buffer = None

    def evaluate(self, expression, *args):
        return self.evaluateInternal(expression, *args)

    def evaluateInternal(self, expression, *args):
        self.resetLastError()
        command = expression.format(*args)
        
        if self.print_commands:
            print "command tx: " + command
            
        ret = self.so.engEvalString(self.engine, command)
        err = self.getLastError()
        if err is not None and err.__len__() >0:
            print "Wrong command: " + expression.format(*args)
            print err
            return 1
        return ret

    def resetLastError(self):
        self.so.engEvalString(self.engine, "lasterror('reset')")

    def getLastError(self):
        self.so.engEvalString(self.engine, "err = lasterror; err = err.message")
        return self.getString("err")

    def evaluateAsString(self, expression, *args):
        if self.so.engEvalString(self.engine, expression.format(*args)) == 0:
            return self.buffer.buffer.value
        else:
            return None

    def getMatrix(self, name):
        aa = self.so.engGetVariable(self.engine, name)
        if aa is None:
            return None
        else:
            return Matrix(aa,self.so)

    def getString(self, name):
        ptr = self.so.engGetVariable(self.engine,name)
        if ptr is None:
            return None
        length = self.so.mxGetN(ptr)
        if length == 0:
            return None
        ptr = self.so.mxGetData(ptr)
        str = string_at(ptr, length*2)
        #print len(str)
        str = str.decode("utf-16")
        #print len(str)
        #print str
        return str

    def getValueType(self, name):
        ptr = self.so.engGetVariable(self.engine, name)
        return self.so.mxGetClassID(ptr)

    def getElementCount(self, name):
        ptr = self.so.engGetVariable(self.engine, name)
        return self.so.mxGetN(ptr) * self.so.mxGetM(ptr)


class Matrix:
    def __init__(self, pointer, so):
        self.max = pointer
        self.so = so

    def asMatrix(self):
        fromArray = self.max
        so = self.so
        dataPtr = so.mxGetData(fromArray) # this returns a void pointer so cast to double in this case
        rows = so.mxGetM(fromArray)
        cols = so.mxGetN(fromArray)
        type = so.mxGetClassID(fromArray)
        toArrayType = c_double * (rows * cols)
        toArray = toArrayType()
        if type == InvokeSo.DOUBLE:
            memmove(toArray, dataPtr, rows * cols * sizeof(c_double))
            matrix = []
            while toArray != []:
                matrix.append(toArray[:cols])
                toArray = toArray[3:]
            return matrix
        else:
            return None

    def asVector(self):
        fromArray = self.max
        so = self.so
        dataPtr = so.mxGetData(fromArray) # this returns a void pointer so cast to double in this case
        rows = so.mxGetM(fromArray)
        cols = so.mxGetN(fromArray)
        type = so.mxGetClassID(fromArray)
        toArrayType = c_double * (rows * cols)
        toArray = toArrayType()
        #print rows
        #print cols
        #print so.mxGetData(fromArray)
        if type == InvokeSo.DOUBLE:
            memmove(toArray, dataPtr, rows * cols * sizeof(c_double))
            #print toArray[0]
            return toArray
        else:
            return None


class MatrixDescription:
    def __init__(self, pointer, so):
        if pointer is not None:
            self.rows = so.mxGetM(pointer)
            self.cols = so.mxGetN(pointer)
            self.type = so.mxGetClassID(pointer)
            self.name = so.mxGetName(pointer)
