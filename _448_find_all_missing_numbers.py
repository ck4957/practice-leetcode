'''
Topic: Array
Difficulty: Easy

Find all missing numbers in a given array of integers.

Time Complexity: O(n)
Space Complexity: O(n)

Worst Case: If all numbers are present, we still need to create the full set.

Pseudo code:

1. Initialize a set to keep track of all numbers in the array.
2. Loop through the array and add each number to the set.
3. Initialize a list to store missing numbers.
4. Loop through the range from 1 to n (inclusive):
   a. If a number is not in the set, add it to the missing numbers list.
5. Return the list of missing numbers.

'''
def find_missing_numbers(nums):
    n = len(nums)
    all_numbers = set(range(1, n + 1))
    present_numbers = set(nums)
    missing_numbers = all_numbers - present_numbers
    return list(missing_numbers)