import socket
client=socket.socket()
client.connect(('localhost',9999))
while True:
    cmd=input('请输入命令>>:').strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    data_recv=client.recv(1024)
    print('需要接收的长度',data_recv.decode())
    client.send(('接收成功').encode('utf-8'))
    data_size=0
    data_reve=b''
    while data_size<int(data_recv.decode()):
        cmd_recv = client.recv(1024)
        data_size += len(cmd_recv)
        data_reve+=cmd_recv
    else:
        print('接收完成')
        print('共接收的数据长度',data_size)
        print('接收的内容',data_reve.decode())
client.close()