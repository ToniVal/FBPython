class boolOperators(): # Lets have different boolean operators listed here.

    def bAnd(self, in1, in2): # Basic AND operation with 2 inputs, output and inverse output. 
        self.in1 = in1
        self.in2 = in2

        if self.in1 == True and self.in2 == True:
            out = True
        else:
            out = False
        
        return out