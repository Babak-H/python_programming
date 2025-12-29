import os.path


def check_path(file_path, data_files):
    '''
    Arguments:
        file_path(str): The file path to the JSON, or folder.
        data_files(list): A list to store the valid file paths, initially set to empty list.

    Return:
        int: An integer of 1 if the path given does not exist, or an int of 2 if the file path is a formatted JSON file or 3 if the given path is a json object and not directory
        tuple: A tuple of the valid file paths that can be parsed.

    checks to see if a directory exists, if not shows message and sends error code. 
    if given path is a directory, goes through it recursively and adds all files with .json format and returns them back via a tuple
    '''
    if not os.path.exists(file_path):
        print(file_path + " does not exist.")
        return 1
    elif os.path.isdir(file_path):
        for file in os.listdir(file_path):
            # The line below features calling the function within itself, which is refereed to
            # as 'recursion'. Recursion is needed here to meet the requirement : "to check the
            # contents of any nested folders".   
            if os.path.isdir(os.path.join(file_path, file)):    
                check_path(os.path.join(file_path, file), data_files)
            # do Not reformat already formatted files
            elif file.endswith(".json") and "_formatted.json" not in file:
                data_files.append(os.path.join(file_path, file))
    elif not os.path.isdir(file_path):
        return 2
    
    return tuple(data_files)


def get_usr_input(msg: str) :
    '''
    Arguments:
         msg(str): The message to prompt the user.
    Returns:
        str - the user's input
        
    prompts the user with a given message to get their input, uses .strip and .normpath to escape the address for windows os
    '''
    user_input = input(msg).strip()  
    safe_addr = os.path.normpath(user_input)
    return safe_addr
