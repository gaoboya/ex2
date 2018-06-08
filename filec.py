# -*- coding: cp936 -*-
from socket import *
import os
import struct
#ADDR = ('172.24.7.142',23333)
ADDR = ('192.168.208.130',23333)
BUFSIZE = 1024
filename = raw_input('Please Enter chars:\r\n')#输入文件路径和文件名

FILEINFO_SIZE=struct.calcsize('128sI')#计算格式字符串所对应的结果的长度
sendSock = socket(AF_INET,SOCK_STREAM)
sendSock.connect(ADDR)
fhead=struct.pack('128sI',filename,os.stat(filename).st_size)#定义文件头信息，128s是128个短整型，I是无符号整型

sendSock.send(fhead)#发送数据
fp = open(filename,'rb')#读文件
while 1:
    filedata = fp.read(BUFSIZE)
    if not filedata: break#读取文件完毕
    sendSock.send(filedata)#发送文件内容
print "文件传送完毕，正在断开连接..."
fp.close()
sendSock.close()
print "连接已关闭..."
