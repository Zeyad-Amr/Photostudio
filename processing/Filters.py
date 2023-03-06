import cv2
from matplotlib import pyplot as plt
import numpy as np
import random

""" 
# TODO:
1. Add additive noise to the image
- For example: Uniform, Gaussian, Salt and Pepper

2. Filter the noisy image using the following low pass filter:
- Average, Gaussian, Median

3. Detect the edges of the image using the following masks: 
- Sobel, Roberts, Prewitt and Canny edge detection

"""


class Filters:
    def __init__(self, image):
        self.image = image

    def salt_pepper_noise(image):
        # Getting the dimensions of the image
        row, col = image.shape

        # Randomly pick some pixels in the
        # image for coloring them white
        # Pick a random number between 300 and 10000
        number_of_pixels = random.randint(2000, 3000)
        for i in range(number_of_pixels):

            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to white
            image[y_coord][x_coord] = 255

        # Randomly pick some pixels in
        # the image for coloring them black
        # Pick a random number between 300 and 10000
        number_of_pixels = random.randint(2000, 3000)
        for i in range(number_of_pixels):

            # Pick a random y coordinate
            y_coord = random.randint(0, row - 1)

            # Pick a random x coordinate
            x_coord = random.randint(0, col - 1)

            # Color that pixel to black
            image[y_coord][x_coord] = 0

        return image
