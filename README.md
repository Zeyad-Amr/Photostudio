# Photostudio

Photostudio is a web project that aims to enhance images using various image processing techniques. It covers noise removal, edge detection, and histogram analysis, as well as color to grayscale transformation and frequency domain filters. Local and global thresholding is also included, as well as hybrid image creation. The project is designed to provide a comprehensive understanding of image processing techniques and their practical applications.

## Technologies
- Frontend: React ts
- Backend: Django
- Processing: Python, opencv, matplotlib, numpy

## Features
### Filters
The given class Filters contains various image processing algorithms for adding noise, applying smoothing filters and detecting edges to an image.

#### Add Noise Algorithms
1. `salt_pepper_noise(image, range)`:
    - This function adds salt and pepper noise to the image. The function takes two arguments: the input image and the range of noise to be added.
    - The noise range is a value between 0 and 255, where 0 means no noise and 255 means full noise.
    - The algorithm generates a random matrix of the same size as the input image and multiplies it by 255.
    - It then checks for values less than the given range and assigns 0 to those pixels (pepper noise) and values greater than 255 minus the range and assigns 255 to those pixels (salt noise).
    - Finally, the function will add salt and pepper noise to the input image.
    
![WhatsApp Image 2023-03-14 at 7 32 04 PM](https://user-images.githubusercontent.com/68791488/225124415-cb2d74a2-0f94-419f-a845-9fae28da55ec.jpeg)

2. `gaussian_noise(image, range)`:
    - This function adds Gaussian noise to the image. The function takes two arguments: the input image and the range of noise to be added. The noise range is a value that controls the variance of the Gaussian distribution.
    - The algorithm generates a random Gaussian distribution of the same size as the input image with mean 0 and standard deviation equal to the given range.
    - It then adds this noise to the input image.
    - Finally, the function will add Gaussian noise to the input image.
    
![WhatsApp Image 2023-03-14 at 7 31 49 PM](https://user-images.githubusercontent.com/68791488/225124652-f466e75e-ba1e-4baf-b80c-267cbb7f9b0b.jpeg)


3. `uniform_noise(image, range)`:
    - This function adds uniform noise to the image.
    - The function takes two arguments: the input image and the range of noise to be added.
    - The noise range is a value that controls the range of uniform distribution.
    - The algorithm generates a random uniform distribution of the same size as the input image with low equal to minus the given range and high equal to the given range. It then adds this noise to the input image.
    - Finally, the function will add uniform noise to the input image.

![WhatsApp Image 2023-03-14 at 7 31 33 PM](https://user-images.githubusercontent.com/68791488/225124678-e0e1974f-9313-4564-9afa-fa1932f85650.jpeg)


#### Smoothing Filters Algorithms
1. `average_filter(image, kernel_size)`:
    - This function applies an average filter to the image.
    - The function takes two arguments: the input image and the kernel size of the filter.
    - The algorithm convolves the kernel of the given size with the input image to obtain the filtered image. The value of each pixel in the filtered image is the average of the values of the corresponding pixels in the kernel.
    - Finally, the function will apply an average filter to the input image.
    
2. `median_filter(image, kernel_size)`:
    - This function applies a median filter to the image.
    - The function takes two arguments: the input image and the kernel size of the filter.
    - The algorithm convolves the kernel of the given size with the input image to obtain the filtered image.
    - The value of each pixel in the filtered image is the median of the values of the corresponding pixels in the kernel.
    - Finally, the function will apply a median filter to the input image.
    
3. `gaussian_filter(image, kernel_size)`:
    - This function applies a Gaussian filter to the image. The function takes two arguments: the input image and the kernel size of the filter.
    - The algorithm generates a Gaussian kernel of the given size and standard deviation of 2. It then convolves this kernel with the input image to obtain the filtered image.
    - Finally, The function will apply a Gaussian filter to the input image.

#### Edges Detection Algorithms
1. `sobel_edge_detector(image)`:
    - This function performs edge detection using the Sobel operator.
    - The method initializes two 3x3 filters, vertical_grad_filter and horizontal_grad_filter, which are the Sobel operators for detecting vertical and horizontal edges in an image, respectively.
    - The filters are designed to give more weight to the central pixel and less weight to the surrounding pixels.
    - Then, the method calls the __detect_edges_helper method with the input image and these two filters as arguments. The __detect_edges_helper method applies the filters on the image to detect edges and returns a gradient image that represents the strength of the edges and the angles of the gradients at each pixel.
    - Finally, the sobel_edge_detector method returns the gradient image obtained from __detect_edges_helper.

    
2. `prewitt_edge_detector(image)`:
    - This function performs edge detection using the Prewitt operator.
    - The method initializes two 3x3 filters, vertical_grad_filter and horizontal_grad_filter, which are the Prewitt operators for detecting vertical and horizontal edges in an image, respectively.
    - The filters are designed to give equal weight to all pixels in the image.
    - Then, the method calls the __detect_edges_helper method with the input image and these two filters as arguments. The __detect_edges_helper method applies the filters on the image to detect edges and returns a gradient image that represents the strength of the edges and the angles of the gradients at each pixel.
    - Finally, the sobel_edge_detector method returns the gradient image obtained from __detect_edges_helper.

    
3. `roberts_edge_detector(image)`:
    - This function performs edge detection using the Prewitt operator.
    - The method initializes two 3x3 filters, vertical_grad_filter and horizontal_grad_filter, which are the Prewitt operators for detecting vertical and horizontal edges in an image, respectively.
    - The filters are designed to give more weight to the diagonal pixels and less weight to the surrounding pixels.
    - Then, the method calls the __detect_edges_helper method with the input image and these two filters as arguments. The __detect_edges_helper method applies the filters on the image to detect edges and returns a gradient image that represents the strength of the edges and the angles of the gradients at each pixel.
    - Finally, the sobel_edge_detector method returns the gradient image obtained from __detect_edges_helper.

    
4. `canny_edge_detector(image, range)`:
    - This function performs edge detection using the Canny edge detection algorithm on an input image. The steps of the algorithm are as follows:
    - Gaussian filter: The input image is first smoothed using a Gaussian filter to reduce noise and remove small details.
    - Sobel edge detector: The Sobel operator is applied to the smoothed image to obtain the gradient magnitude and direction at each pixel.
    - Non-maximum suppression: The gradient magnitude is thinned down to a one-pixel wide edge by suppressing all gradients except the local maxima in the gradient direction.
    - Double threshold and hysteresis: A double threshold is applied to the gradient magnitude image to classify each pixel as either an edge or non-edge pixel. 
    - The pixels with gradient magnitude above the high threshold are considered edge pixels, while those below the low threshold are considered non-edge pixels.
    - The pixels between the two thresholds are classified as edge pixels only if they are connected to other edge pixels.
    - The range parameter is used to set the high threshold of the double thresholding step. The low threshold is set to zero.
    - Finally, the output image is returned. It will have white pixels indicating edges and black pixels indicating non-edges.
