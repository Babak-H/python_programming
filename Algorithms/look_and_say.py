
"""
look and say sequence
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

to generate a memeber of the sequence from the previous memeber, read off the digits of the previous memeber,
counting the number of digits in groups of the same digit. for example:

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
1211 is read off as "one 1, one 2, then two 1s" or 111221.
111221 is read off as "three 1s, two 2s, then one 1" or 312211.

we will define the look-and-say sequence and also determine a way to generate the Nth element 
in the sequence
"""
# ================================
# find Nth element on the look and say sequence

# 1211


def next_numbers(s):
    result = []
    i = 0
    while i < len(s):  # loop thorogh until we reach last number:
        count = 1
        # loop through untul the number isn't being repeated anymore
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count += 1

        result.append(str(count) + s[i])
        i += 1  # move to next charcter after repetition

    return ''.join(result)


n = 4
s = "1"
for i in range(n):
    # s is same for both argument and variable, so next time that we use it, argument will be result of the previous operation
    s = next_numbers(s)  
    print(s)
