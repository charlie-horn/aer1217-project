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
        self.vicon_topic = '/vicon/ARDroneCarre/ARDroneCarre'
        self.sub_vicon = rospy.Subscriber(self.vicon_topic, TransformStamped, self.get_vicon_data)
        self.pub_traj = rospy.Publisher('/desired_position', Twist, queue_size=10)
        #self.path_des = 'lin' #'cir'

        self.freq = 3 #10 #50

        self.x_des = []
        self.y_des = []
        self.z_des = []
        self.yaw_des = []
        self.count = 0

        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0

        self.total_count = 2 # 2 points for linear, 25 points for circular
        self.thresh = 0.1
        self.linear(self.total_count/2)
        #self.circular(self.total_count / 2)
        self.traj_timer = rospy.Timer(rospy.Duration(1. / self.freq), self.pub_des_pos)

    def set_path(self, path):
        for point in path[1:]:
            while 
        return

    def linear(self, n):
        x1 = np.linspace(-1, 1, n)
        x2 = np.linspace(1, -1, n)
        self.x_des = np.concatenate((x1, x2))

        y1 = np.linspace(-1, 1, n)
        y2 = np.linspace(1, -1, n)
        self.y_des = np.concatenate((y1, y2))

        z1 = np.linspace(1, 2, n)
        z2 = np.linspace(2, 1, n)
        self.z_des = np.concatenate((z1, z2))

        self.yaw_des = np.zeros(int(2*n)) #?

    def circular(self, n):
        r = 1
        theta = np.linspace(0, 2*np.pi, n*2)
        self.x_des = np.cos(theta) * r
        self.y_des = np.sin(theta) * r

        z1 = np.linspace(0.5, 1.5, n)
        z2 = np.linspace(1.5, 0.5, n)
        self.z_des = np.concatenate((z1, z2))

        #self.yaw_des = np.zeros(2 * n)

        self.yaw_des = np.linspace(-np.pi, np.pi, n*2)

    # callback function for vicon
    def get_vicon_data(self, vicon_msg):
        self.x = vicon_msg.transform.translation.x
        self.y = vicon_msg.transform.translation.y
        self.z = vicon_msg.transform.translation.z
        quaternion = np.array([vicon_msg.transform.rotation.x,
                               vicon_msg.transform.rotation.y,
                               vicon_msg.transform.rotation.z,
                               vicon_msg.transform.rotation.w])
        euler = euler_from_quaternion(quaternion)
        self.yaw = euler[2]

    def pub_des_pos(self, point):
        msg = Twist()
        msg.linear.x = self.x_des[self.count]
        msg.linear.y = self.y_des[self.count]
        msg.linear.z = self.z_des[self.count]
        msg.angular.z = self.yaw_des[self.count]

        self.pub_traj.publish(msg)
        
        update_count = self.check_dist(self.x_des[self.count], self.x) and \
                       self.check_dist(self.y_des[self.count], self.y) and \
                       self.check_dist(self.z_des[self.count], self.z) and \
                       self.yaw_check(self.yaw_des[self.count], self.yaw)

        if update_count:
            if self.count < self.total_count-1:
                self.count += 1
            else:
                self.count = 0

    # check distance of desired and actual value to determine if proceed
    def check_dist(self, des, act):
        if abs(des - act) > self.thresh:
            return False
        else:
            return True

    def yaw_check(self,des,act):
        yaw_error = des - act
        if yaw_error > np.pi:
            yaw_error = yaw_error - 2 * np.pi
        if yaw_error > self.thresh:
            return False
        else:
            return True

if __name__ == '__main__':
    rospy.init_node('desired_positions')
    landmarks = [1,2,3,4]
    origin = (0, 0, 0, 0, 0, 0)
    casa_loma = (7.13, 5.79, 0, 0, 0, 0.62)
    cn_tower = (3.21, 1.43, 0, 0, 0, -1.33)
    nathan_phillips = (1.92, 6.61, 0, 0, 0, 2.87)
    princes_gate = (8.73, 4.77, 0, 0, 0, -0.44)
    
    paths = [
                [ [],
                    [origin, casa_loma], # origin to Casa Loma
                    [origin, cn_tower], # origin to CN Tower
                    [origin, nathan_phillips], # origin to Nathan Phillips
                    [origin, princes_gate], # origin to Pronce's Gate
                ],
                [ [], [],
                    [casa_loma, cn_tower], # Casa Loma to CN Tower
                    [casa_loma, nathan_phillips], # Casa Loma to Nathan Phillips
                    [casa_loma, princes_gate], # Casa Loma to Princes Gate
                ],
                [ [], [], [],
                    [cn_tower, nathan_phillips], # CN Tower to Nathan Phillips
                    [cn_tower, princes_gate], # CN Tower to Prince's Gate
                ],
                [ [], [], [], [],
                    [nathan_phillips, princes_gate] # Nathan Phillips to Prince's Gate
                ]
            ]

    position_generator = ROSDesiredPositionGenerator()
    current_position = 0 # Start at the origin
    for landmark in landmarks:
        target = locations[landmark]
        if current_position < landmark:
            path = paths[current_position, landmark]
        else:
            path = paths[landmark, current_position]
            path = reversed(path)

        position_generator.set_path(path)
        current_position = landmark

    rospy.spin()
