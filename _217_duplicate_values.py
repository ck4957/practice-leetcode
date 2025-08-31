'''
Difficulty: Easy
Topic: Arrays

217. Contains Duplicate

Nested loop approach:

1. Iterate through each element in the array.
2. For each element, iterate through the remaining elements to check for duplicates.
3. If a duplicate is found, return True.
4. If no duplicates are found after checking all elements, return False.
Time Complexity: O(n^2)

Space Complexity: O(1)

Use a set to track seen elements:

1. Initialize an empty set.
2. Iterate through each element in the array.
3. If the element is already in the set, return True.
4. If not, add it to the set.
5. If no duplicates are found, return False.

Set is implemented as a hash table.
lookup/insert/delete operations are O(1) on average.

Time Complexity: O(n)

Space Complexity: O(n)

'''

def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

def contains_duplicate_2(nums):
    if len(set(nums)) < len(nums):
        return True    
    return False