'''
#26: Remove Duplicates from Sorted Array

Difficulty:
Easy

Problem:
Given an integer array `nums` sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in `nums`.

Instructions:
- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially. The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.
'''

# Solution: 
def remove_duplicates(nums):
    # Handle empty array
    if not nums:
        return 0
    
    # i keeps track of the position for the next unique element
    i = 0
    
    # j scans through the array
    for j in range(1, len(nums)):
        # If current element is different from the previous unique element
        if nums[j] != nums[i]:
            # Move i forward and update its value
            i += 1
            nums[i] = nums[j]
    
    # Return the length of the unique part (i + 1, because i is 0-indexed)
    return i + 1

# Example:
nums = [1, 1, 2, 2, 3, 4, 5, 5]

# Output: 5, nums = [1, 2, 3, 4, 5, ...]
k = remove_duplicates(nums)
print(f"k = {k}, nums[:k] = {nums[:k]}")

'''
Explanation:

1. Handle the case of an empty array.
2. Use two pointers:
   - `i`, which keeps track of the position where the next unique element should be placed.
   - `j`, which scans through the array looking for unique elements.
3. When `j` finds an element different from the current unique element at position `i`, we:
   - Increment `i` to move to the next position
   - Copy the unique element at position `j` to position `i`
4. Finally, we return `i + 1` as the length of the unique part of the array (since `i` is 0-indexed).

- The time complexity is O(n) where n is the length of the array, as we traverse the array once.
- The space complexity is O(1) as we modify the array in-place without using extra space proportional to the input size.
''' 