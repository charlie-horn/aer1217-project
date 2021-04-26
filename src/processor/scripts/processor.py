#!/usr/bin/env python2

from target_identifier import TargetIdentifier
from localization import Localizer
from cluster import Cluster
from pose_estimation import LM_pose
import cv2

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
        self.bridge = CvBridge()

        self.sub_cam = rospy.Subscriber("/ardrone/bottom/image_raw", Image, self.identify_targets)
        self.sub_pos = rospy.Subscriber("/vicon/ARDroneCarre/ARDroneCarre", TransformStamped, self.store_pos)

        self.ob_locations = []
        self.radius_list = []

        self.lm_locations = []
        self.crop_list = []
        #self.yaw_list = []

        self.epsilon = Duration(5)
        self.frames = 0
        self.obstacle_frames = 0
        self.landmark_frames = 0
        self.not_pixels = 0
        self.time_filtered = 0

        return

    def identify_targets(self, msg):
        self.frames +=1

        # convert bag image to cv2 image
        img = self.bridge.imgmsg_to_cv2(msg, "bgr8")

        # get pixel location for obstacles and landmarks
        ob_pixels, radius_pixel = self.target_identifier.identify_obstacle(img)
        lm_pixels, crop_img, yaw = self.target_identifier.identify_landmark(img, self.pos)

        # if no obstacles or landmark are found
        if not ob_pixels and not lm_pixels:
            self.not_pixels+=1
            return

        else:
            # if obstacles are found
            if ob_pixels:
                self.obstacle_frames+=1

                # convert pixel location of centroids to world frame
                new_locations = self.localizer.localize(ob_pixels, self.pos)
                self.ob_locations += new_locations

                # convert pixel location of edge point to world frame
                point = self.localizer.localize(radius_pixel, self.pos)

                # calculate radius
                radius = []
                for i in range(len(point)):
                    radius.append(np.sqrt((new_locations[i][0] - point[i][0]) ** 2 + (new_locations[i][1] - point[i][1]) ** 2))
                self.radius_list += radius

                # # keep track of obstacle locations
                # f = open('/home/demi/aer1217/labs/src/processor/ob_location.txt', 'a')
                # for i in range(len(new_locations)):
                #     f.writelines('\n' + np.array2string(new_locations[i][0])+' '+ np.array2string(new_locations[i][1])+' '+ str(radius[i]))
                # f.close()

            # if landmarks are found
            if lm_pixels:
                self.landmark_frames += 1

                # convert pixel location of centroids to world frame
                new_locations = self.localizer.localize(lm_pixels, self.pos)
                self.lm_locations += new_locations

                # # keep track of landmark locations
                # f = open('/home/demi/aer1217/labs/src/processor/lm_location.txt', 'a')
                # for i in range(len(new_locations)):
                #     f.writelines('\n' + np.array2string(new_locations[i][0]) + ' ' + np.array2string(new_locations[i][1]))
                # f.close()

                # save crop images of landmark for further process
                self.crop_list.append(crop_img)

                # save current yaw angle of the drone for further process
                f = open('/home/demi/aer1217/labs/src/processor/lm_pose.txt', 'a')
                for i in range(len(yaw)):
                    f.writelines('\n' + str(yaw[i]))
                f.close()
        return

    def store_pos(self, msg):
        self.pos = msg
        return


if __name__ == '__main__':
    rospy.init_node("processor", disable_signals=True)

    data_processor = Processor()
    cluster = Cluster()

    try:
        rospy.spin()

        # cluster obstacle locations and radius
        r = np.array(data_processor.radius_list).reshape(-1, 1)
        l = data_processor.ob_locations
        cluster.cluster(np.hstack((l,r)),0.4, 15)

        # cluster landmark locations
        cluster = Cluster()
        cluster.cluster(data_processor.lm_locations, 0.3, 30)

        # print result
        print("\nShutting Down")
        print("Total frames: ", data_processor.frames)
        print("Obstacle frames: ", data_processor.obstacle_frames)
        print("Landmark frames: ", data_processor.landmark_frames)
        print("No pixels: ", data_processor.not_pixels)
        print("Time filtered: " ,data_processor.time_filtered)

        # save all cropped landmark images for for further process
        count = 0
        for i in range(len(data_processor.crop_list)):
            for j in range(len(data_processor.crop_list[i])):
                count+=1
                crop_img = data_processor.crop_list[i][j]
                cv2.imwrite('/home/demi/aer1217/project/lm_img/{}.jpg'.format(count), crop_img)

        rospy.shutdown()

    except KeyboardInterrupt:
        print("Shutting down.")
