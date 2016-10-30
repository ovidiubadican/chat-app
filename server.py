#!/usr/bin/python3
import socket, select, sys
from config import PORT, RECV_BUFFER

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import pickle

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
            
            # receive the key from client
            client_key_string = clientsocket.recv(RECV_BUFFER)
            if client_key_string:
                client_key = pickle.loads(client_key_string)
                ack = 'ack'.encode('utf-8')
                clientsocket.send(ack)            

                # generate RSA keys
                random_generator = Random.new().read
                key = RSA.generate(1024, random_generator)

                # extract public key
                public_key = key.publickey()

                # serialize key for sending across network
                to_send = pickle.dumps(public_key)
                clientsocket.send(to_send)

                client_ack = clientsocket.recv(RECV_BUFFER)
                if client_ack.decode('utf-8') == 'ack':
                    print("Secure channel set up with %s:%s" % addr)

             
        else:
            # receive message from client
            cipher_string = sock.recv(RECV_BUFFER)

            if len(cipher_string) != 0:
               
                cipher = pickle.loads(cipher_string)
                signature = cipher[0]
                hash = cipher[1]
                client_message = key.decrypt(cipher[2]).decode('utf-8')
                authentic = client_key.verify(hash, signature)
                if authentic:
                    print(client_message)
                else:
                    print("Could not verify message authenticity!")

            else:
                
                print("Client %s:%s has disconnected!" % addr)
                connection_list.remove(sock)
                sock.close()

serversocket.close()
sys.exit()
