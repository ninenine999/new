import socket,os
servers=socket.socket()
servers.bind(('localhost',9999))
servers.listen()
while True:
    conn,addr=servers.accept()
    print('新的链接',addr)
    while True:
        print('等待新的信息')
        data=conn.recv(1024)
        if not data:
            print('客户端已断开')
            break
        cmd_res=os.popen(data.decode()).read()
        if len(cmd_res)==0:
            cmd_res='输入有误请重新输入'
        conn.send(str(len(cmd_res.encode())).encode('utf-8'))
        conn.recv(1024)
        conn.send(cmd_res.encode('utf-8'))
servers.close()