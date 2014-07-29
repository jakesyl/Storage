import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.debug)
logger2 = logging.getlogger(name)
logger.info('Start reading database')
# read database here

records = {'john': 55, 'tom': 66}
logger2.debug('Records: %s', records)
logger.info('Updating records ...')
# update records here

logger.info('Finish updating records')