"""
Problem Description: Given a 2D grid indicating land and water, count the number of islands.

Do it recursively.

INPUT = [
    [0,0,1],
    [0,0,1],
    [1,0,0],
]

where 0 = water and 1 = land

OUTPUT = 2
"""

# m : number of rows
# n : number of columns

def get_neighbors(node, m, n):
    a = node[0]
    b = node[1]
    neighbors = []
    
    if a-1 >=0:
        neighbors.append((a-1, b))
    
    if b-1 >=0:
        neighbors.append((a, b-1))
        
    if a+1 < m:
        neighbors.append((a+1, b))
        
    if b+1 < n:
        neighbors.append((a, b+1))
    
    return neighbors
    

def dfs(grid, node, visited, m, n):
    for r,c in get_neighbors(node, m, n):
        value = grid[r][c]
        if (r,c) not in visited and value:
            visited.add((r,c))
            dfs(grid, (r,c), visited, m, n)
        


def counting_islands(grid):
    m = len(grid)
    n= len(grid[0])
    visited = set()
    islands = 0
    
    for row in range(m):
        for column in range(n):
            value = grid[row][column]
            if value and (row, column) not in visited:
                visited.add((row, column))
                dfs(grid, (row, column), visited, m, n)
                islands+=1
    
    return islands

"""
MANUAL TRIAL

INPUT = [
    [0,0,1],
    [0,0,1],
    [1,0,0],
]
m = 3
n = 3
visited = set()
islands = 0

visited = set((0,0), (0,1))
dfs(grid, (0,2), visited, 3, 3)

"""