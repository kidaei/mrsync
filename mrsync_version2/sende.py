#fonction pour lancer l'envoyeur et repondre a chaque requete en envoyant le fichier au receveur

import os
import messag

def sender(dest_dir, sender_pid):
    while True:
        tag, file = messag.receive(sender_pid)
        if tag == "REQ":
            with open(os.path.join(dest_dir, file), "rb") as f:
                data = f.read()
            messag.send(sender_pid, "DAT", data)
        elif tag == "CHK":
            messag.send(sender_pid, "SIZ", os.stat(os.path.join(dest_dir, file)).st_size)

