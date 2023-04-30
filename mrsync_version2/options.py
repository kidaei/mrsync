
import argparse

parser = argparse.ArgumentParser(
    description='mrsync is a program that behaves in much the same way that rsync does, but has less options')
parser.add_argument("SRC", help="Source file")
parser.add_argument("DST", help="Source file", nargs='?')
parser.add_argument("-r", "--recursive", action="store_true",
                    help="rsync files recursevly")
parser.add_argument("-v", "--verbosity", action="count", default=0,
                    help="increase output verbosity")
parser.add_argument("--list-only", dest="listOnly", action="store_true",
                    help="rsync files recursevly", default=True)

args = parser.parse_args()

print(args.SRC)
