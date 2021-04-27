# Modified files/directories
    - aer1217-project/src/publisher/scripts/
    - aer1217-project/src/processor/scripts/
    - aer1217-project/src/aer1217_ardrone_simulator/scripts/
    - refresh_source.sh
    - project2021.world
    - obstacles.csv
    - landmarks.csv
    - ardrone_simulator.launch
    - RRT_star.ipynb

# Detect and locate obstacles and landmarks
    - Add "<path>/aer1217-project/src" to $ROS_PACKAGE_PATH
    - Place the bag file under src/publisher/
    
    - Create a text file "lm_pose.txt" in the directory of "<path>/aer1217-project/src/processor"
    - Create a folder "lm_img" in the directory of "<path>/aer1217-project/"
    
    - Change the director of line 8-11 of "<path>/aer1217-project/src/processor/scripts/pose_estimation.py" as "<path>/aer1217-project/src/processor/scripts/landmark/xxx.png"
    - Change the director of line 23 of "<path>/aer1217-project/src/processor/scripts/pose_estimation.py" as "<path>/aer1217-project/lm_img/"
    - Change the director of line 26 of "<path>/aer1217-project/src/processor/scripts/pose_estimation.py" as "<path>/aer1217-project/src/processor/lm_pose.txt"
    
    - Change the director of line 103 of "<path>/aer1217-project/src/processor/scripts/processor.py" as "<path>/aer1217-project/src/processor/lm_pose.txt"
    - Change the director of line 146 of "<path>/aer1217-project/src/processor/scripts/pose_estimation.py" as "<path>/aer1217-project/lm_img/{}.jpg"
    
    - Run "roslaunch <path>/aer1217-project/src/publisher/launch/publisher.launch
    - Run "python "pose_estimation.py" in the directory of "<path>/aer1217-project/src/processor/scripts"

# Visit landmarks
    - take obstacle locations from obstacles.csv and put them in project2021.world
    - Take landmark locations from landmarks.csv and put them in project2021.world
    - run refresh_source.sh to copy files to the aer1217 main repository
    - run "roslaunch aer1217_ardrone_simulator ardrone_simulator.launch"
    
