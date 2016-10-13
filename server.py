#!/usr/bin/python3
import socket, select, sys
from config import *

connection_list = []

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, PORT))
serversocket.listen(5)
connection_list.append(serversocket)
print("The chat server was started on port %d" % PORT)
print("Waiting for client connections...")

while True:
    # Get the list of sockets which are readable with select
    read_sockets, write_sockets, error_sockets = select.select(connection_list, [], [])

    for sock in read_sockets:
        # New connection
        if sock == serversocket:
            clientsocket, addr = serversocket.accept()
            connection_list.append(clientsocket)
            print("Client %s:%s connected!" % addr)

        # Incomming message from client
        else:
            data = sock.recv(RECV_BUFFER)
            print("Message received: ", data.decode('utf-8'))
            sys.exit()
