import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
from math import sqrt
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

class sobel_edge_detector:
    def __init__(self, path= None, img= None):
        if path != None:
            self.image = mpimg.imread(path)
        else:
            self.image = img
        self.orig_img = self.image
        self.vertical_grad_filter = np.array([[1, 0, -1],[2, 0, -2],[1, 0, -1]])
        self.horizontal_grad_filter = np.array([[1, 2, 1],[0, 0, 0],[-1, -2, -1]])
        print(self.image)

    def cvt2gray(self):
        self.image = np.dot(self.image, [1, 1, 1])//3
        self.image = self.image/255
        print(self.image)

    def detect_edges(self):
        self.cvt2gray()
        kernel_width = self.vertical_grad_filter.shape[0]//2
        grad_ = np.zeros(self.image.shape)

        self.image = np.pad(self.image, pad_width= ([kernel_width, ], [kernel_width, ]), 
        mode= 'constant', constant_values= (0, 0))
        for i in range(kernel_width, self.image.shape[0] - kernel_width):
            for j in range(kernel_width, self.image.shape[1] - kernel_width):
                x = self.image[i - kernel_width: i + kernel_width + 1, j - kernel_width: j + kernel_width + 1]
                x = x.flatten() * self.vertical_grad_filter.flatten()
                sum_x = x.sum()

                y = self.image[i - kernel_width: i + kernel_width + 1, j - kernel_width: j + kernel_width + 1]
                y = y.flatten() * self.horizontal_grad_filter.flatten()
                sum_y = y.sum()
        
                grad_[i - kernel_width][j - kernel_width] = sqrt(sum_x**2 + sum_y**2)
        self.image = grad_
        return self.image
        # loc_time = time.localtime(time.time())
        # m = str(loc_time.tm_year) + str(loc_time.tm_mon) + str(loc_time.tm_mday) + str(loc_time.tm_hour) + str(loc_time.tm_min) + str(loc_time.tm_sec)
        # img_save_name = 'sobel_edge_det_' + m + ".jpg"
        # plt.imsave(img_save_name, self.image)

    def show_image(self, orig = 0):
        if orig == 1:
            plt.imshow(self.orig_img)
            plt.show()
        if orig == 0:
            for i in range(len(self.image)):
                for j in range(len(self.image[0])):
                    self.image[i][j] = 1 - self.image[i][j] 
            plt.imshow(self.image, cmap= 'gray')
            plt.show()

if __name__ == "__main__":
    img = sobel_edge_detector("test.jpg")
    img.show_image(1)
    img.detect_edges()
    img.show_image()
    