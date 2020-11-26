import socket
import sys

HOST = '127.0.0.1'
PORT = 65432

HEADERSIZE = 10

MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ServerAddress = (HOST, PORT)
print("starting up on" + HOST + " port " + "{:02d}".format(PORT))
MySocket.bind(ServerAddress)

MySocket.listen(5)

ClientSocket, address = MySocket.accept()
print('Connection from', address) 

while True:
    data = ClientSocket.recv(HEADERSIZE)
    if len(data) > 0:
    	print(f"received data: {data}")
    	ClientSocket.send(bytes("OK", "utf-8"))



