__author__ = 'yunong'
import string

# class MyWordCout:
#     def __init__(self):
#         do sth
        # print "init"


# def buildWordTable(self, input):
    # files = os.listdir(os.curdir)
    # print files
    #
    # f = []
    # for(dirpath, dirnames, filenames) in walk('/'):
    #     print f.extend(filenames)
    #     break

fread = open('./wc_input/a.txt', 'r')
for line in fread:
    for word in line.split():
        #remove punct
        word = word.translate(string.maketrans("", ""), string.punctuation)
        word = word.lower()
        print word
