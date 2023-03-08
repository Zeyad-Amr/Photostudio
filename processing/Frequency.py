import numpy as np


class Frequency:
    def __init__():
        pass

    def get_max_frequency(img):
        rows = img.shape[0]
        columns = img.shape[1]
        img = np.fft.fft2(img)
        img = np.fft.fftshift(img)
        max = 0
        for i in range(rows):
            for j in range(columns):
                if img[i][j] > max:
                    max = img[i][j]
        return max

    def get_min_frequency(img):
        rows = img.shape[0]
        columns = img.shape[1]
        img = np.fft.fft2(img)
        img = np.fft.fftshift(img)
        min = 0
        for i in range(rows):
            for j in range(columns):
                if img[i][j] < min:
                    min = img[i][j]
        return min

    def low_pass_filter(img, cutoff):
        rows = img.shape[0]
        columns = img.shape[1]
        img = np.fft.fft2(img)
        img = np.fft.fftshift(img)
        for i in range(rows):
            for j in range(columns):
                if (i - rows/2)**2 + (j - columns/2)**2 > cutoff**2:
                    img[i][j] = 0
        img = np.fft.ifftshift(img)
        img = np.fft.ifft2(img)
        return img

    def high_pass_filter(img, cutoff):
        rows = img.shape[0]
        columns = img.shape[1]
        img = np.fft.fft2(img)
        img = np.fft.fftshift(img)
        for i in range(rows):
            for j in range(columns):
                if (i - rows/2)**2 + (j - columns/2)**2 < cutoff**2:
                    img[i][j] = 0
        img = np.fft.ifftshift(img)
        img = np.fft.ifft2(img)
        return img

    def hypridImages(img1, img2):
        return img1+img2
