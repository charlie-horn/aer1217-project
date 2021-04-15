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

from rrt_star import RRT_star

class ROSDesiredPositionGenerator(object):
    """ROS interface for publishing desired positions."""
    # write code here for desired position trajectory generator
    def __init__(self, altitude):
        self.vicon_topic = '/vicon/ARDroneCarre/ARDroneCarre'
        self.sub_vicon = rospy.Subscriber(self.vicon_topic, TransformStamped, self.get_vicon_data)
        self.pub_traj = rospy.Publisher('/desired_position', Twist, queue_size=10)
        #self.path_des = 'lin' #'cir'

        self.freq = 3 #10 #50

        self.x_des = []
        self.y_des = []
        self.z_des = altitude
        self.yaw_des = []
        self.count = 0

        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0

        #self.total_count = 2 # 2 points for linear, 25 points for circular
        self.thresh = 0.1
        self.traj_timer = rospy.Timer(rospy.Duration(1. / self.freq), self.pub_des_pos)

    def set_path(self, x_vals, y_vals, yaw_vals):
        self.finished = False
        self.total_count = len(x_vals)
        print("-------", self.total_count, "points")
        self.count = 0
        self.x_des = x_vals
        self.y_des = y_vals
        self.yaw_des = yaw_vals
        return

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
        msg.linear.z = self.z_des

        #msg.angular.z = self.yaw_des[self.count]

        self.pub_traj.publish(msg)
        
        update_count = self.check_dist(self.x_des[self.count], self.x) and \
                       self.check_dist(self.y_des[self.count], self.y) #and \
                       #self.check_dist(self.z_des, self.z) #and \
                       #self.yaw_check(self.yaw_des[1][self.count], self.yaw)

        if update_count:
            if self.count < self.total_count-1:
                print(self.count)
                self.count += 1
            else:
                self.count = 0
                self.finished = True

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
    landmarks = [0,1,2,3,4,0]

    altitude = 3

    origin = (1, 1, altitude, 0, 0, 0)
    casa_loma = (7.13, 5.79, altitude, 0, 0, 0.62)
    cn_tower = (3.21, 1.43, altitude, 0, 0, -1.33)
    nathan_phillips = (1.92, 6.61, altitude, 0, 0, 2.87)
    princes_gate = (8.73, 4.77, altitude, 0, 0, -0.44)

    locations = [origin, casa_loma, cn_tower, nathan_phillips, princes_gate]
    
    position_generator = ROSDesiredPositionGenerator(altitude)
    position_generator.set_path([1],[1],[0])
    current_position = origin # Start at the origin
    for landmark in landmarks:
        print("----------- Going to landmark", landmark)
        start = current_position
        end = locations[landmark]
        planner = RRT_star((start[0],start[1]), (end[0],end[1]), 2, 100)
        
        planner.plan()
        print("----------- Done planning")
        x_vals, y_vals = planner.convertNodes()
        x_vals.reverse()
        y_vals.reverse()
        print("--- Start", start[0], start[1])
        for i,x in enumerate(x_vals):
            print(x,y_vals[i])
        yaw_vals = np.zeros((1,len(x_vals)))
        position_generator.set_path(x_vals,y_vals,yaw_vals)
        #position_generator.set_path([end[0]],[end[1]],[end[5]])
        while not position_generator.finished:
            pass
        current_position = end

    rospy.spin()
