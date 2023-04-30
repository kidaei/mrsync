# fonction pour lancer le generateur et envoyer des requetes a l'envoyeur pour chaque fichier manquant ou necessitant une mise a jour

import os
import messag


def generator(dest_dir, sender_pid, files):
    for file in files:
        if not os.path.exists(os.path.join(dest_dir, file)):
            messag.send(sender_pid, "REQ", file)
        else:
            local_size = os.stat(os.path.join(dest_dir, file)).st_size
            remote_size = messag.send(sender_pid, "CHK", file)
            if remote_size != local_size:
                messag.send(sender_pid, "REQ", file)


def compare_lists(dest_dir, sender_pid, files):
    remote_files = os.listdir(dest_dir)
    if set(files) != set(remote_files):
        generator(dest_dir, sender_pid, files)
