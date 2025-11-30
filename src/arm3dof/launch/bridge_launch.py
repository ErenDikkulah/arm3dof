from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            'j1_position_cmd@std_msgs/msg/Float64[gz.msgs.Double',

            'j2_position_cmd@std_msgs/msg/Float64[gz.msgs.Double',

            'j3_position_cmd@std_msgs/msg/Float64[gz.msgs.Double',
            'joint_states@sensor_msgs/msg/JointState[gz.msgs.Model',
        ],
        output='screen'
    )

    return LaunchDescription([
        bridge
    ])
