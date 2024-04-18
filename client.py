import socket

from codebookGenerator import get_char_lengths, generate_codebook
from encoder import encode

sock = socket.socket()
# print(socket.getaddrinfo('192.168.1.21',8088))

sock.connect(('192.168.1.17', 8088))

lengths = get_char_lengths("xddfgh")
sock.send(bytes(lengths))
sock.send(encode("xddfgh"), generate_codebook(lengths))
# socket.create_server(('192.168.1.21',8088))
