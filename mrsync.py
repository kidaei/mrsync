#!/usr/bin/python3
from sender import *
from options import args
print("rr")


if not args.DST:
    # Activate list-only in case of 1 argument:
    args.listOnly = True

runSender(args)
