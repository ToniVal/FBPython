class arithmeticOperators(): # Basic arithmetic functions, probably the best way to operate with numbers is to convert all to float and carry the type through the operation.

    def numInOut(in1): # Number converter and type saver. incomp. //opType, in1, numOutType
        #if opType == "input":
        #    numInType = type(in1)
        #    out = float(in1)

        #if opType == "output":
        #    if numOutType == "<class 'int'>":
        #        out = int(in1)
        #    if numOutType == "<class 'float'>":
        #        out = float(in1)

        # ^^Do i need those^^

        out = in1

        return out, #numInType

    def numAdd(in1, in2):

        out = in1 + in2

        return out
    
    def numSub(in1, in2):

        out = in1 - in2

        return out
    
    def numMult(in1, in2):

        out = in1 * in2

        return out
    
    def numDivd(in1, in2):

        out = in1/in2

        return out
    