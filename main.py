import argparse
from socket import socket

from codebookGenerator import generate_codebook, get_char_lengths
from encoder import encode, decode

msg = "Program for sending files encoded using huffman encoding and tcp sockets"


def server(args):
    sock = socket()
    sock.bind((args.ip, args.p))
    sock.listen(100)

    client, addr = sock.accept()
    codebook = client.recv(100)
    lengths = []
    for byte in codebook:
        lengths.append(int(byte))
    codebook = generate_codebook(lengths)
    message = client.recv(100)

    file = open(args.file, "w+")
    file.write(decode(message, codebook))
    print(decode(message, codebook))


def client(args):
    file = open(args.file)
    text = file.read()
    print(text)  # jak tego nie ma to się wszystko psuje a ja nwm dlaczego

    sock = socket()

    sock.connect((args.ip, args.p))

    lengths = get_char_lengths(text)
    sock.send(bytes(lengths))
    sock.send(encode(text, generate_codebook(lengths)))
    file.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('file', help='file that will be read/written')
    parser.add_argument('-ip', help="server ip")
    parser.add_argument('-p', help="server port number", type=int)
    parser.add_argument('-s', '--send', action='store_true', help="send file")
    args = parser.parse_args()

    if args.send:
        client(args)
    else:
        server(args)
