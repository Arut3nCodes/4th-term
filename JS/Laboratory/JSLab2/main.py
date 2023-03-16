import countAllGigabytes
import pathAndSizeOfLargestResource
import ratioOfFilesWithCertainFileFormats
import reducers
import filters
import protocolFilter
import timeFilter
import dateFilter
import addressFilter
def fileReader():
    with open('NASA', encoding='utf8') as file:
        listOfLines = []
        for line in file:
            if(line != ''):
                #print(line)
                listOfLines.append(line.split())
        file.close()
        return listOfLines

def readLine(listOfLines):
    for line in listOfLines:
        for part in line:
            print(part, end=" ")
        print()

if __name__ == '__main__':
    listOfLines = fileReader()
    #protocolReducer.reduceByProtocolAndCountLines(listOfLines, 404)
    #countAllGigabytes.countAndPrintOutSummaryGigabytes(listOfLines)
    #pathAndSizeOfLargestResource.printOutPathAndSizeOfLargestResource(listOfLines)
    #ratioOfFilesWithCertainFileFormats.printOutRatioOfGraphicFilesToAllFiles(listOfLines)
    #protocolFilter.filterByProtocol(listOfLines, 404)
    #timeFilter.printResourcesInBetweenHours(listOfLines, 22, 6)
    # !!!!! dateFilter.printResourcesOnDay(listOfLines, 1)
    addressFilter.printOutOnlyWithAdress(listOfLines, '.pl')

