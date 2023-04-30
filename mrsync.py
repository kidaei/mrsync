#!/usr/bin/python3
from options import args
from sender import *

if not args.DST:
    # Activate list-only in case of 1 argument:
    args.listOnly = True

runSender(args)
