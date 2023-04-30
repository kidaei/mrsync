# fonction pour envoyer et recevoir des messages

import os
import pickle


def send(fd, tag, v):
    msg = pickle.dumps((tag, v))
    return os.write(fd, (len(msg)).to_bytes(3, 'big') + msg)


def receive(fd):
    msg_length = int.from_bytes(os.read(fd, 3), 'big')
    msg = os.read(fd, msg_length)
    return pickle.loads(msg)
