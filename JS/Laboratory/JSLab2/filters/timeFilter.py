
def printResourcesInBetweenHours(listOfLines, leftLimit, rightLimit):
    try:
        if(0 < int(leftLimit) < 24 and 0 < int(rightLimit) < 24):
            if(leftLimit <= rightLimit):
                for line in listOfLines:
                    if(leftLimit <= int(line[3][-8:-6]) < rightLimit and line[-1] != '-'):
                        print(line[-4])
                        #for part in line:
                        #    print(part, end=' ')
                        #print()
            else:
                for line in listOfLines:
                    if((int(line[3][-8:-6]) < rightLimit or leftLimit <= int(line[3][-8:-6])) and line[-1] != '-'):
                        print(line[-4])
                        # for part in line:
                        #    print(part, end=' ')
                        # print()
        else:
            raise Exception()
    except ValueError:
        print("Wrong type of data passed into function")
    except Exception:
        print("Numbers passed should be in range [1-24]")