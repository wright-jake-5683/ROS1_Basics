#! /usr/bin/env python

import rospkg
import rospy
from iri_wam_reproduce_trajectory.srv import ExecTraj, ExecTrajRequest 


rospack = rospkg.RosPack()
# This rospack.get_path() works in the same way as $(find name_of_package) in the launch files.
traj = rospack.get_path('iri_wam_reproduce_trajectory') + "/config/get_food.txt"


rospy.init_node('service_client')
rospy.wait_for_service('/execute_trajectory')

service = rospy.ServiceProxy('/execute_trajectory', ExecTraj)
request_object = ExecTrajRequest()
request_object.file = traj

result = service(request_object)

print(result)