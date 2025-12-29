import logging
import os
from pathlib import Path
from datetime import datetime

# Const Variables
SQL_SERVER = "***"
SQL_DATABASE = "***"
SQL_DRIVER = "***"
SQL_SCHEMA = "***"
CSV_ENCODING = "ISO-8859-1"
MID_SERVER_PATH = "***"

# Setting up the logging system
LOGGING_FORMAT = '%(asctime)s - %(levelname)s: %(message)s'
# one level up in directory
temp_logs_path = Path(os.path.dirname(__file__)).parents[0]
LOG_FOLDER_PATH = os.path.join(temp_logs_path, 'LOGS')
if not Path(LOG_FOLDER_PATH).is_dir():
    os.makedirs(LOG_FOLDER_PATH)  # creating folder 'LOGS'

date_now = datetime.now()
Log_file_name = "{year}.{month}.{day}_ETL_SNOW.log".format(year=date_now.year,
                                                           month=str(date_now.month).zfill(2),
                                                           day=str(date_now.day).zfill(2))

LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH, Log_file_name)
del temp_logs_path, date_now, Log_file_name  # free up some memory

logging.basicConfig(filename=LOG_FILE_PATH, 
                    format=LOGGING_FORMAT, 
                    level=logging.INFO)



