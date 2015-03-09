__author__ = 'nathanlrf'


from AbstractHeapClass import AbstractHeap


class MaxHeap(AbstractHeap):
    def __init__(self):
        AbstractHeap.__init__(self)

    def compare(self, a, b):
        return a < b


class MinHeap(AbstractHeap):
    def __init__(self):
        AbstractHeap.__init__(self)


    def compare(self, a, b):
        return a > b
