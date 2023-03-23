from pprint import *
from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *
from dictionaryLogGetter import *
from dictEntriesDataManip import *

if __name__ == '__main__':
    listOfLines = read_log()
    dictOfLines = log_to_dict(listOfLines)
    # print(dictOfLines)
    pprint(dictOfLines, indent=2, depth=2)