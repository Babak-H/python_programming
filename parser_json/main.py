import usr_input
import parse_file
import sys


def error_handle(check_return):
    '''
    Arguments:
        check_return(str): the return value of check_path function
    Returns:
        None
        
    will exit program if value given to it is 0 or 1 (file not eixsting or already processed), if tuple is empty it will show an error message
    '''
    if isinstance(check_return, tuple):
        if len(check_return) == 0:
            print("There are no valid files to process in the folder provided.")
            sys.exit(1)   
    elif check_return == 1:
        sys.exit(1)
    elif check_return == 2:
        print("the address provided is a file, we can only accept a directory")
        sys.exit(1)
    
    
def main():
    '''
    Arguments: None
    Returns: None
    
    invokes the code necessary to run the program as intended
    '''
    given_path = usr_input.get_usr_input("Please enter the path of the the folder containing the files: ")
    tup = usr_input.check_path(given_path, [])
    error_handle(tup)
    start_process(tup)
  
  
def start_process(tup):
    '''
    Arguments:
        tup(Tuple): Tuple of valid JSON pathes generated from check_path
    Returns: None

    calculate number of file and employees processed, process each file and save it in new JSON-formatted file, call print_output function
    '''
    num_files = 0
    for f in tup:
        emp_l = parse_file.get_json_content(f)
        emp_l_formatted = parse_file.process_each_emp(emp_l)
        parse_file.generate_formatted_file(emp_l_formatted, f)
        num_files += len(emp_l_formatted)
    print_output(len(tup), num_files)




def print_output(num_files, num_emps):
    '''
    Arguments:
        num_files(int): The number of valid files that were processed.
        num_emps(int): The number of valid employee entries that were processed.
    Return: None.
    
    Display the number of files and employees processed in the format seen below
    '''
    print(f"""
          ============================================================ 
          ---------------------Processing Summary--------------------- 
          ============================================================ 
          Number of files processed: {num_files}
          Number of employee entries 
            formatted and calculated: {num_emps}
          """)


if __name__ == "__main__":
    main()