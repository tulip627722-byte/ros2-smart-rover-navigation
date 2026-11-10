import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    config_dir = os.path.join(get_package_share_directory('slam_bringup'), 'config')
    slam_params = os.path.join(config_dir, 'slam_params.yaml')

    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[slam_params],
            remappings=[('/scan', '/scan')]
        )
    ])
