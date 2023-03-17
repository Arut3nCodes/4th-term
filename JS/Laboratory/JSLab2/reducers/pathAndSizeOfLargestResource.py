import fileReader


def printOutPathAndSizeOfLargestResource(listOfLines):
    pathOfLargest = ''
    sizeOfLargest = 0
    for line in listOfLines:
        if(line[-1] != '-'):
            if(int(line[-1]) > sizeOfLargest):
                pathOfLargest = line[-4]
                sizeOfLargest = int(line[-1])
    print(f'Path of the largest resource is "{pathOfLargest}" and it\'s size is {sizeOfLargest}')