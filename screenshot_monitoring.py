import os

# The os.environ object in Python is a mapping (dictionary-like) object that represents the environment variables of the current process.
# It is loaded when the os module is imported, typically during Python startup, and reflects the environment at that time.
# Any subsequent changes to the system environment do not affect os.environ unless they are made through os.environ itself.
os.environ["SSL_CERT_FILE"] = "/tls/root_ca.pem"

import json
import logging
import re
import shutil
from datetime import datetime, timezone
from logging import getLogger
import yaml

import botocore
import botocore.session
from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
from botocore.exceptions import ClientError

# Return a logger with the specified name, creating it if necessary.
LOGGER = getLogger(__name__)
SECRET_DATA = None


def parse_yaml_file(yaml_file_path):
    """read a yaml file and return its content"""
    with open(yaml_file_path, "r") as yaml_file:
        yaml_data = yaml.safe_load(yaml_file)
    return yaml_data


def create_or_clean_screenshot_folder(folder):
    """given folder path, try to create it, if an error is thrown, call another function to empty it"""
    try:
        os.mkdir(folder) 
    except FileExistsError:
        folder_cleanup(folder)   
        LOGGER.debug(f"Target folder already exist {folder}")  


def folder_cleanup(folder):
    """go through the given folder, if there is a file or link under it, then remove it, if there is a subfolder, delete it and its entire content"""
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)    
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                # shutil.rmtree(file_path) function in Python is used to delete an entire directory tree (a folder and all its contents, including subfolders and files)
                # If the folder does not exist, it will raise a FileNotFoundError.
                # If the folder is read-only, it will raise a PermissionError
                shutil.rmtree(file_path)       
        except Exception as e:
            LOGGER.debug("Failed to delete %s, Reason: %s" % (file_path, e))      
            

def check_if_file_exists(path):
    """if given path does NOT exist, send critical level log and abort the script"""
    if not os.path.exists(path):
        LOGGER.critical(
            f"file {path} does not exist, please check documentation and create it."
        )
        exit()
        
        
def write_config_file(CONFIG_FILE_PATH, parameter, value):
    """write the given parameter and value to the json file, if file doesn't exist, create it"""
    try:
        with open(CONFIG_FILE_PATH, "r+") as file:
            config = json.load(file) # Read entire file
            config[parameter] = value # add this key-value to the config 
            # method in Python moves the file cursor to the beginning of the file. This is useful when working with file objects in read (r), write (w), or append (a) modes
            # move cursor back to the beginning of the file
            file.seek(0)
            json.dump(config, file, indent=4)
            file.truncate()
            LOGGER.debug(f"Writing {parameter} to {CONFIG_FILE_PATH}.")
    except FileNotFoundError:
        with open(CONFIG_FILE_PATH, "w") as file:
            json.dump({parameter: value}, file, indent=4)
            LOGGER.debug(f"created {CONFIG_FILE_PATH} and writing {parameter}")
            

def read_config_file(CONFIG_FILE_PATH, parameter):
    """read a parameter's value from json config file, if not return None"""
    try:
        with open(CONFIG_FILE_PATH, "r") as file:
            config = json.load(file)
            LOGGER.debug(f"Parameter {parameter} read from {CONFIG_FILE_PATH}")
            return config.get(parameter)
    except FileNotFoundError:
        LOGGER.debug(f"Config file {CONFIG_FILE_PATH} not found")
        return None


def url_environment_replacer(url, link) :
    """find 'environment' in url string and replace it with link string, return new url string"""
    if "environment" in url:
        try:
            LOGGER.debug(f"replaced healthcheck environment in {url}, by target {link}")
            # re.sub(pattern, repl, string)
            url = re.sub(r"environment", link, url)
        except KeyError as e:
            LOGGER.warning(f"Unknown url:link mapping {e}. Please check {url} and mapping")
    return url


def transform_time(timestamp, structure="short"):
    """transform timestamp into datatime in str format"""
    # timestamp example => 1735488123.456789
    timestamp = int(timestamp) / 1000
    # Convert Unix timestamp to datetime
    dt_object = datetime.fromtimestamp(timestamp, timezone.utc)
    if structure == "short":
        return dt_object.strftime("%H:%M:%S")
    return dt_object.strftime("%Y-%m-%d-%H:%M:%S")
    


def all_experiments_start_end(data):
    """get earliest and latest data points from the 'data' dictionary and return them"""
    if "start" in data and "end" in data:
        lowest_start = data["start"]
        biggest_end = data["end"]
    else:
        biggest_end = max(event["end"] for event in data.values())
        lowest_start = min(event["start"] for event in data.values())
        
    return f"S_{transform_time(lowest_start, structure='long')}-E_{transform_time(biggest_end, structure='long')}"


def get_secret(secret_name, region_name):
    """get secret from AWS secret_manager"""
    getLogger("botocore").setLevel(logging.ERROR)
    try:
        # Create a Secrets Manager client
        client = botocore.session.get_session().create_client(
            service_name="secretsmanager", region_name=region_name
        )
        LOGGER.info(f"Fetching the details for the secret name {secret_name}")
        cache_config = SecretCacheConfig()
        cache = SecretCache(config=cache_config, client=client)
        secret= cache.get_secret_string(secret_name)
        secret_data = json.loads(secret)
        return secret_data
    except ClientError as e:
        LOGGER.error(f"Exception details: {e}")