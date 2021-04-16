import roslib
import rospy
import numpy as np
import cv2

from geometry_msgs.msg import TransformStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix

class TargetIdentifier():
    def __init__(self):
        self.pixels = []

        self.k_matrix = np.array([[604.62, 0, 320.5],
                                  [0, 604.62, 180.5],
                                  [0, 0, 1]])

        self.k_inv = np.linalg.inv(self.k_matrix)

        return

    def identify_obstacle(self, img_original):
        edge = cv2.Canny(img_original, 50, 100)
        img2 = cv2.GaussianBlur(edge, (5, 5), cv2.BORDER_DEFAULT)

        _,contours, _ = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        center_list = []
        radius_list = []
        dist_thresh = 2
        rad_thresh = 15

        for contour in contours:
            (x, y), radius = cv2.minEnclosingCircle(contour)

            sum_diff = 0
            for c in contour:
                dist = np.sqrt((c[0][0] - x) ** 2 + (c[0][1] - y) ** 2)
                diff = abs(dist - radius)
                sum_diff += diff
            sum_diff /= len(contour)
            if sum_diff < dist_thresh and radius > rad_thresh:
                if len(contour) > 20:
                    center_list.append((int(x), int(y)))
                    radius_list.append((int(x), int(y)+int(radius)))

        return center_list, radius_list

    def identify_landmark(self,img_original):
        edge = cv2.Canny(img_original, 50, 100)
        img2 = cv2.GaussianBlur(edge, (5, 5), cv2.BORDER_DEFAULT)

        _, contours, _ = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        center_list = []

        for contour in contours:
            rect = cv2.minAreaRect(contour)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            width = rect[1][0]
            height = rect[1][1]
            center = rect[0]

            if width > 170 and height > 170:
                center_list.append((int(center[0]), int(center[1])))

        return center_list

