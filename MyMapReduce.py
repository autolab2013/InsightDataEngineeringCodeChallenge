__author__ = 'nathanlrf'

import Utilities


class MyMapReduceClass:
    def __init__(self):
        return


def myMap(text):
    results = []
    for w in text:
        # True if w contains non-alphanumeric characters
        if not w.isalnum():
            w = Utilities.cleanStr(w)
    # True if w is a title-cased token
        w = w.lower()
        results.append((w, 1))
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


def myReduce(Mapping):
    return Mapping[0], sum(pair[1] for pair in Mapping[1])