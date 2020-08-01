"""
Python Logging

INFO: Confirmation that things are working as expected.

DEBUG: Detailed information, typically of interest only when diagnosing problems.

WARNING: An indication that something unexpected happened, or indicative of some problem in the near future
(e.g. ‘disk space low’). The software is still working as expected.

ERROR: Due to a more serious problem, the software has not been able to perform some function.

CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

critical > error > warning > debug > info
"""

import logging

# logging to the console
# logging.basicConfig(level=logging.DEBUG)

# logging to a file
# logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:%(levelname)s:%(message)s')

# more advanced logging

# get name of this current file and create the logger object
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # set logging level

# set the format how to write the text to logger
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

# set the file to write logs in it and set the logging level
file_handler = logging.FileHandler('test.log')

# even though our logger is set to level DEBUG , since file is set to ERROR, it won't write to log file
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# stream handler shows all levels of logging to the console
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# add the handler to the logger object
logger.addHandler(file_handler)
logger.addHandler(stream_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    # logging an error with traceback to log file
    except ZeroDivisionError:
        logger.exception('Tried to divide by zero')
    else:
        return result


num_1, num_2 = 10, 20

add_result = add(num_1, num_2)
subtract_result = subtract(num_1, num_2)

logger.debug(f'add: {num_1} + {num_2} = {add_result}')
logger.debug(f'subtract: {num_1} - {num_2} = {subtract_result}')

x, y = 1, 0
div_num = divide(x, y)