'''
#1: Two Sum

Difficulty:
Easy

Problem:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Instructions:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- *Only one valid answer exists.
'''

# Solution: 
def two_sum(nums, target):
    # To store number and index mappings
    num_map = {}
    
    for i, num in enumerate(nums):
        # Find complement needed to reach the target
        comp = target - num
        
        # If complement exists already in the map, return its and the current index
        if comp in num_map:
            return [num_map[comp], i]
        
        # Otherwise, add current number and index to the map
        num_map[num] = i
    
    return []


# Example 1:
nums1 = [2, 7, 11, 15]
target1 = 9

# Output: [0, 1]
print(two_sum(nums1, target1))


# Example 2:
nums2 = [3, 2, 4]
target2 = 6

# Output: [1, 2]
print(two_sum(nums2, target2))


# Example 3:
nums3 = [3, 3]
target3 = 6

# Output: [0, 1]
print(two_sum(nums3, target3))


'''
Explanation:

1. Create a hash map to store each number and its index as we iterate through the array.
2. For each number, calculate its complement (target - current number).
3. Check if the complement already exists in the hash map.
4. If it does, we've found our pair and can return their indices.
5. If not, add the current number and its index to the hash map and continue.

- The time complexity is O(n) where n is the length of the array, since it is a single pass through the array. 
- The space complexity is O(n) incase all elements need to be stored in the map.
'''