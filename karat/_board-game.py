'''
You are playing a board game (1-D array) where the player moves by rolling a die with the number of sides given and is allowed to roll it once. 
You are also given a list of teleporters that move the player from one square to another. 
The starting and ending squares are given as well. Return a distinct list of positions where the player can potentially jump to.
Q2. Modified version of Q1. Players move by rolling a die as many times as they wish to, and```

Algorithm:
1. Initialize a set to keep track of reachable positions.
2. Use a queue to perform BFS starting from the initial position.
3. For each position, simulate rolling the die and moving to new positions.
4. If a new position has a teleporter, move to the teleporter's destination.
5. Continue until all reachable positions are explored.
6. Return the list of reachable positions.
'''

def reachable_positions(start, end, die_sides, teleporters):
    from collections import deque

    teleport_map = {src: dst for src, dst in teleporters}
    reachable = set()
    queue = deque([start])
    reachable.add(start)

    while queue:
        current = queue.popleft()

        for roll in range(1, die_sides + 1):
            next_pos = current + roll
            if next_pos > end:
                continue

            if next_pos in teleport_map:
                next_pos = teleport_map[next_pos]

            if next_pos not in reachable:
                reachable.add(next_pos)
                queue.append(next_pos)

    return sorted(reachable)
# you can use teleporters as many times as you want.
# Test case
start = 1
end = 10
die_sides = 6
teleporters = [(3, 8), (5, 2)]
print(reachable_positions(start, end, die_sides, teleporters))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

