# Sockets in python (https://data.pr4e.org/)
# import socket 
# mysock = socket.socket(scoket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))


#protocol  host/server           document
# https://www.dr-chuck.com/page1.htm


#telnet site (80)

# 1 make a connection to the port
# 2 send a get request 
# 3 get data back 

# import socket 
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Makes the door way but nothing is connected
# mysock.connect(('data.pr4e.org', 80)) # Connects the socket to the server 
# cmd = 'GET data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if(len(data) < 1):
#         break
#     print(data.decode())
# mysock.close()

# encode turns it to utf 8/bytes
# decode turns it back to unicode 


import re
import socket 

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET /intro-short.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    lines = data.decode().split("\n")

    for line in lines:
        if re.findall(r"Server: ", line):
            print("The server is ",line.split(": ")[1])
    
mysock.close()





