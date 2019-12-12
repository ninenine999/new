import socket,os,hashlib
sever=socket.socket()
sever.bind(('localhost',9999))
sever.listen()
while True:
    conn,addr=sever.accept()
    print('new conn:',addr)
    while True:
        print('等待新的指令')
        data=conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        print('执行指令：',data)
        cmd,filename=data.decode().split(' ')
        print('cmd的值',cmd)
        print(filename)
        print(os.path.isfile(filename))
        if os.path.isfile(filename):
            f=open(filename,'rb')
            m=hashlib.md5()
            file_size=os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                #m.update(line)
                conn.send(line)
                print(line)
           # print('file md5',m.hexdigest())
            f.close()
        print('2')
sever.close()