class boolOperators(): # Lets have different boolean operators listed here.

    def bAnd(in1, in2): # Basic AND operation with 2 inputs and 1 output. 

        if in1 == True and in2 == True:
            out = True
        else:
            out = False
        
        return out
    
    def bOr(in1, in2): # Basic OR operation with 2 inputs and 1 output.

        if in1 == True or in2 == True:
            out = True
        else:
            out = False
        
        return out
    
    def bNot(in1): # Basic NOT operation with 1 input and 1 output.

        if in1 == True:
            out = False
        else:
            out = True
        
        return out