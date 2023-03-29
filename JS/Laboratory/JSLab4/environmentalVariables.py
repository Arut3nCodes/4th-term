from os import *
from sys import argv

def envVarRead():
    if len(argv) == 1:
        for KEY, VALUE in environ:
            print(f'{KEY}: {VALUE}')
    else:
        for param in argv:
            if param in environ:
                print(f'{param}: {environ[param]}')
            else:
                print(f'Parameter {param} d')
if __name__ == '__main__':
    envVarRead()
