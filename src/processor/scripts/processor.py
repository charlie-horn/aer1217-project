#!/usr/bin/env python2

from target_identifier import TargetIdentifier
from localization import Localizer
from cluster import Cluster
import roslib
import rospy
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
from rospy.rostime import Duration

from geometry_msgs.msg import Twist, TransformStamped
from sensor_msgs.msg import Image

from cv_bridge import CvBridge
import numpy as np

class Processor():
    def __init__(self):
        self.target_identifier = TargetIdentifier()
        self.localizer = Localizer()
        #self.sub_cam = rospy.Subscriber("/lab3_cam", Image, self.identify_targets)
        self.sub_cam = rospy.Subscriber("/ardrone/bottom/image_raw", Image, self.identify_targets)
        #self.sub_pos = rospy.Subscriber("/lab3_pos", TransformStamped, self.store_pos)
        self.sub_pos = rospy.Subscriber("/vicon/ARDroneCarre/ARDroneCarre", TransformStamped, self.store_pos)
        #self.pub_locations = rospy.Publisher('/lab3_locations', numpy_msg(Floats), queue_size="0")
        #self.pub_locations = rospy.Publisher('/lab3_locations', numpy_msg(Floats), queue_size="0")
        self.bridge = CvBridge()
        self.ob_locations = []
        self.radius_list = []
        self.lm_locations = []
        self.epsilon = Duration(5)
        self.frames = 0
        self.obstacle_frames = 0
        self.landmark_frames = 0
        self.not_pixels = 0
        self.time_filtered = 0
        return

    def identify_targets(self, msg):
        self.frames +=1
        # if self.frames < 400:
        #     return
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        ob_pixels, radius_pixel = self.target_identifier.identify_obstacle(img)
        lm_pixels = self.target_identifier.identify_landmark(img)
        cam_time = msg.header.stamp
        pos_time = self.pos.header.stamp
        time_diff = abs(cam_time - pos_time)
       
        if not ob_pixels and not lm_pixels:
            self.not_pixels+=1
            return
        #elif time_diff < self.epsilon:
        else:
            if ob_pixels:
                self.obstacle_frames+=1
                new_locations = self.localizer.localize(ob_pixels, self.pos)
                self.ob_locations += new_locations

                point = self.localizer.localize(radius_pixel, self.pos)
                radius = []
                for i in range(len(point)):
                    radius.append(np.sqrt((new_locations[i][0] - point[i][0]) ** 2 + (new_locations[i][1] - point[i][1]) ** 2))
                self.radius_list += radius
                #self.pub_locations.publish(new_locations)

                # f = open('/home/demi/aer1217/labs/src/processor/ob_location.txt', 'a')
                # for i in range(len(new_locations)):
                #     f.writelines('\n' + np.array2string(new_locations[i][0])+' '+ np.array2string(new_locations[i][1])+' '+ str(radius[i]))
                # f.close()

            if lm_pixels:
                self.landmark_frames += 1
                new_locations = self.localizer.localize(lm_pixels, self.pos)
                self.lm_locations += new_locations

                # f = open('/home/demi/aer1217/labs/src/processor/lm_location.txt', 'a')
                # for i in range(len(new_locations)):
                #     f.writelines('\n' + np.array2string(new_locations[i][0]) + ' ' + np.array2string(new_locations[i][1]))
                # f.close()

        return

    def store_pos(self, msg):
        self.pos = msg
        return


if __name__ == '__main__':

    rospy.init_node("processor", disable_signals=True)
    data_processor = Processor()
    cluster = Cluster()
    #rospy.on_shutdown(cluster.cluster)

    try:
        rospy.spin()
        r = np.array(data_processor.radius_list).reshape(-1, 1)
        l = data_processor.ob_locations
        cluster.cluster(np.hstack((l,r)))
        cluster = Cluster()
        cluster.cluster(data_processor.lm_locations)
        print("\nShutting Down")
        print("Total frames: ", data_processor.frames)
        print("Obstacle frames: ", data_processor.obstacle_frames)
        print("Landmark frames: ", data_processor.landmark_frames)
        print("No pixels: ", data_processor.not_pixels)
        print("Time filtered: " ,data_processor.time_filtered)
        rospy.shutdown()
    except KeyboardInterrupt:
        print("Shutting down.")
