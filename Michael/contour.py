import numpy as np
import cv2
import math
import matplotlib.pyplot as plt


def points_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)
def is_point_inside_polygon(x_list, y_list, x, y):
    """
    Determines whether a point is inside a closed polygon.

    Parameters:
        x_list (list): A list of x-coordinates of the polygon vertices in order.
        y_list (list): A list of y-coordinates of the polygon vertices in order.
        x (float): The x-coordinate of the point to test.
        y (float): The y-coordinate of the point to test.

    Returns:
        bool: True if the point is inside the polygon, False otherwise.
    """
    n = len(x_list)
    inside = False
    p1x, p1y = x_list[0], y_list[0]
    for i in range(1, n + 1):
        p2x, p2y = x_list[i % n], y_list[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
        p1x, p1y = p2x, p2y
    return inside


def circle_contour(center, radius, numberOfPoints, x_coordinates, y_coordinates):
    # Compute the angular resolution of the contour
    resolution = 2 * np.pi / numberOfPoints

    # Generate the contour points
    for i in range(numberOfPoints):
        # Compute the angle of the current contour point
        angle = i * resolution

        # Compute the x and y coordinates of the current contour point
        x = center[0] + radius * np.cos(angle)
        y = center[1] - radius * np.sin(angle)

        # Store the coordinates in the output arrays
        x_coordinates[i] = int(round(x))
        y_coordinates[i] = int(round(y))
    return x_coordinates,y_coordinates

def draw_contour(Image, numberOfPoints, x_coordinates, y_coordinates):
    for i in range(numberOfPoints):
        next = (i + 1) % numberOfPoints
        img = cv2.line(Image, (y_coordinates[i], x_coordinates[i]), (y_coordinates[next], x_coordinates[next]), (255, 0, 0), 2)
    # plt.imshow(img)
    # plt.axis('off')
    # plt.show()

def contour_area(numberOfPoints, x_coordinates, y_coordinates):
    area = 0.0
    # Calculate value of shoelace formula => 1/2 [ (x1y2 + x2y3 + … + xn-1yn + xny1) – (x2y1 + x3y2 + … + xnyn-1 + x1yn) ]
    j = numberOfPoints - 1
    for i in range(numberOfPoints):
        area += (x_coordinates[j] + x_coordinates[i]) * (y_coordinates[j] - y_coordinates[i])
        j = i # j is previous vertex to i
    return abs(area / 2.0)

def contour_perimeter(x_points, y_points, points_n):
    distance_sum = 0
    for i in range(points_n):
        next_point = i + 1
        if i == points_n - 1:
            next_point = 0

        distance = points_distance(x_points[i], y_points[i], x_points[next_point], y_points[next_point])
        distance_sum += distance
    return distance_sum


def internal_energy(x_points, y_points, points_n, alpha, beta):
    curv_sum = 0
    cont_sum = 0
    avg_dist = contour_perimeter(x_points, y_points, points_n) / points_n

    # Compute the average angle between adjacent line segments
    avg_angle = 0
    for i in range(points_n):
        next_point = (i + 1) % points_n
        dx = x_points[next_point] - x_points[i]
        dy = y_points[next_point] - y_points[i]
        angle = math.atan2(dy, dx)
        if angle < 0:
            angle += 2 * math.pi
        avg_angle += angle
    avg_angle /= points_n

    # Compute the energy due to contour smoothness and curvature
    for i in range(points_n):
        next_point = (i + 1) % points_n
        prev_point = (i + points_n - 1) % points_n

        # Compute the distance between adjacent contour points
        dist = points_distance(x_points[i], y_points[i], x_points[next_point], y_points[next_point])

        # Compute the deviation from the desired distance
        cont_dev = dist - avg_dist
        cont_sum += cont_dev * cont_dev

        # Compute the angle deviation between adjacent line segments
        dx1 = x_points[i] - x_points[prev_point]
        dy1 = y_points[i] - y_points[prev_point]
        dx2 = x_points[next_point] - x_points[i]
        dy2 = y_points[next_point] - y_points[i]
        angle1 = math.atan2(dy1, dx1)
        angle2 = math.atan2(dy2, dx2)
        if angle1 < 0:
            angle1 += 2 * math.pi
        if angle2 < 0:
            angle2 += 2 * math.pi
        curv_sum += abs(angle1 - angle2 - avg_angle) * abs(angle1 - angle2 - avg_angle)

    energy = alpha * cont_sum + beta * curv_sum
    return energy

def external_energy(source):
    filtered_Gaussian = cv2.GaussianBlur(source, (3, 3), 0)
    gray = cv2.cvtColor(filtered_Gaussian, cv2.COLOR_BGR2GRAY)
    edges = (cv2.Canny(gray, 0, 255))
    # cv2.imshow('Grayscale Image', gray_img)
    

    # Convert the image to grayscale
    gray_img = cv2.cvtColor(filtered_Gaussian, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('edges.jpg',edges)
    # Show the grayscale image
    plt.imshow(edges, cmap='gray')
    plt.axis('off')
    plt.show()
    return edges


def window_neighbours(size):
    window = []
    point = []


    for i in range(-size // 2, size // 2 + 1):
        for j in range(-size // 2, size // 2 + 1):
            point = [i, j]
            window.append(point)

    return window

def greedy_contour(source, iterations, alpha, beta, gamma, x_points, y_points, points_n, window_size, plot):
    sobel_energy = external_energy(source)
    window = window_neighbours(window_size)
    current_x = np.zeros(180)
    current_y = np.zeros(180)


    plot_img = None
    point_energy = 0
    min_energy = 0
    min_index = 0
    movements = 0
    iteration = 0
    loob = True
    threshold = 10
    neighbours_size = pow(window_size, 2)

    while loob:
        movements = 0

        for i in range(points_n):
            min_energy = float('inf')

            for j in range(neighbours_size):
                current_x[i] = x_points[i] + window[j][0]
                current_y[i] = y_points[i] + window[j][1]

                # if not is_point_inside_polygon(x_points,y_points,current_x[i],current_y[i]):
                #     continue

                if (current_x[i] < sobel_energy.shape[0] and current_x[i] > 0 and current_y[i] > 0 and current_y[i] < sobel_energy.shape[1]):
                    # print(current_x[i],current_y[i])
                    point_energy = sobel_energy[int( current_x[i]),int( current_y[i])] * -1 * gamma + internal_energy(current_x, current_y,points_n, alpha, beta)

                    if point_energy < min_energy:
                        min_energy = point_energy
                        min_index = j

            if min_energy < float('inf'):
                x_points[i] = x_points[i] + window[min_index][0]
                y_points[i] = y_points[i] + window[min_index][1]

                if window[min_index][0] != 0 or window[min_index][1] != 0:
                    movements += 1

        iteration += 1
        # plt.imshow(cv2.cvtColor(source, cv2.COLOR_BGR2RGB))
        # plt.scatter(current_x,current_y, s=5, c='r')
        # plt.show()
        if plot == True:
            plot_img = sobel_energy.copy()
            
            draw_contour(plot_img, points_n, x_points, y_points)
            cv2.imshow("Active Contour", plot_img)
            cv2.waitKey(10)
        print(iteration)
        if iteration > iterations or movements < threshold:
            loob = False
            # cv2.waitKey(0)
            break
            

    return x_points,y_points