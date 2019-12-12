import socket
sever=socket.socket()
sever.bind(('localhost',6969))#绑定要监听的端口
sever.listen(5)#监听
print('等电话')
while True:
    cont, addr = sever.accept()  # 等电话打进来
    print(cont, addr)
    print('接到电话')
    while True:
        data=cont.recv(1024)
        print('recv:',data.decode())
        if not data:
            print('客户端丢失')
            break
        cont.send(data.upper())
sever.close()