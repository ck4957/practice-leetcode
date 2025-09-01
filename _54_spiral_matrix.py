'''
Topic: Array
Difficulty: Medium
Given an m x n matrix, return all elements of the matrix in spiral order.
Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
Time Complexity: O(m*n), where m is the number of rows and n is the number of columns in the matrix.
Space Complexity: O(1), as we are using a constant amount of space.
'''


'''
matrix = [
    [1,2,3,4], 
    [5,6,7,8],  
    [9,10,11,12]
]

-> first row of matrix
    matrix.pop(0) -> [1, 2, 3, 4]
    Leftovers: [[5, 6, 7, 8], [9, 10, 11, 12]]
-> last element of each remaining row
    for row in matrix:
        if row:
            row.pop() -> [8, 12]
            Leftovers: [[5, 6, 7], [9, 10, 11]]
-> last row in reverse order
    matrix.pop()[::-1] -> [11, 10, 9]
    Leftovers: [[5, 6, 7]]
-> first element of each remaining row in reverse order
    for row in matrix[::-1]:
        if row:
            row.pop(0) -> [5, 6, 7]
'''

def spiral_order_v2(matrix):
    
    res = []

    while matrix:
        # Take the first row/list of matrix
        res += matrix.pop(0)
        
        # Take the last element of each remaining row
        for row in matrix:
            if row:
                res.append(row.pop())
                
        # Take the last row in reverse order
        if matrix:
            res += matrix.pop()[::-1]
        # Take the first element of each remaining row in reverse order
        for row in matrix[::-1]:
            if row:
                res.append(row.pop(0))
    return res