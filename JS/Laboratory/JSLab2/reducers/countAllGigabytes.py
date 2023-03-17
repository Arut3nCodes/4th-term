def countAndPrintOutSummaryGigabytes(listOfLines):
    bytes = 0
    for line in listOfLines:
        if(line[-1] != '-'):
            bytes += int(line[-1])
    gigabytes = bytes / (1024**3)
    print("Amount of data in gigabytes equals to %.2f" % gigabytes)
