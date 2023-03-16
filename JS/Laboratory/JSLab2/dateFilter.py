import datetime


def printResourcesOnDay(listOfLines, day):
    for line in listOfLines:
        date = datetime.date.fromisodate(line[4][1:9])
        if(date.weekday() == day):
            for part in line:
                print(part, end=' ')
            print()
