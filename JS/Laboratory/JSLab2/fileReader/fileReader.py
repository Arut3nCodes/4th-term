import sys


def readFile():
    listOfLines = []
    for line in sys.stdin:
        listOfLines.append(line.rstrip().split())
    return listOfLines


if __name__ == '__main__':
    readFile()
