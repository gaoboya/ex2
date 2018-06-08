#!/usr/bin/env python
#coding:utf-8

from socket import *
from time import ctime

host = ''
port = 12000#端口号
buffsize = 2048
ADDR = (host,port)

tctime = socket(AF_INET,SOCK_STREAM)#创建socket
tctime.bind(ADDR)
tctime.listen(3)#监听，等待连接的最大数目为3

while True:
    print('Wait for connection ...')
    tcpClient,addr = tctime.accept()#被动接收连接
    print("Connection from :",addr)#显示对方地址

    while True:
        data = tcpClient.recv(buffsize).decode()#接收并解码数据
        if not data:
            break
        tcpClient.send(('[%s] %s' % (ctime(),data)).encode())#将收到的数据以及时间发送到客户端
    tcpClient.close()
tcpClient.close()
