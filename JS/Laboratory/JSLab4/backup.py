import os
from sys import argv
import datetime
import subprocess

def findOrCreateBackupsFolder():
    homeDir = os.path.expanduser("~")
    if ('BACKUP_DIRS' in os.environ):
        homeDir = os.environ['BACKUP_DIRS']
    if not os.path.exists(homeDir + "\.backups"):
     os.makedirs(homeDir + '\.backups')
     if (os.path.exists(homeDir + "\.backups")):
        print(".backups created succesfully")
    return homeDir

def createCopy(dirPath, elemOfZipFile, fileName):
    zipFileFinalPath = elemOfZipFile + '\.backups\ '[0:-1] + fileName
    subprocess.run(["powershell.exe", "-Command", f"Compress-Archive -Path {dirPath}\* -DestinationPath {zipFileFinalPath}"])
def writeLogFile(originalPathToDir, nameOfCopy):
    with open(os.environ['BACKUP_DIRS'] + '\.backups\logFile.csv', "a") as file:
        file.write(f'Copy-ID: {datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")} ')
        file.write(f'Date: {datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")} ')
        file.write(f'Original-Path: {originalPathToDir} ')
        file.write(f'Copy-Name: {nameOfCopy} \n')


if __name__ == '__main__':
    if os.path.isdir(argv[1]):
        dirPath = argv[1]
        dirPath = os.path.abspath(dirPath)
        elemOfZipFile = findOrCreateBackupsFolder()
        zipFileName = datetime.datetime.now().strftime('%Y%m%d%H%M%S') + "-" + dirPath.split('\\')[-1] + ".zip"
        copyName = createCopy(dirPath, elemOfZipFile, zipFileName)
        writeLogFile(dirPath, zipFileName)
