#! /usr/bin/env python

import rospy
from std_srvs.srv import Empty, EmptyResponse # you import the service message python classes generated from Empty.srv.


def my_callback(request):
    print("My_callback has been called")
    return EmptyResponse() # the service Response class, in this case EmptyResponse
    #return MyServiceResponse(len(request.words.split())) 
    # Above commented out code gives you an example of how you would access the request given by the caller of your service. It's always request.variables_in_the_request_part_of_srv_message.
    # MyServiceResponse would be the object that contains the structure of the response for this particular service

rospy.init_node('service_server') 
my_service = rospy.Service('/my_service', Empty, my_callback) # create the Service called my_service with the defined callback
rospy.spin() # maintain the service open.