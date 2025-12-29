# worker tasks and time problem

A = [6, 3, 2, 7, 5, 5]

A = sorted(A)
print(A)

# here we need to loop through half of length since we pair each 2 numbers from out to middle
for i in range(len(A)//2):
    print(A[i], A[~i])

'''
~0 = -1 : last one
~1 = -2 : one to last
~3 = -3 : two to the last element
'''