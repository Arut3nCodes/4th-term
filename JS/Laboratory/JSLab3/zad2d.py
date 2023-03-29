from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *

if __name__ == '__main__':
    tupleLog = read_log()
    tupleLog = get_failed_reads(tupleLog, False)
    for line in tupleLog:
        print(line)