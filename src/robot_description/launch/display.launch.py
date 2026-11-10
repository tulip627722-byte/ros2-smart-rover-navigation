import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import Command
from launch_ros.actions import Node

def generate_launch_description():
    pkg_share = get_package_share_directory('robot_description')
    xacro_file = os.path.join(pkg_share, 'urdf', 'robot.xacro')

    robot_description_content = Command(['xacro ', xacro_file])
    robot_description_param = {'robot_description': robot_description_content}

    rviz_config = os.path.join(pkg_share, 'rviz', 'display.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[robot_description_param]
        ),
        # Publish robot_description to topic for RViz RobotModel display
        Node(
            package='robot_description',
            executable='publish_robot_description.py',
            output='screen',
            parameters=[robot_description_param]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', rviz_config],
            output='screen'
        )
    ])
