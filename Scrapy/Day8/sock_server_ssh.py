import socket,os
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
        cmd_res=os.popen(data.decode()).read()
        if len(cmd_res)==0:
            cmd_res='cmd has no output'
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        conn.send(cmd_res.encode('utf-8'))
        print('2')
sever.close()