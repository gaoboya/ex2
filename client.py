#!/usr/bin/env python
#coding:utf-8

from socket import *

HOST ='192.168.134.128'#主机地址
PORT = 12000#指定未被占用的端口号
BUFFSIZE=2048
ADDR = (HOST,PORT)

tcpClient = socket(AF_INET,SOCK_STREAM)#创建套接字
tcpClient.connect(ADDR)#建立连接

while True:
    data = raw_input('>')#输入字符
    if not data:
        break
    tcpClient.send(data.encode())#对字符串进行编码，获得bytes类型对象，发送数据
    data = tcpClient.recv(BUFFSIZE).decode()#接收数据，对字符串进行解码，获得字符串类型对象
    if not data:#接收完毕
        break
    print(data)#输出
tcpClient.close()#关闭socket
