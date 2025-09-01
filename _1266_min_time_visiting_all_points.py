'''
Topic: Array
Difficulty: Easy
Given a list of points where each point is represented as a tuple (x, y), this function calculates the minimum time required to visit all points starting from the first point. The time taken to move from one point to another is determined by the Manhattan distance between the two points.

Example:

Input: points = [(1,1),(2,3),(4,5)]
Output: 7

Time Complexity: O(n), where n is the number of points.
Space Complexity: O(1), as we are using a constant amount of space.

'''


'''
Approach:
1. We can use a brute force approach to calculate the minimum time required to visit all points.
2. We will calculate the Manhattan distance between all pairs of points and keep track of the minimum distance.
3. Finally, we will return the minimum distance as the result.

Time Complexity: O(n^2), where n is the number of points.
Space Complexity: O(1), as we are using a constant amount of space.
'''
def brute_force_approach(points):
    min_time = float('inf')
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            time = abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])
            min_time = min(min_time, time)
    return min_time

def minTimeToVisitAllPoints(points):
    total_time = 0
    for i in range(1, len(points)):
        total_time += abs(points[i][0] - points[i-1][0]) + abs(points[i][1] - points[i-1][1])
    return total_time

def minTimeToVisitAllPoints_v2(points):
    total_time = 0
    x1, y1 = points.pop()
    while points:
        x2, y2 = points.pop()
        total_time += max(abs(x2 - x1), abs(y2 - y1))
        x1, y1 = x2, y2
    return total_time