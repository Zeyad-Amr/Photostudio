# from contour import circle_contour,greedy_contour,cv2,contour_area,contour_perimeter,draw_contour
import contour as cn
import cv2
import numpy as np


# active contour
original_image = cv2.imread("images/circle.jpeg")
points = 60
sz = original_image.shape
x_cooridinates = np.zeros(points, dtype=np.int32)
y_cooridinates = np.zeros(points, dtype=np.int32)
x_cooridinates,y_cooridinates = cn.circle_contour((sz[0] // 2, sz[1] // 2+50), 90, points, x_cooridinates, y_cooridinates)
# greedy_contour(original_image, 100, 2, 0.9, 20, x_cooridinates, y_cooridinates, points, 5)
x_cooridinates,y_cooridinates = cn.greedy_contour(original_image, 30, 1, 2, 100, x_cooridinates, y_cooridinates, points, 11, True)
# external_energy(original_image)
chaincode,normalisedToRotation,normalisedToStartingPoint = cn.getChainCode(x_cooridinates,y_cooridinates)
print(normalisedToStartingPoint)
print(f"contour area : {cn.contour_area(len(x_cooridinates),x_cooridinates,y_cooridinates)} m^2")

# calculate area of the contour
perimeter = cn.contour_perimeter(x_cooridinates, y_cooridinates, points)
# area = contour_area(points, x_cooridinates, y_cooridinates)
cn.draw_contour(original_image,points,x_cooridinates,y_cooridinates)
print(f"contour perimeter : {perimeter} m")