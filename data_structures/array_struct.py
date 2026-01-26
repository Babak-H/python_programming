# Python Array
# arrays are similar to python lists but all values have the same type

from array import array as arr

vals = arr('i', [5, -8, 9, 2, 10])
print(vals)
print(vals.buffer_info())  # info of the array   : (address, size)
print(vals.typecode)  # type of values in array


vals.append(11)
print(vals)

vals.remove(-8)
print(vals)

vals.reverse()
print(vals)

print(vals[0]

for e in vals:
    print(e)


# create new array from the old one
new_arr = arr(vals.typecode, (a*a for a in vals))
