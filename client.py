#!/usr/bin/python3
import socket, select, sys
from config import PORT
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
"""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
socket_list = [s]

try:
    s.connect((host, PORT))
except:
    print("Unable to connect!")
    sys.exit()

print("Connected to the chat server.")
print("Sending a test message...")
"""
# the data we want to send
data = "Test message."

# generate pair or RSA keys
key = RSA.generate(2048, random_generator)

# create a SHA256 hash from the plaintext data
hash = SHA256.new(data).digest()
print(hash)
"""
try:
    s.send(data.encode('utf-8'))
except:
    print("Sending message failed!")
    sys.exit()
"""
