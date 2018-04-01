import socket
s= socket.socket()
port = 12345
msg=input("What do u wanna say?")
s.bind ((socket.gethostname(),port))
s.listen(5)
while True:
	c,addr=s.accept()
	print ('connected with ',addr)
	c.send (msg.encode())
	print(c.recv(1024).decode())
	c.close()
s.close()