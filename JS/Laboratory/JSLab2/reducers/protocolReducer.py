def reduceByProtocolAndCountLines(listOfLines, protocol):
    try:
        counter = 0
        for line in listOfLines:
            if (int(line[-2]) == int(protocol)):
                counter += 1
        print(f"There are {counter} lines that used {protocol} protocol")

    except ValueError:
        print("You didn't pass a number into function")