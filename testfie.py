'''s = input()[::-1]
q = int(input())
for i in range(q):
    p = input()[::-1]
    s1 = s[:]
    count = 0
    for k in range(len(p)):
        if p[k] in s1:
            idx = s1.index(p[k])
            s1 = s1[idx+1:]
            count += 1
        else:
            break
    print(count)'''
import numpy as np
from matplotlib import pyplot as plt

x = np.arange(-np.pi/2,np.pi/2,0.01)

y = np.zeros(x.shape)
a0 = (2/np.pi)*((np.pi**2/18)+0.5+((3**0.5)*np.pi/6))
print(a0)
n = 1000
for i in range(1,n+1):
    y += ((1/np.pi)*((np.sin((i+1)*np.pi/6)/(i+1))+(np.sin((i-1)*np.pi/6)/(i-1))) +((np.pi/6+3**0.5)*np.sin(i*np.pi/2)/(i*np.pi)) +
    ((np.pi/6-3**0.5)*np.sin(i*np.pi/6)/(i*np.pi))+np.cos(i*np.pi/2)/(i**2)-np.cos(i*np.pi/6)/(i**2))*np.cos(i*x)
   # print(y)


y += a0/2

plt.plot(x,y)


# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(-np.pi,np.pi,100)
# y = x
# plt.plot(x,y)
# plt.show()