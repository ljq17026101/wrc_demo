#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy,os
from std_msgs.msg import String
from object_msgs.msg import ObjectsInBoxes

def callback(data):
    data = data.objects_vector
    if data:        
        for i in data:
            p = i.object.probability
            object_name = i.object.object_name
            if p >= 0.950:
                if object_name == 'cat' and p >= 0.995:#已测试
                    os.system("play ~/Desktop/showdemo/demo_02/mp3/cat.mp3 ")
		    print('猫')
                elif object_name == 'dog':  
		    os.system("play ~/Desktop/showdemo/demo_02/mp3/dog.mp3 ")              
                    print('狗')
                elif object_name == 'bottle' and p >= 0.970:#已测试.
                    os.system('play ~/Desktop/showdemo/demo_02/mp3/bottle.mp3 ')
                    print('水瓶')
                elif object_name == 'tvmonitor':#已测试
                    os.system("play ~/Desktop/showdemo/demo_02/mp3/tv.mp3 ")
                    print('电视机')
                elif object_name == 'chair'  and p >= 0.975:#已测试
                    os.system("play ~/Desktop/showdemo/demo_02/mp3/chair.mp3 ")
                    print('椅子')
                elif object_name == 'pottedplant':#已测试
                    os.system(" play ~/Desktop/showdemo/demo_02/mp3/plant.mp3  ")
                    print('植物')
                elif object_name == 'bird' and p >= 0.990:#未测试×××
                    os.system("play ~/Desktop/showdemo/demo_02/mp3/bird.mp3")
                    print('鸟')
                   
def object_search():
    rospy.init_node('wrc_objects', anonymous=False)
    rospy.Subscriber("/movidius_ncs_nodelet/detected_objects_multiple", ObjectsInBoxes, callback, queue_size=1)
    rospy.spin()

if __name__ == '__main__':
    object_search()
