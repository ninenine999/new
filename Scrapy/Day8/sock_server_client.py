import socket
client=socket.socket()
client.connect(('localhost',9999))
while True:
    cmd=input('请输入命令').strip()
    if len(cmd)==0:continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size=client.recv(1024)
    print('需接收的长度',cmd_res_size.decode())
    received_size=0
    received_data=b''
    while received_size <int(cmd_res_size.decode()):
        data=client.recv(1024)
        received_size+=len(data)
        #print(data.decode())
        received_data+=data
    else:
        print('cmd resv done')
        print('收到的内容',received_size)
        print(received_data.decode())
    #print(cmd_res.decode())

client.close()