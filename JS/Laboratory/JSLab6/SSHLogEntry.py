import sshFileReader
import filters
import ipaddress
class SSHLogEntry:
    def __init__(self, line):
        dictLine = sshFileReader.correctDict(sshFileReader.lineToDict(line))
        self.date = dictLine['date']
        self.host = dictLine['host']
        self.rawInput = line
        self.PID = dictLine['PID']
    def __str__(self):
        return "Date-["+str(self.date)+"]|Host-["+str(self.host)+"]|PID-["+str(self.PID)+"]|RawInput-["+str(self.rawInput)

    def returnIP(self):
        iplist = filters.getIpv4sFromLog(sshFileReader.lineToDict(self.rawInput))
        match iplist:
            case []:
                return None
            case _:
                return ipaddress.IPv4Address(iplist[0])
