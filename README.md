<h1 align="center">
 <strong>Photostudio</strong>
 <br/><br/>
</h1>

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [How to Use](#how-to-use)
- [Features](#features)
- [Filters Class](#filters-class)
- [Histogram Class](#histogram-class)
- [Frequency Class](#frequency-class)
- [Hough Class](#hough-class)
- [Active Contour Class](#active-contour-class)
- [Contributing](#contributing)
- [Developers](#developers)

## Introduction
Photostudio is a web project that aims to enhance images using various image processing techniques. It covers noise removal, edge detection, and histogram analysis, as well as color to grayscale transformation and frequency domain filters. Local and global thresholding is also included, as well as hybrid image creation. In addition to hough transform for detecting lines, circles and ellipses in image and applying active contour to image. The project is designed to provide a comprehensive understanding of image processing techniques and their practical applications.

## Technologies
- Frontend: React ts
- Backend: Django
- Processing: Python, opencv, matplotlib, numpy

## How to Use

1. Clone the repository using the command `git clone https://github.com/Zeyad-Amr/Photostudio`
2. Install frontend dependencies using `npm install`
3. Install backend packages in virtual enviroment using `pip install -r requirements.txt`
4. Start the development server for the backend using `py manage.py runserver`
5. Start the development server for the frontend using `npm start`
6. Open [http://localhost:3000](http://localhost:3000) in your browser to view the app.

### Frontend
This is a React TypeScript project that uses components to render UI elements. It uses React Router for navigation and Redux for state management.

In the client directory, you can run:
```
$ npm install
Install all needed dependencies.

$ npm start
Builds the app for production to the `build` folder.
```

### Backend
This is a Django project that provides APIs for the frontend React app. It uses Django REST framework for building APIs.

In the backend directory, you can run:

```
$ pip install -r requirements.txt
install all required packages for the project.

$ python manage.py migrate
Applies any pending migrations to the database.

$ python manage.py runserver
Runs the development server for the backend.

$ python manage.py test
Runs the tests for the backend.

```

## Features
### Filters Class
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
    
![WhatsApp Image 2023-03-14 at 7 59 27 PM](https://user-images.githubusercontent.com/68791488/225125058-17cb0214-6759-44b2-8d35-4aa922aab3c1.jpeg)

2. `median_filter(image, kernel_size)`:
    - This function applies a median filter to the image.
    - The function takes two arguments: the input image and the kernel size of the filter.
    - The algorithm convolves the kernel of the given size with the input image to obtain the filtered image.
    - The value of each pixel in the filtered image is the median of the values of the corresponding pixels in the kernel.
    - Finally, the function will apply a median filter to the input image.
    
![WhatsApp Image 2023-03-14 at 7 59 55 PM](https://user-images.githubusercontent.com/68791488/225125248-7d9f8c86-98cd-4423-aa9c-86c2ab770eca.jpeg)

    
3. `gaussian_filter(image, kernel_size)`:
    - This function applies a Gaussian filter to the image. The function takes two arguments: the input image and the kernel size of the filter.
    - The algorithm generates a Gaussian kernel of the given size and standard deviation of 2. It then convolves this kernel with the input image to obtain the filtered image.
    - Finally, The function will apply a Gaussian filter to the input image.

![WhatsApp Image 2023-03-14 at 7 59 41 PM](https://user-images.githubusercontent.com/68791488/225125229-87c7ed2b-c6ea-44c3-ac1b-a0984b3996d5.jpeg)


#### Edges Detection Algorithms
1. `sobel_edge_detector(image)`:
    - This function performs edge detection using the Sobel operator.
    - The method initializes two 3x3 filters, vertical_grad_filter and horizontal_grad_filter, which are the Sobel operators for detecting vertical and horizontal edges in an image, respectively.
    - The filters are designed to give more weight to the central pixel and less weight to the surrounding pixels.
    - Then, the method calls the __detect_edges_helper method with the input image and these two filters as arguments. The __detect_edges_helper method applies the filters on the image to detect edges and returns a gradient image that represents the strength of the edges and the angles of the gradients at each pixel.
    - Finally, the sobel_edge_detector method returns the gradient image obtained from __detect_edges_helper.

![WhatsApp Image 2023-03-14 at 8 05 24 PM](https://user-images.githubusercontent.com/68791488/225125506-8efcfe2f-f217-41c8-b804-d3f265df8ec1.jpeg)

    
2. `prewitt_edge_detector(image)`:
    - This function performs edge detection using the Prewitt operator.
    - The method initializes two 3x3 filters, vertical_grad_filter and horizontal_grad_filter, which are the Prewitt operators for detecting vertical and horizontal edges in an image, respectively.
    - The filters are designed to give equal weight to all pixels in the image.
    - Then, the method calls the __detect_edges_helper method with the input image and these two filters as arguments. The __detect_edges_helper method applies the filters on the image to detect edges and returns a gradient image that represents the strength of the edges and the angles of the gradients at each pixel.
    - Finally, the sobel_edge_detector method returns the gradient image obtained from __detect_edges_helper.

![WhatsApp Image 2023-03-14 at 8 05 34 PM](https://user-images.githubusercontent.com/68791488/225125555-55136785-ca5f-4d85-84aa-f45826f9aaa0.jpeg)


3. `roberts_edge_detector(image)`:
    - This function performs edge detection using the Prewitt operator.
    - The method initializes two 3x3 filters, vertical_grad_filter and horizontal_grad_filter, which are the Prewitt operators for detecting vertical and horizontal edges in an image, respectively.
    - The filters are designed to give more weight to the diagonal pixels and less weight to the surrounding pixels.
    - Then, the method calls the __detect_edges_helper method with the input image and these two filters as arguments. The __detect_edges_helper method applies the filters on the image to detect edges and returns a gradient image that represents the strength of the edges and the angles of the gradients at each pixel.
    - Finally, the sobel_edge_detector method returns the gradient image obtained from __detect_edges_helper.

![WhatsApp Image 2023-03-14 at 8 05 44 PM](https://user-images.githubusercontent.com/68791488/225125574-4147227e-d6be-4190-bedf-0cb1dca2a1c9.jpeg)

    
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

![WhatsApp Image 2023-03-14 at 8 05 54 PM](https://user-images.githubusercontent.com/68791488/225125600-dcbf4932-e85c-4968-a590-146f3bc2cc82.jpeg)

5. `__detect_edges_helper(image, kernel_size, vertical_grad_filter=None, horizontal_grad_filter=None):`
    - This function takes in an image and two optional filter arrays - `vertical_grad_filter` and `horizontal_grad_filter` - that are used to calculate the gradient in the vertical and horizontal directions.
    - The image is normalized by dividing every pixel value by 255, which scales the pixel values to be between 0 and 1. 
    - The function initializes the width of the kernel as half the height of the `vertical_grad_filter`.
    - It initializes two empty arrays - `gradient` and `self.angles` - to hold the gradient magnitude and direction information, respectively.
    - The image is padded with zeros around its edges to ensure that the kernel can be applied to all pixels in the image.
    - The function loops through every pixel in the image, skipping the padded edges.
    - For each pixel, the function extracts a sub-image of size `(kernel_width*2 + 1, kernel_width*2 + 1)` centered at the pixel.
    - The filter is applied to the sub-image by element-wise multiplication of the filter array with the sub-image, followed by a summation of the resulting array. This process is repeated for both the vertical and horizontal filters to obtain the vertical and horizontal gradient components.
    - The gradient magnitude at the pixel is calculated by taking the square root of the sum of the squared vertical and horizontal gradient components.
    - The gradient direction at the pixel is calculated using the `arctan2` function in numpy, which returns the angle between the positive x-axis and the line passing through the origin and the pixel.
    - The gradient magnitude and direction values are stored in the `gradient` and `self.angles` arrays, respectively.
    - The `gradient` array is returned as the output of the function.

6. `__non_maximum_suppression(image):`
    - This function performs non-maximum suppression on the gradient magnitude image to thin the edges and keep only the strongest edges. The input to the function is obtained from the output of the `__detect_edges_helper` function.
    - The function first converts the angles from radians to degrees and removes negative angles. Then it creates a zero matrix of the same size as the input image to store the output. It then loops through the image and for each pixel, it checks the angle of the gradient and compares the pixel's value to its neighbors in the direction of the gradient.
    - If the pixel's value is greater than or equal to the value of its neighbors in the direction of the gradient, the pixel's value is kept in the output.
    - Otherwise, the pixel's value is set to zero. This process eliminates all pixels that are not local maxima in the direction of the gradient.
    - Finally, the output image is scaled to have values between 0 and 255 and returned.

7. `__double_threshold_hysteresis(image, low, high):`
    - This function performs hysteresis thresholding on the input image.
    - After applying the Canny edge detection algorithm, the edges are classified as strong edges or weak edges. The thresholds for strong and weak edges are defined by the `high` and `low` values respectively.
    - The code creates a zero matrix called `result` with the same dimensions as the input image. Then, it sets the pixels that are above the high threshold to strong and the pixels that are above the low threshold but below the high threshold to weak.
    - To perform hysteresis, the code starts with a strong edge pixel and checks its 8 neighboring pixels in all directions using the `dx` and `dy` arrays. 
    - If a neighboring pixel is a weak edge pixel, it is marked as strong and added to the strong edge list. The process continues until all weak edge pixels that are connected to strong


### Histogram Class

The given class Histogram contains methods for performing image processing tasks such as histogram equalization, normalization, global and local thresholding, and color channel splitting.

1. `getImg()`
    - This method returns the image array associated with the instance.

2. `operateOn(img)`
    - This method sets the image array associated with the instance to the passed image array `img`.

3. `equalize()`
    - This method performs histogram equalization on the image array. It computes the histogram and the cumulative sum of the pixel intensities and then scales the cumulative sum to the range of [0, 255].
    - Then, it maps each pixel intensity of the input image to its corresponding intensity in the equalized image using the scaled cumulative sum.
    - The output of the function is the equalized image.

![WhatsApp Image 2023-03-14 at 8 10 57 PM](https://user-images.githubusercontent.com/68791488/225128966-fb6a8497-0232-4ff8-ad70-e66a5001c9dd.jpeg)

4. `normalize()`
    - This method normalizes the image array by dividing each pixel intensity by maximum intensity and then scaling it to a range of [0, 255].
    - The output of the function is the normalized image.
    
![WhatsApp Image 2023-03-14 at 9 02 51 PM](https://user-images.githubusercontent.com/68791488/225129270-9833f26a-5d54-4905-b2f4-e8dc3474ecb8.jpeg)


5. `applyGlobalThreshold(threshold)`
    - This method applies a global thresholding operation on the image array.
    - It sets all pixel intensities greater than the threshold to 255 and all other pixel intensities to 0. 
    - The output of the function is the thresholded image.

![WhatsApp Image 2023-03-14 at 8 11 51 PM](https://user-images.githubusercontent.com/68791488/225129172-52485c8b-81a2-473b-85ad-b8c83f73783e.jpeg)

6. `applyLocalThreshold(blockSize=10, C=5)`
    - This method applies a local thresholding operation on the image array.
    - It uses a sliding window of size blockSize to compute a local threshold for each pixel based on the mean intensity of the pixels in the window and a constant C.
    - If the intensity of the pixel is greater than or equal to the local threshold, it is set to 255, otherwise it is set to 0.
    - The output of the function is the thresholded image.
    
![WhatsApp Image 2023-03-14 at 8 11 35 PM](https://user-images.githubusercontent.com/68791488/225129114-4e9042f9-0e74-44e3-9760-d734a402bfd1.jpeg)

7. `split()`
    - This method splits the image array into its three color channels, i.e., red, green, and blue.
    - It creates three new arrays of the same size as the input image and assigns the red, green, and blue values of each pixel to their corresponding arrays.
    - The output of the function is a tuple containing the red, green, and blue arrays.


8. `getCumSum(arr)`
    - This method takes a one-dimensional array `arr` and returns its cumulative sum.

9. `grayScale()`
    - This method is a function that returns a grayscale representation of an image. It achieves this by averaging the intensity values of the red, green, and blue color channels of the image.
    - It first extracts the individual red, green, and blue color channels using the getRedFrame(), getGreenFrame(), and getBlueFrame() methods. It then divides each channel by 3 and adds them together to obtain a single grayscale value for each pixel.

![WhatsApp Image 2023-03-14 at 8 12 08 PM](https://user-images.githubusercontent.com/68791488/225129241-527bd6b1-e04f-4a3f-8d32-4149ce672d49.jpeg)


10. `getHistoGram(arr2d, bins=256)`
    - This method takes a two-dimensional array arr2d and computes its histogram using the specified number of bins.
    - It returns a one-dimensional array representing the histogram.

11. `flatten(arr2d)`
    - This method takes a two-dimensional array `arr2d` and returns a flattened one-dimensional array.

12. `getCumulative2d(img)`
    - This is a helper method that takes a two-dimensional image array and returns its two-dimensional cumulative sum array.

13. `getSumAndNum(cumulative, bottomRightX, bottomRightY, topLeftX, topLeftY)`
    - This is a helper method that takes a two-dimensional cumulative sum array `cumulative` and the coordinates of the top-left and bottom-right corners of a rectangular region and returns the sum of the pixel intensities in the region and the number of pixels in the region.


### Frequency Class

The given class Frequency contains methods for applying frequency-based image processing techniques, specifically Fourier transforms, high-pass/low-pass filtering and hybrid images.

1. `high_pass_filter(img, filter_range)`
    - This method applies a high-pass filter on the input image img. 
    - It starts by resizing the image to a fixed size (512x512). It then applies a Fourier transform on the image using the np.fft.fft2 method.
    - The Fourier transform shifts the low frequency components of the image towards the corners and high frequency components towards the center of the image.
    - The next step is to define a filter mask which will be applied on the Fourier transformed image to remove the low frequency components from the image.
    - The filter mask is a binary mask of size the same as input image with values 1 for pixels where the distance from the center of the image is greater than the filter_range and 0 otherwise. The mask is applied to the Fourier transformed image by element-wise multiplication with the np.fft.fftshift method. 
    - After applying the inverse Fourier transform to the filtered image using the np.fft.ifft2 method, it returns the absolute value of the filtered image.



2. `low_pass_filter(img, filter_range)`
    - This method applies a low-pass filter on the input image img. It starts by resizing the image to a fixed size (512x512).
    - It then applies a Fourier transform on the image using the np.fft.fft2 method.
    - The Fourier transform shifts the low frequency components of the image towards the corners and high frequency components towards the center of the image.
    - The next step is to define a filter mask which will be applied on the Fourier transformed image to remove the high frequency components from the image.
    - The filter mask is a binary mask of size the same as input image with values 1 for pixels where the distance from the center of the image is less than the filter_range and 0 otherwise.
    - The mask is applied to the Fourier transformed image by element-wise multiplication with the np.fft.fftshift method.
    - After applying the inverse Fourier transform to the filtered image using the np.fft.ifft2 method, it returns the absolute value of the filtered image.


3. `hypridImages(img1, img2)`
    - This method takes two input images img1 and img2, adds them together and returns the result as the hybrid image.
    - The hybrid image is normalized by dividing by 255 before returning.
    - This method can be used to create hybrid images by combining the low frequency components of one image with the high frequency components of another image.

Hybriding two images, high frequencies of the first first and low frequencies of the second.

![WhatsApp Image 2023-03-14 at 9 03 08 PM](https://user-images.githubusercontent.com/68791488/225130072-580bf255-50cb-4c71-8288-331972b935d6.jpeg)


Hybriding two images, low frequencies of the first first and high frequencies of the second.

![WhatsApp Image 2023-03-14 at 9 03 26 PM](https://user-images.githubusercontent.com/68791488/225130098-e262ff2f-ed82-40f4-8af2-6dbdd0cf6b18.jpeg)


### Hough Class

The given class Hough is a class that implements the Hough transform algorithm for detecting lines, circles, and ellipses in an image.
The Hough Transform is a technique that allows detecting shapes (such as lines, circles, or ellipses) in an image by looking for patterns in a transformed version of the image. The basic idea is to represent the image in a parameter space that describes the geometric properties of the shapes to be detected, and then look for high-density regions in that space, which correspond to the presence of shapes in the original image.


1. `getImg()`
    - Get the image

2. `__get_edges(img, min_edge_threshold, max_edge_threshold)`
    - The function uses the OpenCV library to perform edge detection on the input image. Specifically, it first converts the input image from BGR color space to grayscale using the cv2.cvtColor() function.
    - Then, it applies the Canny edge detection algorithm using the cv2.Canny() function, with the minimum and maximum edge thresholds as inputs. The Canny algorithm is a popular edge detection technique that uses a multi-stage process to detect a wide range of edges in an image.
    - Finally, the function returns the resulting edge image as a NumPy array.
    
3. `__superimpose(lines, color)`
    - This function takes in two arguments - lines and color.
    - The lines parameter is a list of lines represented in the polar coordinate system, where each line is a tuple containing two values - the distance r and the angle theta.
    - The color parameter is a tuple representing the color in RGB format.
    - The function first retrieves the image using the getImg() method of the class, and then creates a copy of the image using np.copy().
    - It then iterates over each line in the lines list and calculates the two endpoints of the line segment in the Cartesian coordinate system.
    - The Cartesian coordinates of the endpoints are calculated using the formula: pt = (x0 + 1000*(-b), y0 + 1000*(a)) and pt2 = (x0 - 1000*(-b), y0 - 1000*(a)).
    - Here, x0 and y0 are the coordinates of the closest point on the line to the origin (0,0) in the polar coordinate system. a and b are the sine and cosine values of theta respectively, which are calculated using math.sin() and math.cos().
    - Finally, it draws a line segment between the two endpoints using the cv2.line() function of the OpenCV library. The src image is modified in-place by this operation, and the modified image is returned at the end of the function.

4. `__hough_lines(src, threshold)`
    - This function performs the Hough Transform algorithm to detect lines in an input image. The Hough Transform is a technique used to detect straight lines in an image by converting the image space into a parameter space. In this parameter space, each point represents a possible line in the original image.
    - The function takes two inputs: src is the binary edge image in which lines are to be detected, and threshold is a value that represents the minimum number of points that must be associated with a line in the parameter space in order for that line to be considered a valid line.
    - The first step of the function is to compute the diagonal of the input image using the Pythagorean theorem. This is used to determine the dimensions of the accumulator matrix, which is a two-dimensional array used to store the votes for each possible line in the parameter space. The size of the accumulator matrix is based on the maximum possible distance between a pixel in the image and the origin, which is given by the diagonal.
    - Next, the function creates an empty accumulator matrix of size (2 * diagonal, 180), where the first dimension represents the distance of the line from the origin and the second dimension represents the angle of the line with respect to the x-axis.
    - The function then iterates over each edge pixel in the input image and calculates the Hough Transform for each edge. This involves looping over all possible angles and distances and incrementing the corresponding cell in the accumulator matrix for each point that lies on a line with that angle and distance. This process generates a matrix with peaks at the positions of the lines in the input image.
    - Finally, the function loops over all the cells in the accumulator matrix and checks if the number of votes for a particular line exceeds the threshold value. If so, the function adds the corresponding line to a list of detected lines, where each line is represented as a tuple of (distance, angle).
    - The function returns a list of detected lines.

5. `detect_lines(threshold, color)`
    - This function is used to detect lines in an image using the Hough Transform algorithm. It takes two arguments - threshold and color.
    - The threshold argument sets the minimum number of pixels required to detect a line. A higher threshold will result in fewer lines being detected, while a lower threshold will result in more lines being detected.
    - The color argument sets the color of the lines that are drawn on the image. By default, the color is set to (255, 0, 0), which is red.
    - First, the function calls the getImg method of the Image class to retrieve the image. Then it calls the private method __get_edges to detect the edges in the image using the Canny edge detection algorithm with a minimum threshold of 50.
    - Next, it calls the private method __hough_lines to detect the lines in the image using the Hough Transform algorithm. This method creates an accumulator matrix with dimensions that cover the range of possible values for r and theta in the Hough space. It then finds the location of the edges in the edge image and calculates the Hough transform for each edge, incrementing the corresponding cells in the accumulator matrix. Finally, it extracts the lines with a number of votes above the specified threshold value.
    - Finally, the function calls the private method __superimpose to draw the detected lines on the original image. This method creates a copy of the original image and iterates over the detected lines, drawing each one in the specified color. The resulting image is returned as the output of the detect_lines function.
   
![WhatsApp Image 2023-03-25 at 12 08 40 AM](https://user-images.githubusercontent.com/68791488/227657323-ea84f0cd-a436-44ed-a324-749ab7da199a.jpeg)

6. `__hough_circles(image, edge_image, r_min, r_max, delta_r, num_thetas, bin_threshold, post_process=True)`
    - This is an implementation of the Hough transform algorithm for detecting circles in an image.
    - The function takes as input the original image, an edge-detected image, and various parameters such as the minimum and maximum radius of the circles to be detected, the step size for the radius, the number of angles to use in the Hough transform, and a threshold for how many votes a circle must receive to be considered a valid candidate.
    - The function first generates a list of all possible circles in the image based on the given radius range and number of angles.
    - It then loops through each edge pixel in the edge image and for each candidate circle, calculates the center of the circle and votes for it in the accumulator.
    - The accumulator is a dictionary that keeps track of the number of votes each candidate circle has received.
    - Once all edge pixels have been processed, the circles are sorted by their vote count and those with a percentage of votes above the given threshold are shortlisted.
    - A post-processing step can be optionally applied to remove duplicate circles that are too close to each other.
    - Finally, the shortlisted circles are drawn on the output image and returned.

7. `detect_circles(self, min_radius, max_radius, threshold, color)`
    - This Function detects circles in an input image using the Hough Circle Transform. The method takes four arguments: min_radius, max_radius, threshold, and color.
    - min_radius and max_radius set the minimum and maximum radii of circles to be detected, respectively. threshold is a value between 0 and 1 that determines the minimum percentage of votes required for a circle to be considered valid. color is a tuple that specifies the color of the detected circles.
    - The method first gets the input image using the getImg() method of the class. It then applies the __get_edges() method to the image to extract the edges. The __get_edges() method uses the Canny Edge Detection algorithm to extract the edges.
    - If the edge image is not None, the method proceeds to call the __hough_circles() method with the input image, edge image, minimum radius, maximum radius, delta radius, number of thetas, and the bin threshold as arguments.
    - The __hough_circles() method applies the Hough Circle Transform to the edge image to detect circles.
    - Finally, it returns the output image which is the input image with the detected circles superimposed on it.
 
![WhatsApp Image 2023-03-25 at 12 38 35 AM](https://user-images.githubusercontent.com/68791488/227657297-f1a5bdb5-477d-4855-9c27-ee62890dc31b.jpeg)


8. `__hough_ellipses(self, image, edge_image, a_min, a_max, delta_a, b_min, b_max, delta_b, num_thetas, bin_threshold, post_process=True)`
    - This is a private method called __hough_ellipses which takes an image, an edge image (binary image with detected edges), the minimum and maximum values for the semi-major and semi-minor axes (a and b), their respective increments (delta_a and delta_b), the number of angles to consider (num_thetas), a bin threshold value (bin_threshold) and a boolean flag to perform post-processing (post_process).
    - The method uses the Hough transform to detect ellipses in the edge image.
    - The accumulator is a dictionary where the key is a tuple of ellipse parameters (x_center, y_center, a, b, t) and the value is the number of votes for that ellipse.
    - The loop over edge pixels is used to vote for all possible ellipses that pass through that point, using the ranges of a, b, and t specified as arguments.
    - The parameter t is the angle at which the major axis is oriented.
    - After all edge pixels have voted, the method sorts the accumulator by the number of votes in descending order and loops through each candidate ellipse. 
    - The current_vote_percentage is the percentage of angles that voted for that ellipse.
    - If it is greater than or equal to the bin threshold, the method checks if there are any previously found ellipses that overlap with this one. If there is no overlap, the ellipse is added to the list of ellipses found.
    - If post-processing is enabled, the method applies a pixel threshold value to filter out very similar ellipses and draws the shortlisted ellipses on the output image in red.
    - Finally, the method returns the output image with the detected ellipses drawn on it.


9. `detect_ellipses(self, min_radius1, max_radius1, min_radius2, max_radius2, threshold, color)`
    - This is a method that uses the Hough transform to detect ellipses in an input image.
    - The method takes several arguments:
       - min_radius1 and max_radius1: the minimum and maximum values for the first radius of the ellipse.
       - min_radius2 and max_radius2: the minimum and maximum values for the second radius of the ellipse.
       - threshold: the minimum percentage of votes required for an ellipse to be considered a valid detection.
       - color: the color of the ellipses to be drawn on the output image.
    - The method first calls a private method __get_edges() to extract edges from the input image using the Canny edge detection algorithm.
    - Then, it calls another private method __hough_ellipses() to perform the Hough transform on the edge image to detect ellipses.
    - The __hough_ellipses() method takes the edge image, the ranges of the two radii, the step sizes for the two radii, the number of angles to consider, and the bin threshold as arguments.
    - It initializes an accumulator dictionary and loops over all edge pixels, voting for all possible ellipses that pass through the current pixel.
    - It then finds ellipses with enough votes to be considered a valid detection, and post-processes the results to remove similar detections. 
    - Finally, it draws the shortlisted ellipses on the output image and returns it.


### Active Contour Class

The given class Active Contour is a class that provides code that implements an Active Contour model, also known as Snake model, which is a framework for performing image segmentation tasks. The model consists of a set of contour points that are iteratively adjusted to align with the boundaries of the object to be segmented. 

1. `points_distance(x1, y1, x2, y2)`
    - This function is used for calculating the distance between any two points in a two-dimensional space.

2. `circle_contour(center, radius, numberOfPoints, x_coordinates, y_coordinates)`
    - This is a function that generates the contour points of a circle given its center, radius, and the desired number of points on the contour. The function takes in five parameters:
       - center: a tuple of the (x,y) coordinates of the center of the circle
       - radius: the radius of the circle
       - numberOfPoints: the number of points on the contour
       - x_coordinates: an array to store the x-coordinates of the contour points
       - y_coordinates: an array to store the y-coordinates of the contour points
    - The function first computes the angular resolution of the contour using the formula resolution = 2 * pi / numberOfPoints. Then, it loops over numberOfPoints to compute the x and y coordinates of each point on the contour using the formulae x = center[0] + radius * cos(angle) and y = center[1] - radius * sin(angle), where angle is the angle of the current point, computed as i * resolution.
    - The x and y coordinates of each contour point are rounded to the nearest integer using the round() function and stored in the output arrays x_coordinates and y_coordinates.
    - Finally, the function returns the two arrays containing the x and y coordinates of the contour points.

3. `draw_contour(Image, numberOfPoints, x_coordinates, y_coordinates)`
    - This function draw_contour() takes four arguments: Image, numberOfPoints, x_coordinates, and y_coordinates. The Image argument is the image on which the contour will be drawn.
numberOfPoints, x_coordinates, and y_coordinates are the output of the circle_contour() function, which returns the x and y coordinates of the contour points.
    - The function then creates a variable img and sets its initial value to 0. It then loops over each point in the contour using a for loop, and for each point, it calculates the coordinates of the next point using modular arithmetic.
    - It then uses the OpenCV line() function to draw a line between the current point and the next point, with a color of (0, 255, 0) and a line thickness of 2.
    - Finally, the function converts the image from BGR format to RGB format using the cvtColor() function from OpenCV, and returns the resulting image.
    - The resulting image should show the contour drawn on top of the original image.
    
4. `contour_area(numberOfPoints, x_coordinates, y_coordinates)`
    - This function takes in the number of points, x and y coordinates of a contour and calculates its area using the shoelace formula.
    - The shoelace formula is a mathematical algorithm that calculates the area of a polygon given the coordinates of its vertices.
    - The formula gets its name from the way it works, which involves multiplying pairs of coordinates and then adding them up in a pattern that resembles lacing up a shoe.
    - The function first initializes the area variable to zero.
    - It then uses a for loop to iterate over each vertex of the contour.
    - The formula requires the use of two vertices at a time, so the function initializes a variable j to the index of the last vertex in the array.
    - The formula multiplies the x coordinate of the current vertex and the y coordinate of the previous vertex and subtracts the x coordinate of the previous vertex and the y coordinate of the current vertex. The result is added to the area variable.
    - After iterating over all vertices, the function returns the absolute value of area divided by 2, which gives the area of the polygon.

5. `contour_perimeter(x_points, y_points, points_n)`
    - The function contour_perimeter takes in the x and y coordinates of a set of points that define a contour, as well as the number of points. It then iterates over each point, calculates the distance to the next point in the sequence, and adds it to a running sum of distances.
    - Finally, the function returns the sum of distances, which corresponds to the perimeter of the contour.
      - Here's a step-by-step breakdown of what the function does:
      - Initialize a variable distance_sum to zero.
      - For each point i in the range 0 to points_n - 1, do the following:
        - a. Compute the index of the next point in the sequence using next_point = i + 1, unless i is the last point in the sequence, in which case next_point is set to zero.
        - b. Compute the distance between the current point (x_points[i], y_points[i]) and the next point (x_points[next_point], y_points[next_point]) using the points_distance function.
        - c. Add the computed distance to distance_sum.
    - Return distance_sum.
    - In summary, the contour_perimeter function calculates the length of a path formed by connecting a sequence of points.


6. `window_neighbours(size)`
    - The function window_neighbours(size) takes an input parameter size, which is the size of the square window.
    - It returns a list of coordinates representing all the neighboring points in a square window around a central point.
    - The function initializes two empty lists, window and point. 
    - It then loops through each pixel in the square window by iterating over a range of (-size // 2, size // 2 + 1) for both x and y coordinates. It creates a new list point to store the current (x, y) coordinate of the current pixel.
    - This point is then appended to the window list, which contains all neighboring points in the window.
    - For example, if the input size is 3, the window list will contain the following points:
       - [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 0], [0, 1], [1, -1], [1, 0], [1, 1]]
    - This can be used, for example, to implement a convolution operation, where the window is centered around each pixel in an image and the neighboring pixels are multiplied with a filter and summed to compute the output value for the central pixel.
    - Finally, the function returns the list of points that represents the window.

7. `convert(list)`
    - The convert() function takes a list of integers as an input argument, and returns an integer formed by concatenating all the integers in the list.
    - Here's how the function works:
       - First, it converts each integer element in the list to a string using a list comprehension: s = [str(i) for i in list]
       - Then it concatenates all the string elements in s using the join() method and converts it to an integer: res = int("".join(s))
       - Finally, it returns the integer res as the output.
    - For example, if we call convert([1, 2, 3, 4]), the function will return the integer 1234.

8. `greedy_contour(source, iterations, alpha, beta, gamma, x_points, y_points, points_n, window_size, plot)`
    - This function implements the greedy algorithm for active contours, which is a method for image segmentation.
    - It takes as input an image (source), the number of iterations (iterations), and various parameters (alpha, beta, gamma) that are used to compute the internal energy of the contour.
    - It also takes as input an initial set of points (x_points, y_points) that define the initial contour, the number of points in the contour (points_n), the size of the neighborhood window (window_size), and a boolean flag (plot) that controls whether or not to display the contour during the algorithm.
    - The function first computes the external energy of the image using the Sobel operator, which is used to attract the contour to edges in the image.
    - It then initializes some variables and enters a loop that iterates until either the number of iterations is exceeded or the number of movements of the contour is less than a threshold value (threshold).
    - In each iteration of the loop, the function considers each point in the contour and evaluates the energy of the contour if the point were to be moved to each of the neighboring points in the neighborhood window.
    - It then selects the neighboring point that results in the minimum energy, and moves the point to that position.
    - If the point is moved, the function increments a counter (movements).
    - The function also computes the internal energy of the contour, which is a measure of how smooth the contour is.
    - This is done using the internal_energy function, which takes as input the current set of points (current_x, current_y) and the various parameters (alpha, beta, gamma).
    - The internal energy is used to prevent the contour from becoming too jagged.
    - The function returns the final set of points that define the contour after the algorithm has converged.

![WhatsApp Image 2023-03-25 at 12 41 26 AM](https://user-images.githubusercontent.com/68791488/227657208-e72c150c-1e79-4fac-a5f2-7cba26b7f129.jpeg)

![WhatsApp Image 2023-03-25 at 12 38 37 AM](https://user-images.githubusercontent.com/68791488/227657212-9ed11af3-93cf-4119-bce8-89ea2fb1d938.jpeg)


9. `internal_energy(x_points, y_points, points_n, alpha, beta)`
    - This code defines a function internal_energy which takes as input x_points and y_points which represent the x and y coordinates of the points of a contour, points_n which is the number of points in the contour, alpha and beta which are weighting factors for the two types of internal energy computed, respectively.
    - The function first computes the average distance between adjacent points in the contour, which is used to compute the deviation of each distance from the average, which is squared and summed over all points to compute the "contour smoothness" energy.
    - Next, the function computes the average angle between adjacent line segments in the contour, which is used to compute the deviation of each angle from the average, which is squared and summed over all points to compute the "curvature" energy.
    - Finally, the function returns the sum of these two energy terms, weighted by alpha and beta, respectively. 
    - This represents the total internal energy of the contour.


10. `external_energy(source)`
    - The external_energy function takes an input image source and applies Gaussian filtering, edge detection using Canny algorithm, and then returns the resulting edges as a binary image.
    - The function first applies Gaussian filtering on the input image using the cv2.GaussianBlur function with a kernel size of (3, 3) and standard deviation of 0.
    - This helps to reduce noise in the image.
    - Then, it converts the filtered image to grayscale using the cv2.cvtColor function with the COLOR_BGR2GRAY flag.
    - Next, it applies edge detection on the grayscale image using the Canny algorithm with low threshold of 0 and high threshold of 255, and stores the resulting binary image in edges.
    - Finally, the function writes the resulting edges to a file named 'edges.jpg' and returns the binary image edges.


11. `normaliseToRotation(chain_code)`
    - The function normaliseToRotation takes a list of chain codes as input and returns a modified version of the list where the chain codes have been normalized to rotation.
    - The function first creates a copy of the input chain code list using the copy() method.
    - It then iterates through the list using a for loop. Inside the loop, it calculates the difference between the current chain code symbol and the next symbol by subtracting the former from the latter.
    - The result is then modulo 8 to normalize it.
    - The normalized symbol is then assigned to the next position in the copied chain code list using the index operator.
    - Finally, the function returns the modified chain code list.


12. `normaliseToStartingPoint(chaincode)`
    - This function takes a chain code as input and returns a normalized version of it, where the starting point of the contour is always the first element in the chain code.
    - To do this, the function first finds the smallest element in the chain code by sorting it, and then finds all the occurrences of that smallest element using the getAllOccurences function (which is not shown here).
    - Next, it rotates the chain code so that each occurrence of the smallest element becomes the first element in the list.
    - It then converts each rotated chain code into an integer using the convert function (which is not shown here).
    - This integer is calculated by concatenating the elements of the chain code and treating them as a base-10 number.
    - The rotated chain code that yields the smallest integer value is chosen as the normalized chain code, and returned by the function.

13. `parametersToAppend(mulByMn, mulByDx, mulByDy, mn, dx, dy)`
    - This function takes in six parameters: mulByMn, mulByDx, mulByDy, mn, dx, and dy.
mulByMn, mulByDx, and mulByDy are values that will be appended to a list multiple times, while mn, dx, and dy are integer values used to determine how many times to append each value.
    - The function starts by creating an empty list codeList.
    - It then appends the value of mulByMn to the codeList mn number of times, effectively appending mulByMn to the list mn times.
    - Next, it subtracts mn from the absolute value of dx and dy. If either value is negative, it takes the absolute value first.
    - Finally, it appends mulByDx to the codeList dx number of times, and appends mulByDy to the codeList dy number of times.
    - The function then returns the codeList which contains the appended values according to the given parameters.

14. `getCodeBetweenTwoPoints(x1, y1, x2, y2)`
    - This function generates a chain code between two points (x1, y1) and (x2, y2) using a specific set of rules for encoding the directions between the points.
    - The function first calculates the differences between the x and y coordinates of the two points, which are used to determine the direction between them.
    - It then calculates the minimum absolute difference between dx and dy, which is used to determine the number of steps required to move in each direction to reach the endpoint.
    - Based on the direction between the two points, the function selects a set of parameters to append to the chain code list using the parametersToAppend() function.
    - The parameter values are determined by a set of rules, which are based on the direction between the two points. The rules assign specific values for the multipliers of mn, dx, and dy, which are used to generate the chain code.
    - The resulting chain code is returned as a list.

15. `getChainCode(contourX, contourY)`
    - This function takes two lists of x and y coordinates that represent the contour of an object in an image.
    - It then iterates over the points in the contour, and for each point, it calls the getCodeBetweenTwoPoints function to calculate the chain code for the line segment between that point and the next point in the contour.
    - The chain codes are appended to a list chaincode.
    - After calculating the chain codes for all the line segments in the contour, the function normalizes the chain code twice: first to rotation, using the normaliseToRotation function, and then to starting point, using the normaliseToStartingPoint function.
    - The three chain codes (original, normalized to rotation, and normalized to starting point) are then returned as a tuple.



## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/new-feature`
3. Make changes and commit them: `git commit -m "Add new feature"`
4. Push the changes to the branch: `git push origin feature/new-feature`
5. Submit a pull request

## Developers

<table align="center">
  <tr>
    <td align="center"><a href="https://github.com/AhmedRaouf481"><img src="https://avatars.githubusercontent.com/u/62951712?v=4" width="100px;" alt=""/><br /><sub><b>Ahmed Abdelraouf</b></sub></a></td>
    <td align="center"><a href="https://github.com/Zeyad-Amr"><img src="https://avatars.githubusercontent.com/u/68791488?v=4" width="100px;" alt=""/><br /><sub><b>Zeyad Amr</b></sub></a></td>
    <td align="center"><a href="https://github.com/momen882001"><img src="https://avatars.githubusercontent.com/u/84360276?v=4" width="100px;" alt=""/><br /><sub><b>Mo'men Mohamed</b></sub></a></td>
    <td align="center"><a href="https://github.com/michaelhany510"><img src="https://avatars.githubusercontent.com/u/69060386?v=4" width="100px;" alt=""/><br /><sub><b>Micheal Hany</b></sub></a></td>
    <td align="center"><a href="https://github.com/Mazen-Aboulkhair"><img src="https://avatars.githubusercontent.com/u/84642500?v=4" width="100px;" alt=""/><br /><sub><b>Mazen Tarek</b></sub></a></td>
  </tr>
</table>

