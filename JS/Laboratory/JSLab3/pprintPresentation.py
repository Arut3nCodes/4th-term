from pprint import *
from logSorter import sort_log
from fileReader import read_log
from tupleLogGetter import *
from dictionaryLogGetter import *
from dictEntriesDataManip import *

# pprint.pprint(object, stream=None, indent=1, width=80, depth=None, *, compact=False, sort_dicts=True, underscore_numbers=False)

if __name__ == '__main__':
    listOfLines = read_log()
    dictOfLines = log_to_dict(listOfLines)
    # print(dictOfLines)
    print(f'Is readable - {isreadable(dictOfLines)}')
    print(f'Is recursive - {isrecursive(dictOfLines)}')
    pprint(dictOfLines, indent=4, depth=1)
