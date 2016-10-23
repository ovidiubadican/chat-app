#!/usr/bin/python3

import socket, sys
from config import PORT, RECV_BUFFER
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
socket_list = [s]

try:
    s.connect((host, PORT))
except:
    print("Unable to connect!")
    sys.exit()

print("Connected to the chat server.")
print("Sending an encrypted test message...")

# plaintext message
data = "Test message.".encode('utf-8')

# generate our keys for encryption
random_generator = Random.new().read
key = RSA.generate(1024, random_generator)

# extract the public key and send it to the server
public_key = key.publickey()
s.send(public_key)
s.recv(RECV_BUFFER)


# generate a hash from the plaintext message and sign it
hash = SHA256.new(data).digest()
signature = key.sign(hash, random_generator)

# encrypt the data to be sent
enc_data = public_key.encrypt(data,random_generator)

try:
    s.send(enc_data)
except:
    print("Sending message failed!")
    sys.exit()
