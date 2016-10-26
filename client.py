#!/usr/bin/python3

from config import PORT, RECV_BUFFER, SERVER
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import socket, select, sys
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
print("Start sending messages...")

data = ""

while data != ":q!":

    data = input("Me: >")
    # generate our keys for encryption
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)

    # extract the public key and send it to the server
    public_key = key.publickey()

    # serialize key to send across network
    to_send = pickle.dumps(public_key)
    s.send(to_send)

    # receive key from server
    server_key_string = s.recv(RECV_BUFFER)
    server_key = pickle.loads(server_key_string)

    # enrypt the data, hash it, sign it, and send it as a tuple
    hash = SHA256.new(data).digest()
    enc_data = server_key.encrypt(data, random_generator)
    signature = key.sign(hash, random_generator)
    data_tuple = (signature, hash, enc_data)

    data_to_send = pickle.dumps(data_tuple)
    s.send(data_to_send)

s.close()
