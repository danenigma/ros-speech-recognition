#!/usr/bin/env python

# NOTE: this example requires PyAudio because it uses the Microphone class
import rospy
from std_msgs.msg import String
import speech_recognition as sr

class SpeechRecognition():

	NODE_NAME = "SPEECH"

	def __init__(self):
		"""init"""
		self.r = sr.Recognizer()
		rospy.init_node(self.NODE_NAME)
		self.pub  = rospy.Publisher("/speech",String,queue_size=1)
	def run(self):	
		"""does speech recognition an publishs it on /speech topic"""
		while not rospy.is_shutdown():
			with sr.Microphone() as source:
			    print("Say something!")
			    audio = self.r.listen(source)
			# recognize speech using Google Speech Recognition
			try:
			    data  = self.r.recognize_google(audio)
			    rospy.loginfo("Google Speech Recognition thinks you said " + data)
			    self.pub.publish(data)	
			except sr.UnknownValueError:
			    rospy.loginfo("Google Speech Recognition could not understand audio")
			    self.pub.publish("Google Speech Recognition could not understand audio")
			except sr.RequestError as e:
			    rospy.loginfo("Could not request results from Google Speech Recognition service; {0}".format(e))
			    self.pub.publish("Could not request results from Google Speech Recognition service")


if __name__ == "__main__":
	s = SpeechRecognition()
	s.run()

