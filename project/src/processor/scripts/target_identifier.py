import roslib
import rospy
import numpy as np
import cv2

from geometry_msgs.msg import TransformStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix

class TargetIdentifier():
    def __init__(self):
        self.pixels = []

        self.k_matrix = np.array([[698.86, 0, 306.91],
                                  [0, 699.13, 150.34],
                                  [0, 0, 1]])
        self.k_inv = np.linalg.inv(self.k_matrix)

        self.d = np.array([0.191887, -0.563680, -0.003676, -0.002037, 0])

        return

    def img_undist(self,img):

        img_undistort = cv2.undistort(img, self.k_matrix, self.d, None)

        return img_undistort

    def identify_targets(self, img_original):
          img_undistort = cv2.undistort(img_original, self.k_matrix, self.d, None)
          img2 = cv2.cvtColor(img_undistort, cv2.COLOR_RGB2GRAY)
          _,mask = cv2.threshold(img2,150,255,cv2.THRESH_BINARY)
          img2 = cv2.bitwise_and(img2, img2,mask = mask)
          _, contours, _ = cv2.findContours(img2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
          contour_list = []
          center_list = []
          cX = 0
          cY = 0
          for contour in contours:
              approx = cv2.approxPolyDP(contour,0.02*cv2.arcLength(contour,True),True)
              area = cv2.contourArea(approx)
              (x,y),radius = cv2.minEnclosingCircle(approx)
              center = (int(x),int(y))
              radius = int(radius)
              if (radius > 10 and radius < 23  and area > 500 and area < 1250):
                  contour_list.append(contour)
                  M = cv2.moments(contour)
                  cX = int(M["m10"] / M["m00"])
                  cY = int(M["m01"] / M["m00"])
                  center_list.append([cX, cY])
          
          return center_list
    
        # img2 = cv2.inRange(img, (140, 140, 140), (160, 160, 160))
        #
        # _, contours, _ = cv2.findContours(binary_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        #
        # center_list = []
        # rad_list = []
        # contour_list = []
        # dist_thresh = 2
        # rad_thresh = 10
        # for contour in contours:
        #     (x, y), radius = cv2.minEnclosingCircle(contour)
        #     sum_diff = 0
        #     for con in contour:
        #         dist = np.sqrt((con[0][0] - x) ** 2 + (con[0][1] - y) ** 2)
        #         diff = abs(dist - radius)
        #         sum_diff += diff
        #     sum_diff /= len(contour)
        #     # print(sum_diff)
        #     if sum_diff < dist_thresh and radius > rad_thresh:
        #         center_list.append((int(x), int(y)))
        #         rad_list.append(radius)
        #         contour_list.append(contour)
