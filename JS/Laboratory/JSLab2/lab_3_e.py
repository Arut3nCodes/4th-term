from fileReader import fileReader
from filters.protocolFilter import filterByProtocol

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    filterByProtocol(listOfLines, 404)