import cv2
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
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
    def __init__():
        pass

    def salt_pepper_noise(image, range):
        row, col = image.shape
        salt_pepper = np.random.random((row, col))*255
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

    def average_filter(image, kernel_size):
        row, col = image.shape
        new_image = np.zeros((row, col))

        # apply filter
        for i in range(row):
            for j in range(col):
                new_image[i, j] = np.mean(
                    image[i:i+kernel_size, j:j+kernel_size])
        return new_image

    def median_filter(image, kernel_size):
        row, col = image.shape
        new_image = np.zeros((row, col))

        # apply filter
        for i in range(row):
            for j in range(col):
                new_image[i, j] = np.median(
                    image[i:i+kernel_size, j:j+kernel_size])
        return new_image

    def gaussian_filter(image, kernel_size):
        row, col = image.shape
        new_image = np.zeros((row, col))
        sigma = 2

        # get kernel
        ax = np.linspace(-(kernel_size - 1) / 2.,
                         (kernel_size - 1) / 2., kernel_size)
        xx, yy = np.meshgrid(ax, ax)
        kernel = np.exp(-0.5 * (np.square(xx) +
                        np.square(yy)) / np.square(sigma))
        kernel = kernel / np.sum(kernel)

        # apply zero padding
        image = np.pad(image, (kernel_size//2, kernel_size//2), 'constant')

        # apply filter
        for i in range(row):
            for j in range(col):
                new_image[i, j] = np.sum(
                    image[i:i+kernel_size, j:j+kernel_size]*kernel)
        return new_image


class sobel_edge_detector:
    def __init__(self, path=None, img=None):
        if path != None:
            self.image = mpimg.imread(path)
        else:
            self.image = img
        self.orig_img = self.image
        self.vertical_grad_filter = np.array(
            [[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        self.horizontal_grad_filter = np.array(
            [[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        print(self.image)

    def cvt2gray(self):
        self.image = np.dot(self.image, [1, 1, 1])//3
        self.image = self.image/255
        print(self.image)

    def detect_edges(self):
        self.cvt2gray()
        kernel_width = self.vertical_grad_filter.shape[0]//2
        grad_ = np.zeros(self.image.shape)

        self.image = np.pad(self.image, pad_width=([kernel_width, ], [kernel_width, ]),
                            mode='constant', constant_values=(0, 0))
        for i in range(kernel_width, self.image.shape[0] - kernel_width):
            for j in range(kernel_width, self.image.shape[1] - kernel_width):
                x = self.image[i - kernel_width: i + kernel_width +
                               1, j - kernel_width: j + kernel_width + 1]
                x = x.flatten() * self.vertical_grad_filter.flatten()
                sum_x = x.sum()

                y = self.image[i - kernel_width: i + kernel_width +
                               1, j - kernel_width: j + kernel_width + 1]
                y = y.flatten() * self.horizontal_grad_filter.flatten()
                sum_y = y.sum()

                grad_[i - kernel_width][j -
                                        kernel_width] = sqrt(sum_x**2 + sum_y**2)
        self.image = grad_
        return self.image
        # loc_time = time.localtime(time.time())
        # m = str(loc_time.tm_year) + str(loc_time.tm_mon) + str(loc_time.tm_mday) + str(loc_time.tm_hour) + str(loc_time.tm_min) + str(loc_time.tm_sec)
        # img_save_name = 'sobel_edge_det_' + m + ".jpg"
        # plt.imsave(img_save_name, self.image)

    def show_image(self, orig=0):
        if orig == 1:
            plt.imshow(self.orig_img)
            plt.show()
        if orig == 0:
            for i in range(len(self.image)):
                for j in range(len(self.image[0])):
                    self.image[i][j] = 1 - self.image[i][j]
            plt.imshow(self.image, cmap='gray')
            plt.show()


###### CANNY######


def sHalf(T, sigma):
    temp = -np.log(T) * 2 * (sigma ** 2)
    return np.round(np.sqrt(temp))


def calculate_filter_size(T, sigma):
    return 2*sHalf(T, sigma) + 1


def MaskGeneration(T, sigma):
    N = calculate_filter_size(T, sigma)
    shalf = sHalf(T, sigma)
    y, x = np.meshgrid(range(-int(shalf), int(shalf) + 1),
                       range(-int(shalf), int(shalf) + 1))
    return x, y


def Gaussian(x, y, sigma):
    temp = ((x ** 2) + (y ** 2)) / (2 * (sigma ** 2))
    return (np.exp(-temp))


def calculate_gradient_X(x, y, sigma):
    temp = (x ** 2 + y ** 2) / (2 * sigma ** 2)
    return -((x * np.exp(-temp)) / sigma ** 2)


def calculate_gradient_Y(x, y, sigma):
    temp = (x ** 2 + y ** 2) / (2 * sigma ** 2)
    return -((y * np.exp(-temp)) / sigma ** 2)


def pad(img, kernel):
    r, c = img.shape
    kr, kc = kernel.shape
    padded = np.zeros((r + kr, c + kc), dtype=img.dtype)
    insert = np.uint((kr)/2)
    padded[insert: insert + r, insert: insert + c] = img
    return padded


def smooth(img, kernel=None):
    if kernel is None:
        mask = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    else:
        mask = kernel
    i, j = mask.shape
    output = np.zeros((img.shape[0], img.shape[1]))
    image_padded = pad(img, mask)
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            output[x, y] = (mask * image_padded[x:x+i, y:y+j]
                            ).sum() / mask.sum()
    return output


def Create_Gx(fx, fy):
    gx = calculate_gradient_X(fx, fy, sigma)
    gx = (gx * 255)
    return np.around(gx)


def Create_Gy(fx, fy):
    gy = calculate_gradient_Y(fx, fy, sigma)
    gy = (gy * 255)
    return np.around(gy)


def ApplyMask(image, kernel):
    i, j = kernel.shape
    kernel = np.flipud(np.fliplr(kernel))
    output = np.zeros_like(image)
    image_padded = pad(image, kernel)
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            output[x, y] = (kernel * image_padded[x:x+i, y:y+j]).sum()
    return output


def Gradient_Magnitude(fx, fy):
    mag = np.zeros((fx.shape[0], fx.shape[1]))
    mag = np.sqrt((fx ** 2) + (fy ** 2))
    mag = mag * 100 / mag.max()
    return np.around(mag)


def Gradient_Direction(fx, fy):
    g_dir = np.zeros((fx.shape[0], fx.shape[1]))
    g_dir = np.rad2deg(np.arctan2(fy, fx)) + 180
    return g_dir


def Digitize_angle(Angle):
    quantized = np.zeros((Angle.shape[0], Angle.shape[1]))
    for i in range(Angle.shape[0]):
        for j in range(Angle.shape[1]):
            if 0 <= Angle[i, j] <= 22.5 or 157.5 <= Angle[i, j] <= 202.5 or 337.5 < Angle[i, j] < 360:
                quantized[i, j] = 0
            elif 22.5 <= Angle[i, j] <= 67.5 or 202.5 <= Angle[i, j] <= 247.5:
                quantized[i, j] = 1
            elif 67.5 <= Angle[i, j] <= 122.5 or 247.5 <= Angle[i, j] <= 292.5:
                quantized[i, j] = 2
            elif 112.5 <= Angle[i, j] <= 157.5 or 292.5 <= Angle[i, j] <= 337.5:
                quantized[i, j] = 3
    return quantized


def Non_Max_Supp(qn, magni, D):
    M = np.zeros(qn.shape)
    a, b = np.shape(qn)
    for i in range(a-1):
        for j in range(b-1):
            if qn[i, j] == 0:
                if magni[i, j-1] < magni[i, j] or magni[i, j] > magni[i, j+1]:
                    M[i, j] = D[i, j]
                else:
                    M[i, j] = 0
            if qn[i, j] == 1:
                if magni[i-1, j+1] <= magni[i, j] or magni[i, j] >= magni[i+1, j-1]:
                    M[i, j] = D[i, j]
                else:
                    M[i, j] = 0
            if qn[i, j] == 2:
                if magni[i-1, j] <= magni[i, j] or magni[i, j] >= magni[i+1, j]:
                    M[i, j] = D[i, j]
                else:
                    M[i, j] = 0
            if qn[i, j] == 3:
                if magni[i-1, j-1] <= magni[i, j] or magni[i, j] >= magni[i+1, j+1]:
                    M[i, j] = D[i, j]
                else:
                    M[i, j] = 0
    return M


def color(quant, mag):
    color = np.zeros((mag.shape[0], mag.shape[1], 3), np.uint8)
    a, b = np.shape(mag)
    for i in range(a-1):
        for j in range(b-1):
            if quant[i, j] == 0:
                if mag[i, j] != 0:
                    color[i, j, 0] = 255
                else:
                    color[i, j, 0] = 0
            if quant[i, j] == 1:
                if mag[i, j] != 0:
                    color[i, j, 1] = 255
                else:
                    color[i, j, 1] = 0
            if quant[i, j] == 2:
                if mag[i, j] != 0:
                    color[i, j, 2] = 255
                else:
                    color[i, j, 2] = 0
            if quant[i, j] == 3:
                if mag[i, j] != 0:
                    color[i, j, 0] = 255
                    color[i, j, 1] = 255

                else:
                    color[i, j, 0] = 0
                    color[i, j, 1] = 0
    return color


def _double_thresholding(g_suppressed, low_threshold, high_threshold):
    g_thresholded = np.zeros(g_suppressed.shape)
    for i in range(0, g_suppressed.shape[0]):		# loop over pixels
        for j in range(0, g_suppressed.shape[1]):
            if g_suppressed[i, j] < low_threshold:  # lower than low threshold
                g_thresholded[i, j] = 0
            # between thresholds
            elif g_suppressed[i, j] >= low_threshold and g_suppressed[i, j] < high_threshold:
                g_thresholded[i, j] = 128
            else:					        # higher than high threshold
                g_thresholded[i, j] = 255
    return g_thresholded


def _hysteresis(g_thresholded):
    g_strong = np.zeros(g_thresholded.shape)
    for i in range(0, g_thresholded.shape[0]):		# loop over pixels
        for j in range(0, g_thresholded.shape[1]):
            val = g_thresholded[i, j]
            if val == 128:			# check if weak edge connected to strong
                if g_thresholded[i-1, j] == 255 or g_thresholded[i+1, j] == 255 or g_thresholded[i-1, j-1] == 255 or g_thresholded[i+1, j-1] == 255 or g_thresholded[i-1, j+1] == 255 or g_thresholded[i+1, j+1] == 255 or g_thresholded[i, j-1] == 255 or g_thresholded[i, j+1] == 255:
                    g_strong[i, j] = 255		# replace weak edge as strong
            elif val == 255:
                g_strong[i, j] = 255		# strong edge remains as strong edge
    return g_strong


# Specify sigma and T value Also calculate Gradient masks
sigma = 0.5
T = 0.3
x, y = MaskGeneration(T, sigma)
gauss = Gaussian(x, y, sigma)

gx = -Create_Gx(x, y)
gy = -Create_Gy(x, y)

# Reading and converting image into grayscale
image = cv2.imread('circle.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# Smoothing
smooth_img = smooth(gray, gauss)

# Applying the Gradient masks
fx = ApplyMask(smooth_img, gx)
fy = ApplyMask(smooth_img, gy)

# Gradient magnitude
mag = Gradient_Magnitude(fx, fy)
mag = mag.astype(int)

# Gradient Direction
Angle = Gradient_Direction(fx, fy)

# Quantization of angles and Non-Max Suppression
quantized = Digitize_angle(Angle)
nms = Non_Max_Supp(quantized, Angle, mag)

# Colorized Image for visualiztion of angles
colorized = color(quantized, mag)
cv2.imwrite('color.jpg', colorized)

# Double Threshold and Hysteresis
threshold = _double_thresholding(nms, 30, 60)
cv2.imwrite('double_thresholded.jpg', threshold)
hys = _hysteresis(threshold)
cv2.imwrite('Result.jpg', hys)
######################################

# robert operator [[-1,-1],[1,1]]
def robert(img):
    r, c = img.shape
    r_sunnzi = [[-1,-1],[1,1]]
    for x in range(r):
        for y in range(c):
            if (y + 2 <= c) and (x + 2 <= r):
                imgChild = img[x:x+2, y:y+2]
                list_robert = r_sunnzi*imgChild
                img[x, y] = abs(list_robert.sum()) # sum and absolute value
    return img

###############################
filter_dim = 5 #A matrix for the gaussian filter
sigma_val = 5 #sigma is the standard deviation
def gaussian_filter(image,filter_size,sigma):
    """This function uses gaussian filter to remove image noise"""
    filtered_image = cv2.GaussianBlur(image,(filter_size, filter_size),sigma)
    return filtered_image
def prewitt_filter(any_image):
    """This function uses prewitt filter to detect image edges"""
    image = gaussian_filter(any_image,filter_size=filter_dim,sigma=sigma_val)
    vertical_filter = np.array([[-1,-1,-1],[0,0,0],[1,1,1]])
    horizontal_filter = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    
    vertical_filtered = cv2.filter2D(image,-1,vertical_filter)
    horizontal_filtered = cv2.filter2D(image,-1,horizontal_filter)
    
    abs_grad_x = cv2.convertScaleAbs(vertical_filtered)
    abs_grad_y = cv2.convertScaleAbs(horizontal_filtered)
    
    grad =cv2.addWeighted(abs_grad_x,0.5,abs_grad_y,0.5,0)  #0.5 is the sqrt of the abs values
    return grad
####################################
if __name__ == "__main__":
    img = sobel_edge_detector("test.jpg")
    img.show_image(1)
    img.detect_edges()
    img.show_image()
