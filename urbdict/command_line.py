import sys
from urbdict import main


def define():
    arg = ' '.join(sys.argv[1:])
    print(arg)
    return main.define(arg)
