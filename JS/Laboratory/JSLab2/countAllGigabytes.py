def countAndPrintOutSummaryGigabytes(listOfLines):
    bytes = 0
    for line in listOfLines:
        bytes += int(line[-1])
    gigabytes = bytes / 2048
    print("Amount of data in gigabytes equals to %.2f" % gigabytes)
