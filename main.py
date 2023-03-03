import ImageOperator
from ImageOperator import ImageOperator
import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg',0)

imgOperator = ImageOperator(img)
newImg =  imgOperator.normalise()
cv2.imwrite('normalised.jpg',newImg)


# plt.imshow(img,cmap='gray')