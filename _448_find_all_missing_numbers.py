'''
Topic: Array
Difficulty: Easy

Find all missing numbers in a given array of integers.

Time Complexity: O(n)
Space Complexity: O(n)

Worst Case: If all numbers are present, we still need to create the full set.
'''
def find_missing_numbers(nums):
    n = len(nums)
    all_numbers = set(range(1, n + 1))
    present_numbers = set(nums)
    missing_numbers = all_numbers - present_numbers
    return list(missing_numbers)