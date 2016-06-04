git clone https://github.com/danenigma/ros-speech-recognition.git;
cd catkin_ws/;
catkin_make;
source ./devel/setup.bash;
roslaunch google_speech_recognition speech_recognition.launch;
