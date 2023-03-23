import math
import cv2
import numpy as np


class Detect:
    def __init__(self, img):
        self.img = img

    def getImg(self):
        return self.img
    
    
    def detect_lines(self, threshold,color= (255,0,0)):
        img = self.getImg()
        # detect edges using the Canny algorithm  
        src = cv2.Canny(img,50, 200, None, 3)
        diagonal = math.ceil(math.sqrt(src.shape[0] * src.shape[0] + src.shape[1] * src.shape[1]))
        # declare the accumulator matrix as zero matrix
        acc = np.zeros((2 * diagonal, 180), dtype=np.uint8)
        lines = []
        
        # find the location of edges
        rows, cols = np.nonzero(src)

        cos_theta = np.cos(np.radians(np.arange(-90, 90)))
        sin_theta = np.sin(np.radians(np.arange(-90, 90)))
        for row, col in zip(rows, cols):
            # calculate the hough transform for each edge
            r = np.round(col * cos_theta + row * sin_theta) 
            acc[r.astype(int), np.arange(180)] += 1

        for i in range(acc.shape[0]):
            for j in range(acc.shape[1]):
                if acc[i, j] >= threshold:
                    lines.append((i , j - 90))

        # draw the lines on the original image
        res = self.superimpose(lines, color)

        return res
        
    def superimpose(self, lines, color):
        img = self.getImg()
        src = np.copy(img)
        for i in range(len(lines)):
            r, theta = lines[i]
            pt1, pt2 = (0, 0), (0, 0)
            a, b = math.cos(math.radians(theta)), math.sin(math.radians(theta))
            x0, y0 = a * r, b * r
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(src, pt1, pt2, color, 1, cv2.LINE_AA)
        return src

