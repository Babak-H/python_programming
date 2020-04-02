# Object Oriented Programming OOP

'''
method : function that is associated with a class
attribute : variable that is associated with a class

when you create methods within class they recieve the instance as first argument automatically, 
by convention we call it "self"
'''

class Employee:
    # class properties
    raise_amount = 1.04
    num_of_emp = 0

    # __init__(self)" is the constructor (initializer) for python classes, each time you create new instance 
    # it will run
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_emp += 1


    # you need to pass the "self" argument to the method to be able to access class properties inside it
    def full_name(self):
        return f'{self.first} {self.last}'.format()
    

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)


    # this is a class method, cls is similar to self, but here we feed the actual class to this method
    # you can also use class methods from instances, but it is not reccomended
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    # here we use the class method as an alternative constructor, to make instances from string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) # this is same as "Employee(first, last, pay)"
    

    # static method doesnt acces instance (self) or the class (cls). it is used just to do some 
    # operation related to this class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)

# returns object of the class
print(emp_1)  # <__main__.Employee object at 0x10712bd30>
print(emp_2)

# you can use both of these ways below
print(emp_1.full_name())
print(Employee.full_name(emp_1))

# ================================
'''
Employee.raise_amount : this is a "class variable", if we change it, it will change for all instances

self.raise_amount : this is a "instance variable", it will only change it for this instance of class
    
python will first check if an instance variable exists, if not it will proceed to find class variable
'''

Employee.set_raise_amount(1.05)
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.raise_amount)

# since raise_amount is class variable we can't see it in properties of instance
print(emp_1.__dict__)
print(Employee.num_of_emp)

# ================================
import datetime

emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steven-Smith-30000"

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)

my_date = datetime.date(2019, 7, 13)
print(Employee.is_workday(my_date))


    





    
