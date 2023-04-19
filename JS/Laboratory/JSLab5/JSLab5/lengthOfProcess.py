import filters
import random

def getAllUsers(listOfLines):
    listOfUniqueNames = []
    for line in listOfLines:
        name = filters.getUsersFromLog(line)
        if name not in listOfUniqueNames and name != 'None':
            listOfUniqueNames.append(name)
    return listOfUniqueNames

def allLinesOfRandomUser(listOfLines):
    listOfUsers = getAllUsers(listOfLines)
    listOfUserLines = []
    randomUser = listOfUsers[random.randint(0, len(listOfUsers))]
    for line in listOfLines:
        if filters.getUsersFromLog(line) == randomUser:
            listOfUserLines.append(line)
    return allLinesOfRandomUser


def getNRandomLinesOfRandomUser(listOfLines, n):
    allLines = allLinesOfRandomUser(listOfLines)
    listOfLinesToReturn = []
    while (len(listOfLinesToReturn) != n):
        listOfLinesToReturn.append(allLines[random.randint(0, len(allLines))])
    return listOfLinesToReturn