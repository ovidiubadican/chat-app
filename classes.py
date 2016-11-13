import socket, pickle
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from functions import generate_rsa
from config import RECV_BUFFER

class Client:

    def __init__(self, serversocket, connection_list):
        # connects the client and returns the updated connection list
        self.clientsocket, self.addr = serversocket.accept()
        connection_list.append(self.clientsocket)
        print("Client %s:%s connected!" % self.addr)
            
        # receive the key from client
        client_key_string = self.clientsocket.recv(RECV_BUFFER)
        if client_key_string:
            self.client_key = pickle.loads(client_key_string)
            ack = 'ack'.encode('utf-8')
            self.clientsocket.send(ack)            

            # generate RSA keys
            to_send, self.key = generate_rsa()
            self.clientsocket.send(to_send)
            random_generator = Random.new().read

            client_ack = self.clientsocket.recv(RECV_BUFFER)
            if client_ack.decode('utf-8') == 'ack':
                print("Secure channel set up with %s:%s" % self.addr)
        

    def encrypt(self, text):
        # input plaintext and outputs the serialized cipher
        hash = SHA256.new(text).digest()
        enc_data = self.client_key.encrypt(text, random_generator)
        signature = key.sign(hash, random_generator)
        data_tuple = (signature, hash, enc_data)
        data_to_send = pickle.dumps(data_tuple)
        return data_to_send

    def decrypt(self, cipher_string):
        # input serialized cipher and outputs plaintext
        cipher = pickle.loads(cipher_string)
        signature = cipher[0]
        hash = cipher[1]
        message = self.key.decrypt(cipher[2]).decode('utf-8')
        authentic = self.client_key.verify(hash, signature)
        if authentic:
            return message

    def disconnect(self, connection_list):
        # disconnects the client and removes the connection from the client list
        self.clientsocket.close()
        connection_list.remove(self.clientsocket)
        print("Client %s:%s has been disconnected..." % self.addr)

