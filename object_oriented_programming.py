"""
method => function that is associated with a class (difference between method and function)
attribute => variable that is associated with a class

when you create methods within class they receive the instance as "first argument" automatically, by convention we call
itself
"""
import datetime


class Employee:
    # class attributes
    raise_amount = 1.04
    num_of_emps = 0

# __init__(self) => is the constructor (initializer) for python classes, each time you create new instance it will run
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # this is class variable, won't be initialized via class instances (objects)
        Employee.num_of_emps += 1

    # you need to pass the "self" argument to the method to be able to access class properties inside it
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # this is a class method, cls is similar to self, but here we feed the actual class to this method
    # you can also use class methods from instances, but it is not recommended
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # here we use the class method as an alternative constructor, to make instances from string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)  # this is same as "Employee(first, last, pay)"

    # static method doesn't access instance (self) or the class (cls). it is used just to do some operation related
    # to this class
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)

print(emp_1)
print(emp_2)

# you can use both of these ways below
print(emp_1.fullname())
print(Employee.fullname(emp_1))
'''
Employee.raise_amount => this is a class variable, if we change it, it will change for all instances
self.raise_amount => this is a instance variable, it will only change it for this instance of class

python will first check if an instance variable exists, if not it will proceed to find class variable
'''
# this is same as "Employee.raise_amount = 1.05"
Employee.set_raise_amount(1.05)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.raise_amount)

# since raise_amount is class variable we can't see it in properties of instance
print(emp_1.__dict__)

print(Employee.num_of_emps)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steven-Smith-30000'

emp_3 = Employee.from_string(emp_str_1)
emp_4 = Employee.from_string(emp_str_2)
# using static method from class
my_date = datetime.date(2019, 7, 13)
print(Employee.is_workday(my_date))


# python Protected and Private methods
class Test:
    def __init__(self):
        self.foo = 11
        # variable with _ means it is better to be private _bar (similar to protected to c#), you still can access this
        # from instances
        self._bar = 23
        # variable with __ means it is actually private, can't be accessed from class instances nor can be accessed by
        # class itself from outside
        self.__baz = 42

     @staticmethod
    def show(self):
        print("1")

t = Test()
print(t._bar)
print(t.__baz)  # throws an error


# inheritance => when you put argument after name of a class it means its another class that we want to inherit from
class Developer(Employee):
    # when you apply a parent method/property in child class, it doesn't affect instances of parent class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


print(help(Developer))
dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("User", "Test", 60000, "Java")

print(dev_1.prog_lang)
print(dev_2.first)
print(Developer.raise_amount, Employee.raise_amount)


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp: Employee):
        if emp not in self.employees:
            self.employees.append(emp)

    def rmv_employee(self, emp: Employee):
        if emp in self.employees:
            self.employees.remove(emp)


mgr_1 = Manager("sue", "Smith", 90000, [dev_1])
print("name of manager : ", mgr_1.last)

mgr_1.add_employee(dev_2)
mgr_1.rmv_employee(dev_1)
print(mgr_1.employees)

# check if object is instance of class :
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))

# Magic / special Methods and overloading
class EmployeeX:
    # all these 3 methods are magic methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # here we are overloading the default str method of this class
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # here we are overloading the default str method of this class
    def __str__(self):
        return '{}-{}'.format(self.first, self.last)

    # this special method adds two objects together (returns their combined pay)
    def __add__(self, other):
        return self.pay + other.pay

emp_1 = EmployeeX("Corey", "Schafer", 50000)
emp_2 = Employee("User", "Test", 60000)
print(emp_1)  # when we print this object this is calling emp_1.__repr__(self)
print(repr(emp_1))  # same as above
print(emp_2)

# both do same operation
print(1 + 2)
print(int.__add__(1, 2))

print(len('test'))
print('test'.__len__())

print(emp_1 + emp_2)

# check if class inherits from another class:
print(issubclass(Developer, Employee))
print(issubclass(Developer, Manager))


# Getters, Setters, Deleters
class EmployeeY:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    # property decorators allow us to use the method like a property of the class | getter
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    # with setter decorator you can overload the method and use it to set properties of the instance
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    # with deleter decorator you can overload the method and use it to set properties of the instance
    @fullname.deleter
    def fullname(self):
        print("Delete!")
        self.first = None
        self.last = None


emp_1 = EmployeeY('John', 'Smith', 40000)

print(emp_1.fullname)  # getter
print(emp_1.email)  # getter

emp_1.fullname = "Corey Schaefer"  # setter
print(emp_1.first)

del emp_1.fullname  # deleter
print(emp_1.first)

'''
whenever python runs a file, it first sets a few special variables, and one of those variables is __name__ and it
sets it to __main__, but if we import this module (file) in other file, it will be different.
therefore, we can use this idea to check if we are running it directly or running it by importing in another module
'''
print(__name__)

def main():
    print("running directly")

if __name__ == "__main__":
    main()
else:
    print("running from import")

# Are multiple classes in a single file recommended?
'''
Python is not exclusively class-based - the natural unit of code decomposition in Python is the module. Modules are just
as likely to contain functions (which are first-class objects in Python) as classes. In Java, the unit of decomposition 
is the class. Hence, Python has one module=one file, and Java has one (public) class=one file.

Python is much more expressive than Java, and if you restrict yourself to one class per file (which Python does not 
prevent you from doing) you will end up with lots of very small files - more to keep track of with very little benefit.
even more important is that in Python, you don't use classes for every- thing; if you need factories, singletons, 
multiple ways to create objects, polymorphic helpers, etc, you use plain functions, not classes or static methods.

once you've gotten over the "it's all classes", use modules to organize things in a way that makes sense to the code 
that uses your components. make the import statements look good.
'''
