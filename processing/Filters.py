import cv2
from matplotlib import pyplot as plt
import numpy as np
import random

""" 
# TODO:
1. Add additive noise to the image
- Uniform
- Gaussian
- Salt and Pepper 

2. Filter the noisy image using the following low pass filter: (Smooting)
- Average
- Gaussian
- Median

3. Detect the edges of the image using the following masks: 
- Sobel
- Roberts
- Prewitt
- Canny

"""


class Filters:
    def __init__(self, image):
        self.image = image

    def salt_pepper_noise(image, range):
        row, col = image.shape
        salt_pepper = np.random.random(row, col)*255
        pepper = salt_pepper < 0+range
        salt = salt_pepper > 255-range
        image[pepper] = 0
        image[salt] = 255
        return image

    def gaussian_noise(image, range):
        row, col = image.shape
        mean = 0
        var = range
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col))
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
        return noisy

    def uniform_noise(image, range):
        row, col = image.shape
        low = -range
        high = range
        noise = np.random.uniform(low, high, (row, col))
        noisy = image + noise
        return noisy
