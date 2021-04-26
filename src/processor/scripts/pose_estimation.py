import numpy as np
import cv2
import math

class LM_pose():
    def __init__(self):
        # reference image
        self.square = cv2.imread('/home/demi/aer1217/labs/src/processor/scripts/landmark/nathan_philips_square.png', 0)
        self.casa = cv2.imread('/home/demi/aer1217/labs/src/processor/scripts/landmark/casa_loma.png', 0)
        self.gate = cv2.imread('/home/demi/aer1217/labs/src/processor/scripts/landmark/princes_gates.png', 0)
        self.cn = cv2.imread('/home/demi/aer1217/labs/src/processor/scripts/landmark/cn_tower.png', 0)

        self.landmark = [self.square, self.casa, self.gate, self.cn]
        self.landmark_name = ["nathan philips square", "casa loma", "princes gates", "cn tower"]
        self.landmark_pose = {"nathan philips square":[], "casa loma":[], "princes gates":[], "cn tower":[]}

        self.sift = cv2.xfeatures2d.SIFT_create()  # initialize SIFT detector

        self.matcher_params = {'algorithm': 1, 'trees': 5, 'checks': 50}
        self.flann = cv2.FlannBasedMatcher(self.matcher_params)

        # load cropped landmark
        self.path = '/home/demi/aer1217/project/lm_img/'

        # load yaw angle of the drone
        filename = '/home/demi/aer1217/labs/src/processor/lm_pose.txt'
        with open(filename) as f:
            content = f.readlines()
        content = [x.strip() for x in content]
        self.content = content[1:]

        return


    def estimate_pose(self):
        index_list = []
        yaw_list = []

        for i in range(len(self.content)):
            crop_img = cv2.imread(self.path + str(i + 1) + '.jpg', 1)

            find = False  # flag indicate if the best matching is found

            for j in range(len(self.landmark)):
                # compute keypoints and descriptors for reference and observation
                src_kp, src_des = self.sift.detectAndCompute(self.landmark[j], None)
                dst_kp, dst_des = self.sift.detectAndCompute(crop_img, None)

                # find matches between reference and observation
                matches = self.flann.knnMatch(src_des, dst_des, k=2)

                # keep track of good matches using Lowe's ratio of 0.6
                good_points = []
                for m, n in matches:
                    if m.distance < 0.6 * n.distance:
                        good_points.append(m)

                # if there are enough good matches -> correct landmark
                if len(good_points) > 20:
                    find = True

                    # convert keypoint into list
                    src_pts = np.float32([src_kp[m.queryIdx].pt for m in good_points]).reshape(-1, 1, 2)
                    dst_pts = np.float32([dst_kp[m.trainIdx].pt for m in good_points]).reshape(-1, 1, 2)

                    # finding homography matrix between reference and observation
                    H, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

                    # compute the angle between reference and observation
                    if np.shape(H) != ():
                        yaw = math.atan2(H[1, 0], H[0, 0])
                        yaw_list.append(yaw)
                        index_list.append(j)
                    else: # place holder
                        yaw_list.append(0)
                        index_list.append(-1)

                    break

            if not find: # place holder
                yaw_list.append(0)
                index_list.append(-1)

        # classify landmark
        for i in range(len(yaw_list)):
            if index_list[i] == -1:
                continue
            else:
                name = self.landmark_name[index_list[i]]
                self.landmark_pose[name].append(yaw_list[i])

        # calculate the average orientation for each landmark
        for name in self.landmark_name:
            average = np.average(self.landmark_pose[name])
            print('{}: {}'.format(name, str(np.round(average,2))))

if __name__ == '__main__':
    LM_pose().estimate_pose()