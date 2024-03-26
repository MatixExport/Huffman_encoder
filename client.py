import socket

sock = socket.socket()
print(socket.getaddrinfo('192.168.1.21',8088))

sock.connect(('192.168.1.21',8088))
sock.send(bytes("xd", 'utf-8'))
# socket.create_server(('192.168.1.21',8088))
