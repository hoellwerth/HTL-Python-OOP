import math

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def angle(self):
        angle = math.atan(self.imag / self.real)
        return (angle / math.pi) * 180
    
    def phasor(self):
        return math.sqrt(math.pow(self.real, 2) + math.pow(self.imag, 2))
