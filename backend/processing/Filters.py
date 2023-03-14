from math import sqrt
import numpy as np


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

    def canny_edge_detector(self, image, range):
        # apply gaussian filter
        image = self.gaussian_filter(image, 5)

        # apply sobel edge detector
        image = self.sobel_edge_detector(image)

        # apply non-maximum suppression
        image = self.__non_maximum_suppression(image)

        # # apply double threshold & hysteresis
        image = self.__double_threshold_hysteresis(image, 0, range)

        return image

    ######################################################################
    # Edge detection Helper functions

    def __detect_edges_helper(self, image, vertical_grad_filter=None, horizontal_grad_filter=None):

        # normalize the image
        image = image/image.max() * 255

        # kernel width initialization
        kernel_width = vertical_grad_filter.shape[0]//2

        # initialize the gradient image
        gradient = np.zeros(image.shape)
        self.angles = np.zeros(image.shape)

        # pad the image
        image = np.pad(image, kernel_width, 'constant')

        # get the image dimensions
        rows, cols = image.shape

        # apply the filter
        for i in range(kernel_width, rows - kernel_width):
            for j in range(kernel_width, cols - kernel_width):

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
                self.angles[i - kernel_width][j -
                                              kernel_width] = np.arctan2(sum_y, sum_x)

        return gradient

    def __non_maximum_suppression(self, image):
        size = image.shape

        # convert angles to degrees
        angles = self.angles * 180. / np.pi

        # remove negative angles and avoid 'numpy.float64' object does not support item assignment
        angles[angles < 0] += 180

        # create a zero matrix with the same dimensions as the image
        suppressed = np.zeros(size)

        # loop through the image
        for i in range(1, size[0] - 1):
            for j in range(1, size[1] - 1):
                # get the angle of the pixel
                if (0 <= angles[i, j] < 22.5) or (157.5 <= angles[i, j] <= 180):
                    value_to_compare = max(image[i, j - 1], image[i, j + 1])
                elif (22.5 <= angles[i, j] < 67.5):
                    value_to_compare = max(
                        image[i - 1, j - 1], image[i + 1, j + 1])
                elif (67.5 <= angles[i, j] < 112.5):
                    value_to_compare = max(image[i - 1, j], image[i + 1, j])
                else:
                    value_to_compare = max(
                        image[i + 1, j - 1], image[i - 1, j + 1])

                # compare the pixel to its neighbours in the direction of the gradient
                if image[i, j] >= value_to_compare:
                    suppressed[i, j] = image[i, j]

        # scale the image to 0-255
        suppressed = np.multiply(suppressed, 255.0 / suppressed.max())

        return suppressed

    def __double_threshold_hysteresis(self, image, low, high):

        weak = 50
        strong = 255

        # get the dimensions of the image
        rows, cols = image.shape

        # create a zero matrix with the same dimensions as the image
        result = np.zeros((rows, cols))

        # get the indices of the pixels that are above the low threshold
        weak_x, weak_y = np.where((image > low) & (image <= high))

        # get the indices of the pixels that are above the high threshold
        strong_x, strong_y = np.where(image >= high)

        # set the pixels that are above the high threshold to strong
        result[strong_x, strong_y] = strong

        # set the pixels that are above the low threshold to weak
        result[weak_x, weak_y] = weak

        # dx , dy are the directions to check for neighbours
        dx = np.array((-1, -1, 0, 1, 1, 1, 0, -1))
        dy = np.array((0, 1, 1, 1, 0, -1, -1, -1))

        # hysteresis
        while len(strong_x):
            x = strong_x[0]
            y = strong_y[0]
            strong_x = np.delete(strong_x, 0)
            strong_y = np.delete(strong_y, 0)
            for direction in range(len(dx)):
                new_x = x + dx[direction]
                new_y = y + dy[direction]
                if ((new_x >= 0 & new_x < rows & new_y >= 0 & new_y < cols) and (result[new_x, new_y] == weak)):
                    result[new_x, new_y] = strong
                    np.append(strong_x, new_x)
                    np.append(strong_y, new_y)
        result[result != strong] = 0
        return result
