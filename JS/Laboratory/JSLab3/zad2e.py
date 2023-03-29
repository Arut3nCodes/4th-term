from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *

if __name__ == '__main__':
    tupleLog = read_log()
    get_entries_by_extention(tupleLog, 'jpg')