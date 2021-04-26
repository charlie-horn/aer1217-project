import roslib
import rospy
import numpy as np
import cv2
import math

from geometry_msgs.msg import TransformStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix,euler_from_matrix

class TargetIdentifier():
    def __init__(self):
        self.pixels = []

        self.k_matrix = np.array([[604.62, 0, 320.5],
                                  [0, 604.62, 180.5],
                                  [0, 0, 1]])

        self.k_inv = np.linalg.inv(self.k_matrix)

        return

    def identify_obstacle(self, img_original):
        # image pre-processing
        edge = cv2.Canny(img_original, 50, 100)
        img2 = cv2.GaussianBlur(edge, (5, 5), cv2.BORDER_DEFAULT)

        # find contour
        _,contours, _ = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        center_list = []
        radius_list = []

        # parameter
        dist_thresh = 2
        rad_thresh = 15

        for contour in contours:
            # find the minimun enclosing circle for each contour
            (x, y), radius = cv2.minEnclosingCircle(contour)

            # calculate distance btw points of contour and centroids
            total_diff = 0
            for c in contour:
                dist = np.sqrt((c[0][0] - x) ** 2 + (c[0][1] - y) ** 2)
                diff = abs(radius - dist)
                total_diff += diff

            avg_diff = total_diff / len(contour)

            # avg_diff within the threshold -> circle
            # radius > threshold -> true detection
            if avg_diff < dist_thresh and radius > rad_thresh:
                center_list.append((int(x), int(y)))
                radius_list.append((int(x), int(y)+int(radius)))

        return center_list, radius_list

    def identify_landmark(self,img_original,pos):
        # image pre-processing
        edge = cv2.Canny(img_original, 50, 100)
        img2 = cv2.GaussianBlur(edge, (5, 5), cv2.BORDER_DEFAULT)

        # find contour
        _, contours, _ = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        center_list = []
        crop_img = []
        yaw_list = []

        for contour in contours:
            # find the minimum area rectangle for each contour
            rect = cv2.minAreaRect(contour)
            width = rect[1][0]
            height = rect[1][1]
            center = rect[0]

            # convert to box format to get corner location
            box = cv2.boxPoints(rect)

            # if both width and height are greater than the threshold -> true detection
            if width > 170 and height > 170:

                center_list.append((int(center[0]), int(center[1])))

                # crop landmark region from original image for further process
                x = box[:, 0]
                y = box[:, 1]
                x_min, x_max = max(int(min(x)), 0), min(int(max(x)), 640)
                y_min, y_max = max(int(min(y)), 0), min(int(max(y)), 360)
                crop_img.append(img_original[y_min:y_max, x_min:x_max])

                # calculate current yaw angle of drone
                quaternion = np.array([pos.transform.rotation.x,
                                       pos.transform.rotation.y,
                                       pos.transform.rotation.z,
                                       pos.transform.rotation.w])
                r_matrix = quaternion_matrix(quaternion)

                _, _, yaw = euler_from_matrix(r_matrix, 'rxyz')
                yaw_list.append(yaw)

        return center_list, crop_img, yaw_list



