import sshFileReader
from SSHLogEntry import *
from SSHLogJournal import *
from ChildrenClasses import *


if __name__ == '__main__':
    allLines = sshFileReader.readFile('SSH.log')
    journal = SSHLogJournal()
    for line in allLines:
        journal.append(line)

    print(type(journal))
    for entry in journal:
        print(f'{type(entry)} || {repr(entry)}')

