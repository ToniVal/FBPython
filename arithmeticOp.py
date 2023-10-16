class arithmeticOperators(): # Basic arithmetic functions, probably the best way to operate with numbers is to convert all to float and carry the type through the operation.

    def numInOut(opType, in1, numOutType): # Number converter and type saver.
        if opType == "input":
            numInType = type(in1)
            out = float(in1)

        if opType == "output":
            if numOutType == "int":
                out = int(in1)
            if numOutType == "float":
                out = float(in1)

        return out, numInType
