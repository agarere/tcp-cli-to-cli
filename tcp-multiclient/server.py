import socket
import sys
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

HEADERSIZE = 100

class myThread (threading.Thread):
   def __init__(self, con):
      threading.Thread.__init__(self)
      self.con = con
   def run(self):
      print("Starting ")
      process_data(self.con)
      print("Exiting ")


def process_data(con):
	print("entring:")
	while True:
		data = con.recv(HEADERSIZE)
		if len(data)>0:
			print(f"received data: {data}")
			con.send(bytes("OK", "utf-8"))	
   	

def ListenThread():
	while True:
		print("-> ListenThread")
		MySocket.listen(1)
		ClientSocket, address = MySocket.accept()
		print('Connection from', address)	
		x_thread = myThread(ClientSocket)
		x_thread.start()


MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ServerAddress = (HOST, PORT)
print("starting up on" + HOST + " port " + "{:02d}".format(PORT))
MySocket.bind(ServerAddress)

#threadLock = threading.Lock()

thread_1 = threading.Thread(target=ListenThread)
thread_1.start()