def printOutRatioOfGraphicFilesToAllFiles(listOfLines):
    counter = 0;
    for line in listOfLines:
        size = len(line[-4])
        if size >= 4:
            if line[-4][size-4:] in ('.gif', 'jpeg', '.jpg', '.xbm'):
                counter += 1
    ratio = counter / len(listOfLines)
    print(f'Long ratio is {counter} to {len(listOfLines)} or in short is %0.2f' % ratio)