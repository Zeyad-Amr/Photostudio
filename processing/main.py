import Greyscale_operator
from Greyscale_operator import GrayScaleOperator

import Colored_operator
from Colored_operator import ColoredOperator

import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread('processing\lena.jpg',0)

imgOperator = GrayScaleOperator(img)
newImg =  imgOperator.applyGlobalThreshold(50)
cv2.imwrite('processing\localthreshold.jpg',newImg)

img = cv2.imread('processing\Red_Color.jpg')
imgOperator = ColoredOperator(img)
r,g,b = imgOperator.split()
print(r),print(g),print(b)


# plt.imshow(img,cmap='gray')