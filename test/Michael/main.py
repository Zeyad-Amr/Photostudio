# from contour import circle_contour,greedy_contour,cv2,contour_area,contour_perimeter,draw_contour
import contour as cn
import cv2
import numpy as np

parametersDict = {
    'apple3.jpeg':{
        'xShift':10,
        'yShift':50,
        'radius':100,
        'iterations':25
    },
    'circle.jpeg':{
        'xShift':0,
        'yShift':50,
        'radius':90,
        'iterations':35
    },
    'BlackApple_1.jpg':{
        'xShift':40,
        'yShift':30,
        'radius':100,
        'iterations':25
    },
    'Convex-Polygon-1.png':{
        'xShift':10,
        'yShift':50,
        'radius':110,
        'iterations':35
    }
}

# active contour
original_image = cv2.imread("images/circle.jpeg")
name = ''

points = 60
sz = original_image.shape
x_cooridinates = np.zeros(points, dtype=np.int32)
y_cooridinates = np.zeros(points, dtype=np.int32)
x_cooridinates,y_cooridinates = cn.circle_contour((sz[0] // 2+parametersDict[name]['xShift'], sz[1] // 2+parametersDict[name]['yShift']), parametersDict[name]['radius'], points, x_cooridinates, y_cooridinates)
# greedy_contour(original_image, 100, 2, 0.9, 20, x_cooridinates, y_cooridinates, points, 5)
x_cooridinates,y_cooridinates = cn.greedy_contour(original_image, parametersDict[name]['iterations'], 1, 2, 5, x_cooridinates, y_cooridinates, points, 11, True)
# external_energy(original_image)
chaincode,normalisedToRotation,normalisedToStartingPoint = cn.getChainCode(x_cooridinates,y_cooridinates)
print(normalisedToStartingPoint)
print(f"contour area : {cn.contour_area(len(x_cooridinates),x_cooridinates,y_cooridinates)} m^2")

# calculate area of the contour
perimeter = cn.contour_perimeter(x_cooridinates, y_cooridinates, points)
# area = contour_area(points, x_cooridinates, y_cooridinates)
img = cn.draw_contour(original_image,points,x_cooridinates,y_cooridinates)

print(f"contour perimeter : {perimeter} m")