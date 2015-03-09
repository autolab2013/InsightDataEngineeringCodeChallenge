__author__ = 'nathanlrf'

from os import listdir
import re


def getFileList(dir):
    return listdir(dir)


def cleanStr(line):
    regex = re.compile('[^a-zA-Z ]')
    result = regex.sub('', line)
    return result.lower()


def swap(list, index_a, index_b):
    list[index_a], list[index_b] = list[index_b], list[index_a]



def tuple_sort(a, b):
    if a[1] < b[1]:
        return 1
    elif a[1] > b[1]:
        return -1
    else:
        return cmp(a[0], b[0])


def loadText(input_dir):
    word_list = []
    files = getFileList(input_dir)
    for f in files:
        with open(input_dir+'/'+f, 'r') as fread:
            for line in fread:
                line = cleanStr(line)
                word_list.append(line)

    return (''.join(word_list)).split()


def getWordNumber(line):
    line = cleanStr(line)
    line = line.split()
    return len(line)

def chunkText(text, proc_num):
    for i in xrange(0, len(text), proc_num):
        yield text[i:i+proc_num]