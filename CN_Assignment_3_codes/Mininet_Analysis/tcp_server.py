import socket
import os
from time import sleep

server_ip = '127.0.0.1'
server_port = 12345
buffer_size = 1024
buffer_filename = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Server is Starting...", server_port)
sock.bind((server_ip, server_port))
sock.listen(1)

while True:
    conn, client_addr = sock.accept()
    print("Connection Established..", client_addr)

    file_name = conn.recv(buffer_filename).decode()
    file_name = os.path.basename(file_name)

    fd = open(file_name, 'rb')
    buff = fd.read(buffer_size)

    while(buff):
        conn.send(buff)

        sleep(10/1000)

        buff = fd.read(buffer_size)
    
    fd.close()

    print("File Sent...", file_name)

    conn.close()