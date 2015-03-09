__author__ = 'nathanlrf'

import Utilities as ut


class MaxHeap:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def addElement(self, element):
        self.list.append(element)
        self.bubbleUp()

    def compare(self, a, b):
        return a < b

    def bubbleDown(self):
        curr = 0
        left = 2*curr+1
        right = 2*curr+2
        while left < self.size():
            child = left
            if right < self.size() and not self.compare(self.list[left], self.list[right]):
                child = right
            if self.compare(self.list[curr], self.list[child]):
                ut.swap(self.list, curr, child)
            curr = child
            left = 2*curr+1
            right = 2*curr+2

    def bubbleUp(self):
        curr = self.size()-1
        parent = (curr-1)/2
        while parent >= 0:
            if self.compare(self.list[parent], self.list[curr]):
                ut.swap(self.list, parent, curr)
            curr = parent
            parent = (curr-1)/2

    def extract(self):
        max = self.list.pop(0)
        self.bubbleDown()
        return max

    def peek(self):
        return self.list[0]


class MinHeap:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def addElement(self, element):
        self.list.append(element)
        self.bubbleUp()

    def compare(self, a, b):
        return a > b

    def bubbleDown(self):
        curr = 0
        left = 2*curr+1
        right = 2*curr+2
        while left < self.size():
            child = left
            if right < self.size() and not self.compare(self.list[left], self.list[right]):
                child = right
            if self.compare(self.list[curr], self.list[child]):
                ut.swap(self.list, curr, child)
            curr = child
            left = 2*curr+1
            right = 2*curr+2

    def bubbleUp(self):
        curr = self.size()-1
        parent = (curr-1)/2
        while parent >= 0:
            if self.compare(self.list[parent], self.list[curr]):
                ut.swap(self.list, parent, curr)
            curr = parent
            parent = (curr-1)/2

    def extract(self):
        small = self.list.pop(0)
        self.bubbleDown()
        return small

    def peek(self):
        return self.list[0]