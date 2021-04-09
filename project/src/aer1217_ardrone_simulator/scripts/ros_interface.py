#!/usr/bin/env python2
"""
ROS Node for controlling the ARDrone 2.0 using the ardrone_autonomy package.
This ROS node subscribes to the following topics:
/vicon/ARDroneCarre/ARDroneCarre
This ROS node publishes to the following topics:
/cmd_vel_RHC
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


class ROSControllerNode(object):
    """ROS interface for controlling the Parrot ARDrone in the Vicon Lab."""
    # write code here to define node publishers and subscribers
    # publish to /cmd_vel topic
    # subscribe to /vicon/ARDroneCarre/ARDroneCarre for position and attitude feedback
    def __init__(self):
        self.rate = rospy.Rate(200)
        self.time_stamp = 0
        #Subscribers
        self.vicon_topic = '/vicon/ARDroneCarre/ARDroneCarre'
        self._vicon_msg = TransformStamped()

        self.x_des = 0
        self.y_des = 0
        self.z_des = 0
        self.yaw_des = 0

        self.sub_vicon = rospy.Subscriber(self.vicon_topic, TransformStamped, self._vicon_callback)
        self.sub_traj = rospy.Subscriber('/desired_position', Twist, self._traj_callback)

        #Publishers
        self.pub_traj = rospy.Publisher('/cmd_vel_RHC', Twist, queue_size=32)
        self.pub_land = rospy.Publisher('/ardrone/land', Empty, queue_size=1)

    def _traj_callback(self, msg):
<<<<<<< HEAD
        # callback function for saving desired position and orientation from planner node
=======
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        self.x_des = msg.linear.x
        self.y_des = msg.linear.y
        self.z_des = msg.linear.z
        self.yaw_des = msg.angular.z
        
        print(x_des, y_des, z_des)


    def _vicon_callback(self, msg):
<<<<<<< HEAD
        # callback for getting the current drone state from the vicon system
        self._vicon_msg = msg
        
    def get_pos(self):
        # get current drone position
        return self._vicon_msg.transform.translation
    
    def get_orient(self):
        # get current orientation and convert to euler 
=======
        self._vicon_msg = msg
        
    def get_pos(self):
        return self._vicon_msg.transform.translation
    
    def get_orient(self):
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        orient_qx = self._vicon_msg.transform.rotation.x
        orient_qy = self._vicon_msg.transform.rotation.y
        orient_qz = self._vicon_msg.transform.rotation.z
        orient_qw = self._vicon_msg.transform.rotation.w
        orient_q = [orient_qx, orient_qy, orient_qz, orient_qw]
        return euler_from_quaternion(orient_q)
    
    def get_time(self):
<<<<<<< HEAD
        # get current time
=======
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
        return self._vicon_msg.header.stamp.nsecs
    
    def land(self):
        # publish landing command
        self.pub_land.publish()

    def set_vel(self, traj):
        # publish trajectory
        self.pub_traj.publish(traj)

if __name__ == '__main__':
    # write code to create ROSControllerNode
<<<<<<< HEAD
    
    # initiate node
    rospy.init_node("ros_interface", disable_signals=True)
    
    # initiate controller and ardrone objects
    positionCtrl = PositionController()
    ardrone = ROSControllerNode()
    # ardrone.time_stamp = ardrone.get_time()
    
=======
    rospy.init_node("ros_interface", disable_signals=True)
    positionCtrl = PositionController()
    ardrone = ROSControllerNode()
    # ardrone.time_stamp = ardrone.get_time()
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
    #first test
    # x_des = 4
    # y_des = 4
    # z_des = 4
    # yaw_des = 1
    
    try:
        while not rospy.is_shutdown():

            #get position nad orientation from vicon
            currentPosition = ardrone.get_pos()
            currentOrientation = ardrone.get_orient()
            #compute desired pose
<<<<<<< HEAD
            dt = max((ardrone.get_time() - ardrone.time_stamp)/pow(10,9), 0.0001) # time duration
            ardrone.time_stamp = ardrone.get_time() 
            x_des, y_des, z_des, yaw_des = ardrone.x_des, ardrone.y_des, ardrone.z_des, ardrone.yaw_des
            # get trajectory command
=======
            dt = max((ardrone.get_time() - ardrone.time_stamp)/pow(10,9), 0.0001)
            ardrone.time_stamp = ardrone.get_time()
            x_des, y_des, z_des, yaw_des = ardrone.x_des, ardrone.y_des, ardrone.z_des, ardrone.yaw_des
>>>>>>> b99e4d7081b7147fd781b7057c19cb23292b5bdb
            traj = positionCtrl.getDesiredState(currentPosition, currentOrientation, x_des, y_des, z_des, yaw_des, dt)
            #publish actuation commands
            ardrone.set_vel(traj)
            #spin
            ardrone.rate.sleep()           
    except KeyboardInterrupt:

        msg = Twist()
        msg.linear.x = 0
        msg.linear.y = 0
        msg.linear.z = 0
        msg.angular.z = 0
        ardrone.set_vel(msg)
        ardrone.land()
        rospy.spin()
        
    rospy.spin()