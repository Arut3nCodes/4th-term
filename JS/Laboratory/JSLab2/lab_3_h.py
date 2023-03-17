from fileReader import fileReader
from filters.addressFilter import printOutOnlyWithAdress

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    printOutOnlyWithAdress(listOfLines, '.pl')