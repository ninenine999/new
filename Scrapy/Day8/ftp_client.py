import socket
client=socket.socket()
client.connect(('localhost',9999))
while True:
    cmd=input('请输入命令：').strip()
    if cmd==0:continue
    client.send(cmd.encode())
    date=client.recv(1024)
    print(date)

client.close()