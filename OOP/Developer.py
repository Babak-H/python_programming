from Employee import Employee

# inheritance
# when you put argument after name of a class it means its another class that we want to inherit from
class Developer(Employee):

    # when you apply a parent method in child class, it doesnt affect instances of parent class
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer("Corey", "Schafer", 50000, "Python")
dev_2 = Developer("User", "Test", 60000, "Java")

print(dev_1.prog_lang)
print(dev_2.first)

print(dev_1.full_name())
#print(help(Developer))