import statistics
import filters
import datetime

def getListOfPairUserSSHTime(listOfLines):
    listOfPairs = []
    currUsername = 'None'
    currTask = ''
    currFirstSSHTime = ''
    currLastSSHTime = ''
    for line in listOfLines:
        if(line['call'] != currTask):
            if currTask == '':
                currTask = line['call']
                currFirstSSHTime = line['date']
            else:
                listOfPairs.append((currUsername, (datetime.datetime.strptime(currLastSSHTime, "%b %d %H:%M:%S") - datetime.datetime.strptime(currFirstSSHTime, "%b %d %H:%M:%S")).total_seconds()))
                currFirstSSHTime = line['date']
                currLastSSHTime = line['date']
                currUsername = 'None'
                currTask = line['call']

        else:
            currLastSSHTime = line['date']
        if(filters.getUsersFromLog(line) != 'None'): currUsername=filters.getUsersFromLog(line)
    return listOfPairs

def calculateGlobalAverageAndStandardDevation(listOfLines):
    listOfRequests = getListOfPairUserSSHTime(listOfLines)
    return statistics.mean(pair[1] for pair in listOfRequests), statistics.stdev(pair[1] for pair in listOfRequests)
def calculateAverageAndStandardDevationForUser(listOfLines, username):
    listOfRequests = list(filter(lambda pair: pair[0] == username, getListOfPairUserSSHTime(listOfLines)))
    return statistics.mean(pair[1] for pair in listOfRequests), statistics.stdev(pair[1] for pair in listOfRequests)

def getMostAndLeastOftenLogginingUser(listOfLines):
    listOfRequests = getListOfPairUserSSHTime(listOfLines)
    dictOfPairsOfNamesAndAmountOfRequests = dict()
    for request in listOfRequests:
        if request[0] in dictOfPairsOfNamesAndAmountOfRequests:
            dictOfPairsOfNamesAndAmountOfRequests[request[0]]+=1
        else:
            dictOfPairsOfNamesAndAmountOfRequests.update({request[0]: 1})
    return (max(dictOfPairsOfNamesAndAmountOfRequests.items(), key=lambda x: x[1]), min(dictOfPairsOfNamesAndAmountOfRequests.items(), key=lambda x: x[1]))