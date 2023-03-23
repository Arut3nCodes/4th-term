def get_entries_by_addr(listOfLines, address):
    filteredList = list()
    for line in listOfLines:
        if line[0] == str(address):
            filteredList.append(line)
    return filteredList


def get_entries_by_code(listOfLines, code):
    try:
        filteredList = list()
        for line in listOfLines:
            if line[3] == int(code):
                filteredList.append(line)
        return filteredList
    except ValueError:
        print('Wrong code type, please pass an integer')

def get_failed_reads(listOfLines, returnOption):
    try:
        listOf400 = list()
        listOf500 = list()
        for line in listOfLines:
            if str(line[-2])[0] == '4':
                listOf400.append(line)
            elif str(line[-2])[0] == '5':
                listOf500.append(line)
        if returnOption:
            return listOf400 + listOf500
        else:
            return tuple(listOf400, listOf500)

    except ValueError:
        print("Wrong value in one of the parameters")

def get_entries_by_extention(listOfLines, extention):
    filteredList = list()
    for line in listOfLines:
        if line[3][-len(extention):] == extention:
            filteredList.append(line)
    return filteredList