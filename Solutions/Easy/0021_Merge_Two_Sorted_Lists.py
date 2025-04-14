'''
#21: Merge Two Sorted Lists

Difficulty:
Easy

Problem:
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Instructions:
- Both l1 and l2 are sorted in non-decreasing order.
- The returned list should also be sorted in non-decreasing order.
'''

# Solution: 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(l1, l2):
    # Create a dummy head node to simplify start
    dummy = ListNode(0)
    current = dummy
    
    # Traverse both lists and compare values
    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    # Attach remaining nodes from either list
    current.next = l1 if l1 else l2
    
    # Return the merged list (excluding the dummy head)
    return dummy.next

# Functions for testing
def list_to_linked_list(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


# Example:
l1 = list_to_linked_list([1, 2, 4])
l2 = list_to_linked_list([1, 3, 4])

# Output: [1, 1, 2, 3, 4, 4]
result = merge_two_lists(l1, l2)
print(linked_list_to_list(result))


'''
Explanation:

1. We create a dummy head node to simplify edge cases and to have a starting point for our result list.
2. We maintain a current pointer to keep track of our position while building the merged list.
3. We iterate through both lists simultaneously, comparing the values of the current nodes:
   - If l1's value is less than or equal to l2's value, we append l1's node to our result list and advance l1.
   - Otherwise, we append l2's node to our result list and advance l2.
4. Once we exhaust one of the lists, we append the remainder of the other list (which is already sorted).
5. Finally, we return the merged list, skipping the dummy head node.

- The time complexity is O(n + m) where n and m are the lengths of the input lists, as we need to visit each node exactly once.
- The space complexity is O(1) since we only rearrange the existing nodes without allocating new ones (except for the dummy head node).
''' 