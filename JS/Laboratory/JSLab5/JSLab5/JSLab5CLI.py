import argparse
import filters
import logger
import lengthOfProcess
import calculations
import sshFileReader
import os.path

def checkIfFileLocationIsCorrect():
    print()

def runChosen(args):
    listOfLines = sshFileReader.readFile(os.path.abspath(args.sshpath))

    match args.command:
        case 'zad2b':
            print(filters.getIpv4sFromLog(listOfLines[0]))
        case 'zad2c':
            print(filters.getUsersFromLog(listOfLines[0]))
        case 'zad2d':
            print(filters.getMessageType(listOfLines[0]['description']))
        case 'zad3':
            print(logger.logAllLines(listOfLines))
        case 'zad4a':
            print(lengthOfProcess.getNRandomLinesOfRandomUser(listOfLines, args.n))
        case 'zad4bI':
            print(calculations.calculateGlobalAverageAndStandardDevation(listOfLines))
        case 'zad4bII':
            print(calculations.calculateAverageAndStandardDevationForUser(listOfLines, args.username))
        case 'zad4c':
            print(calculations.getMostAndLeastOftenLogginingUser(listOfLines))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Main Program')
    parser.add_argument('sshpath', type=str, help='Tutaj podaje sie dokladna sciezke do pliku z logami ssh')
    parser.add_argument('--opt', type=str, help='This argument is used to run cerain ')
    subparser = parser.add_subparsers(description='Helps in running seperate functionalities', help='Użyj parametrów do uruchomienia danej funkcjonalności', dest='command')

    listOfParsed = ['zad2b', 'zad2c', 'zad2d', 'zad3', 'zad4a', 'zad4bI', 'zad4bII','zad4c']

    for name in listOfParsed:
        if (name == 'zad4a'):
            parser4a = subparser.add_parser(name)
            parser4a.add_argument('n', type=int, help='number of lines')

        elif(name == 'zad4bII'):
            parser4b = subparser.add_parser(name)
            parser4b.add_argument('nickname', type=str, help='Username to calculate for')

        else:
            subparser.add_parser(name)
    runChosen(parser.parse_args())



