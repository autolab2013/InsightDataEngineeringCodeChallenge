__author__ = 'yunong'

import Utilities
import operator
import sys
import multiprocessing
import MyMapReduce as mmr


'''
write freq_dict to filename
'''
def writeResult(filename, freq_dict):
    freq_dict = dict(freq_dict)
    freq_dict = sorted(freq_dict.items(), key=operator.itemgetter(0))
    with open(filename, 'w') as fwrite:
        for key, val in freq_dict:
            fwrite.writelines(key+'\t'+str(val)+'\r\n')


def main():
    proc_num = 8  # number of processes
    args = sys.argv
    if len(args) < 3:
        print "need more paremeter"
        exit(-2)
    input_dir = args[1]
    destination = args[2]
    text = Utilities.loadText(input_dir)
    pool = multiprocessing.Pool(proc_num)
    text_partition = list(Utilities.chunkText(text, proc_num))
    single_tuples = pool.map(mmr.myMap, text_partition)
    token_to_tuples = mmr.myPartition(single_tuples)
    word_freq = pool.map(mmr.myReduce, token_to_tuples.items())
    word_freq.sort(Utilities.tupleSort)
    writeResult(destination, dict(word_freq))

main()