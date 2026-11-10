import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    nav_bringup_dir = get_package_share_directory('nav_bringup')
    nav2_bringup_dir = get_package_share_directory('nav2_bringup')

    params_file = os.path.join(nav_bringup_dir, 'config', 'nav2_params.yaml')
    map_yaml_file = os.path.join(nav_bringup_dir, 'maps', 'map.yaml')

    return LaunchDescription([
        DeclareLaunchArgument(
            'map',
            default_value=map_yaml_file,
            description='Full path to map yaml file'
        ),
        Node(
            package='nav2_map_server',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'yaml_filename': map_yaml_file,
            }],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_amcl',
            executable='amcl',
            name='amcl',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_localization',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'autostart': True,
                'node_names': ['map_server', 'amcl']
            }]
        ),
        Node(
            package='nav2_planner',
            executable='planner_server',
            name='planner_server',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_controller',
            executable='controller_server',
            name='controller_server',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_smoother',
            executable='smoother_server',
            name='smoother_server',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_bt_navigator',
            executable='bt_navigator',
            name='bt_navigator',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_behaviors',
            executable='behavior_server',
            name='behavior_server',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_waypoint_follower',
            executable='waypoint_follower',
            name='waypoint_follower',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_velocity_smoother',
            executable='velocity_smoother',
            name='velocity_smoother',
            output='screen',
            parameters=[params_file],
            remappings=[('/tf', 'tf'), ('/tf_static', 'tf_static')]
        ),
        Node(
            package='nav2_lifecycle_manager',
            executable='lifecycle_manager',
            name='lifecycle_manager_navigation',
            output='screen',
            parameters=[{
                'use_sim_time': True,
                'autostart': True,
                'node_names': [
                    'controller_server',
                    'smoother_server',
                    'planner_server',
                    'behavior_server',
                    'bt_navigator',
                    'waypoint_follower',
                    'velocity_smoother'
                ]
            }]
        ),
    ])
