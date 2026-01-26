# Stack

'''
Stack Data structure
A B C D

we stack all our items on top of each other:
D
C
B
A

if you want to acess item A then you need to take all items D, C, B before accessing A.
* when you add value to stack you "push" it on top of stack
* when you take an element from stack you "pop" it from stack
* we build our stack class based on built-in python lists
'''


class Stack():

    def __init__(self):
        self.items = []

    def push(self, item):  # adds element at top of stack
        self.items.append(item)

    def pop(self):  # gets element from top of stack
        return self.items.pop()

    def get_stack(self):
        return self.items

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]  # -1 returns the last item in the list


s = Stack()
s.push("A")
s.push("B")
print(s.get_stack())

s.push("C")
print(s.get_stack())
s.pop()
print(s.get_stack())

print(s.is_empty())

s.push("D")
print(s.peek())


"""
Use a stack to check whether or not a string has balanced usage of parenthesis.
Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.
Balanced Example: {[]}
Non-Balanced Example: (()
Non-Balanced Example: ))
"""

# from stack import Stack

def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 =="}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

# the idea here is that first we push all left side parenthesis to the stack then when we get a right one, we pop latest
# element of stack and see if it matches the right side one, until we make the stack empty.

def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0
    
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "({[":
            s.push(paren)
        else:
            if s.is_empty(): # this means the string starts we right side prantacies, therefore its unbalanced
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    
        index += 1
    
    if s.is_empty() and is_balanced:
        return True
    else:
        return False
    
print(is_paren_balanced("(({[]}))"))
print(is_paren_balanced("[][]]]"))


'''
Convert integer value to binary using stack data structure

Example : 242
binary representation of 242 :
242 % 2 = 0
121 % 2 = 1
60 % 2 = 0
30 % 2 = 0
15 % 2 = 1
7 % 2 = 1
3 % 2 = 1
1 % 2 = 1
'''
# stack is a good choice here, since first item added to the stack, will be last one coming out
def div_by_2(num):
    s = Stack()
    
    while num > 0:
        r = num % 2
        s.push(r)
        num = num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num += str(s.pop())
        
    return bin_num


print(div_by_2(242))
print(int(div_by_2(242), 2))