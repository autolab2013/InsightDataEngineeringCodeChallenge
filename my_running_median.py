__author__ = 'yunong'

import pandas
import sys
import Utilities as ut
import MyRunningMedianClass as myclass


class RunningMedian:
    def __init__(self):
        self.left = myclass.MaxHeap()
        self.right = myclass.MinHeap()

    def getSize(self):
        return len(self.left.list) + len(self.right.list)

    def updateLists(self, val):
        # maintain abs(len(left) - len(right)) <= 1
        if self.left.size() == 0:
            self.left.addElement(val)
            return
        if self.right.size() == 0:
            self.right.addElement(val)
            if val < self.left.peek():
                big = self.left.extract()
                small = self.right.extract()
                self.left.addElement(small)
                self.right.addElement(big)
            return
        if val < self.getLeftMax():
            self.left.addElement(val)
        elif val > self.getRightMin():
            self.right.addElement(val)
        else:
            self.left.addElement(val)

        if len(self.left.list) == len(self.right.list):
            return
        elif len(self.left.list) > len(self.right.list):
            if len(self.left.list) - len(self.right.list) == 1:
                return
            else:
                self.right.addElement(self.left.extract())
        else:
            self.left.addElement(self.right.extract())

    def getLeftMax(self):
        return self.left.peek()

    def getRightMin(self):
        return self.right.peek()

    def getMedian(self, val):
        self.updateLists(val)
        # print self.left.list
        # print self.right.list
        if len(self.left.list) == len(self.right.list):
            return (self.getLeftMax() + self.getRightMin())/2
        else:
            return self.getLeftMax()


def getMedianList(filelist, input_dir, my_median):
    median_list = []
    word_list = []
    for files in filelist:
        with open(input_dir+'/'+files, 'r') as fread:
            for line in fread:
                word_cnt = ut.getWordNumber(line)
                # word_list.append(word_cnt)
                # word_list.sort()
                # print word_list
                median_list.append(float(my_median.getMedian(word_cnt)))
    return median_list


def writeResult(destination, median_list):
    with open(destination, 'w') as fwrite:
        for med in median_list:
            fwrite.writelines(str(med)+'\r\n')


def main():
    args = sys.argv
    # args = ["", "wc_input", "wc_output/med_result.txt"]
    if len(args) < 3:
        exit(-2)
    input_dir = args[1]
    destination = args[2]
    my_median = RunningMedian()
    median_list = getMedianList(ut.getFileList(input_dir), input_dir, my_median)
    writeResult(destination, median_list)


main()