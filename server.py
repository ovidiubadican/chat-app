#!/usr/bin/python3
import socket, select, sys
from config import PORT, RECV_BUFFER
<<<<<<< HEAD
=======
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import pickle
>>>>>>> a782797b19f24b7d3956fdcbbb89e741ddf03db9

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
            
            # generate RSA keys
            random_generator = Random.new().read
            key = RSA.generate(1024, random_generator)

            # extract public key
            public_key = key.publickey()

            # serialize key for sending across network
            to_send = pickle.dumps(public_key)
            clientsocket.send(to_send)
            print("Server sent key...")

            # receive the key from client
            client_key_string = clientsocket.recv(RECV_BUFFER)
            client_key = pickle.loads(client_key_string)

            if client_key:
                print("Server received client key")

            cipher_string = clientsocket.recv(RECV_BUFFER)
            cipher = pickle.loads(cipher_string)

            if cipher:

                print("The received cypher is:", cipher)
                print("Now verifying if message is authentic...")

                signature = cipher[0]
                hash = cipher[1]
                client_message = key.decrypt(cipher[2]).decode('utf-8')
                authentic = client_key.verify(hash, signature)

                if authentic:
                    print("The message is authentic!")
                    print("The message is:", client_message)
                else:
                    print("The message is NOT authentic!!")
                 
            serversocket.close()
            sys.exit()

        else:
            pass
