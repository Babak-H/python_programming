import csv
from pathlib import Path

DATA_FILE_NAME = 'data.csv'
CFG_FILE_DIR = 'config'
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR.joinpath(CFG_FILE_DIR).joinpath(DATA_FILE_NAME)


def get_data():
    with open(DATA_FILE, "r") as f:
        reader = csv.reader(f)
        next(reader)  # skipping the first row (ids)
        data = [tuple(row) for row in reader]
    return data

# print(get_data())
