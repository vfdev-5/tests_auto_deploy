
# external dependency: numpy
import numpy as np


class Bar(object):

    def __init__(self):
        print("Bar class initialization")
        self.c = np.ones(100)
        self.d = "another test"

    def compute(self, x):
        return self.c * x
