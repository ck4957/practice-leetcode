'''
A 2-D grid that consists of '0' and '+'. '+' means impassable and '0' means passable. 
Return the rows and columns indices that are completely passable (all 0's).

Algorithm:
1. Initialize two lists to keep track of passable rows and columns.
2. Iterate through each row and column to check if they are completely passable.
3. Return the lists of passable rows and columns.

Space Complexity: O(m + n) where m is the number of rows and n is the number of columns.
Time Complexity: O(m*n) where m is the number of rows and n is the number of columns.

'''
def find_passable_indices(grid):
    if not grid or not grid[0]:
        return [], []

    rows = len(grid)
    cols = len(grid[0])
    passable_rows = []
    passable_cols = []

    # Check for passable rows
    for r in range(rows):
        if all(cell == '0' for cell in grid[r]):
            passable_rows.append(r)

    # Check for passable columns
    for c in range(cols):
        if all(grid[r][c] == '0' for r in range(rows)):
            passable_cols.append(c)

    return passable_rows, passable_cols

# Test case
grid = [
    ['0', '0', '+', '0'],
    ['0', '0', '0', '0'],
    ['+', '+', '+', '+'],
    ['0', '0', '0', '0']
]
print(find_passable_indices(grid))  # Output: ([1, 3], [1, 3])'''


'''
You are now given a starting cell, which is on one corner of the grid. 
You can travel in all 4 directions of cells that are passable. 
You have to reach any other passable cell that is on the corner of the grid, which has the minimum distance from the starting cell. 
Return the coordinates of the destination cell. Return -1 if not possible.

Algorithm: BFS

1. Initialize a queue and add the starting cell.
2. While the queue is not empty:
   a. Dequeue the front cell.
   b. If it's a corner cell and not the start, check if it's the closest one.
   c. Enqueue all valid neighboring cells.
3. Return the closest corner cell or -1 if not found.

Space Complexity: O(m*n) in the worst case, where m is the number of rows and n is the number of columns.
Time Complexity: O(m*n) in the worst case, as we may need to visit all cells.

'''

from collections import deque
def min_distance_to_corner(grid, start):
    if not grid or not grid[0]:
        return -1

    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set()
    visited.add(start)
    min_distance = float('inf')
    destination = (-1, -1)

    while queue:
        x, y = queue.popleft()

        # Check if we are at a corner
        if (x == 0 or x == rows - 1) and (y == 0 or y == cols - 1) and (x, y) != start:
            distance = abs(x - start[0]) + abs(y - start[1])
            if distance < min_distance:
                min_distance = distance
                destination = (x, y)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '0' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append((nx, ny))

    return destination if destination != (-1, -1) else -1