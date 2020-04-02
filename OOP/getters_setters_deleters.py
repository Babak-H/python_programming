# getters, setters, deleters

class EmployeeY:

    def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
    
    # property decorators allow us to use the method like a propery of the class
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
    

    # with deleter decorator you can overload the method and use to delete properties of the instance
    @fullname.deleter
    def fullname(self):
        print("Delete!")
        self.first = None
        self.last = None

emp_1 = EmployeeY('John', 'Smith', 40000)

print(emp_1.fullname)
print(emp_1.first)

emp_1.fullname = "Corey Schefer"
print(emp_1.first)

del emp_1.fullname
print(emp_1.first)



