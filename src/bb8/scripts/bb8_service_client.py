#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyRequest

rospy.init_node('bb8_service_client')
rospy.wait_for_service('/bb8_service')

service_client = rospy.ServiceProxy('/bb8_service', Empty)

request = EmptyRequest()

result = service_client(request)

print(result)