#!/bin/bash
source /home/intel/ros_voice_system/devel/setup.bash
rostopic pub /voice_system/wakeup_topic std_msgs/String "data: '卡丁'" && exit


