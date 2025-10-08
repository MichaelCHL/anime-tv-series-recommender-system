import logging
import os
import datetime

LOG_DIRS = 'logs'
os.makedirs(LOG_DIRS, exist_ok=True)
format = '%(asctime)s - %(levelname)s: %(message)s'

logging.basicConfig(
    filename=os.path.join(LOG_DIRS, datetime.datetime.now().strftime('log_%Y-%m-%d.log')),
    level=logging.DEBUG,
    format=format 
)

def get_logger(name):
    return logging.getLogger(name)

