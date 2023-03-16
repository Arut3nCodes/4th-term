def printOutPathAndSizeOfLargestResource(listOfLines):
    path = ''
    size = 0
    for line in listOfLines:
        if(line[-1] != '-'):
            if(int(line[-1]) > size):
                path = line[-4]
                size = int(line[-1])
    print(f'Path of the largest resource is "{path}" and it\'s size is {size}')