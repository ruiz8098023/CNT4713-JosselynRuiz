#TCPClient.py

#Missing import socket line?

from socket import socket, AF_INET, SOCK_STREAM

#Name and port number for the client side
serverName = 'localhost'
serverPort = 12001

#Create an INET and STREAMing socket
clientSocket = socket(AF_INET, SOCK_STREAM) 
#Connecting sockets to localhost server and 12001 port
clientSocket.connect((serverName, serverPort))

#Message to be presented when data is sent to the socket
message = raw_input('Input lowercase sentence: ')
#Sends message created
clientSocket.send(message)

#Message that contains data received from the socket in the form of a string
modifiedMessage = clientSocket.recv(2048)
#Prints message with 'From Server: ' before hand
print 'From Server: ', modifiedMessage
clientSocket.close() #Closing socket