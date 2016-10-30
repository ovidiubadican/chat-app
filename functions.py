from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import pickle

def generate_rsa():
    # generate pair of RSA keys
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    bytes_public_key = pickle.dumps(key.publickey())
    return bytes_public_key, key

def encrypt(text, key, server_key, random_generator):
    # input plaintext and outputs the serialized cipher
    hash = SHA256.new(text).digest()
    enc_data = server_key.encrypt(text, random_generator)
    signature = key.sign(hash, random_generator)
    data_tuple = (signature, hash, enc_data)
    data_to_send = pickle.dumps(data_tuple)
    return data_to_send

def decrypt(cipher_string, key):
    # input serialized cipher and outputs plaintext
    cipher = pickle.loads(cipher_string)
    signature = cipher[0]
    hash = cipher[1]
    message = key.decrypt(cipher[2]).decode('utf-8')
    authentic = client_key.verify(hash, signature)
    if authentic:
        return message

#def broadcast(message):
    # broadcast the message to all the clients
