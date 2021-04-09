#!/usr/bin/env python2
import rosbag
import rospkg
import rospy
from geometry_msgs.msg import Twist, TransformStamped
from sensor_msgs.msg import Image
import subprocess
import time

class Publisher():
    def __init__(self):
        self.pub_cam = rospy.Publisher("/lab3_cam", Image, queue_size="0")
        self.pub_pos = rospy.Publisher("/lab3_pos", TransformStamped, queue_size="0")
        self.pub_vel = rospy.Publisher("/lab3_vel", Twist, queue_size = "0")
        self.package = rospkg.RosPack()
        print(self.package.get_path('publisher'))
        self.bag = rosbag.Bag(self.package.get_path('publisher') + '/lab3.bag')
        return

    def publish_cam(self, msg):
        pass

    def publish_pos(self, msg):
        pass

    def publish_vel():
        pass

if __name__ == '__main__':

    rospy.init_node("publisher", disable_signals=True)
    data_publisher = Publisher()
    package = rospkg.RosPack()
    bag_play = subprocess.Popen(["rosbag", "play", package.get_path('publisher') + '/lab3.bag'])
    try:
        while bag_play.poll() is None:
            time.sleep(1)
        #bag_play.kill()
    except KeyboardInterrupt:
        bag_play.kill()
    

    
    # Read bag file
    #for topic, msg, t in data_publisher.bag.read_messages(topics=[]):
    #    continue
    #    if topic == "/vicon/ARDroneCarre/ARDroneCarre":
    #        data_publisher.pub_pos.publish(msg)
    #    elif topic == "/ardrone/bottom/image_raw":
    #        data_publisher.pub_cam.publish(msg)
    #    elif topic == "/cmd_vel_RHC":
    #        data_publisher.pub_vel.publish(msg)
    #    else:
    #        print("Invalid topic ", topic)
