#Server side chat
#Import socket and respective methods
import socket, select, sys 
from thread import *

#Creation of address domain of socket and type of the socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 
  
#Checks for number of arguments 
if len(sys.argv) != 3: 
    print "Correct usage: script, IP address, port number"
    exit() 
  
#Takes the arguments from comand line - first one is IP_address, second one is Port 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
  
#Binds IP_address and port to the server
server.bind((IP_address, Port)) 
  
#Listens for 100 active connections
server.listen(100) 
  
list_of_clients = [] 

#This function sets the initial view of the client's thread
def clientthread(conn, addr): 
  
    #Sends message to client joining chat room
    conn.send("Welcome to this chatroom!") 
  
    while True: 
            try: 
                #Message of data received
                message = conn.recv(2048) 
                if message: 
  
                    #Prints user's message and address on server terminal
                    print "<" + addr[0] + "> " + message 
  
                    #Calls broadcast function to send message to all 
                    message_to_send = "<" + addr[0] + "> " + message 
                    broadcast(message_to_send, conn) 
  
                else: 
                    #Connection removed if it's broken
                    remove(conn) 
  
            except: 
                continue
  
#This function broadcasts message to all clients except the one sending the message
def broadcast(message, connection): 
    for clients in list_of_clients: 
        if clients!=connection: 
            try: 
                #Sent if connection of other clients is not the same as the one sending the message
                clients.send(message) 
            except: 
                clients.close() 
  
                #Removes the clients with broken link
                remove(clients) 
  
#Remove the first connection in the list
def remove(connection): 
    if connection in list_of_clients: 
        list_of_clients.remove(connection) 
  
while True: 

    #Set to accept a connection request and store two parameters as conn and addr respectively
    conn, addr = server.accept() 
  
    #Holds and maintains list of users
    list_of_clients.append(conn) 
  
    #Prints address of newly connected user
    print addr[0] + " connected"
  
    #New thread for new user
    start_new_thread(clientthread,(conn,addr))     

#Close the server
conn.close() 
server.close() 