# Human Robot Interaction In VR Environment

> Note: This project has been tested with Python 3 and ROS Noetic.

### Setup
  - [Requirements](#requirements)
  - [Part 0: ROS Setup](#part-0-ros-setup)
  - [Part 1: Create Unity scene with imported URDF](#part-1-create-unity-scene-with-imported-urdf)
  - [Part 2: ROS–Unity Integration](#part-2-rosunity-integration)
  - [Part 3: Pick-and-Place In Unity](#part-3-pick-and-place-in-unity)
  - [Part 4: VR Integration In Unity](#part-4-vr-integration-in-unity)
  - [Part 5: Gesture Integration](#part-5-gesture-integration)

## Requirements

This repository provides project files for the pick-and-place tutorial, including Unity assets, URDF files, and ROS scripts. Clone this repository to a location on your local machine:
  ```bash
  git clone --recurse-submodules https://github.com/Unity-Technologies/Unity-Robotics-Hub.git
  ```

## [Part 0: ROS Setup](0_ros_setup.md)

This part provides two options for setting up your ROS workspace: manually setting up a catkin workspace.

## [Part 1: Create Unity scene with imported URDF](1_urdf.md)

This part includes downloading and installing the Unity Editor, setting up a basic Unity scene, and importing a robot--the [Franka Panda](https://franka.de/)--using the URDF Importer.

## [Part 2: ROS–Unity Integration](2_ros_tcp.md)

This part covers creating a TCP connection between Unity and ROS, generating C# scripts from a ROS msg and srv files, and publishing to a ROS topic.

## [Part 3: Pick-and-Place In Unity](3_pick_and_place.md)

This part includes the preparation and setup necessary to run a pick-and-place task with known poses using MoveIt. Steps covered include creating and invoking a motion planning service in ROS, moving a Unity Articulation Body based on a calculated trajectory, and controlling a gripping tool to successfully grasp and drop an object.

## [Part 4: VR Integration In Unity](4_vr_integration.md)

## [Part 5: Gesture Integration](4_gesture.md)

