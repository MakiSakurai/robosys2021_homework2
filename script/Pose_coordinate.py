#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cv2
import mediapipe as mp
import rospy
import math
import sys
from geometry_msgs.msg import Point
from numpy.lib.type_check import imag
from robosys2021_homework2.msg import CustomArray

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def main():
  rospy.init_node("MediaPipe_pose_node")
  hand_position = rospy.Publisher('pose_topic', CustomArray, queue_size=10)
  r = rospy.Rate(10) # 10hz
  cap = cv2.VideoCapture(8)
  array_points = CustomArray()
  array_points.points= [0]
  # For webcam input:
  cap = cv2.VideoCapture(0)
  with mp_pose.Pose(
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as pose:
    while not rospy.is_shutdown():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      # To improve performance, optionally mark the image as not writeable to
      # pass by reference.
      image.flags.writeable = False
      image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
      results = pose.process(image)

      # Draw the pose annotation on the image.
      image.flags.writeable = True
      image_height, image_width, _ = image.shape
      image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

      point_1 = Point()
      point_2 = Point()
      point_3 = Point()
      point_4 = Point()
      array_points.points = []

      if results.pose_landmarks:
          #for pose_landmarks in results.pose_landmarks.landmark:

        for index, landmark in enumerate(results.pose_landmarks.landmark):
          landmark_x = min(int(landmark.x * image_width), image_width - 1)
          landmark_y = min(int(landmark.y * image_height), image_height - 1)
          if index == 13: #左肩
              #cx3,cy3 = landmark.x * image_width, landmark.y * image_height
              ex13,ey13 = landmark_x, landmark_y
              left_elbow_x,left_elbow_y = ex13,ey13
              cv2.circle(image, (int(left_elbow_x),int(left_elbow_y)), 5, (0, 255, 0), 2)
              point_1.x = left_elbow_x
              point_1.y = left_elbow_y

          if index == 14: #右肩
              ex14,ey14 = landmark_x, landmark_y
              right_elbow_x,right_elbow_y = ex14,ey14
              cv2.circle(image, (int(right_elbow_x),int(right_elbow_y)), 5, (0, 255, 0), 2)
              point_2.x = right_elbow_x
              point_2.y = right_elbow_y

              print(point_2.x)
          
          if index == 15: #左手首
              ex15,ey15 = landmark_x, landmark_y
              left_wrist_x,left_wrist_y = ex15,ey15
              cv2.circle(image, (int(left_wrist_x),int(left_wrist_y)), 5, (0, 255, 0), 2)
              point_3.x = left_wrist_x
              point_3.y = left_wrist_y


          if index == 16: #右手首
              ex16,ey16 = landmark_x, landmark_y
              right_wrist_x, right_wrist_y = ex16,ey16
              cv2.circle(image, (int(right_wrist_x),int(right_wrist_y)), 5, (0, 255, 0), 2)   
              point_4.x = right_wrist_x
              point_4.y = right_wrist_y

          array_points.points.append(point_1)
          array_points.points.append(point_2)
          array_points.points.append(point_3)
          array_points.points.append(point_4)

          hand_position.publish(array_points)
          print(array_points.points[0].x)
          
      mp_drawing.draw_landmarks(
        image,
        results.pose_landmarks,
        mp_pose.POSE_CONNECTIONS,
      )
      dst = cv2.resize(image, dsize=(1280, 980))
          #以下エラー出るからコメントアウトしてるけど役割しらべといてね
          #landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
      # Flip the image horizontally for a selfie-view display.
      cv2.imshow('MediaPipe Pose', cv2.flip(dst, 1))
      r.sleep()
      if cv2.waitKey(5) & 0xFF == 27:
        break
    
if __name__ == '__main__':
  try:
    main()
  except rospy.ROSInterruptException: 
    pass  

