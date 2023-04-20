import sshFileReader
import SSHLogEntry
from ChildrenClasses import *
class SSHLogJournal:

    def __init__(self):
        self.listOfLogEntries = []

    def append(self, line):
        dictLine = sshFileReader.lineToDict(line)
        objectt = None
        if dictLine['description'].startswith('Accepted password'):
            objectt = PasswordAcceptedEntry(line)

        elif dictLine['description'].startswith('Failed password'):
            objectt = PasswordDeniedEntry(line)

        elif dictLine['description'].startswith('error:'):
            objectt = ErrorEntry(line)

        else:
            objectt = OtherInformationEntry(line)

        if objectt.validate():
            self.listOfLogEntries.append(objectt)

    def __len__(self):
        return len(self.listOfLogEntries)

    def __iter__(self):
        return iter(self.listOfLogEntries)

    def __contains__(self, checked):
        if checked in self.listOfLogEntries:
            return True
        return False

    def getLogsFromInBetweenTheDates(self, PID):
        finalList = []
        for entry in self:
            if entry.PID == PID:
                finalList.append(entry)
        return finalList
