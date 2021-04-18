#!/usr/bin/env python2

"""ROS Node for publishing desired positions."""

from __future__ import division, print_function, absolute_import

# Import ROS libraries
import roslib
import rospy
import numpy as np

from geometry_msgs.msg import TransformStamped, Twist
from std_msgs.msg import Empty
from tf.transformations import euler_from_quaternion, quaternion_from_euler

from ros_interface import ROSControllerNode
from numpy import floor
import time
from rrt_star import RRT_star

import subprocess

class ROSDesiredPositionGenerator(object):
    """ROS interface for publishing desired positions."""
    # write code here for desired position trajectory generator
    def __init__(self, altitude, skip_points):
        self.skip_points = skip_points
        self.vicon_topic = '/vicon/ARDroneCarre/ARDroneCarre'
        self.sub_vicon = rospy.Subscriber(self.vicon_topic, TransformStamped, self.get_vicon_data)
        self.pub_traj = rospy.Publisher('/desired_position', Twist, queue_size=10)
        #self.path_des = 'lin' #'cir'

        self.freq = 3 #10 #50

        self.x_des = []
        self.y_des = []
        self.z_des = altitude
        self.yaw_des = 0
        self.count = 0

        self.x = 0
        self.y = 0
        self.z = 0
        self.yaw = 0

        #self.total_count = 2 # 2 points for linear, 25 points for circular
        self.thresh = 0.4 #0.25
        self.traj_timer = rospy.Timer(rospy.Duration(1. / self.freq), self.pub_des_pos)

    def set_path(self, x_vals, y_vals, yaw_val):
        self.finished = False
        self.total_count = len(x_vals)
        print("-------", self.total_count, "points")
        self.count = 0
        self.x_des = x_vals
        self.y_des = y_vals
        self.yaw_des = yaw_val
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
        try:
            curr_dist = abs(msg.linear.x - self.x_des[self.count])+abs(msg.linear.y - self.y_des[self.count])
            next_dist = abs(msg.linear.x - self.x_des[self.count+1])+abs(msg.linear.y - self.y_des[self.count+1])
            if curr_dist > next_dist and self.skip_points:
                self.count += 1
        except IndexError:
            pass

        msg.linear.x = self.x_des[self.count]
        msg.linear.y = self.y_des[self.count]
      
        msg.linear.z = self.z_des
        
        if self.count == len(self.x_des)-1:
            msg.angular.z = self.yaw_des
        else:
            msg.angular.z = self.yaw

        self.pub_traj.publish(msg)
        if self.count == len(self.x_des)-1:
            update_count = self.check_dist(self.x_des[self.count], self.x, 0.1) and \
                           self.check_dist(self.y_des[self.count], self.y, 0.1) and \
                           self.check_dist(self.z_des, self.z, 0.4) and \
                           self.yaw_check(self.yaw_des, self.yaw, 0.1)
        else:
            update_count = self.check_dist(self.x_des[self.count], self.x, self.thresh) and \
                           self.check_dist(self.y_des[self.count], self.y, self.thresh) #and \

        if update_count:
            if self.count < self.total_count-1:
                print(self.count)
                self.count += 1
            else:
                #self.count = 0
                self.finished = True

    # check distance of desired and actual value to determine if proceed
    def check_dist(self, des, act, thresh):
        if abs(des - act) > thresh:
            return False
        else:
            return True

    def yaw_check(self,des,act,thresh):
        yaw_error = des - act
        if yaw_error > np.pi:
            yaw_error = yaw_error - 2 * np.pi
        if yaw_error > 0.35*thresh:
            return False
        else:
            return True

if __name__ == '__main__':
    rospy.init_node('desired_positions')
    
    ##### PARAMETERS ######
    landmarks = [1,2,3,4,0]
    landmark_names = {
                0: "Origin",
                1: "Casa Loma",
                2: "CN Tower",
                3: "Nathan Phillips",
                4: "Princes Gate"
            }

    altitude = 2.5
    pause_time = 5
    skip_points = False
    ##### LANDMARKS #####
    origin = (1, 1, altitude, 0, 0, 0)
    casa_loma = (7.149, 5.829, altitude, 0, 0, 0.615)
    cn_tower = (3.21, 1.4, altitude, 0, 0, -1.32)
    nathan_phillips = (1.933, 6.608, altitude, 0, 0,2.85)
    princes_gate = (8.752, 4.74, altitude, 0, 0, -0.477)

    locations = [origin, casa_loma, cn_tower, nathan_phillips, princes_gate]
    
    position_generator = ROSDesiredPositionGenerator(altitude, skip_points)
    position_generator.set_path([1,1],[1,1],0) # Go to starting point
    
   

    current_position = origin # Start at the origin
    for landmark in landmarks:
        print("----------- Going to landmark", landmark_names[landmark])
        start = current_position
        end = locations[landmark]
        planner = RRT_star((start[0],start[1]), (end[0],end[1]), 1.5, 1000)
        
        planner.plan()
        print("----------- Done planning")
        x_vals, y_vals = planner.convertNodes()
        x_vals.reverse()
        x_vals.append(end[0])
        y_vals.reverse()
        y_vals.append(end[1])
        print("--- Start", start[0], start[1])
        for i,x in enumerate(x_vals):
            print(x,y_vals[i])
        yaw_val = end[5]+np.pi/2
        position_generator.set_path(x_vals,y_vals,yaw_val)
        #position_generator.set_path([end[0]],[end[1]],[end[5]])
        while not position_generator.finished:
            pass
        current_position = end
        time.sleep(pause_time)

    #landing_topic = rospy.Publisher('/ardrone/land', Empty, queue_size='1') # land
    #msg = Empty()
    #landing_topic.publish(msg)
    print("----- Landing...")
    subprocess.call(["rostopic","pub","-l","/ardrone/land","std_msgs/Empty"])

    rospy.spin()
