'''
String processing, Spreadsheet encoding
A -> 1
B -> 2
C -> 3
Z -> 26
AA -> 27
AB -> 28
implementing a function that converts a spreadsheet column ID (i.e. "A", "B", "C", ..., "Z", "AA", etc.) 
to the corresponding integer.

Basically here we want to have numbers with base of 26

314 = 3 X 100 + 1 X 10 + 4 X 1
314 = 3 X 10^2 + 1 x 10^1 + 4 X 10^0

A = 1
D = 4

AA = 1 X 26^1 + 1X26^0
ZC = 26 X 26^1 + 3X26^0

AAA = 1 X 26^2 + 1 X 26^1 + 1 X 26^0
'''

# ord() function : A = 65 | Z = 90
# A -> ord('A') - ord('A') + 1
# Z -> ord('Z) - ord('A') + 1

# print(ord('A'))  65
# print(ord('C'))  67
# print(ord('Z'))  90


def char_to_num(s):
    num = 0
    count = len(s) - 1
    for n in s:
        num += 26**count * (ord(n) - ord('A') + 1 )
        count -= 1
    return num
        
print(char_to_num("A"))
print(char_to_num("AA"))
print(char_to_num("ZC"))