def filterByProtocol(listOfLines, protocol):
    for line in listOfLines:
        if(int(line[-2]) == int(protocol)):
            for part in line:
                print(part, end=' ')
            print()