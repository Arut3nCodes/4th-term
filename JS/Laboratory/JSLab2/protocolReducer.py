def reduceByProtocolAndCountLines(listOfLines, protocol):
    counter = 0
    for line in listOfLines:
        if(int(line[8]) == int(protocol)):
            counter += 1
    print(f"There are {counter} lines that used {protocol} protocol")