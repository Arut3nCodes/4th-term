from fileReader import fileReader
from reducers.pathAndSizeOfLargestResource import printOutPathAndSizeOfLargestResource

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    printOutPathAndSizeOfLargestResource(listOfLines)