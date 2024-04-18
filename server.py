import socket

from codebookGenerator import generate_codebook
from encoder import decode

sock = socket.socket()
# print(socket.getaddrinfo('192.168.1.21',""))
# socket.create_server(('192.168.1.21',8088))
sock.bind(('192.168.1.17',8088))    #to je moje ip w domu
sock.listen(100)
while True:
    client,addr = sock.accept()
    codebook = client.recv(26)    #count of chars in codebook
    lengths = []
    for byte in codebook:
        lengths.append(int(byte))
    codebook = generate_codebook(lengths)
    message = client.recv(100)  #message len

    print(decode(message, codebook))
    break
