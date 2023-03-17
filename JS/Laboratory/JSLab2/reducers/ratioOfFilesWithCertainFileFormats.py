def printOutRatioOfGraphicFilesToAllFiles(listOfLines):
    counter = 0;
    for line in listOfLines:
        size = len(line[-4])
        if size >= 4:
            if line[-4][size-4:] in ('.gif', 'jpeg', '.jpg', '.xbm') and line[-1] != '-':
                counter += 1
    ratio = counter / len(listOfLines)
    print(f'Long -> {counter} to {len(listOfLines)} | decimal -> %0.2f' % ratio)