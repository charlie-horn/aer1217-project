#!/usr/bin/env python2

"""ROS Node for publishing desired positions."""

from __future__ import division, print_function, absolute_import

# Import ROS libraries
import roslib
import rospy
import numpy as np

from geometry_msgs.msg import TransformStamped, Twist
from tf.transformations import euler_from_quaternion, quaternion_from_euler

from ros_interface import ROSControllerNode
from numpy import floor

class ROSDesiredPositionGenerator(object):
    """ROS interface for publishing desired positions."""
    # write code here for desired position trajectory generator
    def __init__(self):
<<<<<<< HEAD
        # subscriber & publisher
        self.vicon_topic = '/vicon/ARDroneCarre/ARDroneCarre'
        self.sub_vicon = rospy.Subscriber(self.vicon_topic, TransformStamped, self.get_vicon_data)
        self.pub_traj = rospy.Publisher('/desired_position', Twist, queue_size=10)

        # initialize parameters
=======
        self.vicon_topic = '/vicon/ARDroneCarre/ARDroneCarre'
        self.sub_vicon = rospy.Subscriber(self.vicon_topic, TransformStamped, self.get_vicon_data)
        self.pub_traj = rospy.Publisher('/desired_position', Twist, queue_size=10)
        #self.path_des = 'lin' #'cir'

        self.freq = 3 #10 #50

>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        self.x_des = []
        self.y_des = []
        self.z_des = []
        self.yaw_des = []
<<<<<<< HEAD
=======
        self.count = 0
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb

        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0

<<<<<<< HEAD
        self.count = 0
        self.thresh = 0.1

        self.freq = 3
        
        # select trajectory
        self.total_count = 2  # num of waypoints: 2 points for linear, 25 points for circular
        self.linear(self.total_count / 2)
        # self.total_count = 25  # num of waypoints: 2 points for linear, 25 points for circular
        # self.circular(self.total_count / 2)

        self.path_des = 'lin'  # 'cir'  # parameter for circular v2
	
	self.traj_timer = rospy.Timer(rospy.Duration(1. / self.freq), self.pub_des_pos)

    def linear(self, n):
        # linear trajectory: n - [int] - 0.5 * num of waypoints
=======
        self.total_count = 2 # 2 points for linear, 25 points for circular
        self.thresh = 0.1
        self.linear(self.total_count/2)
        #self.circular(self.total_count / 2)
        self.traj_timer = rospy.Timer(rospy.Duration(1. / self.freq), self.pub_des_pos)

    def linear(self, n):
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        x1 = np.linspace(-1, 1, n)
        x2 = np.linspace(1, -1, n)
        self.x_des = np.concatenate((x1, x2))

        y1 = np.linspace(-1, 1, n)
        y2 = np.linspace(1, -1, n)
        self.y_des = np.concatenate((y1, y2))

        z1 = np.linspace(1, 2, n)
        z2 = np.linspace(2, 1, n)
        self.z_des = np.concatenate((z1, z2))

<<<<<<< HEAD
        self.yaw_des = np.zeros(2*n)

    def circular(self, n):
        # circular trajectory: n - [int] - 0.5 * num of waypoints
        r = 1
        theta = np.linspace(0, 2*np.pi, n*2)

=======
        self.yaw_des = np.zeros(2*n) #?

    def circular(self, n):
        r = 1
        theta = np.linspace(0, 2*np.pi, n*2)
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        self.x_des = np.cos(theta) * r
        self.y_des = np.sin(theta) * r

        z1 = np.linspace(0.5, 1.5, n)
        z2 = np.linspace(1.5, 0.5, n)
        self.z_des = np.concatenate((z1, z2))

<<<<<<< HEAD
        self.yaw_des = np.linspace(-np.pi, np.pi, n*2)


    def get_vicon_data(self, vicon_msg):
        # callback function for vicon
        # get actual current position and yaw
=======
        #self.yaw_des = np.zeros(2 * n)

        self.yaw_des = np.linspace(-np.pi, np.pi, n*2)

    # callback function for vicon
    def get_vicon_data(self, vicon_msg):
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        self.x = vicon_msg.transform.translation.x
        self.y = vicon_msg.transform.translation.y
        self.z = vicon_msg.transform.translation.z
        quaternion = np.array([vicon_msg.transform.rotation.x,
                               vicon_msg.transform.rotation.y,
                               vicon_msg.transform.rotation.z,
                               vicon_msg.transform.rotation.w])
        euler = euler_from_quaternion(quaternion)
        self.yaw = euler[2]

    def pub_des_pos(self, i):
<<<<<<< HEAD
        # publish desired position
=======
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        msg = Twist()
        msg.linear.x = self.x_des[self.count]
        msg.linear.y = self.y_des[self.count]
        msg.linear.z = self.z_des[self.count]
        msg.angular.z = self.yaw_des[self.count]

        self.pub_traj.publish(msg)
<<<<<<< HEAD

        # update count if the difference between the actual position and the desired position is less than the threshold
        update_count = self.check_dist(self.x_des[self.count], self.x) and \
                       self.check_dist(self.y_des[self.count], self.y) and \
                       self.check_dist(self.z_des[self.count], self.z) and \
                       self.yaw_check(self.yaw_des[self.count], self.yaw)

        ############################ circular v2 - only 2 checkpoints ########################
=======
        
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
#         if self.path_des == 'cir' or self.path_des == 'lin':
#             if  self.count == 0 or self.count == floor(self.total_count/2)-1:
#                 update_count = self.check_dist(self.x_des[self.count], self.x) and \
#                                self.check_dist(self.y_des[self.count], self.y) and \
#                                self.check_dist(self.z_des[self.count], self.z) and \
#                                self.yaw_check(self.yaw_des[self.count], self.yaw)
#             else:
#                 update_count = 1
#         else:
#             update_count = self.check_dist(self.x_des[self.count], self.x) and \
#                            self.check_dist(self.y_des[self.count], self.y) and \
#                            self.check_dist(self.z_des[self.count], self.z) and \
#                            self.yaw_check(self.yaw_des[self.count], self.yaw)
<<<<<<< HEAD
        #######################################################################################
=======

        update_count = self.check_dist(self.x_des[self.count], self.x) and \
                       self.check_dist(self.y_des[self.count], self.y) and \
                       self.check_dist(self.z_des[self.count], self.z) and \
                       self.yaw_check(self.yaw_des[self.count], self.yaw)
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb

        if update_count:
            if self.count < self.total_count-1:
                self.count += 1
<<<<<<< HEAD
            else:
                self.count = 0


    def check_dist(self, des, act):
        # check difference between desired and actual position to determine if proceed
=======
                print('x = '.format(self.x_des[self.count]))
                print('y = '.format(self.y_des[self.count]))
                print('z = '.format(self.z_des[self.count]))
            else:
                self.count = 0

    # check distance of desired and actual value to determine if proceed
    def check_dist(self, des, act):
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        if abs(des - act) > self.thresh:
            return False
        else:
            return True

    def yaw_check(self,des,act):
<<<<<<< HEAD
        # check difference between desired and actual yaw to determine if proceed
        yaw_error = des - act
        if yaw_error > np.pi: # wrap to pi
=======
        yaw_error = des - act
        if yaw_error > np.pi:
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
            yaw_error = yaw_error - 2 * np.pi
        if yaw_error > self.thresh:
            return False
        else:
            return True

<<<<<<< HEAD

if __name__ == '__main__':
    rospy.init_node('desired_positions')
    ROSDesiredPositionGenerator()
    rospy.spin()
=======
if __name__ == '__main__':
    rospy.init_node('desired_positions')
    ROSDesiredPositionGenerator()
    rospy.spin()
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
