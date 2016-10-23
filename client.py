#!/usr/bin/python3

import socket, sys
from config import PORT, RECV_BUFFER, SERVER
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import pickle

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_list = [s]

try:
    s.connect((SERVER, PORT))
except:
    print("Unable to connect!")
    sys.exit()

print("Connected to the chat server.")

# plaintext message
data = "Super secret message".encode('utf-8')

# generate our keys for encryption
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

# extract the public key and send it to the server
public_key = key.publickey()

# serialize key to send across network
to_send = pickle.dumps(public_key)
s.send(to_send)
print("Client sent key to server...")

# receive key from server
server_key_string = s.recv(RECV_BUFFER)
server_key = pickle.loads(server_key_string)
if server_key:
    print("Client received server key")

print("Sending an encrypted test message...")

hash = SHA256.new(data).digest()
enc_data = server_key.encrypt(data, random_generator)
signature = key.sign(hash, random_generator)
data_tuple = (signature, hash, enc_data)

data_to_send = pickle.dumps(data_tuple)
s.send(data_to_send)

print("Encrypted message sent!")
