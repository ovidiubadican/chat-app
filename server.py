#!/usr/bin/python3
import socket, select, sys
from config import PORT, RECV_BUFFER
from classes import Client

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import pickle

connection_list = []
clients = {}
i = 0 # number of connected clients
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
            temp_obj = Client(serversocket, connection_list)
            clients[temp_obj.clientsocket] = temp_obj
            i = i + 1
            print("There are %d connected clients" % i)
            temp_obj = None

        else:
            # receive message from client
            cipher_string = sock.recv(RECV_BUFFER)

            if len(cipher_string) != 0:
               
                message = clients[sock].decrypt(cipher_string)
                print("%s:%s said:" % clients[sock].addr, end=" ")
                print(message)

            else:
                clients[sock].disconnect(connection_list)
                i = i - 1
                print("There are %d connected clients" % i)

serversocket.close()
sys.exit()
