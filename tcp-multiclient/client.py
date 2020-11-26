import socket
import sys
import time

HOST = '127.0.0.1'
PORT = 65432      
HEADERSIZE = 100

myName = sys.argv[1]

MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerAddress = (HOST, PORT)
print("connecting to" + HOST + " port " + "{:02d}".format(PORT))
MySocket.connect(ServerAddress)

while True:
	MySocket.send(bytes("Hello My Name is " + myName, "utf-8"))
	data = MySocket.recv(HEADERSIZE)
	print(f"received data: {data}")
	time.sleep(2)
