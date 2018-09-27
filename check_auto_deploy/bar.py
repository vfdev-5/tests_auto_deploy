
from enum import Enum

# external dependency: numpy
import numpy as np


class Events(Enum):
    EPOCH_STARTED = "epoch_started"
    EPOCH_COMPLETED = "epoch_completed"
    STARTED = "started"
    COMPLETED = "completed"
    ITERATION_STARTED = "iteration_started"
    ITERATION_COMPLETED = "iteration_completed"
    EXCEPTION_RAISED = "exception_raised"


class Bar(object):

    def __init__(self):
        print("Bar class initialization")
        self.c = np.ones(100)
        self.d = "another test"

    def compute(self, x):
        return self.c * x
