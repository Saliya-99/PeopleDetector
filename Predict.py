import numpy as np
import ImageDataLoad
import InitializeParameters
import InputLabels
import ImgPreprocess
import Sigmoid
import Optimize
import cv2

def predict(x, w, b):
    # x = x.reshape(x.shape[1]*x.shape[2]*x.shape[3], x.shape[0])

    yhat = Sigmoid.sigmoid(w @ x.T+b)

    return yhat
