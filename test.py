import numpy as np
a = np.array([1.1,2,3,0,3]).reshape(1,5)
a[a == 0] = 0.01
print(a)