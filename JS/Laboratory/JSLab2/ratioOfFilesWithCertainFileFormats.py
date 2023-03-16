def printOutRatioOfGraphicFilesToAllFiles(listOfLines):
    counter = 0;
    for line in listOfLines:
        match line[-4][-4:-1]:
            case ".gif" | ".jpg" | "jpeg" | "*.xbm":
                counter += 1
    ratio = counter / listOfLines.len
    print(f'Long ratio is {counter} to {listOfLines.len} or in short is %0.2f' % ratio)