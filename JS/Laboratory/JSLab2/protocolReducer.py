def reduceByProtocolAndCountLines(listOfLines, protocol):
    counter = 0
    for line in listOfLines:
        if(int(line[-2]) == int(protocol)):
            counter += 1
    print(f"There are {counter} lines that used {protocol} protocol")

def findMistakes(listOfLines, protocol):
    for line in listOfLines:
        if(int(line[-2]) == int(protocol)):
            for part in line:
                print(part, end=' ')
            print()