import socket

s = socket.socket()
print("Socket Created")

s.bind(("localhost",8989)) # port number -> (0-65535)

s.listen(3)
print("Waiting for Connections")


while True:
	c,addr = s.accept()
	print("connected with : ",addr)

c.send("Welcome To Future")