'''
#13: Roman to Integer

Difficulty:
Easy

Problem:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

```
Symbol       Value
I            1
V            5
X            10
L            50
C            100
D            500
M            1000
```

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:
- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Instructions:
- 1 <= s.length <= 15
- s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
- It is guaranteed that s is a valid roman numeral in the range [1, 3999].
'''

# Solution:
def RomanToInteger(s):
    # Need a mapping of Roman numerals to their values to start
    values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    # Iterate through from right to left
    for char in reversed(s):
        current_value = values[char]
        
        # If current value is greater than or equal to previous value, add it to total
        if current_value >= prev_value:
            total += current_value
        # Else, subtract it (will handle the six instances mentioned above)
        else:
            total -= current_value
        
        prev_value = current_value
    
    return total


# Example 1:
s1 = "III"

# Output: 3 (3 ones)
print(RomanToInteger(s1))


# Example 2:
s2 = "LVIII"

# Output: 58 (L = 50, V = 5, III = 3)
print(RomanToInteger(s2))


# Example 3:
s3 = "MCMXCIV"

# Output: 1994 (M = 1000, CM = 900, XC = 90, IV = 4)
print(RomanToInteger(s3))


'''
Explanation:

1. Create a mapping of symbols to values.
2. Start a total sum and a variable to track the previous value.
3. Iterate through the string from right to left (reverse):
   - If the current value is greater than or equal to the previous value, add it to the total.
   - Otherwise, subtract it from the total.
   - Update the previous value with the current iteration value.
4. Return the final total.

- The time complexity is O(n) where n is the length of the string.
- The space complexity is O(1) since the mapping and variables are constant.
''' 