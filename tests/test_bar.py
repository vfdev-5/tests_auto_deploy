
import numpy as np

from check_auto_deploy import Bar


def test_bar():

    bar = Bar()
    assert isinstance(bar.c, np.ndarray)
    assert bar.d == "another test"
