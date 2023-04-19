from os import *
from sys import argv

def envVarRead():
    if len(argv) == 1:
        for KEY, VALUE in environ.items():
            print(f'{KEY}: {VALUE}')
    else:
        for num in range(1, len(argv)-1):
            param = argv[num]
            if str(param) in environ:
                print(f'{param}: {environ[param]}')
            else:
                print(f"Parameter {param} doesn't exit")
