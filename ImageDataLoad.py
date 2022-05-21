import numpy as np
import cv2

def LoadImages(numOfimages,pixSize):

    imgArray = np.zeros((numOfimages,pixSize,pixSize,3))
    for i in range(1,numOfimages+1):
        imgName = str(i) + ".jpg"
        img = cv2.imread("Images/"+imgName)
        img = cv2.resize(img,(pixSize,pixSize))
        #img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #img = cv2.Canny(img,0.1,0.1)
        imgArray[i-1] = img
        #cv2.waitKey(10)
    return imgArray


