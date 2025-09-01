'''
Topic: Array
Difficulty: Medium

Given a 2D grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
Example:
Input:
[
  [1,1,0,0,0],
  [1,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [1,0,1,0,1]
]
Output: 5
Time Complexity: O(m*n), where m is the number of rows and n is the number of columns in the grid.
Space Complexity: O(m*n), as we may use a visited matrix of the same size.

DFS (Depth-First Search): We can use a recursive DFS function to explore all the land cells connected to a given cell, 
marking them as visited.
Data Structures Used:
- Stack (for the DFS implementation)
- Visited matrix (to keep track of visited cells)

BFS (Breadth-First Search): It explores all the neighboring cells at the present depth prior to moving on to cells at the next depth level.
Data Structures Used:
- Queue (for the BFS implementation)
- Visited matrix (to keep track of visited cells)

'''

def numIslands_bfs(grid):
    if not grid:
        return 0
    Rows, Cols = len(grid), len(grid[0])
    visited = [[False for _ in range(Cols)] for _ in range(Rows)]
    island_count = 0

    def bfs(r, c):
        queue = collections.deque()
        queue.append((r, c))
        visited[r][c] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < Rows and 0 <= ny < Cols and grid[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

    for i in range(Rows):
        for j in range(Cols):
            if grid[i][j] == '1' and not visited[i][j]:
                bfs(i, j)
                island_count += 1
    return island_count

    

def numIslands_dfs(grid):
    if not grid:
        return 0

    Rows, Cols = len(grid), len(grid[0])
    visited = [[False for _ in range(Cols)] for _ in range(Rows)]
    island_count = 0

    def dfs(r, c):
        if r < 0 or r >= Rows or c < 0 or c >= Cols:
            return
        if grid[r][c] == '0' or visited[r][c]:
            return
        visited[r][c] = True
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i, j)
                island_count += 1

    return island_count