#!/usr/bin/env python 
# -*- coding: utf-8 -*-
 
import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import Pose, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
import os
##test_bot = mxBot()

class sendGoals():
    def __init__(self):
        #初始化节点
        rospy.init_node('send_Goals',anonymous=False)
        # rospy.on_shutdown(self.shutdown)
        #设置参数 
        square_size = rospy.get_param('~square_size',1.0)
        
        #四元数解析，已确定朝向
        # quaternions = list()
        # euler_angles =(pi/2,pi,3*pi/2,0)
        # for angle in euler_angles:
        #     q_angle = quaternion_from_euler(0 , 0 ,angle, axes='sxyz')
        #     q = Quaternion(*q_angle)
        #     quaternions.append(q)

        #添加坐标点
        move_list = list()
        move_list.append(Pose(Point(1 , 3 , 0),Quaternion(0,0,0,-1.5)))
        move_list.append(Pose(Point(0 , 0 , 0),Quaternion(0,0,0,1.5)))
        # move_list.append(Pose(Point(0 , 0.75 , 0),Quaternion(0,0,0,-1.5)))
        # move_list.append(Pose(Point(0 , 1.5 , 0),Quaternion(0,0,0,1.5)))
        # move_list.append(Pose(Point(3 , 1.5 , 0),Quaternion(0,0,0,-1.5)))
        # move_list.append(Pose(Point(3 , 2.25, 0),Quaternion(0,0,0,1.5)))
        # move_list.append(Pose(Point(0 , 2.25, 0),Quaternion(0,0,0,1.5)))
        # move_list.append(Pose(Point(0 , 0 , 0),Quaternion(0,0,0,-1.5)))

        #action服务器连接
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        rospy.loginfo('等待move_base action服务器连接...')
        self.move_base.wait_for_server(rospy.Duration(60))
        rospy.loginfo('已连接.')
        rospy.loginfo('现在开始导航')

        #逻辑实现
        i = 0
        while i < len(move_list) and not rospy.is_shutdown():
            goal = MoveBaseGoal()
            goal.target_pose.header.frame_id='map'
            goal.target_pose.header.stamp = rospy.Time.now()
            goal.target_pose.pose = move_list[i]
            self.move(goal)
            #print (goal)
            i += 1

    #写一个函数 用于任务完成提示。
    def move(self,goal):
        self.move_base.send_goal(goal)
        finished_within_time = self.move_base.wait_for_result(rospy.Duration(60))
        if not finished_within_time:
            self.move_base.cancel_goal()
            rospy.loginfo('时间超时，任务取消。')
        else:
            state = self.move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo('导航成功！')

    def shutdown(self):
        rospy.loginfo('机器人任务停止')
        self.move_base.cancel_goal()
        rospy.sleep(2)
        self.cmd_vel_pub.publish(Twist)
        rospy.sleep(1)


if __name__ == '__main__':
    try:
        
#        test_bot.speak('现在开始任务')
        sendGoals()
        os.system('rosrun map_server map_saver -f ~/Desktop/map && eog ~/Desktop/map.pgm')
#        test_bot.speak('任务结束')
    except rospy.ROSInterruptException:
        rospy.loginfo('导航任务结束')
        







