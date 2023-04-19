import re

def getIpv4sFromLog(line):
    pattern = r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}'
    return re.findall(pattern, line['description'])
def getUsersFromLog(line):
    pattern = r'user ([A-z0-9]+)|user\=([A-z0-9]+)'
    found = re.findall(pattern, line['description'])
    match found:
        case [(x, '')] if x not in ['authentication', 'unknown']:
            return x
        case [('', x)] if x not in ['authentication', 'unknown']:
            return x
        case _:
            return 'None'

def  getMessageType(description):
    listOfResponses = ['login successful', 'login failed', 'connection closed', 'wrong password', 'wrong username', 'breakin attempt']
    listOfPatterns = [r'^Accepted password', r'authentication failure|authentication failure;', r'^Connection closed|^Received disconnect', r'^Failed password', r'^[I,i]nvalid user', r'BREAK-IN ATTEMPT!']
    for i in range(0,7):
        if(i == 6):
            return 'else'
        elif re.search(listOfPatterns[i], description):
            return listOfResponses[i]


