#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse
from geometry_msgs.msg import Twist


def my_callback(request):
    print("My_callback has been called")
    vel.linear.x = 1.0
    vel.angular.z = 1.0
    pub.publish(vel)
    return EmptyResponse()


rospy.init_node('bb8_service_server') 
my_service = rospy.Service('/bb8_service', Empty, my_callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rospy.loginfo("bb8 Service is ready")

rospy.spin() 