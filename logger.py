import logging
import os
import sys

# Define Logger
logger = logging.getLogger('nsb')

# Setup log message look and handler types
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s')
file_handler = logging.FileHandler("{p}/{fn}".format(p=os.path.dirname(os.path.realpath(sys.argv[0])), fn='nsb.log'), encoding='utf-8', mode='w')
stream_handler = logging.StreamHandler(stream=sys.stdout)

log_handlers = []
log_handlers.append(file_handler)
log_handlers.append(stream_handler)

for h in log_handlers:
    h.setFormatter(formatter)
    logger.addHandler(h)

# Set level of log messages to record
logger.setLevel(logging.DEBUG)
