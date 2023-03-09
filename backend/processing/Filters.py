import cv2
from math import sqrt
import numpy as np

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
    def __init__(self):
        pass

    ######################################################################
    # Add noise to the image algorithms

    def salt_pepper_noise(self, image, range):
        row, col = image.shape
        salt_pepper = np.random.random((row, col))*255
        pepper = salt_pepper < 0+range
        salt = salt_pepper > 255-range
        image[pepper] = 0
        image[salt] = 255
        return image

    def gaussian_noise(self, image, range):
        row, col = image.shape
        mean = 0
        var = range
        sigma = var ** 0.5
        gauss = np.random.normal(mean, sigma, (row, col))
        gauss = gauss.reshape(row, col)
        noisy = image + gauss
        return noisy

    def uniform_noise(self, image, range):
        row, col = image.shape
        low = -range
        high = range
        noise = np.random.uniform(low, high, (row, col))
        noisy = image + noise
        return noisy

    ######################################################################
    # Smoothing filters algorithms

    def average_filter(self, image, kernel_size):
        row, col = image.shape
        new_image = np.zeros((row, col))

        # apply filter
        for i in range(row):
            for j in range(col):
                new_image[i, j] = np.mean(
                    image[i:i+kernel_size, j:j+kernel_size])
        return new_image

    def median_filter(self, image, kernel_size):
        row, col = image.shape
        new_image = np.zeros((row, col))

        # apply filter
        for i in range(row):
            for j in range(col):
                new_image[i, j] = np.median(
                    image[i:i+kernel_size, j:j+kernel_size])
        return new_image

    def gaussian_filter(self, image, kernel_size):
        row, col = image.shape
        new_image = np.zeros((row, col))
        sigma = 2

        # get kernel
        kernel = self.__gaussian_kernel(kernel_size, sigma)

        # apply zero padding
        image = np.pad(image, (kernel_size//2, kernel_size//2), 'constant')

        # apply filter
        for i in range(row):
            for j in range(col):
                new_image[i, j] = np.sum(
                    image[i:i+kernel_size, j:j+kernel_size]*kernel)
        return new_image

    def __gaussian_kernel(self, kernel_size, sigma):
        ax = np.linspace(-(kernel_size - 1) / 2.,
                         (kernel_size - 1) / 2., kernel_size)
        xx, yy = np.meshgrid(ax, ax)
        kernel = np.exp(-0.5 * (np.square(xx) +
                        np.square(yy)) / np.square(sigma))
        kernel = kernel / np.sum(kernel)
        return kernel

    ######################################################################
    # Edge detection algorithms

    def sobel_edge_detector(self, image):
        vertical_grad_filter = np.array(
            [[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        horizontal_grad_filter = np.array(
            [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        return self.__detect_edges_helper(image, vertical_grad_filter, horizontal_grad_filter)

    def prewitt_edge_detector(self, image):
        vertical_grad_filter = np.array(
            [[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        horizontal_grad_filter = np.array(
            [[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        return self.__detect_edges_helper(image, vertical_grad_filter, horizontal_grad_filter)

    def roberts_edge_detector(self, image):
        vertical_grad_filter = np.array([[0, 0, 0], [0, 1, 0], [0, 0, -1]])
        horizontal_grad_filter = np.array([[0, 0, 0], [0, 0, 1], [0, -1, 0]])
        return self.__detect_edges_helper(image, vertical_grad_filter, horizontal_grad_filter)

    def __detect_edges_helper(self, image, vertical_grad_filter=None, horizontal_grad_filter=None):
        # convert to grayscale image
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # normalize the image
        image = image/255

        # kernel width initialization
        kernel_width = vertical_grad_filter.shape[0]//2

        # initialize the gradient image
        gradient = np.zeros(image.shape)

        # pad the image
        image = np.pad(image, kernel_width, 'constant')

        for i in range(kernel_width, image.shape[0] - kernel_width):
            for j in range(kernel_width, image.shape[1] - kernel_width):

                # obtain the horizontal gradients
                x = image[i - kernel_width: i + kernel_width +
                          1, j - kernel_width: j + kernel_width + 1]
                x = x.flatten() * vertical_grad_filter.flatten()
                sum_x = x.sum()

                # obtain the vertical gradients
                y = image[i - kernel_width: i + kernel_width +
                          1, j - kernel_width: j + kernel_width + 1]
                y = y.flatten() * horizontal_grad_filter.flatten()
                sum_y = y.sum()

                # calculate the gradient
                gradient[i - kernel_width][j -
                                           kernel_width] = sqrt(sum_x**2 + sum_y**2)

        return gradient
