import logging

logger = logging.getLogger(__name__)

def log_all():
    logger.debug ("Debug")
    logger.info ('Info')
    logger.warning ('Warning')
    logger.error ('Error')
    logger.critical ('Critical')
    logger.fatal ('*'*50)

if __name__ == '__main__':
    log_all()