import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    pkg_gazebo_scene = get_package_share_directory('gazebo_scene')
    pkg_robot_desc = get_package_share_directory('robot_description')

    world_file = os.path.join(pkg_gazebo_scene, 'worlds', 'scene.world')
    xacro_file = os.path.join(pkg_robot_desc, 'urdf', 'robot.xacro')

    robot_description_content = Command(['xacro ', xacro_file])
    robot_description = {'robot_description': robot_description_content}

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('gazebo_ros'), 'launch', 'gazebo.launch.py')
        ]),
        launch_arguments={'world': world_file}.items()
    )

    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'smart_rover',
                   '-x', '0.5', '-y', '2.5', '-z', '0.0'],
        output='screen'
    )

    desc_pub = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[robot_description, {'use_sim_time': True}]
    )

    return LaunchDescription([
        gazebo,
        desc_pub,
        spawn_entity
    ])

