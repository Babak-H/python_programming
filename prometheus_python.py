#!/usr/bin/python

import requests
import json
import time
from logging import getLogger
import os

MD_URL = "http://localhost:8008"
PREFIX = 'metadefender'
ENV = "alpha"
DEFAULT_INTERACTIVE_ENGINES = ["compression_13_windows", "dlp_13_windows", "oesis_13_windows"]
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY environment variable not set")

LOGGER = getLogger(__name__)


def request_endpoint(path, api_key):
    """Issue a request to the given Meta Defender api and return the response in json object"""
    try:
        response = requests.get(MD_URL+path, headers={'apikey': api_key})
        return json.loads(response.text)
    except Exception as e:
        LOGGER.error(f"ERROR: failed to request endpoint {path}: {e}")
        return {}


def write_metrics():
    metrics_list = []
    # Get MD current load and queue
    try:
        resp = request_endpoint("/stat/nodes", API_KEY)
        load = resp["statuses"][0]["load"]
        scan_queue = resp["statuses"][0]["scan_queue"]
        
        metrics_list.append({"load": load})
        metrics_list.append({"scan_queue": scan_queue})
    except Exception as e:
        LOGGER.error(f"ERROR: Failed to get load or queue metrics: {e}")
        
    # Get the number of active/inactive engines
    try:
        active_engines = 0
        inactive_engines = 0
        resp = request_endpoint("/stat/nodes", API_KEY)
        
        for engine in resp["statuses"][0]["engines"]:
            if engine["id"] not in DEFAULT_INTERACTIVE_ENGINES:
                if engine["active"] is True:
                     active_engines += 1
                else:
                    inactive_engines += 1
        metrics_list.append({"active_engines": active_engines})
        metrics_list.append({"inactive_engines": inactive_engines})
    except Exception as e:
        LOGGER.error(f"ERROR: Failed to get the number of active/inactive engines, {e}")
        
    # Get MD license info
    try:
        resp = request_endpoint("/admin/license", API_KEY)
        days_left = resp.get("days_left", 0)
        
        if resp.get("online_activated"):
            online_activated = 1
        else:
            online_activated = 0
        
        metrics_list.append({"online_activated": online_activated})
        metrics_list.append({"days_left": days_left})
    except Exception as e:
        LOGGER.error(f"ERROR: Failed to get license info, {e}")
    
    # nburnham: Get Average processing time of files, last 50 scans
    try:
        process_time = []
        resp = request_endpoint("/stat/log/scan", API_KEY)
        scanned_file_list = resp["scans"]
        
        for i in scanned_file_list:
            p_time = i["scan_results"]["total_time"]
            process_time.append(p_time)
        average_file_process_time = sum(process_time) / len(process_time)
        metrics_list.append({"average_file_process_time": average_file_process_time})
    except Exception as e:
        LOGGER.error(f"ERROR: Failed to get the file process duration, {e}")
    
    try:
        with open("./prom_metrics/metrics.prom", "w") as f:
            f.seek(0)
            for metric in metrics_list:
                # name = list(metric.keys())[0]
                # value = list(metric.values())[0]
                name, value = next(iter(metric.items()))
                metric_str = f"{name}{{role=\"{PREFIX}\",env=\"{ENV}\"}} {value}\n"
                f.write(metric_str)
    except FileNotFoundError as e:
        LOGGER.error(f"ERROR: Directory './prom_metrics/' does not exist, {e}")
    except PermissionError as e:
        LOGGER.error(f"ERROR: Permission denied writing to metrics file, {e}")
    except Exception as e:
        LOGGER.error(f"ERROR: Failed to write metrics to file, {e}")
        
        
if __name__ == "__main__":
    while True:
        write_metrics()
        time.sleep(10) # Adjust the interval as needed
            
        
# curl --request GET --url 'http://localhost:8008/stat/nodes' --header 'apikey:*********' | jq