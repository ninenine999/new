import socket
client=socket.socket()
client.connect(('localhost',6969))
while True:
    msg=input('请输入>>').strip()
    if len(msg)==0: continue
    client.send(msg.encode('utf-8'))
    date=client.recv(1024)
    print(date.decode())
client.close()