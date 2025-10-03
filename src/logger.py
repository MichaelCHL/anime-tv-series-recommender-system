import logging
import os
import datetime

LOG_DIRS = 'logs'
os.makedirs(LOG_DIRS, exist_ok=True)
format = '%(asctime)s - %(levelname)s: %(messgage)s'

logging.basicConfig(
    filename=datetime.datetime.now().strftime('log_%Y-%m-%d.log')
    level=logging.DEBUG,
    format=format 
)

def logger(name):
    return logging.getLogger(name)

