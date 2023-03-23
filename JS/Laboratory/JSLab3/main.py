from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *
from dictionaryLogGetter import *
from dictEntriesDataManip import *

if __name__ == '__main__':
    listOfLines = read_log()
    # listOfLines = sort_log(listOfLines, 0)
    dictOfLines = log_to_dict(listOfLines)
    print_dict_entry_dates(dictOfLines)