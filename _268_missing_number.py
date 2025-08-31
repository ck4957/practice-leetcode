'''
Difficulty: Easy
Topic: Arrays

268. Missing Number

Input: An array of integers containing n distinct numbers taken from 0, 1, 2, ..., n.
Output: The missing number in the array.

Example:

Input: [3, 0, 1]
Output: 2

1. Calculate the expected sum of numbers from 0 to n.
2. Calculate the actual sum of numbers in the array.
3. The missing number is the difference between the expected sum and the actual sum.

Time Complexity: O(n)

Space Complexity: O(1)



'''

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

def missing_number_2(nums):
    nums.sort() # Sort the array: n log n

    for i, v in enumerate(nums):
        if i != v:
            return i

        if v == len(nums)-1:
            return v+1