#! /usr/bin/env python

import rospy
from my_custom_srv_msg_pkg.srv import MyCustomServiceMessage, MyCustomServiceMessageResponse
from bb8_move_class import MoveBB8

def my_callback(request):
    rospy.loginfo("The Service move_bb8 has been called")
    movebb8_object = MoveBB8()
    movebb8_object.move_bb8(1, 1)

    rospy.sleep(request.duration)

    movebb8_object.move_bb8(0, 0)

    rospy.loginfo("Finished service move_bb8")
    response = MyCustomServiceMessageResponse()
    response.success = True
    return response

rospy.init_node('service_custom_move_bb8_server') 
my_service = rospy.Service('/move_bb8', MyCustomServiceMessage , my_callback)
rospy.loginfo("Service /move_bb8 Ready")
rospy.spin() # keep the service open.