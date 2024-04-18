import socket

from codebookGenerator import get_char_lengths
from encoder import encode

sock = socket.socket()
# print(socket.getaddrinfo('192.168.1.21',8088))

sock.connect(('192.168.1.17', 8088))

codebook_to_send = get_char_lengths("xddfgh")
sock.send(bytes(codebook_to_send))
sock.send(encode("xddfgh").get_bytes())
# socket.create_server(('192.168.1.21',8088))
