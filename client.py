import socket
import sys
import time

HOST = '127.0.0.1'
PORT = 65432      
HEADERSIZE = 100


myID = sys.argv[1]
destinationID = sys.argv[2]

myName = sys.argv[3]

MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerAddress = (HOST, PORT)
print("connecting to" + HOST + " port " + "{:02d}".format(PORT))
MySocket.connect(ServerAddress)

while True:
	msg = "["
	msg += myID
	msg += ":"
	msg += destinationID
	msg += ":"
	msg += myName
	msg += "]"
	MySocket.send(bytes(msg, "utf-8"))
	data = MySocket.recv(HEADERSIZE)
	print(f"received data: {data}")
	time.sleep(2)