from fileReader import fileReader
from reducers.ratioOfFilesWithCertainFileFormats import printOutRatioOfGraphicFilesToAllFiles

if __name__ == '__main__':
    listOfLines = fileReader.readFile()
    printOutRatioOfGraphicFilesToAllFiles(listOfLines)