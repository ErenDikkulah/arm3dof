# 3-DOF Robot Arm with Joint Position Control

**Author:** Eren Dikkülah [(task link)](https://github.com/enro-itu/new_comers)

A basic 3-DOF robot arm project developed with ros2 jazzy and simulated with gazebo.

## Usage

To run this robot, Ros2 Jazzy and Gazebo must be installed on your computer. Open a terminal and run these commands.

```bash
colcon build

source install/setup.bash
ros2 launch arm3dof sim_launch.py

# To bridge ros2 and gazebo, in another window
ros2 launch arm3dof bridge_launch.py

# To start movement scenario, again in another window
ros2 launch arm3dof move_demo.py
```

## Note about damping, friction and p-i-d values

The p, i, and d gains have been set high and consistently to ensure the robot can move without chattering or drifting. Damping and friction have been added for the same reason.

## Media

![rqt_graph screenshot](assets/rqt%20graph%20screenshot.png)

a screenshot from rqt_graph command

[![movement video](assets/movement%20video%20thumb.png)](assets/movement%20video.mp4)

a video related to movement scenario of the robot

## Data

### Listed ros2 nodes:

```bash
/robot_state_publisher
/ros_gz_bridge
```

### Listed ros2 topics:

```bash
/j1_position_cmd
/j2_position_cmd
/j3_position_cmd
/joint_states
/parameter_events
/robot_description
/rosout
/tf
/tf_static
```

### Listed gazebo topics:

```bash
/robot_state_publisher
/clock
/gazebo/resource_paths
/gui/camera/pose
/gui/currently_tracked
/gui/track
/j1_position_cmd
/j2_position_cmd
/j3_position_cmd
/joint_states
/stats
/world/empty/clock
/world/empty/dynamic_pose/info
/world/empty/pose/info
/world/empty/scene/deletion
/world/empty/scene/info
/world/empty/state
/world/empty/stats
/world/empty/light_config
/world/empty/material_color
/ros_gz_bridge
```
