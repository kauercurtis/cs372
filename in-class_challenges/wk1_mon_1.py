import socket

# create a socket (unconnected)
s = socket.socket()

# connect to something
remote = ("example.com", 80)
s.connect(remote)

# read data
data = s.recv(40) # up to 40 bytes
while data != b'':
    data = data.decode()
    print(data, end="")
    data = s.recv(40)

# close the socket
s.close()