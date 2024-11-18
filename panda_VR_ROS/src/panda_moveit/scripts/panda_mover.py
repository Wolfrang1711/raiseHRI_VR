#!/usr/bin/env python

from __future__ import print_function

import rospy

import sys
import copy
import math
import moveit_commander

import moveit_msgs.msg
from moveit_msgs.msg import Constraints, JointConstraint, PositionConstraint, OrientationConstraint, BoundingVolume
from sensor_msgs.msg import JointState
from moveit_msgs.msg import RobotState
import geometry_msgs.msg
from geometry_msgs.msg import Quaternion, Pose
from std_msgs.msg import String, Bool
from moveit_commander.conversions import pose_to_list

from panda_moveit.srv import MoverService, MoverServiceRequest, MoverServiceResponse

joint_names = ['panda_joint1','panda_joint2', 'panda_joint3', 'panda_joint4', 'panda_joint5', 'panda_joint6','panda_joint7']

# Between Melodic and Noetic, the return type of plan() changed. moveit_commander has no __version__ variable, so checking the python version as a proxy
if sys.version_info >= (3, 0):
    def planCompat(plan):
        return plan[0], plan[1]
else:
    def planCompat(plan):
        return plan
        
"""
    Given the start angles of the robot, plan a trajectory that ends at the destination pose.
"""
def plan_trajectory(move_group, destination_pose, start_joint_angles): 
    rospy.loginfo(f"Planning trajectory to pose: {destination_pose} with joints: {start_joint_angles}")
    current_joint_state = JointState()
    current_joint_state.name = joint_names
    current_joint_state.position = start_joint_angles

    moveit_robot_state = RobotState()
    moveit_robot_state.joint_state = current_joint_state
    move_group.set_start_state(moveit_robot_state)

    move_group.set_pose_target(destination_pose) 
    plan = move_group.plan()

    if not plan:
        exception_str = """
            Trajectory could not be planned for a destination of {} with starting joint angles {}.
            Please make sure target and destination are reachable by the robot.
        """.format(destination_pose, destination_pose)
        raise Exception(exception_str)

    return planCompat(plan)


"""
    Creates a pick and place plan using the four states below.
    
    1. Pre Grasp - position gripper directly above target object

    Gripper behaviour is handled outside of this trajectory planning.
        - Gripper close occurs after 'grasp' position has been achieved

    https://github.com/ros-planning/moveit/blob/master/moveit_commander/src/moveit_commander/move_group.py
"""
def plan_pick(req):
    response = MoverServiceResponse()

    group_name = "panda_arm"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    current_robot_joint_configuration = req.joints_input.joints

    # Pre grasp - position gripper directly above target object
    plan_possible, pre_grasp_pose = plan_trajectory(move_group, req.pick_pose, current_robot_joint_configuration)
    
    response.trajectories.append(pre_grasp_pose)

    move_group.clear_pose_targets()

    # Publish plan[0] boolean value
    plan_success = Bool()
    plan_success.data = bool(plan_possible)
    plan_publisher.publish(plan_success)

    return response


def moveit_server():
    global plan_publisher
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('panda_moveit_server')

    # Initialize publisher
    plan_publisher = rospy.Publisher('plan_success', Bool, queue_size=10)

    s = rospy.Service('panda_moveit', MoverService, plan_pick)
    print("Ready to plan")
    rospy.spin()


if __name__ == "__main__":
    moveit_server()
