__author__ = 'yunong'

import Utilities
import pandas as pd
import sys


def getFreqList(input_dir, filename):
    freq_list = pd.Series()
    with open(input_dir+'/'+filename, 'r') as fread:
        for line in fread:
            line = Utilities.cleanStr(line)
            freq_list = freq_list.add(pd.Series(line.split()).value_counts(), fill_value=0)
    return freq_list


def writeResult(filename, freq_dict):
    with open(filename, 'w') as fwrite:
        for key in freq_dict:
            fwrite.writelines(str(key)+'\t'+str(freq_dict.get(key))+'\r\n')


def main():
    args = sys.argv
    if len(args) < 3:
        exit(-2)
    input_dir = args[1]
    output_dir = args[2]
    freq_list = pd.Series()
    for filename in Utilities.getFileList(input_dir):
        freq_list = freq_list.add(getFreqList(input_dir, filename), fill_value=0)
    freq_dict = freq_list.to_dict()
    writeResult(output_dir, freq_dict)

main()