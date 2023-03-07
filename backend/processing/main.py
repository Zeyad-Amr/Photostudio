from Histograms import Histograms
from Histograms import ColoredOperator
# from matplotlib import pyplot as plt

import cv2
import numpy as np
# from matplotlib import pyplot as plt

img = cv2.imread('../images/lena.jpg', 0)

imgOperator = Histograms(img)
newImg = imgOperator.applyGlobalThreshold(50)
cv2.imwrite('../images/localthreshold.jpg', newImg)

img = cv2.imread('../images/Red_Color.jpg')
print(img.shape)
imgOperator = ColoredOperator(img)
r, g, b = imgOperator.split()
# print(r), print(g), print(b)


# plt.imshow(img, cmap='gray')
