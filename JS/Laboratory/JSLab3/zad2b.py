from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *

if __name__ == '__main__':
    tupleLog = read_log()
    tupleLog = get_entries_by_addr(tupleLog, '199.72.81.55')
    for line in tupleLog:
        print(line)