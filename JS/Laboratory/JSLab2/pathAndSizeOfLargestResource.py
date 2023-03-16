def printOutPathAndSizeOfLargestResource(listOfLines):
    path = ''
    size = 0
    for line in listOfLines:
        if(int(line[-1]) > size):
            path = line[-4]
            size = line[-1]
    print(f'Path of the largest resource is "{path}" and it\'s size is {size}')