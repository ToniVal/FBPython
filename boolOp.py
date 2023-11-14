class boolOperators(): # Lets have different boolean operators listed here.
   
    def bInOut(in1): # Basic INPUT/OUTPUT operator, this if for making the I/O defination easier.

        out = in1

        return out
   
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
    
    def bSR(b_set, b_reset): # Set Reset latch

        if b_set == True and b_reset == False and prevState == False:
            nextState = True
        elif b_set == False and b_reset == True and prevState == True:
            nextState = False
        else:
            nextState = prevState

        prevState = nextState
        return nextState