'''
Topic: Array
Difficulty: Easy

Find two numbers in an array that add up to a specific target.

Time Complexity: O(n)
Space Complexity: O(n)

Example:
Input: numbers = [2, 7, 11, 15], target = 9
Output: (0, 1)

Worst Case: If no solution exists, we still need to check all elements.

Pseudo code:

1. Initialize an empty dictionary (num_dict) to store numbers and their indices.
2. Loop through the array with index:
   a. For each number, calculate its complement (target - num).
   b. Check if the complement exists in num_dict:
      i. If it exists, return the pair of indices (num_dict[complement], current_index).
   c. If it doesn't exist, add the current number and its index to num_dict.
3. If no pair is found, return None.

'''
def two_sum(numbers, target):
    num_dict = {} # Dictionary to store numbers and their indices
    for i, num in enumerate(numbers):
        # Calculate complement - the number needed to reach the target
        complement = target - num
        if complement in num_dict:
            return (num_dict[complement], i)
        num_dict[num] = i
    return None


 '''
 Brute Force Approach

 Time Complexity: O(n^2)
 Space Complexity: O(1)
'''
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None