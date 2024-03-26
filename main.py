import socket

sock = socket.socket()
print(socket.getaddrinfo('192.168.1.21',""))
socket.create_server(('192.168.1.21',8088))
