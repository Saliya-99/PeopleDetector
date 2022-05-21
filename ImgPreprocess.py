import numpy as np
import ImageDataLoad



def preprocessed(dataSet):
    x_preprocessed = dataSet.reshape(dataSet.shape[0], dataSet.shape[1] * dataSet.shape[2] * dataSet.shape[3])
    return x_preprocessed

