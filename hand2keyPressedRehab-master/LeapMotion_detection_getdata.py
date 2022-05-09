###########################################################
# hand2keyPressedRehab 
# 16/07/2020 Lausanne,Switzerland
# LeapMotion Solution 
# Contact: hackahealth.geneva@gmail.com
# Autors: Sixto Alcoba-Banqueri (include your names if you do any collaboration in the code)
###########################################################

import sys
import Leap
#import thread
import time
#import numpy as np

class LeapMotionListener(Leap.Listener): 
	finger_names=['Thumb','Index','Middle','Ring','Pinky']
	bone_names=['Metacarpal','Proximal','Intermediate','Distal']
	distance = [None,None,None,None]
	distance_to_palm = [None,None,None,None,None]
	angle_finger_meta = [None,None,None,None,None]
	angle_finger_prox = [None,None,None,None,None]
	angle_palm = [None,None,None,None,None]
	print_one = True
	finger_data={}

	def on_init(self,controller):  # see this link for the on_... https://developer-archive.leapmotion.com/documentation/python/api/Leap.Listener.html
		print ("Initialized")

	def on_disconnect(self,controller):
		print ("Motion Sensor Disconnected")

	def on_exit(self,controller):
		print ("Exited")

	def on_frame(self,controller): # called everytime the leapmotion get a new frame
		frame = controller.frame() # get the last frame of the Leapmotion

		# initialized some variables 
		Index_found= False
		Thumb_found=False
		Middle_found=False
		Pinky_found=False
		Ring_found=False

		# test different types of distances  :
		self.distance[0]= None
		self.distance[1]= None
		self.distance[2]= None
		self.distance[3]= None

		self.distance_to_palm[0] = None
		self.distance_to_palm[1] = None
		self.distance_to_palm[2] = None
		self.distance_to_palm[3] = None
		self.distance_to_palm[4] = None



#		for hand in frame.hands:
#			print("palm position :", str(hand.palm_position))

		self.angle_finger_meta[0] = None 
		self.angle_finger_meta[1] = None 
		self.angle_finger_meta[2] = None 
		self.angle_finger_meta[3] = None 
		self.angle_finger_meta[4] = None 

		self.angle_finger_prox[0] = None 
		self.angle_finger_prox[1] = None 
		self.angle_finger_prox[2] = None 
		self.angle_finger_prox[3] = None 
		self.angle_finger_prox[4] = None 

		self.angle_palm[0] = None 
		self.angle_palm[1] = None 
		self.angle_palm[2] = None 
		self.angle_palm[3] = None 
		self.angle_palm[4] = None 
		
		for finger in frame.fingers:  # loop for each fingers: Thumb, Index, Middle, Ring, Pinky

			# get distal bone info for each fingers : https://developer-archive.leapmotion.com/documentation/cpp/api/Leap.Bone.html
			if finger.type== Leap.Finger.TYPE_INDEX:
				Index_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL) 
				Index_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL) 
				Index_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL) 
				Index_found=True

			if finger.type== Leap.Finger.TYPE_THUMB:
				Thumb_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
				Thumb_proximal_bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)  # for thumb we use intermediate and proximal because there is no metacarpal
				Thumb_meta_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL) 
				Thumb_found=True

			if finger.type== Leap.Finger.TYPE_MIDDLE:
				Middle_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
				Middle_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
				Middle_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL)  
				Middle_found=True

			if finger.type== Leap.Finger.TYPE_PINKY:
				Pinky_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
				Pinky_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL) 
				Pinky_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL) 
				Pinky_found=True

			if finger.type== Leap.Finger.TYPE_RING:
				Ring_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
				Ring_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
				Ring_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL)  
				Ring_found=True
				


			# If all the fingers are found, compute the distance between the distal bone of the thumb and the other fingers 
			if(Index_found and Thumb_found and Middle_found and Pinky_found and Ring_found): 
					self.distance[0]= Thumb_distal_bone.center.distance_to(Index_distal_bone.center)
					self.distance[1]= Thumb_distal_bone.center.distance_to(Middle_distal_bone.center)
					self.distance[2]= Thumb_distal_bone.center.distance_to(Ring_distal_bone.center)
					self.distance[3]= Thumb_distal_bone.center.distance_to(Pinky_distal_bone.center)
					#self.distance[4]= Thumb_distal_bone.center.distance_to(hand.palm_position)


					self.finger_data['distal']=[Thumb_distal_bone.center,Index_distal_bone.center,Middle_distal_bone.center,Ring_distal_bone.center,Pinky_distal_bone.center]
					self.finger_data['proximal']=[Thumb_proximal_bone.prev_joint,Index_proximal_bone.prev_joint,Middle_proximal_bone.prev_joint,Ring_proximal_bone.prev_joint,Pinky_proximal_bone.prev_joint]
					self.finger_data['meta']=[Thumb_meta_bone.prev_joint,Index_meta_bone.prev_joint,Middle_meta_bone.prev_joint,Ring_meta_bone.prev_joint,Pinky_meta_bone.prev_joint]

					for hand in frame.hands:

						self.distance_to_palm[0] = Thumb_distal_bone.center.distance_to(hand.palm_position)
						self.distance_to_palm[1] = Index_distal_bone.center.distance_to(hand.palm_position)
						self.distance_to_palm[2] = Middle_distal_bone.center.distance_to(hand.palm_position)
						self.distance_to_palm[3] = Ring_distal_bone.center.distance_to(hand.palm_position)
						self.distance_to_palm[4] = Pinky_distal_bone.center.distance_to(hand.palm_position)
					
						self.angle_finger_meta[0] = (Thumb_distal_bone.next_joint-Thumb_proximal_bone.prev_joint).angle_to(Thumb_meta_bone.prev_joint-Thumb_proximal_bone.prev_joint)
						self.angle_finger_meta[1] = (Index_distal_bone.next_joint-Index_proximal_bone.prev_joint).angle_to(Index_meta_bone.prev_joint-Index_proximal_bone.prev_joint)
						self.angle_finger_meta[2] = (Middle_distal_bone.next_joint-Middle_proximal_bone.prev_joint).angle_to(Middle_meta_bone.prev_joint-Middle_proximal_bone.prev_joint)
						self.angle_finger_meta[3] = (Ring_distal_bone.next_joint-Ring_proximal_bone.prev_joint).angle_to(Ring_meta_bone.prev_joint-Ring_proximal_bone.prev_joint)
						self.angle_finger_meta[4] = (Pinky_distal_bone.next_joint-Pinky_proximal_bone.prev_joint).angle_to(Pinky_meta_bone.prev_joint-Pinky_proximal_bone.prev_joint)

						self.angle_finger_prox[0] =  Thumb_distal_bone.direction.angle_to(Thumb_proximal_bone.direction)
						self.angle_finger_prox[1] =  Index_distal_bone.direction.angle_to(Index_proximal_bone.direction)
						self.angle_finger_prox[2] =  Middle_distal_bone.direction.angle_to(Middle_proximal_bone.direction)
						self.angle_finger_prox[3] =  Ring_distal_bone.direction.angle_to(Ring_proximal_bone.direction)
						self.angle_finger_prox[4] =  Pinky_distal_bone.direction.angle_to(Pinky_proximal_bone.direction)

						self.angle_palm[0] = (Thumb_distal_bone.next_joint-Thumb_proximal_bone.prev_joint).angle_to(hand.palm_position-Thumb_proximal_bone.prev_joint)
						self.angle_palm[1] = (Index_distal_bone.next_joint-Index_proximal_bone.prev_joint).angle_to(hand.palm_position-Index_proximal_bone.prev_joint)
						self.angle_palm[2] = (Middle_distal_bone.next_joint-Middle_proximal_bone.prev_joint).angle_to(hand.palm_position-Middle_proximal_bone.prev_joint)
						self.angle_palm[3] = (Ring_distal_bone.next_joint-Ring_proximal_bone.prev_joint).angle_to(hand.palm_position-Ring_proximal_bone.prev_joint)
						self.angle_palm[4] = (Pinky_distal_bone.next_joint-Pinky_proximal_bone.prev_joint).angle_to(hand.palm_position-Pinky_proximal_bone.prev_joint)

						self.finger_data['palm']=[hand.palm_position]
					#print('dist 3',self.distance[3])
#					print('dist thumb',self.distance_to_palm[0])
#					print('dist index',self.distance_to_palm[1])
#					print('dist middle',self.distance_to_palm[2])
#					print('dist ring',self.distance_to_palm[3])
#					print('dist pinky',self.distance_to_palm[3])
		return self.distance, self.distance_to_palm, self.angle_palm, self.angle_finger_meta, self.angle_finger_prox, self.finger_data


def main():
	listener = LeapMotionListener() #The Listener class defines a set of callback functions that you can override
									# in a subclass to respond to events dispatched by the Controller object.

	controller=Leap.Controller()	# The Controller class is your main interface to the Leap Motion Controller. 
									#https://developer-archive.leapmotion.com/documentation/python/api/Leap.Controller.html#Leap.Controller
	
	controller.add_listener(listener) # assign the controller to the listener 
	
	print ("Press enter to quit")
	#https://www.delftstack.com/fr/howto/python/keyboard-interrupt-python/
	try:
		line = sys.stdin.readline()
	except KeyboardInterrupt : 
		pass 
	finally:
		controller.remove_listener(listener)

if __name__=="__main__":
	main()