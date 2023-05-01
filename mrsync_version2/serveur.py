# fonction pour lancer le serveur et se connecter via des tubes

import os
import sys
import messag
import generat


def server():
    r, w = os.pipe()
    # r1, w1 = os.pipe()

    pid = os.fork()
    if pid == 0:  # fils --> sender
        os.close(r)
        # os.close(w1)
        # fdr = os.fdopen(r1, 'r')
        fdw = os.fdopen(w, 'w')
        messag.send(fdw, "ARGS", " ".join(sys.argv[1:]))
        # cnt = fdr.read()
        # generat.query_managment(cnt, fdw)
        return pid

    else:
       # os.close(r1)
        os.close(w)  # pére --> reciver
        fdr = os.fdopen(r, 'r')
        # fdw = os.fdopen(w1, 'w')
        cnt = fdr.read()

        generat.query_managment(cnt, None)
        return pid
