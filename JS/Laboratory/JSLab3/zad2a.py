from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *

if __name__ == '__main__':
    tupleLog = read_log()
    tupleLog = sort_log(tupleLog, 0)
    for line in tupleLog:
        print(line)
