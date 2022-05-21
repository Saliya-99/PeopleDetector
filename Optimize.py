import numpy as np
import Sigmoid
import Predict

def Optimize(numOfiter,alpha,X,Y,w,b):
    costs = np.zeros((1, numOfiter))
    for i in range(numOfiter):
        m = X.shape[1]
        A = Sigmoid.sigmoid(w @ X.T + b)
        '''A1 = A
        A[A==0] = 10**-15
        B = 1-A1
        B[B==0] = 10**-15'''
        #cost = (-1 / m) * (np.dot(Y, np.log(A).T) + np.dot((1 - Y), np.log(1 - A).T))
        Yhat = A
        loss = 1. / m * np.square(Yhat - Y).sum()
        dy_pred = 1. / m * (2.0 * (Yhat - Y))

        dw = dy_pred @ X
        db = dy_pred.sum(axis=0) * 1
        w = w - alpha * dw
        b = b - alpha * db
        costs[0, i] = loss
    return w, b, costs
