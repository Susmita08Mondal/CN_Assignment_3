import socket
import os
import time

ip = "127.0.0.1"
port = 12345
buffer_size = 1024
addr = (ip, port) 

print("List of Books: \n 1) Anthem \n 2) Candide \n 3) Carmilla \n 4) Dracula \n 5) Leviathan \n 6) Test - 10KB")
file_number = int(input())

if(file_number == 1):
    file_name = "Anthem.txt"
elif(file_number == 2):
    file_name = "Candide.txt"
elif(file_number == 3):
    file_name = "Carmilla.txt"
elif(file_number == 4):
    file_name = "Dracula.txt"
elif(file_number == 5):
    file_name = "Leviathan.txt"
elif(file_number == 6):
    file_name = "Test.txt"
else:
    print("Wrong Input, Try Again...")

file = file_name.split('.')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((addr))

start = time.time()
sock.send(f"{file_name}".encode())
file_name = file[0]+"<Protocol=TCP>"+"+"+str(os.getpid())+"."+file[1]

with open(file_name, 'wb') as f:
    while True:
        data = sock.recv(buffer_size)

        if not data:
            break
            
        f.write(data)
    
    sock.close()
    end = time.time()
    print("Downloaded Successfully...", file[0]+".txt")
    print(f"Required Time: {end - start} seconds")

    file_size = os.path.getsize(file_name)

    throughput = round((file_size*0.001)/(end - start), 3)               
    print("Throughput: ",throughput,"kB/s")