def printResourcesInBetweenHours(listOfLines, leftLimit, rightLimit):
    if(leftLimit <= rightLimit):
        for line in listOfLines:
            if(0 <= leftLimit < int(line[4][-8:-6]) <  rightLimit < 24):
                for part in line:
                    print(part, end=' ')
                print()
    else:
        for line in listOfLines:
            if(0 <= int(line[4][-8:-6]) <= leftLimit | rightLimit <= int(line[4][-8:-6]) < 24):
                for part in line:
                    print(part, end=' ')
                print()

