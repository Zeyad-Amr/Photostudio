import ImageOperator
from ImageOperator import ImageOperator
import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread('processing\lena.jpg',0)

imgOperator = ImageOperator(img)
newImg =  imgOperator.applyLocalThreshold()
cv2.imwrite('processing\localthreshold.jpg',newImg)


# plt.imshow(img,cmap='gray')