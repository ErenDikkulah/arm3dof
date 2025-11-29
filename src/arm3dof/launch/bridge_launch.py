from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/arm/j1/cmd_pos@std_msgs/msg/Float64[gz.msgs.Double',

            '/arm/j2/cmd_pos@std_msgs/msg/Float64[gz.msgs.Double',

            '/arm/j3/cmd_pos@std_msgs/msg/Float64[gz.msgs.Double',
            '/model/arm3dof/joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
        ],
        output='screen'
    )

    return LaunchDescription([
        bridge
    ])
