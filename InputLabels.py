import numpy as np

def inputLabels():
    Y = [1,1,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,
                  1,0,1,1,0,1,0,0,1,1,1,1,0,0,1,0,1,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,1]
    l1 = []
    for i in Y:
        num = int(not(i))
        l1.append([i,num])
    l1 = np.array(l1)
    Y = l1.T
    return Y

