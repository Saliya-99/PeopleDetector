import numpy as np


def Initialize(features):
    std = 1e-2
    w = std * np.random.randn(2, features)
    b = np.zeros((2,1))
    return w,b