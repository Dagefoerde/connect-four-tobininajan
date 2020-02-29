import numpy

class Linear:

    def __init__(self, w, b):
        self.w = w
        self.b = b

    def call(self, inputs):
        return numpy.matmul(inputs, self.w) + self.b
