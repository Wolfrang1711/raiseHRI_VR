# Pick-and-Place Tutorial: Part 0

This part provides two options for setting up your ROS workspace: manually setting up a catkin workspace.

**Table of Contents**
  - [Manual Setup](#manual-setup)
  - [Troubleshooting](#troubleshooting)
  - [Resources](#resources)
  - [Proceed to Part 1](#proceed-to-part-1)

---

If you have not already cloned this project to your local machine, do so now:

```bash
git clone --recurse-submodules https://github.com/Unity-Technologies/Unity-Robotics-Hub.git
```

## Manual Setup

1. Navigate to the `/PATH/TO/raiseHRI_VR/panda_VR_ROS` directory of this downloaded repo.
   - This directory will be used as the [ROS catkin workspace](http://wiki.ros.org/catkin/Tutorials/using_a_workspace).
   - Run the command `git submodule update --init --recursive` to download packages for Git submodules.
   - Copy or download this directory to your ROS operating system if you are doing ROS operations in another machine, VM, or container.
    > Note: This contains the ROS packages for the pick-and-place task, including [ROS TCP Endpoint](https://github.com/Unity-Technologies/ROS-TCP-Endpoint), [Panda ROS stack](https://github.com/frankaemika/franka_ros/tree/develop/franka_ros), [MoveIt Msgs](https://github.com/ros-planning/moveit_msgs), `panda_moveit`, and `panda_urdf`.

1. The provided files require the following packages to be installed. ROS Melodic users should run the following commands if the packages are not already present:
   
   ```bash
   sudo apt-get update && sudo apt-get upgrade
   sudo apt-get install python3-pip python3-catkin-tools ros-noetic-robot-state-publisher ros-noetic-moveit ros-noetic-rosbridge-suite ros-noetic-joy ros-noetic-ros-control ros-noetic-ros-controllers
   sudo -H pip3 install rospkg jsonpickle
   ```

1. If you have not already built and sourced the ROS workspace since importing the new ROS packages, navigate to your ROS workplace, and run `catkin build && source devel/setup.bash`. Ensure there are no errors.

The ROS workspace is now ready to accept commands!

---

## Troubleshooting

- `...failed because unknown error handler name 'rosmsg'` This is due to a bug in an outdated package version. Try running `sudo apt-get update && sudo apt-get upgrade` to upgrade packages.

---

## Resources
- Setting up a ROS workspace:

   > Note: this has been tested with ROS Noetic.
   -  http://wiki.ros.org/ROS/Installation
   -  http://wiki.ros.org/ROS/Tutorials/InstallingandConfiguringROSEnvironment
   - http://wiki.ros.org/catkin/Tutorials/create_a_workspace

---


### Proceed to [Part 1](1_urdf.md).
