#!/usr/bin/python3
import socket, select, sys
from config import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
socket_list = [s]

try:
    s.connect((host, PORT))
except:
    print("Unable to connect!")
    sys.exit()

print("Connected to the chat server. Start sending messages!")
print("Sending a test message...")

data = "Test message."
try:
    s.send(data.encode('utf-8'))
except:
    print("Sending message failed!")
    sys.exit()

"""
while True:
    # Get the list of sockets which are readable with select
    read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

    for sock in read_sockets:
        data = "Test message."
        try:
            sock.send(data.encode('utf-8'))
        except:
            print("Sending message failed!")
            sys.exit()
"""
