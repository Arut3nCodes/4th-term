from dictionaryLogGetter import *
from dictEntriesDataManip import *
from fileReader import *


if __name__ == '__main__':
    dictLine = get_addr(log_to_dict(read_log()))
    print(dictLine)