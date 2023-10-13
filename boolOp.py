class boolOperators(): # Lets have different boolean operators listed here.

    def bAnd(self, in1, in2): # Basic AND operation with 2 inputs and 1 output. 
        self.in1 = in1
        self.in2 = in2

        if self.in1 == True and self.in2 == True:
            out = True
        else:
            out = False
        
        return out
    
    def bOr(self, in1, in2): # Basic OR operation with 2 inputs and 1 output.
        self.in1 = in1
        self.in2 = in2

        if self.in1 == True and self.in2 == True:
            out = True
        else:
            out = False
        
        return out
    
    def bNot(self, in1): # Basic NOT operation with 1 input and 1 output.
        self.in1 = in1

        if self.in1 == True:
            out = False
        else:
            out = True
        
        return out