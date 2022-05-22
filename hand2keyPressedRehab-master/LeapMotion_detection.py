###########################################################
# hand2keyPressedRehab
# 16/07/2020 Lausanne,Switzerland
# LeapMotion Solution
# Contact: hackahealth.geneva@gmail.com
# Autors: Sixto Alcoba-Banqueri (include your names if you do any collaboration in the code)
###########################################################

import sys
import Leap
import _thread
import time
import numpy as np


class LeapMotionListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky', 'Wrist']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    distance = [None, None, None, None, None, None]
    advance_distance = [None, None, None, None, None, None]
    palm_distance = [None, None, None, None]
    palm = [None, None, None]
    print_one = True
    finger_rest_thumb = None
    finger_rest_index = None
    finger_rest_middle = None
    finger_rest_ring = None
    finger_rest_pinky = None
    finger_rest_wrist = None
    init = True
    distance_performance = [None, None, None, None, None, None]

    def on_init(self, controller):
        print("Initialized")

    def on_disconnect(self, controller):
        print("Motion Sensor Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        Index_found = False
        Thumb_found = False
        Middle_found = False
        Pinky_found = False
        Ring_found = False
        self.distance[0] = None
        self.distance[1] = None
        self.distance[2] = None
        self.distance[3] = None
        self.distance[4] = None
        self.distance[5] = None

        self.advance_distance[0] = None
        self.advance_distance[1] = None
        self.advance_distance[2] = None
        self.advance_distance[3] = None
        self.advance_distance[4] = None
        self.advance_distance[5] = None

        self.distance_performance[0] = None
        self.distance_performance[1] = None
        self.distance_performance[2] = None
        self.distance_performance[3] = None
        self.distance_performance[4] = None
        self.distance_performance[5] = None

        self.palm_distance[0] = None
        self.palm_distance[1] = None
        self.palm_distance[2] = None
        self.palm_distance[3] = None

        self.palm[0] = None
        self.palm[1] = None
        self.palm[2] = None

        for finger in frame.fingers:

            if finger.type == Leap.Finger.TYPE_THUMB:
                Thumb_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                Thumb_proximal_bone = finger.bone(
                    Leap.Bone.TYPE_INTERMEDIATE)  # for thumb we use intermediate and proximal because there is no metacarpal
                Thumb_meta_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                Thumb_found = True

            if finger.type == Leap.Finger.TYPE_INDEX:
                Index_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                Index_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                Index_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                Index_found = True

            if finger.type == Leap.Finger.TYPE_MIDDLE:
                Middle_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                Middle_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                Middle_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                Middle_found = True

            if finger.type == Leap.Finger.TYPE_RING:
                Ring_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                Ring_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                Ring_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                Ring_found = True

            if finger.type == Leap.Finger.TYPE_PINKY:
                Pinky_distal_bone = finger.bone(Leap.Bone.TYPE_DISTAL)
                Pinky_proximal_bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                Pinky_meta_bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                Pinky_found = True

            if (Index_found and Thumb_found and Middle_found and Pinky_found and Ring_found):
                #					self.distance[0]= Thumb_distal_bone.center.distance_to(Thumb_distal_bone.center)
                #					self.distance[1]= Thumb_distal_bone.center.distance_to(Index_distal_bone.center)
                #					self.distance[2]= Thumb_distal_bone.center.distance_to(Middle_distal_bone.center)
                #					self.distance[3]= Thumb_distal_bone.center.distance_to(Ring_distal_bone.center)
                #					self.distance[4]= Thumb_distal_bone.center.distance_to(Pinky_distal_bone.center)

                for hand in frame.hands:

                    if self.init:
                        self.finger_rest_thumb = Thumb_distal_bone.next_joint - hand.palm_position
                        self.finger_rest_index = Index_distal_bone.next_joint - hand.palm_position
                        self.finger_rest_middle = Middle_distal_bone.next_joint - hand.palm_position
                        self.finger_rest_ring = Ring_distal_bone.next_joint - hand.palm_position
                        self.finger_rest_pinky = Pinky_distal_bone.next_joint - hand.palm_position
                        self.finger_rest_wrist = hand.palm_position.y
                        self.init = False
                    # SIMPLE MODE
                    self.distance[0] = Thumb_distal_bone.center.distance_to(
                        hand.palm_position)  # distance between tip of the thumb and palm position
                    self.distance[1] = (Index_distal_bone.next_joint - Index_proximal_bone.prev_joint).angle_to(
                        Index_meta_bone.prev_joint - Index_proximal_bone.prev_joint)
                    self.distance[2] = (Middle_distal_bone.next_joint - Middle_proximal_bone.prev_joint).angle_to(
                        Middle_meta_bone.prev_joint - Middle_proximal_bone.prev_joint)
                    self.distance[3] = (Ring_distal_bone.next_joint - Ring_proximal_bone.prev_joint).angle_to(
                        Ring_meta_bone.prev_joint - Ring_proximal_bone.prev_joint)
                    self.distance[4] = (Pinky_distal_bone.next_joint - Pinky_proximal_bone.prev_joint).angle_to(
                        Pinky_meta_bone.prev_joint - Pinky_proximal_bone.prev_joint)
                    self.distance[5] = (hand.palm_position.y)

                    self.palm_distance[0] = Index_distal_bone.center.distance_to(hand.palm_position)
                    self.palm_distance[1] = Middle_distal_bone.center.distance_to(hand.palm_position)
                    self.palm_distance[2] = Ring_distal_bone.center.distance_to(hand.palm_position)
                    self.palm_distance[3] = Pinky_distal_bone.center.distance_to(hand.palm_position)
                    # ADVANCED MODE
                    # self.advance_distance[0] = Thumb_distal_bone.next_joint.distance_to(Thumb_proximal_bone.prev_joint) # distance between tip of the thumb and palm position
                    self.advance_distance[0] = Thumb_distal_bone.center.distance_to(hand.palm_position)
                    self.advance_distance[1] = Thumb_distal_bone.center.distance_to(Index_distal_bone.next_joint)
                    self.advance_distance[2] = Thumb_distal_bone.center.distance_to(Middle_distal_bone.next_joint)
                    self.advance_distance[3] = Thumb_distal_bone.center.distance_to(Ring_distal_bone.next_joint)
                    self.advance_distance[4] = Thumb_distal_bone.center.distance_to(Pinky_distal_bone.next_joint)
                    self.advance_distance[5] = self.palm_distance[0] + self.palm_distance[1] + self.palm_distance[2] + \
                                               self.palm_distance[3]

                    # print(Thumb_distal_bone.next_joint)

                    self.palm[0] = hand.palm_position.x
                    self.palm[1] = hand.palm_position.y
                    self.palm[2] = hand.palm_position.z
                    #

                    self.distance_performance[0] = self.finger_rest_thumb.distance_to(
                        Thumb_distal_bone.next_joint - hand.palm_position)
                    self.distance_performance[1] = self.finger_rest_index.distance_to(
                        Index_distal_bone.next_joint - hand.palm_position)
                    self.distance_performance[2] = self.finger_rest_middle.distance_to(
                        Middle_distal_bone.next_joint - hand.palm_position)
                    self.distance_performance[3] = self.finger_rest_ring.distance_to(
                        Ring_distal_bone.next_joint - hand.palm_position)
                    self.distance_performance[4] = self.finger_rest_pinky.distance_to(
                        Pinky_distal_bone.next_joint - hand.palm_position)
                    self.distance_performance[5] = hand.palm_position.y - self.finger_rest_wrist
                    #print(self.distance_performance[0])
        # print('distance-leap fichier', self.distance)
        # print('palm-leap fichier', self.palm)
        return self.palm, self.distance, self.advance_distance, self.distance_performance


def main():
    listener = LeapMotionListener()
    controller = Leap.Controller()
    controller.add_listener(listener)
    print("Press enter to quit")
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()