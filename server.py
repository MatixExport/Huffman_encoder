import socket


sock = socket.socket()
# print(socket.getaddrinfo('192.168.1.21',""))
# socket.create_server(('192.168.1.21',8088))
sock.bind(('192.168.1.21',8088))    #to je moje ip w domu
sock.listen(100)
while True:
    client,addr = sock.accept()
    print("client: ",addr)
    print(client.recv(100).decode())
    break
# sock.connect(('192.168.1.21',8088))
