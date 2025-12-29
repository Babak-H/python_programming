# this script looks for unread emails, download the attachments
# unread mail -> extract attachments -> create dataframe -> send to sql

from time import sleep
from assets.connections import *
from assets import config_file as config
from win32com.client import Dispatch
import datetime
import os
import pandas as pd
import shutil
import logging
import sys

# Gets the current working directory
# Returns the parent directory of the current working directory
# Adds that parent directory to the beginning of Python’s module search path (sys.path), giving it top priority when importing modules, It allows your script to import Python modules from the parent directory of where it’s running
sys.path.insert(0, os.path.dirname(os.getcwd()))

# new instance of database_connection class
new_db = Database_connection(config.SQL_SERVER, "***", config.SQL_DRIVER)
new_db.create_connection()

# set up folder paths
cwd = os.path.dirname(os.getcwd())
folder_path = os.path.join(cwd, 'Avaya_data')
archive_folder_path = os.path.join(folder_path, 'archive')

# start outlook
outlook = Dispatch('Outlook.Application')
mapi = outlook.GetNamespace('MAPI')
inbox = mapi.GetDefaultFolder("6")
parent = inbox.parent
inbox = parent.folders("AVAYA_TEST")
inbox_test = inbox.Items

# Iterate over all mails in AVAYA_TEST folder in outlook
files_path_list = []
for msg in inbox_test:
    if msg.Unread == True:
        att = msg.attachments
        for item in att:
            sleep(10)  # wait for the file to be downloaded
            file_name = item.FileName
            # can be changed to csv, txt, ...
            if file_name.endswith('.xlsx'):
                file_path = os.path.join(folder_path, file_name)
                files_path_list.append(file_path)
                item.SaveAsFile(file_path)
        msg.Unread = False  # mark email as read

# concatenate all files into one dataframe
final_dataframe = pd.DataFrame()
for file_ in files_path_list:
    try:
        # Tries to read the 'Interval Raw' sheet from the Excel file
        temp_df = pd.read_excel(file_, 'Interval Raw')
    except:
        # If the first sheet ('Interval Raw') doesn’t exist (or another error occurs), it tries reading the fallback sheet 'Interval Raw_RWE' instead
        temp_df = pd.read_excel(file_, 'Interval Raw_RWE')
    final_dataframe = pd.concat([final_dataframe, temp_df], sort=False)

# create new instacne of SQL_operation class
new_table = SQL_operations(database='***',
                           schema='***',
                           DataFrame=final_dataframe,
                           table_name='***',
                           engine=new_db.engine)

# insert dataframe into sql db
if new_table.check_if_table_exists():
    new_table.insert_data()
else:
    new_table.create_table_skeleton()
    new_table.truncate_table()
    new_table.insert_data()

# move all downloaded from Outlook files into archive folder (after inserting data into database)
for file_ in files_path_list:
    # basename => the actual file name from the full address
    file_name = os.path.basename(file_)
    archive_file_path = os.path.join(archive_folder_path, file_name)
    shutil.move(file_, archive_file_path)
