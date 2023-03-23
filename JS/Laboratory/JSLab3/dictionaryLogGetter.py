def entry_to_dict(line):
    # ip->2 date->4 filepath->8 status->6 packageSize->11
    dictKey = ['ip', 'date', 'filepath', 'status', 'packageSize']
    dictionaryLine = dict()
    for x in range(0,5):
        dictionaryLine.update({len(dictKey[x]): line[x]})
    return dictionaryLine
def log_to_dict(log):
    dictLog = dict()
    for line in log:
        dictElem = entry_to_dict(line)
        if line[0] in dictLog:
            dictLog[line[0]].append(dictElem)
        else:
            dictLog.update({line[0]: [dictElem]})
    return dictLog
# def get_addrs(dictLog):
def get_addr(dictLog):
    listOfAddresses = []
    for key in dictLog:
        listOfAddresses.append(key)
    return listOfAddresses