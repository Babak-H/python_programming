# python protected and private methods

class Test:
    def __init__(self):
        self.foo = 11
        # variable with _ means it is better to be private _bar (similar to protected to c#), 
        # you still can access this from instances
        self._bar = 23

        # variable with __ means it is actually private, cant be accessed from class instances 
        # nor can be accessed by class itself from outside
        self.__baz = 42

    def show(self):
            print("1")

t = Test()
t.show()
print(t._bar)  # can be accessed, but isn't visible from autocomplete
print(t.__baz)  # can't be accessed, returns error