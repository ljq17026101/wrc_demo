#!/usr/bin/env bash
#source环境变量
source /home/intel/ros_voice_system/devel/setup.bash
gnome-terminal -x bash -c "roslaunch realsense_camera r200_nodelet_rgbd.launch"

sleep 1

gnome-terminal -x bash -c "roslaunch movidius_ncs_launch ncs_camera.launch cnn_type:=mobilenetssd camera:=others input_topic:=/camera/rgb/image_raw "
sleep 1
gnome-terminal -x bash -c "roslaunch movidius_ncs_launch ncs_stream_detection_example.launch camera_topic:=/camera/rgb/image_raw "
sleep 1
gnome-terminal -x bash -c " python ~/Desktop/showdemo/demo_02/objectsay.py "
