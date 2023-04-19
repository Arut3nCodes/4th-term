import os
from sys import argv
import subprocess

def readDataFromFile(path):
    with open(path, "r") as fileContent:
        line = fileContent.readline()
        line = line.split()
        lineTags = ['filePath', 'countOfChars', 'countOfWords', 'countOfLines', 'mostOccChar', 'mostOccWord']
        dct = dict()
        for i in range(0, 6):
            dct.update({lineTags[i]: line[i]})
        return dct

def runAllProcesses(pathToFile):
    javaProgram = "FilesToRead/Main.java"
    subprocess.run(["javac", javaProgram])
    subprocess.run(["java", "Main", pathToFile])


def printOutEvenMoreInformation():
    if os.path.isdir(argv[1]):
        dirPath = argv[1]
        listOfFiles = os.listdir(dirPath)
        runAllProcesses(listOfFiles[0])

    else:
        print("Specified path is not a path to directory")
