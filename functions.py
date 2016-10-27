from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import pickle

def generate_rsa():
    # generate pair of RSA keys
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    public_key = key.publickey()
    to_send = pickle.dumps(public_key)
    return to_send

def encrypt(text, server_key):
    # input plaintext and outputs the serialized cipher
    hash = SHA256.new(data).digest()
    enc_data = server_key.encrypt(data, random_generator)
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
