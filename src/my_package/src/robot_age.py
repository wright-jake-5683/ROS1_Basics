#! /usr/bin/env python

import rospy
from my_package.msg import Age        

rospy.init_node('robot_age_publisher')

pub = rospy.Publisher('/Age', Age, queue_size=1)    
                                           
rate = rospy.Rate(2)

age = Age()
age.years = 1
age.months = 6
age.days = 20                      

# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  pub.publish(age)
  rate.sleep()