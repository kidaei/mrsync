import os
import sys
import re

# Feature to add: Activate Regex i.e: ./mrsync *.py --list-only ....... etc


def copyFile(files, dst):
    for f in files:
        f =
        print(f)

    ...


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
        # for f in files:

    return filesDir
