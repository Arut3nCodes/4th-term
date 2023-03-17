from fileReader import fileReader
from reducers.countAllGigabytes import countAndPrintOutSummaryGigabytes

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    countAndPrintOutSummaryGigabytes(listOfLines)