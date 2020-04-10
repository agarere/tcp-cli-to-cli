import socket
import sys
import threading
import time

HOST = '127.0.0.1'
PORT = 65432

HEADERSIZE = 100

MessageList = ["[xxxx:xxxx:data]", "[xxxx:xxx1:data]"]

class myThread (threading.Thread):
   def __init__(self, con):
      threading.Thread.__init__(self)
      self.con = con
   def run(self):
      print("Starting ")
      process_data(self.con)
      print("Exiting ")


def checkMessage(msg):
	data_list = list(msg)
	src_id = data_list[1]
	src_id += data_list[2]
	src_id += data_list[3]
	src_id += data_list[4]
	for message in MessageList:
		message_parsed = list(message)
		des_id = message_parsed[6]
		des_id += message_parsed[7]
		des_id += message_parsed[8]
		des_id += message_parsed[9]
		if des_id == src_id:
			MessageList.remove(message)
			return message

	return "no"		


def process_data(con):
	print("entring:")
	while True:
		data = con.recv(HEADERSIZE)
		MessageList.append(data.decode("utf-8"))
		if len(data)>0:
			print(f"received data: {data}")
			x_string = data.decode("utf-8")
			flag = 0
			while not flag:
				send_msg = checkMessage(x_string)
				if send_msg != "no":
					con.send(bytes(send_msg, "utf-8"))
					flag = 1	


def ListenThread():
	while True:
		print("-> ListenThread")
		MySocket.listen(1)
		ClientSocket, address = MySocket.accept()
		print('Connection from', address)	
		x_thread = myThread(ClientSocket)
		x_thread.start()
		print(MessageList)


MySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
MySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

ServerAddress = (HOST, PORT)
print("starting up on" + HOST + " port " + "{:02d}".format(PORT))
MySocket.bind(ServerAddress)

#threadLock = threading.Lock()

thread_1 = threading.Thread(target=ListenThread)
thread_1.start()