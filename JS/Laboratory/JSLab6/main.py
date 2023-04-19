import sshFileReader
from SSHLogEntry import *

if __name__ == '__main__':
    allLines = sshFileReader.readFile('smallTest.txt', flag=True)
    listOfObj = []
    for line in allLines:
        listOfObj.append(SSHLogEntry(line))

    for obj in listOfObj:
        print(obj)
        print(obj.returnIP())