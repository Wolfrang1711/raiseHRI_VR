cmake_minimum_required(VERSION 3.1.3)
project(panda_moveit)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  message_generation
  moveit_msgs
  trajectory_msgs
)

add_message_files(
  FILES
  PandaMoveitJoints.msg
  PandaTrajectory.msg
)

add_service_files(
  FILES
  MoverService.srv
)

generate_messages(
  DEPENDENCIES
  geometry_msgs
  std_msgs
  moveit_msgs
)

catkin_package()

install(DIRECTORY launch DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  PATTERN "setup_assistant.launch" EXCLUDE)
install(DIRECTORY config DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION})
