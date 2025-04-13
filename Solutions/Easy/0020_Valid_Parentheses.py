'''
#20: Valid Parentheses

Difficulty:
Easy

Problem:
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

Instructions:
- An input string is valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.
'''

# Solution: 
def is_valid_paren(s):
    # Create a mapping of closing brackets to their opening counterparts
    brackets_map = {')': '(', '}': '{', ']': '['}
    
    # Start an empty stack to keep track of opening brackets
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If the character is a closing bracket
        if char in brackets_map:
            # Pop the top element from the stack, or use a dummy value if stack is empty
            top_element = stack.pop() if stack else '#'
            
            # If the popped element doesn't match the corresponding opening bracket, return False
            if brackets_map[char] != top_element:
                return False
        # If the character is an opening bracket, push it onto the stack
        else:
            stack.append(char)
    
    # If the stack is empty, all brackets were properly closed
    return len(stack) == 0

# Example:
s = "()[]{}"

# Output: True
print(is_valid_paren(s))

'''
Explanation:

1. We create a dictionary mapping each closing bracket to its corresponding opening bracket.
2. We iterate through each character in the string.
3. If the character is a closing bracket:
   - We try to pop the top element from the stack.
   - If the stack is empty or the popped element doesn't match the expected opening bracket, then the string is invalid.
4. If the character is an opening bracket, we push it onto the stack.
5. After processing all characters, the string is valid if and only if the stack is empty (all opening brackets have been matched with closing brackets).

- The time complexity is O(n) where n is the length of the string.
- The space complexity is O(n) in the worst case (ex: an input of all opening brackets).
''' 