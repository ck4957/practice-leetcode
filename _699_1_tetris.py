'''
You are given a 2d matrix which consist of the following symbols 
".", "#", "*", where 
"." represent free cell, 
"#" represent a obstacle,
"*" denotes shape. 
Your task is to find out the minimum obstacle to remove from the matrix 
so that the shapes falls down to the bottom.

Test Case:

[["*", "*", "*", "*"],
["#", "*", ".", "*"],
[".", ".", "#", "."],
[".", "#", ".", "#"] ]

Output = 4

Simulation:

Initial matrix:

[["*", "*", "*", "*"],
["#", "*", ".", "*"],
[".", ".", "#", "."],
[".", "#", ".", "#"] ]

After removing matrix[1][0]

[[".", ".", ".", "."],
["*", "*", "*", "*"],
[".", "*", "#", "*"],
[".", "#", ".", "#"] ]

After removing matrix[2][2], matrix[3][1], matrix[3][3], we get

[[".", ".", ".", "."],
[".", ".", ".", "."],
["*", "*", "*", "*"],
[".", "*", ".", "*"] ]

which will give us the output 4
'''

def min_obstacles(matrix):
    if not matrix or not matrix[0]:
        return 0
    R = len(matrix)
    C = len(matrix[0])
    count = 0
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == '#':
                # check if there is * above in the same column
                has_star_above = False
                for k in range(i):
                    if matrix[k][j] == '*':
                        has_star_above = True
                        break
                if has_star_above:
                    count += 1
    return count
def solve(matrix):
    ans, R, C = 0, len(matrix), len(matrix[0])
    for col in range(C):
        has_star_above = False
        # Find the highest shape in the column
        for row in range(R):
            if matrix[row][col] == '*':
                has_star_above = True
            elif matrix[row][col] == '#':
                if has_star_above:
                    ans += 1
    return ans
# Test case
matrix = [
    ["*", "*", "*", "*"],
    ["#", "*", ".", "*"],
    [".", ".", "#", "."],
    [".", "#", ".", "#"]
]
print(min_obstacles(matrix))  # Output: 4
print(solve(matrix))  # Output: 4

"""
PERFORMANCE ANALYSIS:

1. min_obstacles() function:
   Time Complexity: O(R * C * R) = O(R² * C)
   - Outer loops: O(R * C) to iterate through each cell
   - Inner loop: O(R) to check for stars above each obstacle
   - In worst case, we check all rows above for each cell
   
   Space Complexity: O(1)
   - Only using constant extra space for variables (count, has_star_above, etc.)
   - No additional data structures that grow with input size

2. solve() function:
   Time Complexity: O(R * C)
   - Single pass through the matrix: O(R * C)
   - For each column, we process each row exactly once
   - No nested loops that depend on matrix size
   
   Space Complexity: O(1)
   - Only using constant extra space for variables (ans, has_star_above, etc.)
   - No additional data structures

COMPARISON:
- solve() is MORE EFFICIENT with O(R * C) vs min_obstacles() with O(R² * C)
- Both have the same space complexity O(1)
- solve() uses a single-pass algorithm that's optimal for this problem
- min_obstacles() has redundant work by checking stars above for each obstacle separately

RECOMMENDATION: Use solve() function for better performance, especially for large matrices.
"""

# Performance testing with timing
import time

def performance_test():
    # Create a larger test matrix
    large_matrix = []
    for i in range(100):  # 100x100 matrix
        row = []
        for j in range(100):
            if i < 20:  # First 20 rows have stars
                row.append('*')
            elif i % 3 == 0:  # Every 3rd row has obstacles
                row.append('#')
            else:
                row.append('.')
        large_matrix.append(row)
    
    print("Performance Test on 100x100 matrix:")
    print("=" * 40)
    
    # Test min_obstacles function
    start_time = time.time()
    result1 = min_obstacles(large_matrix)
    end_time = time.time()
    time1 = end_time - start_time
    print(f"min_obstacles(): {result1} obstacles, Time: {time1:.6f} seconds")
    
    # Test solve function
    start_time = time.time()
    result2 = solve(large_matrix)
    end_time = time.time()
    time2 = end_time - start_time
    print(f"solve():         {result2} obstacles, Time: {time2:.6f} seconds")
    
    print(f"Speed improvement: {time1/time2:.2f}x faster")

# Run the performance test
performance_test()