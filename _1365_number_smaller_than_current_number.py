'''
Find the number of elements smaller than the current element in an array.

Example:
Input: nums = [8, 1, 2, 2, 3]
Output: [4, 0, 1, 1, 2]

Time Complexity: O(n^2) - In the worst case, we compare each element with all others.
Space Complexity: O(1) - We are using a constant amount of space for the count variable.

Worst Case: If all elements are unique and in descending order, we need to compare each element with all others.
'''
def smaller_numbers_than_current(nums):
    result = []

    temp = nums.copy()
    temp.sort()
    
    d = {}
    for i, num in enumerate(temp):
        if num not in d:
            d[num] = i
    
    for i in nums:
        result.append(d[i])
        

    for i, num in enumerate(nums):
        for x in nums:
            if x < num:
                count+=1
        result.append(count)
    return result


'''
Time Complexity: O(n^2)
Space Complexity: O(1)
'''
def brute_force_smaller_numbers(nums):
    result = []
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count += 1
        result.append(count)
    return result