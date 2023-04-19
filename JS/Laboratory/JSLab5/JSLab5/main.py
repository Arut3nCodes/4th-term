from sshFileReader import readFile
from filters import *
from logger import logAllLines
import calculations

def debugFunc(listOfLines):
    for line in listOfLines:
        print(f'{line}: \n' +
              f'\t{getIpv4sFromLog(line)}\n' +
              f'\t{getUsersFromLog(line)}\n' +
              f'\t{getMessageType(line["description"])}\n')
def debugLogging(listOfLines):
    logAllLines(listOfLines)

if __name__ == '__main__':
    listOfLines = readFile("test.txt")
    # debugFunc(listOfLines)
    #logAllLines(listOfLines)
    print(calculations.getListOfPairUserSSHTime(listOfLines))
    print(calculations.calculateGlobalAverageAndStandardDevation(listOfLines))
    print(calculations.calculateAverageAndStandardDevationForUser(listOfLines, 'webmaster'))
    print(calculations.getMostAndLeastOftenLogginingUser(listOfLines))