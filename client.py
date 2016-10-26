#!/usr/bin/python3

from config import PORT, RECV_BUFFER, SERVER
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
import socket, select, sys
import pickle
from functions import generate_rsa, encrypt

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

random_generator = Random.new().read
data = ""
public_key = generate_rsa()
s.send(public_key)

# receive key from server
server_key_string = s.recv(RECV_BUFFER)
server_key = pickle.loads(server_key_string)

while data != ":q!":

    data = input("Me: > ").encode('utf-8')
    data_to_send = encrypt(data, server_key)
    s.send(data_to_send)

s.close()
