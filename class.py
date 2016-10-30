import socket, pickle
from Crypto import Random
from Crypto.PublicKey import RSA

class Client:

    def __init__(self, serversocket, connection_list):
        
        self.clientsocket, self.addr = serversocket.accept()
        connection_list.append(self.clientsocket)
        print("Client %s:%s connected!" % self.addr)
            
        # receive the key from client
        self.client_key_string = self.clientsocket.recv(RECV_BUFFER)
        if self.client_key_string:
            self.client_key = pickle.loads(client_key_string)
            self.ack = 'ack'.encode('utf-8')
            self.clientsocket.send(ack)            

            # generate RSA keys
            self.random_generator = Random.new().read
            self.key = RSA.generate(1024, self.random_generator)

            # extract public key
            self.public_key = self.key.publickey()

            # serialize key for sending across network
            self.to_send = pickle.dumps(self.public_key)
            self.clientsocket.send(self.to_send)

            self.client_ack = self.clientsocket.recv(RECV_BUFFER)
            if self.client_ack.decode('utf-8') == 'ack':
                print("Secure channel set up with %s:%s" % self.addr)
                return connection_list

