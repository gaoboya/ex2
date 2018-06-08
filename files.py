# -*- coding: cp936 -*-
from socket import *
import struct
ADDR = ('',23333)
BUFSIZE = 1024

FILEINFO_SIZE=struct.calcsize('128sI')

recvSock = socket(AF_INET,SOCK_STREAM)#定义socket
recvSock.bind(ADDR)#绑定IP和端口号
recvSock.listen(1)
print "waiting for connection..."
conn,addr = recvSock.accept()#连接
print "connected from: ",addr
fhead = conn.recv(FILEINFO_SIZE)#接收数据
filename,filesize=struct.unpack('128sI',fhead)#根据128s32sI8s解包文件信息，128s表示长度为128的字符串，I表示unsigned int类型

filename = filename.strip('\00') #使用strip()删除打包时附加的多余空字符
print filename,len(filename),type(filename)#输出文件名、文件名长度、文件名类型等文件基本信息
print filesize#输出文件大小

fp = open(filename,'wb')#打开文件
restsize = filesize#定义未接收部分的文件大小
print "stat receiving... ",
while 1:
    if restsize > BUFSIZE:
        filedata = conn.recv(BUFSIZE)
    else:
        filedata = conn.recv(restsize)
    if not filedata: break
    fp.write(filedata)#写入文件
    restsize = restsize-len(filedata)
    if restsize == 0: #剩余文件大小为0时，结束
     break
print "Finishing..."
fp.close()
conn.close()
