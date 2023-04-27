import os
import message

def generate(src_dir, dst_dir, list_files):
    for file in list_files:
        src_path = os.path.join(src_dir, file)
        dst_path = os.path.join(dst_dir, file)
        if not os.path.exists(dst_path) or os.path.getmtime(src_path) > os.path.getmtime(dst_path):
            # send request to sender for this file
            # envoie une requete au sender pour ce fichier
            message.send("GET " + file)
            # receive file from sender and write to destination
            # recois un fichier venant du sender et ecrit pour la destination 
            with open(dst_path, "wb") as f:
                while True:
                    data = message.recv()
                    if data == b"END":
                        break
                    f.write(data)

