import socket
import sys

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except (socket.error, msg):
	print ('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message :' + msg[1])
	sys.exit();
print ("Socket Created")

host = 'www.google.com'
port = 80

try:
	remote_ip = socket.gethostbyname(host)

except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

print ('IP address of ' + host + ' is ' + remote_ip)

s.connect((remote_ip, port))

print ('Socket Connceted to ' + host + ' on ip ' + remote_ip)

#Send more data to remote server
message = b'GET / HTTP/1.1\r\n\r\n'

try:
	#Set the whole string
	s.sendall(message)
except (socket.error):
	#Send failed
	print ("Send failed")
	sys.exit()

print ("Message send successfully")

#Now receive data
reply = s.recv(4096)

print (reply)

s.close()
