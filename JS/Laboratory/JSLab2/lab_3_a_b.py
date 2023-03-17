from fileReader import fileReader
from reducers import protocolReducer

if __name__ == '__main__':
    listOfLists = fileReader.readFile()
    protocolReducer.reduceByProtocolAndCountLines(listOfLists, 302)