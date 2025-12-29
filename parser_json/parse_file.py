import json
import re
import math
import os

def get_json_content(file):
    '''
    Arguments:
        file(str): the path to the json file to get its content
    Return: 
        the content of the file passed into the function, a list of dictionaries
    
    reads the json file and returns a list of dictionaries, where each dict is a person's info    
    '''
    with open(file, "r") as f:
        data = json.load(f)
    return data
   

def validate_phone_number(phone_number):
    '''
    Arguments:
        phone_number(str): the phone number of the employee
    Return: 
        int, if phone number is invalid return 1, if valid the 10 digit phone number
    
    makes sure the phone number that was given is valid  
    '''
    phone_number = phone_number.strip()
    pattern= r"\d{10}"
    if re.fullmatch(pattern, phone_number):
        return phone_number
    else:
        print(f"{phone_number} is not a valid US phone number, skipping this employee entry...")
        return 1


def validate_zip(zip_code):
    '''
    Arguments:
        zip_code(str): the zip_code of the employee
    Return: 
        int, if zip_code is invalid return 1, if valid the 5 digit phone number
    
    makes sure the zip_code that was given is valid  
    '''    
    zip_code = zip_code.strip()
    pattern = r"\d{5}"
    if re.fullmatch(pattern, zip_code):
        return zip_code
    else:
        print(f"{zip_code} is not a valid US zip_code, skipping this employee entry...")
        return 1
    

def generate_email(first_name, last_name):
    '''
    Arguments:
        first_name(str): The employees first name.
        last_name(str): The employees last.
    Return:
        str: The company email in the format of <first letter of the first name><full last name>@comp.com all in lower case.
        
    Generate the email address for the employee entry to follow the format detailed above. 
    '''   
    return f"{first_name.strip().lower()}{last_name.strip().lower()}@comp.com"


def generate_salary(job_id, state):
    '''
    Arguments:
        job_id(str): job_id of the employee, 
        state(str): the US state the employee is located at
    Return:
        int: calculated salary of the employee
        
    Generate the email address for the employee entry to follow the format detailed above. 
    '''
    salary = 0
    special_states = ['NY', 'CA', 'OR', 'WA', 'VT']
    if job_id.startswith("SA"):
        salary = 60000
    elif job_id.startswith("HR"):
        salary = 70000
    elif job_id.startswith("IT"):
        salary = 80000
    if job_id.endswith("MNG"):
        salary += salary * 0.05
    if state in special_states:
        salary += salary * 0.015
        
    return int(math.ceil(salary))


def process_each_emp(emp_list):
    '''
    Arguments:
        emp_list(list): list of employees extracted from json file
    Return:
        list: a list of dictionaries where each dict is a employee's info
        
    process each employee's info and format it to our desired style.
    '''
    emp_list_formatted = []
    for emp in emp_list:
        emp_formatted = {}
        phone_num = validate_phone_number(emp["Phone Number"])
        zip_code = validate_zip(emp["Zip Code"])
        if phone_num == 1 or zip_code == 1:
            continue
        
        emp_formatted["Phone Number"] = phone_num
        emp_formatted["Zip Code"] = zip_code
        emp_formatted["Company Email"] = generate_email(emp["First Name"], emp["Last Name"])
        emp_formatted["Salary"] = generate_salary(emp["Job ID"], emp["State"])
        
        for k,v in emp.items():
            if k in ["First Name", "Last Name", "Address Line 1", "Address Line 2", "City", "Job Title"]:
                v = v.strip().lower().capitalize()
                emp_formatted[k] = v
            elif k in ["Date Of Birth (mm/dd/yyyy)", "State", "Job Title", "Job ID"]:
                emp_formatted[k] = v
                
        emp_list_formatted.append(emp_formatted)
    return emp_list_formatted
 
def generate_formatted_file(emp_list, orig_path):
    '''
    Arguments:
        emp_list(list): A list of dictionaries where each dictionary is the employee entry after being formatted
        orig_path(str): The file path of the original file that was passed in.
    Return: None

    create a new file based on the original file with formatted content and save it with "_formatted.json" ending, 
    uses indent=2 to make the new file human-readable
    '''  
    dir = os.path.dirname(orig_path) 
    name = os.path.splitext(os.path.basename(orig_path))[0]
    filename = name+"_formatted.json"
    full_address = os.path.join(dir, filename)
    with open(full_address, "w", encoding="utf-8") as f:
        json.dump(emp_list, f, indent=2)
