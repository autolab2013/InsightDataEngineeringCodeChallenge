__author__ = 'nathanlrf'

import Utilities

class MyMapReduceClass:
    def __init__(self):
        return


def myMap(text):
    results = []
    for word in text:
        # True if w contains non-alphanumeric characters
        if not word.isalnum():
            word = Utilities.cleanStr(word)
        word = word.lower()
        results.append((word, 1))
    return results


def myPartition(single_tuple):
    tf = {}
    for sublist in single_tuple:
        for p in sublist:
            # Append the tuple to the list in the map
            try:
                tf[p[0]].append(p)
            except KeyError:
                tf[p[0]] = [p]
    return tf


def myReduce(mapping):
    return mapping[0], sum(pair[1] for pair in mapping[1])