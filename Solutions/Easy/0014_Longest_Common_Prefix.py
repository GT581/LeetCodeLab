'''
#14: Longest Common Prefix

Difficulty:
Easy

Problem:
Write a function to find the longest common prefix string amongst an array of strings.

Instructions:
- If there is no common prefix, return an empty string "".
- All given inputs are in lowercase letters a-z.
'''

# Solution: 
def longest_common_prefix(strings):
    # If an empty list, return an empty string
    if not strings:
        return ""
    
    # Find the shortest string to limit comparisons
    shortest_str = min(strings, key=len)
    
    # Iterate through characters of the shortest string
    for i, char in enumerate(shortest_str):
        # Check if the character at position i is the same for all strings
        for other_str in strings:
            if other_str[i] != char:
                # If not, return the prefix found so far
                return shortest_str[:i]
    
    # If we go through the entire shortest string, that is the prefix
    return shortest_str

# Example:
strings = ["flower", "flow", "flight"]

# Output: "fl"
print(longest_common_prefix(strings))

'''
Explanation:

1. Handle the edge case where the input list is empty.
2. Find the shortest string in the list to limit comparisons (the common prefix can't be longer than the shortest string).
3. For each character in the shortest string, check if that character appears in the same position across all strings.
4. If we find a mismatch, return the common prefix found so far.
5. If we make it through the whole shortest string without finding a mismatch, the shortest string itself is the common prefix.

- The time complexity is O(S) where S is the sum of all characters in all strings.
- The space complexity is O(1) as we only use a constant amount of extra space.
''' 