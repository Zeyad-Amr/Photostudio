import ImageOperator
from ImageOperator import ImageOperator
import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread('processing\lena.jpg',0)

imgOperator = ImageOperator(img)
newImg =  imgOperator.applyGlobalThreshold(100)
cv2.imwrite('processing\globalThreshold.jpg',newImg)


# plt.imshow(img,cmap='gray')