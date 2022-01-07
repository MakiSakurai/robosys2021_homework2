#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import moveit_commander
import geometry_msgs.msg
import math
from geometry_msgs.msg import Point
from geometry_msgs.msg import Twist
from robosys2021_homework2.msg import CustomArray

class pose_main():
    def __init__(self):
        rospy.init_node('MediaPipe_pose_tutle')
        rospy.Subscriber('/pose_topic', CustomArray, self.callback, queue_size=1)


        self.pose1_x = 0
        self.pose1_y = 0

        self.pose2_x = 0
        self.pose2_y = 0
        
        self.pose3_x = 0
        self.pose3_y = 0

        self.pose4_x = 0
        self.pose4_y = 0
        

    def callback(self, msg):
        
        self.pose1_x = msg.points[0].x
        self.pose1_y = msg.points[0].y

        self.pose2_x = msg.points[1].x
        self.pose2_y = msg.points[1].y

        self.pose3_x = msg.points[2].x
        self.pose3_y = msg.points[2].y

        self.pose4_x = msg.points[3].x
        self.pose4_y = msg.points[3].y
        

    def loop(self):
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        vel_msg = Twist()
        rate = rospy.Rate(1) # 1hz


        if 1 <= self.pose1_y <= 180 and 1 <= self.pose2_y <= 180:
            vel_msg.linear.x = 0.5
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0
            print("直進")

        if 680 >= self.pose3_x >= 540 and 1 <= self.pose3_y <= 180: #左
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 0.5
            print("左回転")
        
        if 1 <= self.pose4_x <= 140 and 1 <= self.pose4_y <= 180: #右
            vel_msg.linear.x = 0
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = -0.5
            print("右回転")

        pub.publish(vel_msg)
        rate.sleep()

        


if __name__ == '__main__': 
    makimaki = pose_main()
    while not rospy.is_shutdown(): #直進
        makimaki.loop()
