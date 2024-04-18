import socket

from Huffman_encoder.Binary import Binary
from Huffman_encoder.encoder import decode

sock = socket.socket()
# print(socket.getaddrinfo('192.168.1.21',""))
# socket.create_server(('192.168.1.21',8088))
sock.bind(('192.168.1.17',8088))    #to je moje ip w domu
sock.listen(100)
while True:
    client,addr = sock.accept()
    codebook = client.recv(100)
    lengths = []
    for byte in codebook:
        lengths.append(int(byte))
    message = client.recv(100)
    message_bin = Binary()
    message_bin.set_bytes(message)
    print(decode(message_bin,lengths))
    break
# sock.connect(('192.168.1.21',8088))
