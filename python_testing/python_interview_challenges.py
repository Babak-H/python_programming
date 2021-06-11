import string


'''
implement an algorithm to determine if a string has all unique characters
'''
s1 = 'unique'
s2 = 'bear'


def is_unique(s):
    return len(s) == len(set(s))


print(is_unique(s1))
print(is_unique(s2))

'''
given two string, write a function to decide if one is a permutation of the other

"driving"
"drivign" -> valid
"ddriving" -> not valid
'''

str_1 = "the cow jumps over the moon"
str_2 = "the mo on jumps over the cow"


def is_perm(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False
    if sorted(str1) == sorted(str2):
        return True


print("permutation", is_perm(str_1, str_2))

'''
check if an string is a palindrome (read same from both start and end)

racecar
'''


def is_palindrome(s):
    s = s.replace(" ", "").lower()
    s = s.translate(str.maketrans('', '', string.punctuation))

    if s == s[::-1]:
        return True
    else:
        return False


print(is_palindrome("racecar"))
print(is_palindrome("computer"))
print(is_palindrome("Dammit I'm mad"))

'''
given an array of integers, return indices of the two numbers such that they add up to specific target.
cant use one number twice

nums = [1, 3, 11, 2, 7]
target = 9

9 - 1 = 8 -> {8:0}
9 - 3 = 6 -> {8:0, 6:1}
9 - 11 = -2 -> {8:0, 6:1, -2:11}
'''

nums = [1, 5, 11, 2, 7]
target = 7


def two_sums(nums, target):
    if len(nums) <= 1:
        return False

    aux_dict = {}
    for i in range(len(nums)):
        if nums[i] in aux_dict.keys():
            return nums[i], nums[aux_dict[nums[i]]]
        else:
            aux_dict[target - nums[i]] = i


print(two_sums(nums, target))


"""
Given an array of integers, every element appears twice except for one.
Find that single one.
Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?
Example :
Input : [1, 2, 2, 3, 1]
Output : 3
"""

def find_singular(num_list):
    ans=0
    for i in range(len(num_list)):
        ans ^= num_list[i]   # 1^2^2^3^1   XOR model : 0^1 = 1 and 0^0 = 0 => 1^1 = 0, 0^2 = 2, 2^2 = 0, 0^3 = 3
    return ans

print(find_singular([1, 2, 2, 3, 1]))


"""
Write a iterative and recursive function that implements the factorial
of a number.
n! = n * n - 1 * ... * 1

5! = 5 * 4 * 3 * 2 * 1 = 120
"""

def factorial_iter(n):
    x = 1
    for i in range(n, 0, -1):
        x = x*i
    return x
    
print(factorial_iter(5))

def fact_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recursive(n-1)

print(fact_recursive(5))


"""
URLify: Write a method to replace all spaces in a string with '%20'. You may
assume that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.
"""

def URLify(s):
    return s.replace(" ", '%20')

# without builtin function:
def URLify_custom(s):
    input_len = len(s)
    url = ""

    for i in range(input_len):
        if s[i] == " ":
            url += "%20"
        else:
            url += s[i]
    return url

print(URLify("hello world"))
print(URLify_custom("hello world"))


"""
Anagram:
Given two strings, check whether two given strings are anagram of each other or not. 
An anagram of a string is another string that contains same characters, only the order 
of characters can be different. For example, “act” and “tac” are anagram of each other.
"""

input_str_1 = "practice makes perfect"
input_str_2 = "perfect makes practice"

input_str_3 = "allergy"
input_str_4 = "allergic"

def angram(s_1, s_2):
    if sorted(s_1.replace(" ", "").lower()) == sorted(s_2.replace(" ", "").lower()):
        return True
    else:
        return False

print(angram(input_str_1 ,input_str_2))
print(angram(input_str_3 ,input_str_4))


# another solution with less complexity, using hashtable
def angram_hash(s_1, s_2):
    s_1 = s_1.replace(" ", "").lower()
    s_2 = s_2.replace(" ", "").lower()

    if len(s_1) == len(s_2): 
        alphabet = "abcdefghijklmnopqrstuvwxyz"
                                # keys         # values
        dict_1 = dict.fromkeys(list(alphabet), 0)
        dict_2 = dict.fromkeys(list(alphabet), 0)

        for i in range(len(s_1)):
            dict_1[s_1[i]] += 1
            dict_2[s_2[i]] += 1

        return dict_1 == dict_2
    else:
        return False

print(angram_hash(input_str_1 ,input_str_2))
print(angram_hash(input_str_3 ,input_str_4))


"""
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix.
Assume N*M is odd.
For example,
Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]
A = [1, 2, 3, 3, 5, 6, 6, 9, 9]
Median is 5. So, we return 5.
"""
mat = [[1, 3, 5],
      [2, 6, 9],
      [3, 6, 9]]

def return_median(mat):
    l = sorted([i for row in mat for i in row])
    return l[len(l) // 2]

print(return_median(mat))


"""
String Compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa
would become a2b1c5a3. If the"compressed" string would not become smaller than
the original string, your method should return the original string. You can
assume the string has only uppercase and lowercase letters (a-z).
"""

input_str_test_1 = "aabcccccaaa"
input_str_test_2 = "aaaaaabbccbcaabb"

def string_compression(s):
    if len(s) == len(set(s)):
        return s
    else:
        num = 1
        final = ""
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                num += 1
            else:
                final += s[i]+str(num)
                num=1

        final += s[i]+str(num)
        return final

print(string_compression("aabcccccaaa"))
print(string_compression("aaaaaabbccbcaabb"))


'''
String Rotation: Given two strings, s1 and s2, write code to check if s2 is
a rotation of s1 (e.g. "waterbottle" is a rotation of "erbottlewat")
'''
test_rot_str_1 = "waterbottle"
test_rot_str_2 = "erbottlewat"

test_rot_str_3 = "watertables"
test_rot_str_4 = "erbottlewat"

def check_rotation(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

print(check_rotation(test_rot_str_1, test_rot_str_2))
print(check_rotation(test_rot_str_3, test_rot_str_4))



