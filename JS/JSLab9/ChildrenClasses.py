from SSHLogEntry import *
from sshFileReader import lineToDict
import re


class PasswordAcceptedEntry(SSHLogEntry):

    def __init__(self, line):
        SSHLogEntry.__init__(self, line)
        listOfFound = re.search(r"Accepted password for (?P<username>\w+).* (?P<portNumber>[0-9]*) ssh2$", line)
        self.username = listOfFound['username']
        self.port = listOfFound['portNumber']

    def __repr__(self):
        return SSHLogEntry.__repr__(self)+f"  |  username - [{self.username}]  |  port - [{self.port}]"

    def validate(self):
        if self._SSHLogEntry__rawInput.startswith('Accepted password'):
            return True
        else:
            return False


class PasswordDeniedEntry(SSHLogEntry):
    def __init__(self, line):
        SSHLogEntry.__init__(self, line)
        listOfFound = re.search(r": Failed password .* (?P<username>.*) from .* (?P<portNumber>[0-9]*) ssh2$", line)
        self.username = listOfFound['username']
        self.port = listOfFound['portNumber']

    def __repr__(self):
        return SSHLogEntry.__repr__(self)+f"  |  username - [{self.username}]  |  port - [{self.port}]"

    def validate(self):
        if self._SSHLogEntry__rawInput.startswith('Failed password'):
            return True
        else:
            return False


class ErrorEntry(SSHLogEntry):

    def __init__(self, line):
        SSHLogEntry.__init__(self, line=line)
        self.errorType = re.search(r"error: (?P<errorType>.*)", self._SSHLogEntry__rawInput)['errorType']

    def __repr__(self):
        return SSHLogEntry.__repr__(self)+f"  |  errorType - [{self.errorType}]"

    def validate(self):
        if self._SSHLogEntry__rawInput.startswith('error:'):
            return True
        else:
            return False


class OtherInformationEntry(SSHLogEntry):

    def __init__(self, line):
        SSHLogEntry.__init__(self, line)

    def __repr__(self):
        return SSHLogEntry.__repr__(self)

    def validate(self):
        return True