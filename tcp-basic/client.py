import socket
import sys
import time

HOST = '127.0.0.1'
PORT = 65432      
HEADERSIZE = 10

MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerAddress = (HOST, PORT)
print("connecting to" + HOST + " port " + "{:02d}".format(PORT))
MySocket.connect(ServerAddress)

while True:
	MySocket.send(bytes("Hello", "utf-8"))
	data = MySocket.recv(HEADERSIZE)
	print(f"received data: {data}")
	time.sleep(2)



#MySocket.close()

'''
while True:

	FullMessage = ''
	NewMessage = True

	while True:
		message = MySocket.recv(16)
		if NewMessage:
			print(f"new message length: {message[:HEADERSIZE]}")
			msglen = int(len(message[:HEADERSIZE]))
			NewMessage = False

		FullMessage += message.decode("utf-8")

		if len(FullMessage)-HEADERSIZE == msglen:
			print("full msg recvd")
			print(FullMessage[HEADERSIZE:])
			NewMessage = True
			FullMessage = ''


	print(FullMessage)
'''
