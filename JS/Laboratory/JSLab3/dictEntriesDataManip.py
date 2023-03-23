import datetime

def print_dict_entry_dates(dictLog):
    for key, values in dictLog.items():
        requestsCount = 0
        earliestRequest = values[0][4]
        lastRequest = values[0][4]
        requestsWith200 = 0

        for line in values:
            requestsCount += 1
            if(earliestRequest > line[4]):
                earliestRequest = line[4]
            elif(lastRequest < line[4]):
                lastRequest = line[4]
            if line[6] == 200:
                requestsWith200 += 1

        print('-----------------------------------')
        print(f'Host name: {key}')
        print(f'Count of requests: {requestsCount}')
        print(f'First request: {earliestRequest.strftime("%d/%b/%Y %H:%M:%S")}')
        print(f'Latest request: {lastRequest.strftime("%d/%b/%Y %H:%M:%S")}')
        print(f'Ratio of 200 to the rest: {requestsWith200} to {requestsCount}')