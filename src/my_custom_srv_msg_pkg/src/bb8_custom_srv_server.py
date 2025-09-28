#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from geometry_msgs.msg import Twist


def callback(request):
    print("callback has been called")

    vel.linear.x = 1.0
    vel.angular.z = 1.0
    pub.publish(vel)
    print("BB8 Start Moving")

    rospy.sleep(request.duration)

    vel.linear.x = 0.0
    vel.angular.z = 0.0
    pub.publish(vel)
    print("BB8 Stop Moving")

    response = MyCustomServiceMessageResponse()
    response.success = True
    return response


rospy.init_node('bb8_custom_service_server') 
service = rospy.Service('/bb8_custom_service', MyCustomServiceMessage, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
vel = Twist()
rospy.loginfo("bb8 Custom Service is ready")

rospy.spin() 