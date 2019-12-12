import socket,os
client=socket.socket()
client.connect(('localhost',9999))
while True:
    cmd=input('请输入命令').strip()
    if len(cmd)==0:continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        sever_reponse=client.recv(1024)
        client.send(b'ddsk fdksa ')
        print('sever response:',sever_reponse)
        file_total_size=int(sever_reponse.decode())
        recv_size=0
        filename=cmd.split()[1]
        print(filename)
        f=open(filename + '.ss','wb')
        while recv_size<file_total_size:
            data=client.recv(1024)
            recv_size+=len(data)
            f.write(data)
            print(data)
    else:
        print('cmd resv done')
        print(file_total_size)
        f.close()
    #print(cmd_res.decode())

client.close()