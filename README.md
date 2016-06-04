
**ROS wrapper for google's speech recognition APi**
---------------------------------------------------

 This is based on [Speech Recognition](https://github.com/Uberi/speech_recognition) 
 
----------

**Installing**
 
> sudo pip install SpeechRecognition

**Requirements**
	

 - Python 2.6, 2.7, or 3.3+ (required)
 - PyAudio 0.2.9+
 
**Running it**
 - git clone https://github.com/danenigma/ros-speech-recognition.git
 - cd catkin_ws/
 - catkin_make
 - source ./devel/setup.bash
 - roslaunch google_speech_recognition speech_recognition.launch
