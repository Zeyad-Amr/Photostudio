import numpy as np
import Greyscale_operator
from Greyscale_operator import GrayScaleOperator

class ColoredOperator:
    
    def __init__(self,img):
        self.img = img
        r,g,b = self.split()
        self.red = r
        self.green = g
        self.blue = b
    def getImg(self):
        return self.img 
    def getRedFrame(self):
        return self.red
    def getGreenFrame(self):
        return self.green
    def getBlueFrame(self):
        return self.blue
    
    
    #splits the img to 3 frames r,g,b
    #the img must be colored
    def split(self):
        img = self.getImg()
        
        # determining width and height of original image
        w, h = img.shape[:2]
        
        # new Image dimension with 4 attribute in each pixel 
        r = np.zeros_like(img)
        g = np.zeros_like(img)
        b = np.zeros_like(img)
        print( w )
        print( h )
        
        for i in range(w):
            for j in range(h):
                # ratio of RGB will be between 0 and 1
                b[i][j]=(img[i][j][0])
                g[i][j]=(img[i][j][1])
                r[i][j]=(img[i][j][2])
        return r,g,b
    