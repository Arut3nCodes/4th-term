from dictionaryLogGetter import *
from dictEntriesDataManip import *
from fileReader import *


if __name__ == '__main__':
    tupleLog = read_log()
    dictLine = entry_to_dict(tupleLog[0])
    print(dictLine)