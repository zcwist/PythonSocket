import socket
import sys
from thread import *

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket created')

try:
	s.bind((HOST,PORT))
except (socket.error, msg):
	print ("Bind failed. Error code : " + str(msg[0]) + 'Message ' + msg[1])
	sys.exit()

print ("Socket bind complete")

s.listen(10)
print ("Socket now listening")

# #wait to accept a connection - blocking call
# conn, addr = s.accept()

# print ("Connected with " + addr[0] + ":" + str(addr[1]))

# #now keep talking with the client
# data = conn.recv(1024)
# conn.sendall(data)

# conn.close()
# s.close()



# #now keep talking with the client
# while 1:
# 	#wait to accept a connection - bloking call
# 	conn, addr = s.accept()
# 	print ("Connected with " + addr[0] + ":" + str(addr[1]))

# 	data = conn.recv(1024)
# 	reply = b'OK...' + data
# 	if not data:
# 		break

# 	conn.sendall(reply)

# conn.close()
# s.close()


def clientthread(conn):
	#Sending message to connected client
	conn.send('Welcome to the server. Type something and hit enter\n')

	#infinite loop so that function do not terminate and thread do not end.
	while True:

		#Receiving from client
		data = conn.recv(1024)
		reply = b'OK...' + data
		if not data:
			break
		conn.sendall(reply)

	#came out of the loop
	conn.close

while 1:
	#wait to accept a connection - blocking call
	conn, addr = s.accept()
	print ("Connected with " + addr[0] + ":" + str(addr[1]))

	start_new_thread(clientthread,(conn,))

s.close()
