'''
#9: Palindrome Number

Difficulty:
Easy

Problem:
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

Instructions:
- A palindrome is a number that reads the same forward and backward.
- For example, 121, 1331, and 12321 are palindromes.
'''

# Solution: 
def is_palindrome(x):
    # Check for a negative number
    if x < 0:
        return False
    
    # Convert number to a string and return if it equals its reverse
    x_str = str(x)
    return x_str == x_str[::-1]


# Example:
x = 121

# Output: True
print(is_palindrome(x))


'''
Explanation:

1. Check if the number is negative, since the negative sign will disqualify the number.
2. Convert the number to a string, and check if it in reverse equals itself.

- The time complexity is O(n) where n is the number of digits in the input number. 
- The space complexity is O(n) for storing the string representation / size of the number.
''' 