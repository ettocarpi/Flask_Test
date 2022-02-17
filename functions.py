import logging
import constants

def log(message,level=logging.INFO):
    #Log_Format = "%(levelname)s %(asctime)s - %(message)s"
    Log_Format = constants.LOG_FORMAT
    logging.basicConfig(filename = constants.LOG_PATH,
                    filemode='a',
                    format = Log_Format, 
                    level = level)
    logger = logging.getLogger(message)
    if level == logging.INFO:
        logger.info(message)
    if level == logging.ERROR:
        logger.error(message)