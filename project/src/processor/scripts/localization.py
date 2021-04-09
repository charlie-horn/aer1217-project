import roslib
import rospy
import numpy as np

from geometry_msgs.msg import TransformStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler, quaternion_matrix

class Localizer():
    def __init__(self):
        #self.best_guess = np.empty((2,6))
        
        # T_cb
        self.b2c = np.array([[0, -1, 0, 0],
                             [-1, 0, 0, 0],
                             [0, 0, -1, 0],
                             [0, 0, 0, 1]])
        
        # T_bc
        self.c2b = np.linalg.inv(self.b2c)
        
        # camera intrinsic matrix 
        self.k_matrix = np.array([[698.86, 0, 306.91],
                                  [0, 699.13, 150.34],
                                  [0, 0, 1]])

        self.k_inv = np.linalg.inv(self.k_matrix)


    def transform_b2v(self, pos):
        # T_vb
        b2v = np.identity(4)
        b2v[0, 3] = pos.transform.translation.x
        b2v[1, 3] = pos.transform.translation.y
        b2v[2, 3] = pos.transform.translation.z

        quaternion = np.array([pos.transform.rotation.x,
                               pos.transform.rotation.y,
                               pos.transform.rotation.z,
                               pos.transform.rotation.w])
        r_matrix = quaternion_matrix(quaternion)

        b2v[0:3, 0:3] = r_matrix[0:3, 0:3]
        return b2v

    def localize(self, pixel, pos):
        coord_list = []

        for i in range(len(pixel)):
            pixel_coord = np.array([pixel[i][0], pixel[i][1], 1]).reshape(-1, 1)  # xs, ys
            normal_proj = np.dot(self.k_inv, pixel_coord)  # xn, yn
            xn = normal_proj[0][0]
            yn = normal_proj[1][0]

            b2v = self.transform_b2v(pos) # T_vb
            c2v = b2v.dot(self.c2b) # T_vc

            z = pos.transform.translation.z # height of the drone
            
            p_cam = np.array([xn*z, yn*z, z, 1]) # location of camera frame
            p_vic = np.dot(c2v, p_cam) # transform from camera frame to vicon frame

            coord = p_vic[:2] # 2D coordinates
            coord_list.append(coord)

        return coord_list






