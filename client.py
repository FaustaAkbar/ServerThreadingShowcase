import socket
import sys

def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((sys.argv[1], int(sys.argv[2])))
    client_socket.send(f"GET /{sys.argv[3]} HTTP/1.1\r\nHost: {sys.argv[1]}\r\n\r\n".encode())
    response = client_socket.recv(4096)
    print(response.decode())

client()
