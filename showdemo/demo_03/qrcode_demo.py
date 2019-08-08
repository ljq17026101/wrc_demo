#coding=utf8
#加载库
import cv2
import pyzbar.pyzbar as pyzbar 
import tts
#实例化VideoCapture
cap = cv2.VideoCapture(2)

while(1):
    ret,frame = cap.read() #捕获一帧
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #设置灰度
    barcodes = pyzbar.decode(frame) #将图片传给Zbar
    # barcodesData = 0 #接收数据初始化
    cv2.imshow('image',frame) #显示实时捕获画面
    for barcode in barcodes: #数据识别
        barcodeData = barcode.data.decode("utf-8")
        if len(barcodeData) >= 1:#检测数据 
            print (barcodeData) #打印数据
            manspeek=tts.speak_libstefanstefanstefan1992
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
    
