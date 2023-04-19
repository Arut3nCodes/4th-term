from os import *
from sys import argv

def printOutAllDirs():
    print(f'{"-" * 20}LIST OF ENVIRONMENTAL VARIABLES{"-" * 20}')

    [print(path) for path in filter(lambda path: path != '', environ['PATH'].split(sep=';'))]

    print("-" * 40)

def printOutAllDirsWithExecs():
    print(f'{"-" * 20}PATHS WITH EXECS IN DIR{"-" * 20}')

    for path in filter(lambda path: path != '', environ['PATH'].split(sep=';')):
        print(f'{path} -> ', end='')
        l = list()
        [l.append(execfile) for execfile in listdir(path) if str(execfile)[-3:] == 'exe']
        print()
        print(f'{l} \n {"-" * 40}')
def printOutPathInfo():
    if '-a' in argv:
        printOutAllDirs()
    if '-b' in argv:
        printOutAllDirsWithExecs()