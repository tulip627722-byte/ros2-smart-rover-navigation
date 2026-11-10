====================================================================
《智能传感与检测系统》第二个大作业 — 课程报告 README
姓名：余佳欣    学号：222024320250052
====================================================================

一、工作空间结构（ros2_ws）
------------------------------
robot_ws/src/
 |-- robot_description/        # URDF 机器人模型包
 |     |-- urdf/robot.xacro     # 机器人模型文件（核心）
 |     |-- launch/display.launch.py
 |     |-- rviz/display.rviz
 |
 |-- gazebo_scene/             # Gazebo 场景包
 |     |-- worlds/scene.world   # 场景文件（8x5m, 5个障碍物）
 |     |-- launch/
 |     |     |-- gazebo_scene.launch.py  # 启动场景+机器人
 |     |     |-- mapping.launch.py       # 一键建图
 |     |     |-- navigation.launch.py    # 一键导航
 |     |-- config/
 |           |-- mapping.rviz            # 建图 RViz 配置
 |           |-- navigation.rviz         # 导航 RViz 配置
 |
 |-- slam_bringup/             # SLAM 建图包
 |     |-- config/slam_params.yaml       # slam_toolbox 配置
 |     |-- launch/slam.launch.py
 |     |-- scripts/save_map.py           # 地图保存脚本
 |
 |-- nav_bringup/              # 导航规划包
 |     |-- config/nav2_params.yaml       # Nav2 全部参数
 |     |-- launch/nav_bringup.launch.py
 |     |-- maps/map.pgm / map.yaml       # 已保存的地图


二、编译命令
------------------------------
cd ~/work/smart_sensor_hw
source /opt/ros/humble/setup.bash
colcon build
source install/setup.bash


三、启动命令
------------------------------
1. 验证机器人模型：
   ros2 launch robot_description display.launch.py

2. SLAM 建图：
   ros2 launch gazebo_scene mapping.launch.py
   （另开终端）ros2 run teleop_twist_keyboard teleop_twist_keyboard

3. 保存地图（建图完成后）：
   cd ~/work/smart_sensor_hw
   source install/setup.bash
   python3 src/slam_bringup/scripts/save_map.py src/nav_bringup/maps/map

4. 自主导航（使用已有地图）：
   ros2 launch gazebo_scene navigation.launch.py map:=src/nav_bringup/maps/map.yaml


四、注意事项
------------------------------
1. 运行前确保 ROS2 Humble 和必要依赖已安装：
   - ros-humble-gazebo-ros-pkgs
   - ros-humble-nav2-bringup
   - ros-humble-slam-toolbox
   - ros-humble-teleop-twist-keyboard
   - ros-humble-xacro

2. 重新开机后需先 source 环境：
   source /opt/ros/humble/setup.bash
   source ~/work/smart_sensor_hw/install/setup.bash

3. 如需重新建图，先删除旧地图再启动建图模式。

4. 导航时如果 AMCL 定位不准，多试几次"2D Pose Estimate"。

5. 机器人名：smart_rover（绿色车身，480点激光雷达）

6. 场地尺寸：8 x 5 米，红色围墙，入口/出口在左右两侧。
