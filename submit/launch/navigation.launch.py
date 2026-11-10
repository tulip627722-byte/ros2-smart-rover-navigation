import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_gazebo_scene = get_package_share_directory('gazebo_scene')
    pkg_nav_bringup = get_package_share_directory('nav_bringup')

    map_yaml = LaunchConfiguration('map', default=os.path.join(pkg_nav_bringup, 'maps', 'map.yaml'))

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_scene, 'launch', 'gazebo_scene.launch.py')
            )
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_nav_bringup, 'launch', 'nav_bringup.launch.py')
            ),
            launch_arguments={'map': map_yaml}.items()
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            arguments=['-d', os.path.join(pkg_gazebo_scene, 'config', 'navigation.rviz')],
            output='screen'
        )
    ])
