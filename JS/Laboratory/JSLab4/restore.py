import os
from sys import argv
import datetime
import subprocess

def analyzeFileHistory():
    with open(os.environ['BACKUP_DIRS'] + '\.backups\logFile.csv', "r") as file:
        listOfTags = ['ID', 'DATE', 'PATHOFORIGINALFILE', 'NAMEOFCOPY']
        listOfDicts = []
        for line in file:
            dct = dict()
            line = line.split(" ")
            for i in range(0,4):
                dct.update({listOfTags[i]: line[1+2*i]})
            listOfDicts.append(dct)
        listOfDicts.reverse()

    return listOfDicts

def printReadable(listOfDicts):
    for log in listOfDicts:
        print(log)

def restoreInDict(pathToRestore, restoreZipFilePath):
    subprocess.run(["cmd", "/c", "del", "/q", f"{pathToRestore}\\*"])
    subprocess.run(["powershell", "Expand-Archive", f"-Path {restoreZipFilePath} -DestinationPath {pathToRestore}"])
    print("Restoration completed succesfully")

if __name__ == '__main__':
    # argv[1] -> dirPath | argv[2] -> version
    listOfDicts = analyzeFileHistory()
    printReadable(analyzeFileHistory())
    restorePath = ""
    if not os.path.exists(argv[1]):
        restorePath = os.getcwd()
    else:
        restorePath = argv[1]
    try:
        fileName = ""
        for log in listOfDicts:
            if(argv[2] == log['ID']):
                fileName = log['NAMEOFCOPY']
        restoreInDict(argv[1], os.environ['BACKUP_DIRS'] + f'\.backups\{fileName}')

    except IndexError:
        print("READ MODE ONLY")