import os
import sys


def copyFile(files, dst):
    for f in files:
        f2 = f.split("/")[1:]
        dirPath = f2[:-1]
        if dirPath != []:
            # TODO : in future we the server should send to client query how has the forme of (makedirs,dirPath).
            # cree dir1/dir2 à l' terieur du dst
            os.makedirs(dst+"/"+"/".join(dirPath), exist_ok=True)
        fd = os.open(f, os.O_RDONLY)  # ouvre en src
        # oure en ecriture en dst
        fd2 = os.open(dst + "/"+"/".join(f2), os.O_WRONLY)

        while True:  # tant qu'on a pas rejoint la fin du file

            cnt = os.read(fd, 1024)
            if len(cnt) == 0:
                break
            os.write(fd2, cnt)
            # TODO : envoyéé cnt au client

        os.close(fd)
        os.close(fd2)

        print(f)


def pathTolist(path, isRecursive, dst, copy):

    if "*" in path:

        path = "."

    if not os.path.exists(path):
        raise Exception("Wrong source path")
    filesDir = []
    files = []
    if isRecursive:
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                files.append(os.path.join(r, file))
                filesDir.append(os.path.join(r, file))
            for directory in d:
                filesDir.append(os.path.join(r, directory))
    else:
        # get the list of all files and directories in the specified directory
        dir_list = os.listdir(path)
        # print the list of all files and directories
        for file in dir_list:
            if path[-1] == "/":
                filesDir.append(path+file)
            else:
                files.append(path+"/"+file)
                filesDir.append(path+"/"+file)

    for f in filesDir:
        print(f)

    if copy:
        copyFile(files, dst)

    return filesDir
