#!/usr/bin/python3

import socket, select, sys, pickle
from Crypto import Random
from config import PORT, RECV_BUFFER, SERVER
from functions import generate_rsa, encrypt

# GUI imports ----------
from PyQt5.QtWidgets import QApplication
from gui import Window
# ----------------------

app = QApplication(sys.argv)
main_window = Window()

# connect to server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_list = [s]

try:
    s.connect((SERVER, PORT))
except:
    Window.logText.insertPlainText("Unable to connect!")
    s.close()
    sys.exit()

print("Connected to the chat server.")

# generate our keys and send public key to server
random_generator = Random.new().read
bytes_public_key, key = generate_rsa()
s.send(bytes_public_key)

# receive acknowledgement from server that has received our public key
server_ack = s.recv(RECV_BUFFER)
server_ack = server_ack.decode('utf-8')
if server_ack == 'ack':
    # receive key from server
    bytes_server_key = s.recv(RECV_BUFFER)
    server_key = pickle.loads(bytes_server_key)

    ack = 'ack'
    if server_key:
        s.send(ack.encode('utf-8'))
        print("Secure channel set up completed\nStart sending messages...")
    else:
        print("Secure channel could not be setup\nNow exiting...")
        s.close()
        sys.exit()

while True:
    text = input("Me: > ")
    data = text.encode('utf-8')
    if text == ":q!":
        s.close()
        sys.exit()
    else:
        data_to_send = encrypt(data, key, server_key, random_generator)
        try:
            s.send(data_to_send)
        except:
            print("Server is offline...")
            s.close()
            sys.exit()

sys.exit(app.exec_())
