import re
import datetime


def correctDict(dictLine):
    dictLine['date'] = datetime.datetime.strptime(dictLine['date'], "%b %d %H:%M:%S")
    if dictLine['date'].month == 1:
        dictLine['date'] = dictLine['date'].replace(year=(dictLine['date'].year+1))
    dictLine
    return dictLine


def lineToDict(line):
    dictLine = dict()
    nametags = ['date', 'host', 'PID', 'description']
    pattern = r"^(?P<date>\w+\s{1,2}\w+ [0-9]{2}:[0-9]{2}:[0-9]{2}) (?P<host>\w+) \w+\[(?P<PID>[0-9]*)]: (?P<description>.+)"
    splitted = re.search(pattern, line)
    for name in nametags:
        dictLine.update({name: splitted[name]})
    return dictLine


def readFile(fileName, flag=False):
    try:
        with open(fileName) as file:
            listOfLines = []
            i = 1
            for line in file:
                listOfLines.append(line)

                if flag:
                    print(f'{i}: {line}')
                    i += 1
            return listOfLines
    except FileNotFoundError:
        print("File doesn't exist")

            