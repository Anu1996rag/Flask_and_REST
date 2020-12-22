import logging
import time
from logging.handlers import TimedRotatingFileHandler

def abc():
    #getting name of the logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    #initiating object
    time_handler = TimedRotatingFileHandler('logs/timedLogs.log',when='s',backupCount=3,interval=1)

    logger.addHandler(time_handler)

    for i in range(5):
        logger.info('Timed File Logger Test')
        time.sleep(5)

if __name__ == "__main__":
    abc()