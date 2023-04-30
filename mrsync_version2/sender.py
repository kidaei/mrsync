from filelist import *


def runSender(args):

    srcPath = args.SRC

    if srcPath == "*":
        srcPath = "."
    dstPath = args.DST

    pathTolist(args)
    if args.verbosity >= 2:
        print("running : ", __file__)
        print("the src file is : ", srcPath)
    elif args.verbosity >= 1:
        print('the src file is : ', srcPath)
