
def filterByProtocol(listOfLines, protocol):
    try:
        for line in listOfLines:
            if (int(line[-2]) == int(protocol)):
                for part in line:
                    print(part, end=' ')
                print()
    except ValueError:
        print("You didn't pass a number into function")
