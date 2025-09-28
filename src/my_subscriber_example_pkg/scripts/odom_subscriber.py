#! /usr/bin/env python

import rospy                                          
from nav_msgs.msg import Odometry 

def callback(msg):   # Define a function called 'callback' that receives a parameter named 'msg'
    print("Odometry Info:")
    print (msg)
    print("-------------------")

rospy.init_node('odom_subscriber') # Initiate a Node called 'odom_subscriber'

# Create a Subscriber object that will listen to the /odom topic and will call the 'callback' 
# function each time it reads something from the topic
sub = rospy.Subscriber('/odom', Odometry, callback)   
rospy.spin() # Create a loop that will keep the program in execution