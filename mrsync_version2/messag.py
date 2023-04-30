# fonction pour envoyer et recevoir des messages

import os
import pickle


def send(fd, tag, cnt):
    '''
    msg = pickle.dumps((tag, v))
    print(msg)
    return fd.write(((len(msg)).to_bytes(3, 'big') + msg).decode())
    '''
    fd.write(tag+"\n"+cnt)


def receive(fd):
    msg_length = int.from_bytes(os.read(fd, 3), 'big')
    msg = os.read(fd, msg_length)
    return pickle.loads(msg)
