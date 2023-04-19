import logging
import sys
from filters import getMessageType

def checkForError(line):
    return line['description'][:5] == 'error'

def log(line, logger):
    allBytes = 3
    for key in line.keys():
        allBytes += len(line[key])
    logger.debug(f'Bytes read: {allBytes}')
    if(checkForError(line)):
        logger.error(line['description'])
    elif(getMessageType(line['description'])=='login failed'):
        logger.warning("Login attempt failed")
    elif(getMessageType(line['description'])=='connection closed'):
        logger.info("Connection was closed")
    elif (getMessageType(line['description']) == 'login successful'):
        logger.info("Login attempt was successful")
    elif (getMessageType(line['description']) == 'breakin attempt'):
        logger.critical("THERE WAS A BREAK-IN ATTEMPT! WATCH-OUT!")

def loggerConfig(logger):
    messageHandler = logging.StreamHandler(sys.stdout)
    errorHandler = logging.StreamHandler(sys.stderr)
    formatter = logging.Formatter('%(asctime)s   %(levelname)s   %(message)s', datefmt='%d-%b-%y %H:%M:%S')

    messageHandler.setLevel(logging.DEBUG)
    messageHandler.setFormatter(formatter)

    errorHandler.setFormatter(formatter)
    errorHandler.setLevel(logging.ERROR)
    errorHandler.addFilter(lambda level: level.levelno != logging.CRITICAL)

    logger.addHandler(messageHandler)
    logger.addHandler(errorHandler)

def logAllLines(listOfLines):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    loggerConfig(logger)
    for line in listOfLines:
        log(line, logger)