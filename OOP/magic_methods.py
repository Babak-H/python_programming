# Magic /special Methods and overloading

class EmployeeX:

    # all these 3 methods are magic methods
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    def __repr__(self):
        return f'Employee({self.first} {self.last} {self.pay})'.format()
    
    def __str__(self):
        return f'{self.first}--{self.last}'.format()

    # this special method adds two objects together (returns their combined pay)
    def __add__(self, other):
        return self.pay + other.pay


emp_1 = EmployeeX("Corey", "Schafer", 50000)
emp_2 = EmployeeX("User", "Test", 60000)

print(emp_1) # when we print this object this is calling emp_1.__str__(self)
print(repr(emp_1))


# most python classes have some built-in special methods
print(1+2)
print(int.__add__(1,2))

print(len('test'))
print('test'.__len__())

print(emp_1 + emp_2)   # calls __add__ on emp_1, this is called method overloading