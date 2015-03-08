__author__ = 'nathanlrf'

from os import listdir
import re


def getFileList(dir):
    return listdir(dir)


def cleanStr(line):
    regex = re.compile('[^a-zA-Z ]')
    return regex.sub('', line)


def swap(list, index_a, index_b):
        list[index_a], list[index_b] = list[index_b], list[index_a]


def getWordNumber(line):
    line = cleanStr(line)
    line = line.split()
    return len(line)