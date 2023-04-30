# fonction pour lancer le generateur et envoyer des requetes a l'envoyeur pour chaque fichier manquant ou necessitant une mise a jour

import os
import messag
import options
import filelist


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


def query_managment(query, fd):
    tag, cnt = query.split("\n", 1)
    if tag == "ARGS":
        args = options.parser.parse_args(cnt.split(" "))
        if not args.DST:
            # Activate list-only in case of 1 argument:
            args.listOnly = True

        srcPath = args.SRC

        if srcPath == "*":
            srcPath = "."
        dstPath = args.DST

        filelist.pathTolist(args, fd)
        if args.verbosity >= 2:
            print("running : ", __file__)
            print("the src file is : ", srcPath)
        elif args.verbosity >= 1:
            print('the src file is : ', srcPath)
    elif tag == "PRINT":
        print(cnt)
