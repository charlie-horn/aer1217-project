#!/usr/bin/env python2
"""
ROS Node for reading bag file and publishing data

This ROS node subscribes to the following topics:


This ROS node publishes to the following topics:
/lab3_position
/lab3_camera

"""

from __future__ import division, print_function, absolute_import

# Import ROS libraries
import roslib
import rospy
import numpy as np

# Import class that computes the desired positions
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import TransformStamped, Twist

from position_controller import PositionController
#from desired_positions import ROSDesiredPositionGenerator

import std_msgs
from std_msgs.msg._Empty import Empty
from numpy import roll


class Interface(object):

    def __init__(self):
        self.rate = rospy.Rate(200)
        self.time_stamp = 0

        #Publishers
        #self.pub_pos = rospy.Publisher('/lab3_position', Twist)
        #self.pub_cam = rospy.Publisher('/lab3_camera', Twist)

    def _traj_callback(self, msg):
        self.x_des = msg.linear.x
        self.y_des = msg.linear.y
        self.z_des = msg.linear.z
        self.yaw_des = msg.angular.z

        # self.x_des = msg.transform.translation.x
        # self.y_des = msg.transform.translation.y
        # self.z_des = msg.transform.translation.z
        # quaternion_des = np.array([msg.transform.rotation.x,
        #                            msg.transform.rotation.y,
        #                            msg.transform.rotation.z,
        #                            msg.transform.rotation.w])
        # euler_des = euler_from_quaternion(quaternion_des)
        # self.yaw_des = euler_des[2]


    def _vicon_callback(self, msg):
        self._vicon_msg = msg
        
    def get_pos(self):
        return self._vicon_msg.transform.translation
    
    def get_orient(self):
        orient_qx = self._vicon_msg.transform.rotation.x
        orient_qy = self._vicon_msg.transform.rotation.y
        orient_qz = self._vicon_msg.transform.rotation.z
        orient_qw = self._vicon_msg.transform.rotation.w
        orient_q = [orient_qx, orient_qy, orient_qz, orient_qw]
        return euler_from_quaternion(orient_q)
    
    def get_time(self):
        return self._vicon_msg.header.stamp.nsecs
    
    def land(self):
        self.pub_land.publish()

    def set_vel(self, traj):
        self.pub_traj.publish(traj)

if __name__ == '__main__':

    rospy.init_node("ros_interface", disable_signals=True)
    data_publisher = Publisher()
    data_processor = Processor()
    
    try:
        # Read bag file
        while not rospy.is_shutdown():
            # Publish data

            # Process Data

    except KeyboardInterrupt:

        # Display final results
        rospy.spin()
        
    rospy.spin()

#     rospy.spin()
