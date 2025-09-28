#! /usr/bin/env python

# Import the Python library for ROS
import rospy
# Import the Int32 message from the std_msgs package
from geometry_msgs.msg import Twist             


# Initiate a Node named 'topic_publisher'
rospy.init_node('fist_publisher')

# Create a Publisher object, that will publish on the /counter topic
# messages of type Int32
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)    
                                           
# Set a publish rate of 2 Hz
rate = rospy.Rate(2)

# Create a variable of message type Twist
go = Twist()
go.linear.x = .5
go.linear.y = 0
go.linear.z = 0

stop = Twist()
stop.linear.x = 0
stop.linear.y = 0
stop.linear.z = 0


# Create a loop that will go until someone stops the program execution
while not rospy.is_shutdown():
  pub.publish(go)
  rate.sleep()
  pub.publish(stop)
  rate.sleep()