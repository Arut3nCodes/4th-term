import datetime

def printResourcesOnDay(listOfLines, day):
    try:
        if(1 <= int(day) <= 7):
            for line in listOfLines:
                date = datetime.datetime.strptime(line[3][1:12], "%d/%b/%Y")
                if(date.weekday()-1 == int(day) and line[-1] != '-'):
                    print(line[-4])
                    # for part in line:
                    #    print(part, end=' ')
                    # print()
        else:
            raise Exception('')
    except ValueError:
        print("Wrong type of value inserted. Please pass a number in range [1-7]")
    except Exception:
        print("A number passed should be in range [1-7]")
