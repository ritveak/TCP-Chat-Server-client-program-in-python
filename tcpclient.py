import socket
s= socket.socket()
port =12345
s.connect((socket.gethostname(),port))
print (s.recv(1024).decode())
a=input("What do u wanna reply?")
s.send(a.encode())
s.close()