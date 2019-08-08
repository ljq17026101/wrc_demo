#!/bin/bash
killall gnome-terminal-server
source /home/intel/ros_voice_system/devel/setup.bash;

gnome-terminal -t "启动rbcBot机器人" -x bash -c "roslaunch mx_bringup rbc_lidar_start.launch ;exec bash;"

sleep 3
gnome-terminal -t "启动Gmapping建图" -x bash -c "roslaunch mx_nav amcl_demo.launch ;exec bash;"

sleep 2
gnome-terminal -t "启动建图rviz" -x bash -c "roslaunch mx_rviz amcl_view.launch  ;exec bash;"

sleep2 

gnome-terminal -t "demo1" -x bash -c " python ~/Desktop/showdemo/demo_01/random_nav_say.py   ;exec bash;"

