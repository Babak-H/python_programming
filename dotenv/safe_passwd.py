# pip install python-dotenv

import os
from dotenv import load_dotenv

# .env does NOT override already existing environment variables by default
load_dotenv(override=True)

API_KEY = os.getenv("API_KEY")

NUMERIC_KEY = int(os.getenv("NUMERIC_KEY"))

USERNAME = os.getenv("USER")

ADDRESS = os.getenv("ADDRESS")

EMAIL = os.getenv("EMAIL")

