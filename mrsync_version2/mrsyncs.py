#!/usr/bin/python3

# cette fonction pouvoir copier des fichiers d'un repertoire A a un repertoire B mais au lieu de ca, elle les dupliques dans le meme repetoire, cela devrais etre fixe quand on connectera tout ca a l'etape 1

import os
import serve
import receve
import generat


def mrsync(src_dir, dest_dir):
    pid = serve.launch
