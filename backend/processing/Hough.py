import math
import cv2
import numpy as np
import math
from collections import defaultdict


class Hough:
    def __init__(self, img):
        self.img = img

    def getImg(self):
        return self.img

    def __get_edges(self, img, min_edge_threshold=100, max_edge_threshold=200):

        # convert to gray scale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Edge detection on the input image
        edge_image = cv2.Canny(
            gray_image, min_edge_threshold, max_edge_threshold)
        return edge_image

    def __superimpose(self, lines, color):
        img = self.getImg()
        src = np.copy(img)
        for i in range(len(lines)):
            r, theta = lines[i]
            pt1, pt2 = (0, 0), (0, 0)
            a, b = math.cos(math.radians(theta)), math.sin(math.radians(theta))
            x0, y0 = a * r, b * r
            pt1 = (int(x0 + 1000 * (-b)), int(y0 + 1000 * (a)))
            pt2 = (int(x0 - 1000 * (-b)), int(y0 - 1000 * (a)))
            cv2.line(src, pt1, pt2, color, 1, cv2.LINE_AA)
        return src

    def __hough_lines(self, src, threshold):
        diagonal = math.ceil(
            math.sqrt(src.shape[0] * src.shape[0] + src.shape[1] * src.shape[1]))
        # declare the accumulator matrix as zero matrix
        acc = np.zeros((2 * diagonal, 180), dtype=np.uint8)
        lines = []

        # find the location of edges
        rows, cols = np.nonzero(src)

        cos_theta = np.cos(np.radians(np.arange(-90, 90)))
        sin_theta = np.sin(np.radians(np.arange(-90, 90)))
        for row, col in zip(rows, cols):
            # calculate the hough transform for each edge
            r = np.round(col * cos_theta + row * sin_theta)
            acc[r.astype(int), np.arange(180)] += 1

        for i in range(acc.shape[0]):
            for j in range(acc.shape[1]):
                if acc[i, j] >= threshold:
                    lines.append((i, j - 90))

        return lines

    def detect_lines(self, threshold, color=(255, 0, 0)):
        img = self.getImg()
        edges = self.__get_edges(img, 50)
        lines = self.__hough_lines(edges, threshold)
        # draw the lines on the original image
        res = self.__superimpose(lines, color)

        return res

    def __hough_circles(self, image, edge_image, r_min, r_max, delta_r, num_thetas, bin_threshold, post_process=True):
        # image size
        img_height, img_width = edge_image.shape[:2]

        # R and Theta ranges
        dtheta = int(360 / num_thetas)

        # Theta ranges from 0 to 360
        thetas = np.arange(0, 360, step=dtheta)

        # Radius ranges from r_min to r_max
        rs = np.arange(r_min, r_max, step=delta_r)

        # Calculate Cos(theta) and Sin(theta) it will be required later
        cos_thetas = np.cos(np.deg2rad(thetas))
        sin_thetas = np.sin(np.deg2rad(thetas))

        circle_candidates = []

        # Generate all possible circles
        for r in rs:
            for t in range(num_thetas):
                circle_candidates.append(
                    (r, int(r * cos_thetas[t]), int(r * sin_thetas[t])))

        accumulator = defaultdict(int)

        # Loop through all the edge pixels
        for y in range(img_height):
            for x in range(img_width):
                if edge_image[y][x] != 0:  # white pixel

                    for r, rcos_t, rsin_t in circle_candidates:
                        x_center = x - rcos_t
                        y_center = y - rsin_t
                        # vote for current candidate
                        accumulator[(x_center, y_center, r)] += 1

        output_img = image.copy()

        out_circles = []

        # Sort the accumulator based on the votes for the candidate circles
        for candidate_circle, votes in sorted(accumulator.items(), key=lambda i: -i[1]):
            x, y, r = candidate_circle
            current_vote_percentage = votes / num_thetas
            if current_vote_percentage >= bin_threshold:
                # Shortlist the circle for final result
                out_circles.append((x, y, r, current_vote_percentage))
                print(x, y, r, current_vote_percentage)

        # Post process the results, can add more post processing later.
        if post_process:
            pixel_threshold = 5
            postprocess_circles = []
            for x, y, r, v in out_circles:

                if all(abs(x - xc) > pixel_threshold or abs(y - yc) > pixel_threshold or abs(r - rc) > pixel_threshold for xc, yc, rc, v in postprocess_circles):
                    postprocess_circles.append((x, y, r, v))
            out_circles = postprocess_circles

        # Draw shortlisted circles on the output image
        for x, y, r, v in out_circles:
            # draw red circle
            output_img = cv2.circle(output_img, (x, y), r, (0, 0, 255), 5)

        return output_img

    def detect_circles(self, min_radius=10, max_radius=200, threshold=0.4, color=(255, 0, 0)):
        img = self.getImg()

        delta_r = 1
        num_thetas = 100

        edge_image = self.__get_edges(img)

        if edge_image is not None:

            print("Detecting Hough Circles Started!")
            circle_img = self.__hough_circles(
                img, edge_image, min_radius, max_radius, delta_r, num_thetas, threshold)
            return circle_img

        else:
            print("Error in input image!")
            return img

    def __hough_ellipses(self, image, edge_image, a_min, a_max, delta_a, b_min, b_max, delta_b, num_thetas, bin_threshold, post_process=True):
        # Image size
        img_height, img_width = edge_image.shape[:2]

        # Ranges for semi-major axis, semi-minor axis, and theta
        a_range = np.arange(a_min, a_max, delta_a)
        b_range = np.arange(b_min, b_max, delta_b)
        dtheta = int(360 / num_thetas)
        theta_range = np.arange(0, 360, step=dtheta)

        # Precompute sin and cos values for each theta
        sin_thetas = np.sin(np.deg2rad(theta_range))
        cos_thetas = np.cos(np.deg2rad(theta_range))

        # Initialize accumulator
        accumulator = defaultdict(int)

        # Loop over edge pixels
        for y in range(img_height):
            for x in range(img_width):
                if edge_image[y][x] != 0:  # White pixel

                    # Vote for all possible ellipses that pass through this point
                    for a in a_range:
                        for b in b_range:
                            for t in range(num_thetas):
                                x_center = x - a * cos_thetas[t]
                                y_center = y - b * sin_thetas[t]
                                accumulator[(x_center, y_center, a, b, t)] += 1

        # Find ellipses with enough votes to be considered
        output_img = image.copy()
        ellipses = []
        for candidate_ellipse, votes in sorted(accumulator.items(), key=lambda i: -i[1]):
            x, y, a, b, t = candidate_ellipse
            current_vote_percentage = votes / num_thetas

            if current_vote_percentage >= bin_threshold:
                # Check if there are any previously found ellipses that overlap with this one
                overlap = False
                for ellipse in ellipses:
                    # Compute distance between centers and angle difference
                    dx = ellipse[0] - x
                    dy = ellipse[1] - y
                    dt = np.abs(ellipse[4] - t)
                    if dt > 180:
                        dt = 360 - dt

                    # Compute the sum of the radii of the two ellipses
                    r_sum = np.sqrt(
                        ellipse[2]**2 + ellipse[3]**2) + np.sqrt(a**2 + b**2)

                    # If the centers are close enough and the angles are similar enough, consider these ellipses as overlapping
                    if np.sqrt(dx**2 + dy**2) < r_sum and dt < 15:
                        overlap = True
                        break

                if not overlap:
                    # Add this ellipse to the list of found ellipses
                    ellipses.append((x, y, a, b, t, current_vote_percentage))
                    print(x, y, a, b, t, current_vote_percentage)

        # Post-process the results
        if post_process:
            pixel_threshold = 5
            postprocess_ellipses = []
            for x, y, a, b, angle, v in out_ellipses:
                # Check if this ellipse is very similar to another already found ellipse
                is_similar = False
                for xe, ye, ae, be, ang, ve in postprocess_ellipses:
                    if abs(x - xe) <= pixel_threshold and abs(y - ye) <= pixel_threshold and abs(a - ae) <= pixel_threshold and abs(b - be) <= pixel_threshold and abs(angle - ang) <= 10:
                        is_similar = True
                        break
                if not is_similar:
                    postprocess_ellipses.append((x, y, a, b, angle, v))
            out_ellipses = postprocess_ellipses

        # Draw shortlisted ellipses on the output image
        for x, y, a, b, angle, v in out_ellipses:
            # Convert ellipse parameters to OpenCV's format
            center = (x, y)
            axes = (a, b)
            angle = angle - 90  # Convert angle from degrees to OpenCV's format
            # Draw red ellipse
            output_img = cv2.ellipse(
                output_img, center, axes, angle, 0, 360, (0, 0, 255), 5)

        return output_img

    def detect_ellipses(self, min_radius1=10, max_radius1=200, min_radius2=10, max_radius2=200, threshold=0.4, color=(255, 0, 0)):
        img = self.getImg()

        delta_r1 = 1
        delta_r2 = 1
        num_thetas = 100

        edge_image = self.__get_edges(img)

        if edge_image is not None:

            print("Detecting Hough Ellipse Started!")

            ellipse_img = self.__hough_ellipses(
                img, edge_image, min_radius1, max_radius1, delta_r1, min_radius2, max_radius2, delta_r2, num_thetas, threshold)
            return ellipse_img

        else:
            print("Error in input image!")
            return img
