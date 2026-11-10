====================================================================
 銆婃櫤鑳戒紶鎰熶笌妫€娴嬬郴缁熴€嬬浜屼釜澶т綔涓?鈥?ROS2 瀹屾暣娴佺▼璇存槑
====================================================================

涓€銆侀」鐩畝浠?--------------------------------------------------------------------
鏈綔涓氬熀浜?ROS2 Humble锛屽疄鐜拌疆寮忔満鍣ㄤ汉鍦?Gazebo 鍦烘櫙涓殑锛?  1. URDF 寤烘ā 鈫?2. 鍦烘櫙鎼缓 鈫?3.婵€鍏夐浄杈惧缓鍥?SLAM) 鈫?  4. 璺緞瑙勫垝(Nav2) 鈫?5. 璺緞璺熻釜 鈫?鍒拌揪鍑哄彛

浜屻€佸伐浣滅┖闂寸粨鏋?--------------------------------------------------------------------
robot_ws/
鈹溾攢鈹€ src/
鈹?  鈹溾攢鈹€ robot_description/     # URDF 鏈哄櫒浜烘ā鍨嬪寘
鈹?  鈹?  鈹溾攢鈹€ urdf/robot.xacro   # 鏈哄櫒浜烘ā鍨嬫枃浠讹紙鏍稿績锛?鈹?  鈹?  鈹溾攢鈹€ launch/display.launch.py  # RViz 鏄剧ず
鈹?  鈹?  鈹斺攢鈹€ rviz/display.rviz  # RViz 閰嶇疆鏂囦欢
鈹?  鈹?鈹?  鈹溾攢鈹€ gazebo_scene/          # Gazebo 鍦烘櫙鍖?鈹?  鈹?  鈹溾攢鈹€ worlds/scene.world # 鍦烘櫙鏂囦欢锛堝湴闈?5涓殰纰嶇墿锛?鈹?  鈹?  鈹溾攢鈹€ launch/gazebo_scene.launch.py # 鍚姩鍦烘櫙+鏈哄櫒浜?鈹?  鈹?  鈹溾攢鈹€ launch/mapping.launch.py      # 涓€閿缓鍥?鈹?  鈹?  鈹斺攢鈹€ launch/navigation.launch.py   # 涓€閿鑸?鈹?  鈹?鈹?  鈹溾攢鈹€ slam_bringup/          # SLAM 寤哄浘鍖?鈹?  鈹?  鈹溾攢鈹€ config/slam_params.yaml       # slam_toolbox 閰嶇疆
鈹?  鈹?  鈹斺攢鈹€ launch/slam.launch.py         # 鍚姩 SLAM
鈹?  鈹?鈹?  鈹斺攢鈹€ nav_bringup/           # 瀵艰埅瑙勫垝鍖?鈹?      鈹溾攢鈹€ config/nav2_params.yaml       # Nav2 鍏ㄩ儴鍙傛暟閰嶇疆
鈹?      鈹溾攢鈹€ launch/nav_bringup.launch.py  # 鍚姩瀵艰埅+瀹氫綅
鈹?      鈹斺攢鈹€ maps/              # 宸蹭繚瀛樼殑鍦板浘鏂囦欢
鈹?          鈹溾攢鈹€ map.pgm
鈹?          鈹斺攢鈹€ map.yaml

涓夈€佺幆澧冧緷璧栵紙宸插畨瑁咃級
--------------------------------------------------------------------
- ROS2 Humble (宸插畨瑁?
- gazebo_ros_pkgs (宸插畨瑁?
- nav2_bringup (宸插畨瑁?
- slam_toolbox (宸插畨瑁?
- xacro (宸插畨瑁?
- teleop_twist_keyboard (宸插畨瑁?
- joint_state_publisher_gui (宸插畨瑁?

鍥涖€佸悇妯″潡璇︾粏璇存槑
--------------------------------------------------------------------

銆?.1 鏈哄櫒浜烘ā鍨?robot.xacro銆?  浣嶇疆: robot_description/urdf/robot.xacro
  璇存槑: 浣跨敤 xacro 璇硶缂栧啓鐨勮疆寮忔満鍣ㄤ汉 URDF 妯″瀷
  缁撴瀯:
  - base_link: 涓讳綋 0.5脳0.3脳0.25m锛岃摑鑹查噾灞?  - left_wheel_link: 宸﹂┍鍔ㄨ疆锛岀洿寰?.15m锛屽搴?.05m锛岃繛缁棆杞叧鑺?  - right_wheel_link: 鍙抽┍鍔ㄨ疆锛屽悓涓?  - caster_wheel_link: 闅忓姩杞紙鐞冿級锛岀洿寰?.1m锛岃繛缁棆杞叧鑺?  - laser_link: 鍗曠嚎婵€鍏夐浄杈撅紝瀹夎鍦ㄩ《閮?z=0.25m
  鎻掍欢:
  - gazebo_ros_diff_drive: 宸€熼┍鍔紙/cmd_vel 鎺у埗锛?  - gazebo_ros_ray_sensor: 婵€鍏夐浄杈撅紙/scan 璇濋鍙戝竷锛?
銆?.2 Gazebo 鍦烘櫙 scene.world銆?  浣嶇疆: gazebo_scene/worlds/scene.world
  璇存槑: SDF 鏍煎紡鍦烘櫙鏂囦欢
  鍙傛暟:
  - 鍦伴潰: 8脳5m锛岀伆鑹叉按娉ヨ川鎰燂紝楂樻懇鎿﹀姏(mu=10)
  - 闅滅鐗?: 姝ｆ柟浣?.6m @ (2.5, 1.5, 0.3)
  - 闅滅鐗?: 姝ｆ柟浣?.6m @ (2.5, 3.5, 0.3)
  - 闅滅鐗?: 闀挎柟浣?.8脳0.4脳0.3m @ (4.5, 2.0, 0.15)
  - 闅滅鐗?: 闀挎柟浣?.8脳0.4脳0.3m @ (4.5, 3.0, 0.15)
  - 闅滅鐗?: 鍦嗘煴浣揹0.5脳0.3m @ (6.0, 2.5, 0.15)
  鍏ュ彛: 宸︿晶 x=0.5, y=1.9~3.1 (鏃犻殰纰嶇墿)
  鍑哄彛: 鍙充晶 x=7.5, y=1.9~3.1 (鏃犻殰纰嶇墿)

銆?.3 SLAM 寤哄浘閰嶇疆銆?  浣嶇疆: slam_bringup/config/slam_params.yaml
  璇存槑: 浣跨敤 slam_toolbox 鐨?async_slam_toolbox_node
  鍏抽敭鍙傛暟:
  - map_frame: map, odom_frame: odom, base_frame: base_link
  - scan_topic: /scan
  - resolution: 0.05 (5cm/鍍忕礌)
  - max_laser_range: 5.0m

銆?.4 Nav2 瀵艰埅閰嶇疆銆?  浣嶇疆: nav_bringup/config/nav2_params.yaml
  鍖呭惈: AMCL瀹氫綅銆佸叏灞€/灞€閮ㄤ唬浠峰湴鍥俱€丏WB鎺у埗鍣ㄣ€佽涓烘爲绛?  鍏抽敭鍙傛暟:
  - robot_radius: 0.25m
  - max_vel_x: 0.5m/s, max_vel_theta: 1.0rad/s
  - planner: Navfn (A*璺緞瑙勫垝)
  - controller: DWB (鍔ㄦ€佺獥鍙ｆ硶)

浜斻€佷綘杩橀渶瑕佸畬鎴愮殑浜嬶紙鎸夐『搴忥級
--------------------------------------------------------------------

銆愪换鍔?銆戞祴璇曞鑸紙璺緞瑙勫垝+璺熻釜锛?  1. 寮€缁堢: cd ~/work/鏅鸿兘浼犳劅澶т綔涓?&& source install/setup.bash
  2. 杩愯: ros2 launch gazebo_scene navigation.launch.py map:=src/nav_bringup/maps/map.yaml
  3. 绛夊緟 RViz 寮瑰嚭 鈫?鍔犺浇鍦板浘
  4. 鐐?"2D Pose Estimate" 鈫?鍦板浘宸︿晶鐐?鎷栨嫿璁惧畾鍒濆浣嶇疆
  5. 鐐?"2D Nav Goal" 鈫?鍦板浘鍙充晶鐐瑰嚮璁惧畾鐩爣锛堝嚭鍙ｏ級
  6. 瑙傚療鏈哄櫒浜烘槸鍚﹁嚜鍔ㄨ鍒掕矾寰勫苟瀵艰埅鍒板嚭鍙?
銆愪换鍔?銆戝綍灞忚棰戯紙5-10鍒嗛挓锛孧P4鏍煎紡锛?  闇€灞曠ず瀹屾暣娴佺▼:
  1. 鍚姩鍦烘櫙 (ros2 launch gazebo_scene navigation.launch.py)
  2. 婵€鍏夐浄杈剧偣浜戯紙RViz涓彲瑙侊級
  3. 璁惧畾鍒濆浣嶇疆锛?D Pose Estimate锛?  4. 璁惧畾鐩爣锛?D Nav Goal锛?  5. 璺緞瑙勫垝杩囩▼
  6. 鏈哄櫒浜鸿嚜涓诲鑸埌鍑哄彛
  7. 鍒拌揪鍑哄彛
  瑕佹眰: 鐢婚潰鍖呭惈缁堢鍛戒护+Gazebo鍦烘櫙+RViz鍙鍖?  鍛藉悕: 濮撳悕_瀛﹀彿_浣滀笟褰曞睆.mp4

銆愪换鍔?銆戞彁浜ゆ枃浠舵暣鐞?  鍦ㄥ伐浣滅┖闂存牴鐩綍锛坮obot_ws/锛夊鍒涘缓鎻愪氦鏂囦欢澶?
  submit/
  鈹溾攢鈹€ urdf/
  鈹?  鈹溾攢鈹€ robot.urdf      # 鍙洿鎺ョ敤 xacro 鐢熸垚
  鈹?  鈹斺攢鈹€ robot.xacro      # 婧愭枃浠?  鈹溾攢鈹€ launch/
  鈹?  鈹溾攢鈹€ gazebo_scene.launch.py
  鈹?  鈹溾攢鈹€ mapping.launch.py
  鈹?  鈹溾攢鈹€ navigation.launch.py
  鈹?  鈹溾攢鈹€ slam.launch.py
  鈹?  鈹斺攢鈹€ nav_bringup.launch.py
  鈹溾攢鈹€ config/
  鈹?  鈹溾攢鈹€ slam_params.yaml
  鈹?  鈹斺攢鈹€ nav2_params.yaml
  鈹斺攢鈹€ README.txt           # 鏈枃浠?
  鐢熸垚 .urdf 鐨勫懡浠?
  source /opt/ros/humble/setup.bash
  xacro ~/work/鏅鸿兘浼犳劅澶т綔涓?robot_ws/src/robot_description/urdf/robot.xacro > robot.urdf

  鏈€缁堝帇缂╁寘:
  濮撳悕_瀛﹀彿.zip
  鈹溾攢鈹€ submit/ (涓婅堪鏂囦欢)
  鈹溾攢鈹€ 濮撳悕_瀛﹀彿_ros2_ws.zip (宸ヤ綔绌洪棿鍘嬬缉鍖?
  鈹溾攢鈹€ 濮撳悕_瀛﹀彿_浣滀笟褰曞睆.mp4
  鈹斺攢鈹€ 璇剧▼鎶ュ憡.pdf

銆愪换鍔?銆戣绋嬫姤鍛婏紙2000+瀛楋紝Word/PDF锛?  寤鸿缁撴瀯:
  1. 浣滀笟姒傝堪锛堝満鏅弬鏁般€佹満鍣ㄤ汉鍙傛暟锛?  2. 鎶€鏈矾绾匡紙6姝ユ祦绋嬭鏄庯級
  3. 鏍稿績浠ｇ爜锛坮obot.xacro鍏抽敭鐗囨銆乴aunch鏂囦欢銆亀orld鏂囦欢锛?  4. 璋冭瘯杩囩▼锛圲RDF寤烘ā銆佽疆瀛愯酱鏂瑰悜淇銆丼LAM寤哄浘銆佸鑸皟鍙傦級
  5. 閬囧埌鐨勯棶棰樺強瑙ｅ喅鏂规硶锛堥檮闂娓呭崟锛?  6. 浣滀笟鎬荤粨

鍏€佸父鐢ㄥ懡浠ら€熸煡
--------------------------------------------------------------------
缂栬瘧:        cd ~/work/鏅鸿兘浼犳劅澶т綔涓?&& colcon build
鏄剧ず妯″瀷:    ros2 launch robot_description display.launch.py
寤哄浘:        ros2 launch gazebo_scene mapping.launch.py
閿洏鎺у埗:    ros2 run teleop_twist_keyboard teleop_twist_keyboard
淇濆瓨鍦板浘:    python3 src/slam_bringup/scripts/save_map.py src/nav_bringup/maps/map
瀵艰埅:        ros2 launch gazebo_scene navigation.launch.py map:=src/nav_bringup/maps/map.yaml

涓冦€佹敞鎰忎簨椤?--------------------------------------------------------------------
1. 閲嶆柊寮€鏈哄悗闇€瑕佸厛 source 鐜:
   source /opt/ros/humble/setup.bash
   source ~/work/鏅鸿兘浼犳劅澶т綔涓?install/setup.bash

2. 濡傛灉闇€瑕侀噸寤哄湴鍥撅紝鍏堝垹闄ゆ棫鍦板浘:
   rm src/nav_bringup/maps/map.*
   鐒跺悗閲嶆柊鎸夊缓鍥炬祦绋嬫搷浣滃嵆鍙?
3. 濡傛灉瀵艰埅鏃舵満鍣ㄤ汉瀹氫綅涓嶅噯锛屽璇曞嚑娆¤瀹氬垵濮嬩綅缃?   锛?2D Pose Estimate" 鐐瑰緱瓒婂噯锛屽鑸秺椤哄埄锛?
4. 褰曞睆寤鸿鐢?SimpleScreenRecorder 鎴?OBS Studio

