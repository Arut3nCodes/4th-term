import sshFileReader
import filters
import ipaddress
import re
from abc import *
class SSHLogEntry(ABC):
    def __init__(self, line):
        dictLine = sshFileReader.correctDict(sshFileReader.lineToDict(line))
        self.date = dictLine['date']
        self.host = dictLine['host']
        self.__rawInput = dictLine['description']
        self.PID = dictLine['PID']

    def __repr__(self):
        return "Date - ["+str(self.date)+"]  |  Host - ["+str(self.host)+"]  |  PID - ["+str(self.PID)+"]  |  RawInput - ["+str(self.__rawInput)+"]"

    def __lt__(self, other):
        if self.date < other.date:
            if self.PID > other.PID:
                return True
        return False

    def __gt__(self, other):
        if self.date > other.date:
            if self.PID < other.PID:
                return True
        return False
    def __eq__(self, other):
        if self.date == other.date and self._SSHLogEntry__rawInput ==  other._SSHLogEntry__rawInput and type(self) == type(other):
            return True
        return False

    def returnIP(self):
        pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
        iplist = re.findall(pattern, self.__rawInput)
        match iplist:
            case []:
                return None
            case _:
                return ipaddress.IPv4Address(iplist[0])

    @abstractmethod
    def validate(self):
        pass

    @property
    def hasIp(self):
        match self.returnIP():
            case None:
                return False
            case _:
                return True
