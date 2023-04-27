import os
import sys


def copyFile(files, dst):
    for f in files:
        f2 = f.split("/")[1:]
        dirPath = f2[:-1]
        if dirPath != []:
            # TODO : in future we the server should send to client query how has the forme of (makedirs,dirPath).
            # cree dir1/dir2 à l' terieur du dst
            os.makedirs(dst+"/".join(dirPath), exist_ok=True)
        fd = open(f, "r")  # ouvre en src
        # oure en ecriture en dst
        fd2 = open(dst + "/".join(f2), "w")  # pas besoin aprés
        cnt = fd.read()
        fd2.write(cnt)
        fd.close()
        fd2.close()

        print(f)


def pathTolist(args):

    if "*" == args.SRC:

        args.SRC = "."

    if not os.path.exists(args.SRC):
        raise Exception("Wrong source path")
    filesDir = []
    files = []
    if args.recursive:
        # r=root, d=directories, f = files
        for r, d, f in os.walk(args.SRC):
            for file in f:
                files.append(os.path.join(r, file))
                filesDir.append(os.path.join(r, file))
            for directory in d:
                filesDir.append(os.path.join(r, directory))
    else:
        # get the list of all files and directories in the specified directory
        dir_list = os.listdir(args.SRC)
        # print the list of all files and directories
        for file in dir_list:
            if args.SRC[-1] == "/":
                filesDir.append(args.SRC+file)
            else:
                files.append(args.SRC+"/"+file)
                filesDir.append(args.SRC+"/"+file)

    for f in filesDir:
        print(f)

    if args.DST != None:
        copyFile(files, args.DST)

    return filesDir
