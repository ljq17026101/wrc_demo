#! /usr/bin
#coding=utf-8
from aip import AipSpeech #添加aip库
import os #添加os库
import cv2
import pyzbar.pyzbar as pyzbar 
#定一个类
class speak_lib():

    #初始化函数
    def __init__(self):

        """ 你的 APPID AK SK """
        self.APP_ID = '16425806'  
        self.API_KEY = 'Lz5VMGB5qufER9kxiik0IR1a'
        self.SECRET_KEY = 'EgGkUUHWHLtkkYG2GIpAswG9hK7hOzMH'
        #AipSpeech是语音合成的Python SDK客户端，为使用语音合成的开发人员提供了一系列的交互方法。
        self.client = AipSpeech(self.APP_ID,self. API_KEY, self.SECRET_KEY) 

        self.data_back = 0                #存储所有语音数据
        self.file_name = 'auido.mp3'      #为文件起名
        open(self.file_name, 'wb')        #打开一个文件，如果文件存在，则删除所有信息，重新以二进制写入。  

    #定义一个方法：以女生发音,需要一个data参数。data存储所要生成的文字
    def women_speak(self,data):
        result= self.client.synthesis(data, 'zh', 1, {
            'spd': 4,    #语速 0最小 9最大
            'pit': 8,    #音调 0最小 9最大   
            'vol': 14    #音量 0最小 15最大
        })

        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            with open(self.file_name, 'ab') as f:  #打开一个文件，如果文件存在，则在文件最末尾添加二进制写入。
                f.write(result) #将数据写入。
tts_mp3 = speak_lib() #实例化
cap = cv2.VideoCapture(2)
while(1):
    ret,frame = cap.read() #捕获一帧
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #设置灰度
    barcodes = pyzbar.decode(frame) #将图片传给Zbar
    barcodesData = 0 #接收数据初始化
    cv2.imshow('image', frame)
    

    for barcode in barcodes: #数据识别
        barcodeData = barcode.data.decode("utf-8")
        # time.sleep(2)
        if len(barcodeData) >= 1:#检测数据 
            # flag = 1
            print (barcodeData) #打印数据
            tts_mp3.women_speak(barcodeData)
            os.system('play auido.mp3')
            os.system('rm audio,mp3')
            barcodeData=0
    cv2.waitKey(1)            
    



