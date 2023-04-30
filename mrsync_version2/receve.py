#fonction pour lancer le serveur receveur et calculer la liste de fichiers dans le repertoire de destination

import os
import messag

def receiver(dest_dir):
    files = os.listdir(dest_dir)
    messag.send(0, "FILES", files)
    return files

def ecrit_fichier(dest_dir, file):
    with open(os.path.join(dest_dir, file), "wb") as f:
        while True:
            tag, data = messag.receive(0)
            if tag == "DAT":
                f.write(data)
            else:
                break
