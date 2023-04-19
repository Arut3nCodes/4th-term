import re
import logger

def lineToDict(line):
    dictLine = dict()
    nametags = ['date', 'host', 'call', 'description']
    pattern = r"^(?P<date>\w+\s{1,2}\w+ [0-9]{2}:[0-9]{2}:[0-9]{2}) (?P<host>\w+) (?P<call>\w+\[[0-9]*]): (?P<description>.+)"
    splitted = re.search(pattern, line)
    for name in nametags:
        dictLine.update({name: splitted[name]})
    return dictLine


def readFile(fileName):
    try:
        with open(fileName) as file:
            listOfLines = []
            for line in file:
                listOfLines.append(lineToDict(line))

            return listOfLines
    except FileNotFoundError:
        print("File doesn't exist")

            