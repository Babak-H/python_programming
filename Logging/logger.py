import logging
import os
from datetime import datetime
from pathlib import Path

LOGGING_FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
LOGS_FOLDER_PATH = os.path.join(os.getcwd(), 'logs')

if not Path(LOGS_FOLDER_PATH).is_dir():
    os.mkdir(LOGS_FOLDER_PATH)

DATE_NOW = datetime.now()
F_PREFIX = "{year}.{month}.{day}".format(year=DATE_NOW.year,
                                         month=str(DATE_NOW.month).zfill(2),
                                         day=str(DATE_NOW.day).zfill(2))
F_SUFFIX = 'Error.log'
LOG_FILE_NAME = f"{F_PREFIX}_{F_SUFFIX}"
LOG_FILE_PATH = os.path.join(LOGS_FOLDER_PATH, LOG_FILE_NAME)
logging.basicConfig(filename=LOG_FILE_PATH,
                    format=LOGGING_FORMAT, level=logging.INFO)
