class Quadrature:

    def __init__(self, func, a, b):
        self.func = func #the lambda function you want to integrate
        self.a = a #lower limit
        self.b = b #upper limit
        self.s = 0 #current value of integral

    def next(self, n, x): #n is the current level of refinement

        if n == 1:
            self.s = 0.5 * (self.b - self.a) * (self.func(a) + self.func(b))
            return self.s
        else:
            for it in range(n - 1):
                it = it << 1
            
            tnm = it
            dell = (self.b - self.a) / tnm #the spacing of the points to be added
            x = self.a + 0.5 * dell

            for _ in range(0, it, self.dell):
                sum += self.func(x)

            self.s = 0.5 * (self.s + (self.b - self.a) * sum / tnm)

            return self.s
                 


        

