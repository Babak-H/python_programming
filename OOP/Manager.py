from Employee import Employee
from Developer import *

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


manager_1 = Manager("sue", "Smith", 90000, [dev_1])
print("name of manager: ", manager_1.full_name())

manager_1.add_employee(dev_2)
manager_1.remove_employee(dev_1)
print(manager_1.employees)

# checl if object is instance of class:
print(isinstance(manager_1, Manager))
print(isinstance(manager_1, Employee))

# check if class inherits from another class:
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))