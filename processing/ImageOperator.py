import tools as tl
from copy import deepcopy
import numpy as np

class ImageOperator:

    def __init__(self,img):
        self.img = img

    def getImg(self):
        return self.img
    
    def operateOn(self,img):
        self.img = img
    
    def equalize(self):
        img = self.getImg()  
        histogram = tl.getHistoGram(img)
        cumulativeSum = tl.getCumSum(histogram)

        cumulativeSum /= cumulativeSum[-1]
        cumulativeSum *= 255
        cumulativeSum = cumulativeSum.astype('uint8')
        
        flattenedImg = tl.flatten(img)
        newImg = cumulativeSum[flattenedImg]
        newImg = np.reshape(newImg,img.shape)

        return newImg
    
    def normalise(self):
        img = self.getImg()
        newImg =  deepcopy(img)
        rows = img.shape[0]
        columns = img.shape[1]
        for i in range(rows):
            for j in range(columns):
                newImg[i][j] = newImg[i][j]/(255) * 400

        return newImg
    def applyGlobalThreshold(self,threshold):
        newImg = self.getImg()
        
        newImg[newImg > threshold] = 255
        newImg[newImg != 255] = 0
        
        return newImg
