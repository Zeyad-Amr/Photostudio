
from copy import deepcopy
import numpy as np


class Histograms:

    def __init__(self, img):
        self.img = img

    def getImg(self):
        return self.img

    def operateOn(self, img):
        self.img = img

    def equalize(self):
        img = self.getImg()
        histogram = self.getHistoGram(img)
        cumulativeSum = self.getCumSum(histogram)

        cumulativeSum /= cumulativeSum[-1]
        cumulativeSum *= 255
        cumulativeSum = cumulativeSum.astype('uint8')

        flattenedImg = self.flatten(img)
        newImg = cumulativeSum[flattenedImg]
        newImg = np.reshape(newImg, img.shape)

        return newImg

    def normalise(self):
        img = self.getImg()
        newImg = deepcopy(img)
        newImg = newImg / np.max(img) * 255

        return newImg

    def applyGlobalThreshold(self, threshold):
        newImg = self.getImg()

        newImg[newImg > threshold] = 255
        newImg[newImg != 255] = 0

        return newImg

    def applyLocalThreshold(self, blockSize=10, C=5):
        inputImg = self.getImg()

        output = np.zeros_like(inputImg)
        cumulative = getCumulative2d(inputImg)

        for x in range(inputImg.shape[0]):
            for y in range(inputImg.shape[1]):

                halfHeight = blockSize // 2

                neighborhoodSum, num = getSumAndNum(
                    cumulative, x + halfHeight, y + halfHeight, x - halfHeight, y - halfHeight)

                # Compute the local threshold using the mean and constant C
                threshold = int(round(neighborhoodSum / (num) - C))

                # Apply the threshold to the pixel
                if inputImg[x][y] >= threshold:
                    output[x][y] = 255
                else:
                    output[x][y] = 0

        return output

    # splits the img to 3 frames r,g,b
    # the img must be colored
    def split(self):
        img = self.getImg()

        # determining width and height of original image
        w, h = img.shape[:2]

        # new Image dimension with 4 attribute in each pixel
        r = np.zeros_like(img)
        g = np.zeros_like(img)
        b = np.zeros_like(img)
        print(w)
        print(h)

        for i in range(w):
            for j in range(h):
                # ratio of RGB will be between 0 and 1
                b[i][j] = (img[i][j][0])
                g[i][j] = (img[i][j][1])
                r[i][j] = (img[i][j][2])
        return r, g, b

    # takes 1darray and return its cumulative sum
    def getCumSum(self, arr):
        a = np.array(arr)
        b = []

        isFirstElement = True
        for i in a:
            if isFirstElement:
                b.append(a[0])
                isFirstElement = False
                continue
            b.append(b[-1] + i)

        b = np.array(b)
        return b

    # takes 2darray and returns 1d histogram array whose index represents
    # the intensity and the value at each index represents the frequency of that intennsity
    def getHistoGram(self, arr2d, bins=256):
        flattenedImage = self.flatten(arr2d)
        print(flattenedImage)

        # array with size of bins, set to zeros
        histogram = np.zeros(bins)

        # loop through pixels and sum up counts of pixels
        for pixel in flattenedImage:
            histogram[int(pixel)] += 1

        # return our final result
        return histogram

    # takes a 2darray and return it as just 1d.
    def flatten(self, arr2d):
        img = np.asarray(arr2d)
        img = img.flatten()
        return img


def getCumulative2d(img):

    w = img.shape[0]
    h = img.shape[1]
    # print(w, h)
    cumulative = np.zeros_like(img, dtype=np.uint32)
    cumulative[0][0] = img[0][0]
    for i in range(1, w):
        cumulative[i][0] = cumulative[i-1][0] + img[i][0]
    for i in range(1, h):
        cumulative[0][i] = cumulative[0][i-1] + img[0][i]
    for i in range(1, w):
        for j in range(1, h):
            cumulative[i][j] = cumulative[i-1][j] + \
                cumulative[i][j-1] - cumulative[i-1][j-1] + img[i][j]
    return cumulative


def getSumAndNum(cumulative, bottomRightX, bottomRightY, topLeftX, topLeftY):
    w = cumulative.shape[0]
    h = cumulative.shape[1]

    # make sure coordinates are inside the shape and if not let it be.
    bottomRightX = max(min(w-1, bottomRightX), 0)
    bottomRightY = max(min(h-1, bottomRightY), 0)
    topLeftX = max(min(w-1, topLeftX), 0)
    topLeftY = max(min(h-1, topLeftY), 0)

    bottomLeftX = bottomRightX
    bottomLeftY = topLeftY

    topRightX = topLeftX
    topRightY = bottomRightY

    # print(cumulative[bottomRightX][bottomRightY])
    blockSum = int(cumulative[bottomRightX][bottomRightY])
    if topRightX > 0:
        blockSum -= cumulative[topRightX-1][topRightY]
    if bottomLeftY > 0:
        blockSum -= cumulative[bottomLeftX][bottomLeftY-1]
    if topLeftX > 0 and topLeftY > 0:
        blockSum += cumulative[topLeftX-1][topLeftY-1]

    n = (bottomRightX-topRightX+1)*(bottomRightY-bottomLeftY+1)

    return blockSum, n


class ColoredOperator:

    def __init__(self, img):
        self.img = img
        r, g, b = self.split()
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

    # splits the img to 3 frames r,g,b
    # the img must be colored

    def split(self):
        img = self.getImg()

        # determining width and height of original image
        w, h = img.shape[:2]

        # new Image dimension with 4 attribute in each pixel
        r = np.zeros_like(img)
        g = np.zeros_like(img)
        b = np.zeros_like(img)
        print(w)
        print(h)

        for i in range(w):
            for j in range(h):
                # ratio of RGB will be between 0 and 1
                b[i][j] = (img[i][j][0])
                g[i][j] = (img[i][j][1])
                r[i][j] = (img[i][j][2])
        return r, g, b

    def grayScale(self):
        return self.getRedFrame() / 3 + self.getGreenFrame() / 3 + self.getBlueFrame() / 3
