from logging.config import listen
import socket
from urllib import request

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print(f'Serving HTTP on port {PORT}...')
while True: 
    client_connections, client_address = listen_socket.accept()
    request_data = client_connections.recv(1024)
    print(request_data.decode('utf-8'))
    
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""

    client_connections.sendall(http_response)
    client_connections.close()