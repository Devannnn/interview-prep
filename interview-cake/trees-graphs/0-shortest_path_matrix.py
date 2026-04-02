"""
Shortest Path in a Binary Matrix

You are given an m x n binary matrix grid where:

0 represents an empty cell

1 represents a blocked cell

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m-1, n-1).

From any cell, you may move up, down, left, or right.

Return the length of the shortest path from start to finish, or -1 if no such path exists

You may assume grid[0][0] == 0

INPUT
grid = [
  [0, 0, 0],
  [1, 1, 0],
  [0, 0, 0]
]

(0,0) → (0,1) → (0,2) → (1,2) → (2,2)
"""

from collections import deque

def shortest_path(node, predecessors):
    list_precedessors = []
    curr_node = node
    while curr_node is not None:
        list_precedessors.append(curr_node)
        curr_node = predecessors[curr_node]
        
    return len(list_precedessors)

def get_neighbors(node, m, n):
    a = node[0]
    b = node[1]
    neighbors = []
    
    if b-1 >= 0:
        left = (a, b-1)
        neighbors.append(left)
    
    if a-1 >= 0:
        top = (a-1, b)
        neighbors.append(top)
    
    if b+1 <= n:
        right = (a, b+1)
        neighbors.append(right)
    
    if a+1 <= m:
        bottom = (a+1, b)
        neighbors.append(bottom)
    
    return neighbors

def bfs_shortest_path(grid):
    queue = deque()
    first_cell = (0,0)
    queue.append(first_cell)
    predecessors = {first_cell: None}
    visited = set([first_cell])
    
    m = len(grid)
    n = len(grid[0])
    
    while len(queue):
        curr_node = queue.popleft()
        
        if curr_node == (m-1,n-1):
            return shortest_path(curr_node, predecessors)
        
        neighbors = get_neighbors(curr_node, m, n)
        
        for neighbor in neighbors:
            if neighbor not in visited and not grid[neighbor[0]][neighbor[1]]:
                queue.append(neighbor)
                visited.add(neighbor)
                predecessors[neighbor] = curr_node
    
    return -1
        
visited = [(0,0)]
curr_node == (2,2)
neighbors = [(0,1), (1,0)]
queue = [(0,1)]
visited = [(0,0), (0,1)]
predecessors = {
    (0,1) : (0,0),
    (0,2) : (0,1),
    (1,2) : (0,2),
    (2,2) : (1,2)
}


# Time Complexity  : O(n+e)
# Space Complexity : O(n)