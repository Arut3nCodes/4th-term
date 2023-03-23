import sys
import datetime

def correctLine(line): # filters useless chars and merges seperate items
    if line[-1] == '-':
        line[-1] = 0
    line[3:5] = [' '.join(line[3:5]).strip('[]')]
    line = list(filter(lambda item: item != '"GET' and item != 'HTTP/1.0"', line))
    line[4:-2] = [' '.join(line[4:-2]).strip('"')]
    filtered = list(filter(lambda t: t != '-', line))
    return filtered

def transformLine(line): # converts list items into correct types and classes
    line[1] = datetime.datetime.strptime(line[1], "%d/%b/%Y:%H:%M:%S %z")
    line[-2] = int(line[-2])
    line[-1] = int(line[-1])
    return line
def read_log():
    listOfLines = []
    for line in sys.stdin:
        line = line.rstrip().split() # splitting string into seperate items
        line = correctLine(line)
        line = transformLine(line)
        listOfLines.append(tuple(line))
    return listOfLines

# tuple final form (address:String, date:dateTime, filepath:String, status:Int, fileSize:Int)


