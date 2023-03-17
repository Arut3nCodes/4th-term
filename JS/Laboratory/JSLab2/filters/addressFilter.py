import fileReader

def printOutOnlyWithAdress(listOfLists, address):
    for line in listOfLists:
        if(line[0][-len(address):] == address):
            for part in line:
                print(part, end=' ')
            print()
