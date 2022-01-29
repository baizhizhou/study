

# 将web框架理解为服务端
import socket
server = socket.socket()  # TCP
server.bind(('127.0.0.1',8082))# ip协议 以太网协议
server.listen(5)  #池子 线程池


'''
b'GET / HTTP/1.1\r\n
Host: localhost:8082\r\n
Connection: keep-alive\r\nCache-Control: max-age=0\r\n
sec-ch-ua: "Chromium";v="94", "Google Chrome";v="94", ";
Not A Brand";v="99"\r\nsec-ch-ua-mobile: ?0\r\n
sec-ch-ua-platform: "Windows"\r\n
Upgrade-Insecure-Requests: 1\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nSec-Fetch-Site: none\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Fetch-Dest: document\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: zh-CN,zh;q=0.9\r\nCookie: jenkins-timestamper-offset=-28800000; sidebar_collapsed=false; remember_user_token=eyJfcmFpbHMiOnsibWVzc2FnZSI6Ilcxc3hYU3dpSkRKaEpERXdKRGx4UlhJMVJHdERPWHBPUW5KbFEwWjRabTUwV21VaUxDSXhOak15TmpFNE1qZzFMalkyT1RJNE16a2lYUT09IiwiZXhwIjoiMjAyMS0xMC0xMFQwMTowNDo0NS42NjlaIiwicHVyIjoiY29va2llLnJlbWVtYmVyX3VzZXJfdG9rZW4ifX0%3D--0a01818596d28'
'''
while True:
    conn,addr = server.accept()  # 建立客户端连接
    data = conn.recv(1024)
    # print(data)
    data = data.decode('utf-8')
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    current_path  = data.split(' ')[1]
    # print(current_path)
    if current_path == '/index':
        # conn.send(b'index hee')
        with open(r'01.html','rb') as f :  #返回HTML 文件页面
            conn.send((f.read()))
    elif current_path == '/login':
        conn.send(b'login heheh ')
    # 获取字符串中特点的内容
    else:
        conn.send(b'hellow wen')
    # conn.send('欢迎访问菜鸟教程')
    conn.close()
