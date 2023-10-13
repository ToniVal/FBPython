class boolOperators(): # Lets have different boolean operators listed here.

    def bAnd(self, in1, in2, out, iout): # Basic AND operation with 2 inputs, output and inverse output. 
        self.in1 = in1
        self.in2 = in2
        self.out = out
        self.iout = iout

        if self.in1 == True and self.in2 == True:
            self.out = True
            self.iout = False
        else:
            self.out = False
            self.iout = True
        
        return self.out, self.iout