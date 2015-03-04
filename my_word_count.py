__author__ = 'yunong'
import os
from os import walk

# class MyWordCout:
#     def __init__(self):
#         do sth
        # print "init"


def buildWordTable(self, input):
    files = os.listdir(os.curdir)
    print files

    f = []
    for(dirpath, dirnames, filenames) in walk('/'):
        print f.extend(filenames)
        break
