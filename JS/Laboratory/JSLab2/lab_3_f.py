from fileReader import fileReader
from filters.timeFilter import printResourcesInBetweenHours

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    printResourcesInBetweenHours(listOfLines, 22, 6)