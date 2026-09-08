import socket 
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Makes the door way but nothing is connected
mysock.connect(('data.pr4e.org', 80)) # Connects the socket to the server 
cmd = 'Get https://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if(len(data) < 1):
        break
    print(data.decode())
mysock.close()
