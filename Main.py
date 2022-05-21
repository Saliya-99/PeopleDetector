import numpy as np
import ImageDataLoad
import InitializeParameters
import InputLabels
import ImgPreprocess
import Sigmoid
import Predict
import Optimize
import cv2
import matplotlib.pyplot as plt

img_size = 32
X_orig = ImageDataLoad.LoadImages(73, img_size)/255
Y = InputLabels.inputLabels()
X = ImgPreprocess.preprocessed(X_orig)

w, b = InitializeParameters.Initialize(X.shape[1])
w_trained, b_trained, costs = Optimize.Optimize(500, 0.1, X, Y, w, b)
# ## w and b are trained to get the optimal values

# imgNew = cv2.imread("Images/21.jpg")
# imgNew = cv2.resize(imgNew,(300,300))/255
w1 = np.reshape(w_trained[0,:],(img_size,img_size,3))
img = (w1 - np.amin(w1))/(np.amax(w1) - np.amin(w1))
print(img)
fig,ax = plt.subplots(1,1,figsize = (10,10))
ax.imshow(img)
a = Predict.predict(X, w_trained, b_trained).T
res = []
y1 = Y.T#reshape((len(X_orig),2))
for l,k in enumerate(a):
    j = [0,0]
    if k[0] -k[1]<0:
        j = [0,1]
    elif k[0] -k[1]>0:
        j = [1,0]

    res.append(y1[l]-j)


print(res)
fig,ax = plt.subplots(1,1,figsize = (10,10))
costs = np.squeeze(costs)
ax.plot(costs)


im2 = cv2.imread('im6.jpg')
im2 = cv2.resize(im2,(img_size,img_size))
im2 = np.array([im2])
X = ImgPreprocess.preprocessed(im2)

a2 = Sigmoid.sigmoid(w @ X.T+b_trained[:,0:1].reshape((2,1)))
print(a2.T)
plt.show()