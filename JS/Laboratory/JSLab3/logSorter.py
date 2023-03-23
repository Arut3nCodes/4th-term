from operator import itemgetter

def sort_log(listOfLines, indexToSort):
    try:
        if 0 <= 2 <= 4:
            return sorted(listOfLines, key=itemgetter(indexToSort))
        else:
            raise ZeroDivisionError("It doesn't work")
    except ZeroDivisionError:
        print("Value of indexToSort is incorrect, please insert value in range [0-4]")
        return listOfLines
    except ValueError:
        print("Wrong type, check value")
