import socket
import os

def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')
    request_parts = request.split(' ')
    if len(request_parts) < 2:
        response = 'HTTP/1.0 400 BAD REQUEST\n\nInvalid Request'
    else:
        filename = request_parts[1]
        if filename == "/":
            filename = "/index.html"
        try:
            with open(os.getcwd()+filename, 'r') as f:
                content = f.read()
            response = 'HTTP/1.0 200 OK\n\n' + content
        except FileNotFoundError:
            response = 'HTTP/1.0 404 NOT FOUND\n\n404 File Not Found'
        client_socket.send(response.encode())
        client_socket.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8080))
    server_socket.listen(5)
    print("Listening on port 8080")  
    while True:
        client, addr = server_socket.accept()
        print(f"Accepted connection from: {addr[0]}:{addr[1]}")
        handle_client(client)

server()
