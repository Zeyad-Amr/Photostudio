# from Histograms import Histograms
# from Histograms import ColoredOperator
# from matplotlib import pyplot as plt
from Filters import Filters
from matplotlib import pyplot as plt

import cv2
# from matplotlib import pyplot as plt

img = cv2.imread('images/02.jpeg')
print(img)
# imgOperator = Histograms(img)
# newImg = imgOperator.getHistoGram()
# cv2.imwrite('../images/localthreshold.jpg', newImg)

# img = cv2.imread('../images/Red_Color.jpg')
# print(img.shape)
# imgOperator = ColoredOperator(img)
# r, g, b = imgOperator.split()
# print(r), print(g), print(b)

ffilter = Filters()
# new = ffilter.salt_pepper_noise(img, 10)
# new = ffilter.uniform_noise(new, 10)
# new = ffilter.gaussian_noise(new, 10)
# new = ffilter.average_filter(new, 3)
# new = ffilter.gaussian_filter(new, 3)
# new = ffilter.median_filter(new, 3)
# new = ffilter.sobel_filter(new)
# new = ffilter.prewitt_edge_detector(img)
# cv2.imshow('image', new)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray')
