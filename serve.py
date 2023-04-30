#fonction pour lancer le serveur et se connecter via des tubes

import os
import sys

def server():
    r, w = os.pipe()
    pid = os.fork()
    if pid:
        os.close(r)
        sys.stdin = os.fdopen(w, 'w')
        return pid
    else:
        os.close(w)
        sys.stdout = os.fdopen(r, 'r')
        return pid

