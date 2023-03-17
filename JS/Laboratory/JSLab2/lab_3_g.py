from fileReader import fileReader
from filters.dateFilter import printResourcesOnDay

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    printResourcesOnDay(listOfLines, 5)