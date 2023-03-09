import numpy as np
import cv2


class Frequency:

    def __init__(self):
        pass

    def high_pass_filter(self,img, filter_range):
        # resize the image
        img = cv2.resize(img, (512, 512))

        # convert to grayscale image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # apply the Fourier transform to the image
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)

        # define the filter mask
        rows, cols = gray.shape
        crow, ccol = rows//2, cols//2
        mask = np.zeros((rows, cols), np.uint8)

        for i in range(rows):
            for j in range(cols):
                dist = np.sqrt((i-crow)**2+(j-ccol)**2)
                if dist > filter_range:
                    mask[i][j] = 1

        # apply the filter mask to the Fourier transformed image
        fshift = fshift * mask

        # apply the inverse Fourier transform to the filtered image
        ishift = np.fft.ifftshift(fshift)
        filtered_image = np.fft.ifft2(ishift)
        filtered_image = np.abs(filtered_image)

        return filtered_image

    def low_pass_filter(self,img, filter_range):
        # resize the image
        img = cv2.resize(img, (512, 512))

        # convert to grayscale image
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # apply the Fourier transform to the image
        f = np.fft.fft2(gray)
        fshift = np.fft.fftshift(f)

        # define the filter mask
        rows, cols = gray.shape
        crow, ccol = rows//2, cols//2
        mask = np.zeros((rows, cols), np.uint8)

        for i in range(rows):
            for j in range(cols):
                dist = np.sqrt((i-crow)**2+(j-ccol)**2)
                if dist < filter_range:
                    mask[i][j] = 1

        # apply the filter mask to the Fourier transformed image
        fshift = fshift * mask

        # apply the inverse Fourier transform to the filtered image
        ishift = np.fft.ifftshift(fshift)
        filtered_image = np.fft.ifft2(ishift)
        filtered_image = np.abs(filtered_image)

        return filtered_image

    def hypridImages(self,img1, img2):
        return img1+img2
