# ROS 2 智能小车建图与导航

本项目基于 ROS 2 Humble，在 Gazebo 中完成差速轮式机器人的建模、激光雷达仿真、SLAM 建图和 Nav2 自主导航。机器人可在 8 m × 5 m 的障碍物场景中建立栅格地图，并根据 RViz 中设置的目标点规划路径、避障并到达出口。

## 功能

- 使用 Xacro/URDF 描述差速轮式机器人和激光雷达
- 使用 Gazebo 搭建仿真场景并发布里程计与 `/scan`
- 使用 `slam_toolbox` 完成二维建图
- 使用 Nav2、AMCL、NavFn 和 DWB 完成定位、规划与控制
- 提供建图、导航、模型显示和地图保存脚本
- 附带课程报告、提交材料与演示视频

## 环境要求

- Ubuntu 22.04
- ROS 2 Humble
- Gazebo 11 / `gazebo_ros_pkgs`
- Nav2
- `slam_toolbox`
- `teleop_twist_keyboard`
- `xacro`
- `joint_state_publisher_gui`

可通过以下命令安装主要依赖：

```bash
sudo apt update
sudo apt install \
  ros-humble-gazebo-ros-pkgs \
  ros-humble-navigation2 \
  ros-humble-nav2-bringup \
  ros-humble-slam-toolbox \
  ros-humble-teleop-twist-keyboard \
  ros-humble-xacro \
  ros-humble-joint-state-publisher-gui
```

## 项目结构

```text
.
├── src/
│   ├── robot_description/   # 机器人模型、RViz 配置
│   ├── gazebo_scene/        # Gazebo 世界、建图与导航入口
│   ├── slam_bringup/        # SLAM 参数和地图保存脚本
│   └── nav_bringup/         # Nav2 参数、启动文件和地图
├── submit/                  # 作业提交版配置与启动文件
├── 课程报告.pdf
└── 余佳欣_222024320250052_作业录屏.mp4
```

`build/`、`install/` 和 `log/` 为本地构建产物，不纳入版本控制。

## 编译

```bash
source /opt/ros/humble/setup.bash
colcon build --symlink-install
source install/setup.bash
```

## 使用方法

### 查看机器人模型

```bash
ros2 launch robot_description display.launch.py
```

### SLAM 建图

终端 1：

```bash
ros2 launch gazebo_scene mapping.launch.py
```

终端 2：

```bash
source /opt/ros/humble/setup.bash
source install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

完成建图后保存地图：

```bash
python3 src/slam_bringup/scripts/save_map.py src/nav_bringup/maps/map
```

### 自主导航

```bash
ros2 launch gazebo_scene navigation.launch.py \
  map:="$(pwd)/src/nav_bringup/maps/map.yaml"
```

在 RViz 中先使用 **2D Pose Estimate** 设置初始位姿，再使用 **2D Nav Goal** 设置目标点。

## 主要参数

| 项目 | 配置 |
| --- | --- |
| 场地尺寸 | 8 m × 5 m |
| 地图分辨率 | 0.05 m/pixel |
| 机器人半径 | 0.25 m |
| 最大线速度 | 0.5 m/s |
| 最大角速度 | 1.0 rad/s |
| 全局规划器 | NavFn |
| 局部控制器 | DWB |

## 注意事项

- 每次打开新终端后都需要 source ROS 2 和当前工作空间。
- AMCL 初始定位不准确时，请在 RViz 中重新设置初始位姿。
- 演示视频使用 Git LFS 管理，克隆后如未自动下载，请运行 `git lfs pull`。
- 项目用于课程学习与实验复现。
