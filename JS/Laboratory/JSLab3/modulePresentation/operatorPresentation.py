# for itemgetter() application lookup logSorter
from operator import *

if __name__ == '__main__':
    a = 2
    b = 4
    # basic operations
    print(f'{a} + {b} = {add(a, b)}')
    print(f'{a} - {b} = {sub(a, b)}')
    print(f'{a} * {b} = {mul(a, b)}')
    print(f'{a} / {b} = {truediv(a, b)}')
    # list operations
    sampleList = [2, 2, 3, 4, 5, 1 ,2]
    print('---------------------------')
    print(f'List content: {sampleList}')
    print(f'Contains 2 -> {contains(sampleList, 2)}')
    print(f'Contains 6 -> {contains(sampleList, 6)}')
    print(f'Count of 2 -> {countOf(sampleList, 2)}')
    # also attrgetter for classes
