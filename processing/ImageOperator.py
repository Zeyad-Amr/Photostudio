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
    def applyLocalThreshold(self,blockSize = 10, C = 5):
        inputImg = self.getImg()
        # if blockSize % 2 == 0:
        #     blockSize += 1
        
        output = np.zeros_like(inputImg)

        for x in range(inputImg.shape[0]):
            for y in range(inputImg.shape[1]):
                # Get the neighborhood around the pixel
                neighborhood = []
                for i in range(-blockSize // 2, blockSize // 2 + 1):
                    for j in range(-blockSize // 2, blockSize // 2 + 1):
                        # Check if the pixel is within the image boundaries
                        px = x + i
                        py = y + j
                        if px >= 0 and px < inputImg.shape[0] and py >= 0 and py < inputImg.shape[1]:
                            neighborhood.append(inputImg[px, py])
                
                # Compute the local threshold using the mean and constant C
                threshold = int(round(np.mean(neighborhood) - C))
                
                # Apply the threshold to the pixel
                if inputImg[x][y] >= threshold:
                    output[x][y] = 255
                else:
                    output[x][y] = 0

        return output