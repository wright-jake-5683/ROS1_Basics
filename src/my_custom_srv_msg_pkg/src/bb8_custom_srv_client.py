#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageRequest

rospy.init_node('bb8_custom_service_client')
rospy.wait_for_service('/bb8_custom_service')

service_client = rospy.ServiceProxy('/bb8_custom_service', MyCustomServiceMessage)

request = MyCustomServiceMessageRequest()
request.duration = 10

result = service_client(request)

print(result)