import numpy as np

def getCumSum(arr):
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

def getHistoGram(arr2d,bins = 256):
    flattenedImage = flatten(arr2d)

    # array with size of bins, set to zeros
    histogram = np.zeros(bins)
    
    # loop through pixels and sum up counts of pixels
    for pixel in flattenedImage:
        histogram[pixel] += 1
    
    # return our final result
    return histogram

def flatten(arr2d):
    img = np.asarray(arr2d)
    img = img.flatten()
    return img